"""
evaluation/visualize.py — Academic Table & Figure Formatting Handler
=====================================================================
Automates generating publication-ready vector figures (PDF/PNG) and
copy-pasteable LaTeX tables directly from raw evaluation metrics.

Usage:
    # 1. Print LaTeX tabular format code from outputs
    python evaluation/visualize.py --mode table --input_dir evaluation/outputs

    # 2. Plot performance comparison charts (PDF format for vector zoom)
    python evaluation/visualize.py --mode plot --plot_type bar --input_dir evaluation/outputs
"""

import argparse
import json
import logging
import os
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(levelname)-8s  %(message)s")


# ---------------------------------------------------------------------------
# LaTeX Table Generator
# ---------------------------------------------------------------------------

def generate_latex_table(metrics: dict) -> str:
    """Format metrics dictionary into a clean LaTeX tabular block.

    Example input: {"WER": 0.125, "BLEU": 28.4, "BERTScore": 0.892}
    """
    lines = [
        "\\begin{table}[t]",
        "\\centering",
        "\\caption{Evaluation Results comparison. Bold indicates best scores.}",
        "\\label{tab:evaluation_results}",
        "\\begin{tabular}{l|c}",
        "\\hline",
        "\\textbf{Metric} & \\textbf{Score} \\\\",
        "\\hline"
    ]

    for metric_name, score in metrics.items():
        # Clean formatting for numbers
        if isinstance(score, float):
            val_str = f"{score:.4f}"
        else:
            val_str = str(score)

        lines.append(f"{metric_name} & {val_str} \\\\")

    lines.extend([
        "\\hline",
        "\\end{tabular}",
        "\\end{table}"
    ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Vector Plotting Handler
# ---------------------------------------------------------------------------

def plot_comparison(metrics: dict, output_path: str, plot_type: str = "bar") -> None:
    """Plot metrics using Matplotlib and save as vector graphics (PDF/PNG)."""
    try:
        import matplotlib.pyplot as plt  # noqa: PLC0415
    except ImportError:
        logging.error("Matplotlib is not installed. Run: pip install matplotlib")
        sys.exit(1)

    # Set academic publication-friendly style parameters
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "figure.titlesize": 14,
        "grid.alpha": 0.3,
        "grid.linestyle": "--"
    })

    keys = list(metrics.keys())
    values = [metrics[k] for k in keys]

    if not keys:
        logging.warning("No metrics found to plot.")
        return

    fig, ax = plt.subplots(figsize=(6, 4), dpi=300)

    if plot_type == "bar":
        # Professional color palette (slate gray / muted blue)
        bars = ax.bar(keys, values, color="#4A6984", edgecolor="#2E3D4C", width=0.5)
        ax.set_ylabel("Score")
        ax.set_title("Model Metrics Comparison")
        ax.grid(axis="y")

        # Label values on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f"{height:.3f}" if isinstance(height, float) else str(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha="center", va="bottom", fontsize=9)

    elif plot_type == "line":
        ax.plot(keys, values, marker="o", color="#D95F02", linewidth=2, markersize=6)
        ax.set_ylabel("Score")
        ax.set_title("Ablation/Scaling Curve")
        ax.grid(True)

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    logging.info("Figure saved successfully -> %s", output_path)


# ---------------------------------------------------------------------------
# Main Execution
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Academic Table & Figure Generator")
    parser.add_argument(
        "--mode",
        choices=["table", "plot", "all"],
        default="all",
        help="Whether to output a LaTeX table, plot a figure, or run both."
    )
    parser.add_argument(
        "--plot_type",
        choices=["bar", "line"],
        default="bar",
        help="Type of plot to generate."
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        default=os.path.join("evaluation", "outputs"),
        help="Directory where metrics.json resides."
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default=os.path.join("evaluation", "outputs"),
        help="Directory to save generated charts and tables."
    )

    args = parser.parse_args()

    metrics_file = os.path.join(args.input_dir, "metrics.json")
    if not os.path.exists(metrics_file):
        logging.warning("Metrics file not found: %s. Creating dummy metrics for testing.", metrics_file)
        os.makedirs(args.input_dir, exist_ok=True)
        metrics = {"WER": 0.145, "BLEU": 26.8, "BERTScore": 0.884}
        with open(metrics_file, "w") as f:
            json.dump(metrics, f, indent=2)
    else:
        try:
            with open(metrics_file) as f:
                metrics = json.load(f)
        except (json.JSONDecodeError, OSError) as exc:
            logging.error("Failed to parse metrics.json: %s", exc)
            sys.exit(1)

    # 1. LaTeX table output
    if args.mode in ["table", "all"]:
        latex_code = generate_latex_table(metrics)
        logging.info("=== LaTeX Tabular Code ===")
        print(latex_code)
        print("==========================")

        latex_output_path = os.path.join(args.output_dir, "table.tex")
        with open(latex_output_path, "w") as f:
            f.write(latex_code)
        logging.info("LaTeX code saved -> %s", latex_output_path)

    # 2. Vector figure plotting
    if args.mode in ["plot", "all"]:
        plot_path = os.path.join(args.output_dir, f"comparison_chart.pdf")
        plot_comparison(metrics, plot_path, plot_type=args.plot_type)


if __name__ == "__main__":
    main()
