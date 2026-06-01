from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (project_root := str(PROJECT_ROOT)) not in sys.path:
    sys.path.insert(0, project_root)

from hpo_baselines.kaggle_playground import load_manifest


def _selected_task_slugs(raw_tasks: str, available: set[str]) -> set[str] | None:
    if raw_tasks == "all":
        return None
    selected = {item.strip() for item in raw_tasks.split(",") if item.strip()}
    if not selected:
        raise ValueError("--tasks must be 'all' or a comma-separated slug list")
    unknown = sorted(selected - available)
    if unknown:
        raise ValueError(f"Unknown Kaggle task slug(s): {', '.join(unknown)}")
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(description="Download Kaggle Playground raw data.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=PROJECT_ROOT / "data" / "kaggle_playground" / "manifest.json",
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=PROJECT_ROOT / "data" / "kaggle_playground" / "raw",
    )
    parser.add_argument(
        "--tasks",
        type=str,
        default="all",
        help="Download 'all' tasks or a comma-separated list of manifest slugs.",
    )
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    selected = _selected_task_slugs(args.tasks, set(manifest.by_slug))
    args.raw_dir.mkdir(parents=True, exist_ok=True)
    for spec in manifest.tasks:
        if selected is not None and spec.slug not in selected:
            continue
        out_dir = args.raw_dir / spec.slug
        out_dir.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [
                "kaggle",
                "competitions",
                "download",
                "-c",
                spec.slug,
                "-p",
                str(out_dir),
                "--unzip",
            ],
            check=True,
        )


if __name__ == "__main__":
    main()
