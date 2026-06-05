"""Lightweight HPO baseline framework for toy regression experiments."""

from .evaluator import BaselineEvaluator, CrossDatasetEvaluator
from .kaggle_playground import (
    KaggleRegressionTask,
    kaggle_mlp_search_space,
    load_manifest,
    nested_task_slugs,
)
from .optimizers import (
    BayesianOptimization,
    CrossDatasetHyperRLOptimizer,
    CrossDatasetLCDQNOptimizer,
    HyperRLOptimizer,
    LearningCurveDQNOptimizer,
    RandomSearch,
)
from .tasks import LCBenchTask, SyntheticRegressionTask

__all__ = [
    "BaselineEvaluator",
    "BayesianOptimization",
    "CrossDatasetEvaluator",
    "CrossDatasetHyperRLOptimizer",
    "CrossDatasetLCDQNOptimizer",
    "HyperRLOptimizer",
    "KaggleRegressionTask",
    "LCBenchTask",
    "LearningCurveDQNOptimizer",
    "RandomSearch",
    "SyntheticRegressionTask",
    "kaggle_mlp_search_space",
    "load_manifest",
    "nested_task_slugs",
]
