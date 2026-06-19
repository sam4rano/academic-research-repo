"""
runner.py — Academic Research Template Runner
==============================================
Entrypoint for running inference and evaluation on a configured dataset
and model. Supports dry-run mode for quick sanity checks.

Usage:
    python runner.py --dry_run --seed 42
    python runner.py --model my_model --dataset my_dataset --seed 0 --output_dir evaluation/outputs
"""

import argparse
import json
import logging
import os
import random
import sys

# ---------------------------------------------------------------------------
# Seed utilities
# ---------------------------------------------------------------------------

def set_seed(seed: int) -> None:
    """Pin ALL random sources for strict reproducibility.

    Covers Python's built-in ``random``, NumPy, and PyTorch (CPU + all
    CUDA devices) when those libraries are installed.  If a library is not
    present the corresponding seed call is silently skipped so that the
    runner works in lightweight environments too.
    """
    random.seed(seed)

    try:
        import numpy as np  # noqa: PLC0415
        np.random.seed(seed)
    except ImportError:
        logging.warning("NumPy not installed — NumPy seed not fixed.")

    try:
        import torch  # noqa: PLC0415
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        # Ensure deterministic CUDA operations where possible.
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except ImportError:
        logging.warning("PyTorch not installed — PyTorch seed not fixed.")

    logging.info("[Seed] All random sources fixed to: %d", seed)


# ---------------------------------------------------------------------------
# Dummy data loader (replace with your real loader)
# ---------------------------------------------------------------------------

def load_dataset(dataset_name: str, dry_run: bool) -> list[dict]:
    """Return a list of {'id', 'input', 'target'} records.

    Replace this stub with your actual HuggingFace / local data loader.
    The dry_run flag limits output to the first item for fast sanity checks.
    """
    logging.info("Loading dataset: %s", dataset_name)
    sample_data = [
        {
            "id": 1,
            "input": "Translate this sentence to French.",
            "target": "Traduisez cette phrase en français.",
        },
        {
            "id": 2,
            "input": "Transcribe the audio input.",
            "target": "Transcription de l'entrée audio.",
        },
    ]
    if dry_run:
        logging.info("[Dry Run] Dataset sliced to %d item(s).", 1)
        return sample_data[:1]
    return sample_data


# ---------------------------------------------------------------------------
# Dummy model inference (replace with your real model wrapper)
# ---------------------------------------------------------------------------

def run_inference(model_name: str, data: list[dict]) -> list[dict]:
    """Run model inference over *data* and return prediction records.

    Replace the dummy prediction below with a real call to your model
    wrapper in ``models/``.
    """
    logging.info("Loading model adapter: %s", model_name)
    results = []
    for item in data:
        logging.info("Processing item ID: %s", item["id"])
        # ── Replace this line with your actual model.generate() call ──
        prediction = f"PREDICTED: {item['input']}"
        results.append(
            {
                "id": item["id"],
                "input": item["input"],
                "prediction": prediction,
                "target": item["target"],
            }
        )
    return results


# ---------------------------------------------------------------------------
# Metric computation
# ---------------------------------------------------------------------------

def compute_metrics(results: list[dict]) -> dict:
    """Compute evaluation metrics over *results*.

    Currently computes Word Error Rate (WER) via ``jiwer`` as a baseline.
    Extend with CometKiwi, BERTScore, ROUGE, etc. as needed for your task.
    Returns a dict mapping metric name → value.
    """
    metrics: dict = {}

    # --- WER (ASR / text generation baseline) ---
    try:
        import jiwer  # noqa: PLC0415
        references = [r["target"] for r in results]
        hypotheses = [r["prediction"] for r in results]
        wer = jiwer.wer(references, hypotheses)
        metrics["WER"] = round(wer, 4)
        logging.info("[Metric] WER = %.4f  (↓ lower is better)", wer)
    except ImportError:
        logging.warning("jiwer not installed — WER not computed. Run: pip install jiwer")

    # --- Add further metrics here as your project grows ---
    # Example (MT / ST):
    #   from comet import download_model, load_from_checkpoint
    #   model = load_from_checkpoint(download_model("Unbabel/wmt22-cometkiwi-da"))
    #   scores = model.predict([{"src": ..., "mt": ...}], batch_size=8)
    #   metrics["CometKiwi"] = round(scores.system_score, 4)
    #
    # Example (Summarisation):
    #   from bert_score import score as bert_score
    #   P, R, F1 = bert_score(hypotheses, references, lang="en", verbose=False)
    #   metrics["BERTScore_F1"] = round(F1.mean().item(), 4)

    return metrics


# ---------------------------------------------------------------------------
# Output persistence
# ---------------------------------------------------------------------------

def save_outputs(results: list[dict], metrics: dict, output_dir: str) -> None:
    """Persist predictions and metric scores to *output_dir*."""
    os.makedirs(output_dir, exist_ok=True)

    predictions_path = os.path.join(output_dir, "predictions.json")
    metrics_path = os.path.join(output_dir, "metrics.json")

    try:
        with open(predictions_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        logging.info("Predictions saved → %s", predictions_path)

        with open(metrics_path, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2, ensure_ascii=False)
        logging.info("Metrics saved      → %s", metrics_path)
    except OSError as exc:
        logging.error("Failed to write outputs: %s", exc)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Academic Research Template Runner Script",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--model",
        type=str,
        default="baseline_model",
        help="Name or path of the model checkpoint / Hugging Face ID.",
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default="sample_dataset",
        help="Name or local path of the dataset to evaluate on.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for full reproducibility.",
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Limit dataset to 1 item for quick sanity checking.",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=os.path.join("evaluation", "outputs"),
        help="Directory where predictions.json and metrics.json are written.",
    )
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    # 1. Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    logging.info("=" * 60)
    logging.info("Academic Research Runner  |  model=%s  dataset=%s  seed=%d",
                 args.model, args.dataset, args.seed)
    logging.info("=" * 60)

    # 2. Pin random seeds
    set_seed(args.seed)

    # 3. Load data
    data = load_dataset(args.dataset, dry_run=args.dry_run)

    # 4. Run inference
    results = run_inference(args.model, data)

    # 5. Compute metrics
    metrics = compute_metrics(results)

    # 6. Persist outputs
    save_outputs(results, metrics, output_dir=args.output_dir)

    logging.info("Run complete. Outputs in: %s", args.output_dir)


if __name__ == "__main__":
    main()
