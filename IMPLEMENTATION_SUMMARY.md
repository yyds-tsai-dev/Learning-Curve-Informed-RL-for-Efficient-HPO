# Hyp-RL 跨資料集實現修改總結

## 修改概述

根據提供的論文結論，本次修改實現了 Hyp-RL 的核心貢獻：**跨資料集的權重繼承與元學習**。

### 核心改進點

#### 1️⃣ 單一網路權重繼承
- **原始設計**: 每個資料集獨立訓練，每次初始化新的 DQN 網路
- **改進設計**: 單一 DQN 網路跨所有資料集持續更新，權重不重置
- **實現**: `_CrossDatasetDQNController` 管理全局網路，所有 episodes 共享

#### 2️⃣ 元特徵條件化
- **原始設計**: LSTM 沒有關於資料集特性的先驗知識
- **改進設計**: 元特徵（數據集統計特性）初始化 LSTM 隱藏狀態
- **實現**: 修改 `_LSTMQNetwork.forward()` 接收 meta_features，用 `h0_proj` 和 `c0_proj` 初始化

#### 3️⃣ 隨機資料集採樣
- **原始設計**: 按順序遍歷資料集
- **改進設計**: 在訓練迴圈中隨機從資料集分佈採樣
- **實現**: `optimize_cross_dataset()` 中的 `rng.choice(self.tasks)`

## 文件修改詳解

### 📝 hpo_baselines/optimizers.py

#### 修改 1: 增強 `_LSTMQNetwork`

**目的**: 支援元特徵初始化隱藏狀態

```python
# 新增參數
meta_dim: int = 0

# 新增初始化
if meta_dim > 0:
    self.h0_proj = nn.Linear(meta_dim, lstm_hidden)
    self.c0_proj = nn.Linear(meta_dim, lstm_hidden)

# 修改 forward 方法簽名
def forward(
    self, inputs: torch.Tensor, 
    meta_features: torch.Tensor | None = None  # 新參數
) -> torch.Tensor:

# 條件化初始化
if meta_features is not None and self.h0_proj is not None:
    h0 = self.h0_proj(meta_features).unsqueeze(0)
    c0 = self.c0_proj(meta_features).unsqueeze(0)
    _, (hidden, _) = self.lstm(packed, (h0, c0))
```

**影響**: 所有使用 LSTM 的地方都可選擇性地接收元特徵進行條件化

#### 修改 2: 更新 `_DQNController` 兼容性

**目的**: 確保現有單任務訓練仍能工作

```python
# _build_q_network 中
meta_dim=0,  # 單任務不使用元特徵初始化

# _select_action 中
if isinstance(network, _LSTMQNetwork):
    q_values = network(tensor, meta_features=None).squeeze(0)

# _train_step 中
if isinstance(online, _LSTMQNetwork):
    q_selected = online(states, meta_features=None).gather(...)
```

**影響**: 向後相容，不影響現有代碼

#### 新增: `_CrossDatasetDQNController`

**核心算法**:

```
1. 初始化單一共享 DQN 網路
2. 預計算所有任務的配置、動作向量、元特徵
3. for episode in total_episodes:
   - 隨機選擇任務: task = rng.choice(tasks)
   - 初始化歷史: history = zeros(max_budget, row_dim)
   - for iteration in range(budget):
     - 從歷史構建狀態: state = history.reshape(-1)
     - ε-貪心選擇: action = select_action(Q_network, state, meta_features)
     - 評估: result = task.evaluate(config[action])
     - 記錄轉移: history[iteration] = [action_vec, reward, meta, curve_features]
     - 訓練共享網路: loss = train_step()
     - 更新目標網路 (if needed)
   - 記錄評估結果
```

**關鍵特性**:
- ✅ 單一網路跨所有任務（權重共享）
- ✅ 元特徵作為狀態一部分
- ✅ 隨機任務採樣
- ✅ 支援學習曲線特徵（可選）

#### 新增: 優化器包裝類

```python
class CrossDatasetHyperRLOptimizer(BaseOptimizer):
    """基礎方法"""
    def optimize(self, tasks, total_episodes, seed)
    
class CrossDatasetLCDQNOptimizer(CrossDatasetHyperRLOptimizer):
    """加上學習曲線特徵的方法"""
```

### 📝 hpo_baselines/evaluator.py

#### 新增: `CrossDatasetEvaluator`

**目的**: 支援跨資料集評估

**特點**:
- 兼容 `BaselineEvaluator` API
- 支援多個 seed 的重複運行
- 自動處理跨資料集 vs 單任務方法
- 結果儲存與總結

```python
evaluator = CrossDatasetEvaluator(
    tasks=tasks,
    methods=[method1, method2],
    total_episodes=50,
    seeds=[0, 1, 2],
)

traces = evaluator.run()
evaluator.save(traces, output_dir)
```

### 📝 hpo_baselines/__init__.py

**修改**: 匯出新的類

```python
from .optimizers import (
    CrossDatasetHyperRLOptimizer,
    CrossDatasetLCDQNOptimizer,
)
from .evaluator import CrossDatasetEvaluator

__all__ = [
    ...,
    "CrossDatasetHyperRLOptimizer",
    "CrossDatasetLCDQNOptimizer",
    "CrossDatasetEvaluator",
]
```

### 📝 scripts/run_cross_dataset_training.py

**新增**: 完整的運行範例

```bash
python scripts/run_cross_dataset_training.py \
    --datasets "adult,higgs,yeast" \
    --total-episodes 50 \
    --seeds 3
```

### 📝 CROSS_DATASET_IMPLEMENTATION.md

**新增**: 詳細的實現指南文檔

## 演算法對應

### 論文 Algorithm 1 實現對應

| 論文概念 | 實現位置 | 代碼 |
|---------|--------|------|
| 單一 DQN 網路 $\theta$ | `_CrossDatasetDQNController.online` | `online = self._build_q_network(...)` |
| 隨機資料集採樣 $D \sim Unif(\mathcal{D})$ | `optimize_cross_dataset()` | `task = rng.choice(self.tasks)` |
| 狀態編碼 (含元特徵) | `_history_row()` | 包含 meta + curve features |
| 策略條件化 | `_LSTMQNetwork.forward()` | `network(state, meta_features)` |
| 權重繼承 | `optimize_cross_dataset()` | 每個 episode 重用網路，只更新不重置 |
| 目標網路更新 | `optimize_cross_dataset()` | `target.load_state_dict(online.state_dict())` |

## 使用案例

### 案例 1: 基礎跨資料集訓練

```python
from hpo_baselines import CrossDatasetHyperRLOptimizer, LCBenchTask
import json

data = json.load(open("data/tiny_lcbench.json"))
tasks = [
    LCBenchTask("data/tiny_lcbench.json", "adult", data=data),
    LCBenchTask("data/tiny_lcbench.json", "higgs", data=data),
]

optimizer = CrossDatasetHyperRLOptimizer(total_episodes=50)
traces = optimizer.optimize(tasks, total_episodes=50, seed=0)
```

### 案例 2: 完整評估

```python
from hpo_baselines import CrossDatasetEvaluator, CrossDatasetHyperRLOptimizer, CrossDatasetLCDQNOptimizer

evaluator = CrossDatasetEvaluator(
    tasks=tasks,
    methods=[
        CrossDatasetHyperRLOptimizer(total_episodes=50),
        CrossDatasetLCDQNOptimizer(total_episodes=50),
    ],
    seeds=[0, 1, 2],
)

traces = evaluator.run()
summary = evaluator.summarize(traces)
```

## 驗證

### 預期行為

1. **權重持續更新**: 網路權重在 episodes 間不重置
2. **元特徵初始化**: LSTM 隱藏狀態由元特徵初始化
3. **隨機採樣**: 不同 episodes 會隨機選擇不同任務
4. **逐步改進**: Simple Regret 應隨時間遞減

### 測試建議

```python
# 驗證權重共享
controller = _CrossDatasetDQNController(...)
traces = controller.optimize_cross_dataset(10, seed=0)

# 檢查 episodes 的多樣性
task_distribution = [t.task for e in traces for t in e.evaluations]
# 應該包含多個不同的任務名稱

# 檢查性能改進
for trace in traces:
    regrets = [r.val_score for r in trace.evaluations]
    # regrets 應該單調遞減或波動較小
```

## 技術細節

### 狀態維度計算

```
state_dim = max_single_episode_budget * row_dim

其中 row_dim = 
  + hyperparameter_vector_dim
  + 1 (reward)
  + meta_features_dim
  + 5 (if include_curve_features else 0)
```

### 元特徵規範化

```python
def _meta_features(task):
    values = np.asarray(task.meta_features(), dtype=np.float32)
    scale = np.linalg.norm(values)
    return values / (scale + 1e-8)  # L2 規範化
```

### 學習曲線特徵

```python
def _curve_features(curve):
    # [value, min, first_deriv, second_deriv, improvement]
    tail = curve[-min(8, len(curve)):]
    ...
    return np.array([...], dtype=np.float32)
```

## 環境要求

- **Python**: 3.12+ (PEP 695 type 語法)
- **核心依賴**: torch, numpy, scipy (與原項目相同)
- **可選**: matplotlib (用於結果可視化)

## 性能考量

### 計算複雜度

- **時間**: O(total_episodes × max_budget × (forward + backward))
- **空間**: O(replay_buffer_size × state_dim)

### 建議超參數

| 參數 | 推薦值 | 範圍 |
|------|-------|------|
| total_episodes | 50-100 | 10-500 |
| hidden_sizes | (128, 128) | (64, 64)-(256, 256) |
| replay_size | 1024 | 512-4096 |
| batch_size | 32 | 16-64 |
| learning_rate | 1e-3 | 1e-4-1e-2 |
| epsilon_start | 1.0 | 0.5-1.0 |
| epsilon_end | 0.05 | 0.01-0.1 |

## 後續擴展

### 可能的改進

1. **優先級重放** - 優先採樣高 TD-error 的轉移
2. **雙 Q 網路** - 減少 Q 值過估計
3. **分佈式訓練** - 多進程/多 GPU 並行訓練
4. **適應性元學習** - 動態調整元特徵權重
5. **無模型知識蒸餾** - 將元知識遷移到輕量級模型

## 參考

- 原始論文: Hyp-RL (論文引用信息)
- PEP 695: Type Parameter Syntax (Python 3.12)
- DQN 論文: Human-level control through deep reinforcement learning

---

**最後更新**: 2026-05-02
**實現者**: AI Assistant (GitHub Copilot)
**測試狀態**: ⏳ 待 Python 3.12 環境驗證
