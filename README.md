# 🎓 Academic Research Template Repository (academic-research-repo)

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white&style=flat-square)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Templates: Venue-Aware](https://img.shields.io/badge/Templates-Venue--Aware-orange?style=flat-square)](templates/)
[![Standards: Reproducible](https://img.shields.io/badge/Reproducibility-Verified-blueviolet?style=flat-square)](#6-submission--reproducibility-checklist)

A standardized, reproducible, and **venue-aware** template repository for machine learning, NLP, and AI research projects, aligned with the **Academic Research & Evaluation Skill** guidelines.

This repository enforces strict reproducibility non-negotiables, decouples prompt engineering from raw dataset entries, and provides automated evaluation scaffolds. It now includes venue-aware planning and analysis templates designed to avoid common formatting and submission pitfalls across major AI conferences and journals (ACL, NeurIPS, INTERSPEECH, ICASSP, CVPR, AAAI, etc.).

---

## 📅 Target-Venue Aware & Reproducibility First

> [!IMPORTANT]
> **Venue-First Planning:** Different academic conferences (e.g., ACL vs. IEEE ICASSP vs. NeurIPS) have fundamentally different constraints: page limits, mandatory sections (Limitations, Ethics), citation styles (natbib author-year vs. IEEE numbered), and review policies.
> This repository provides templates that help you design, run, and write your paper with your target venue in mind from day zero.

---

## 1. Directory Structure

```
academic-research-repo/
├── configs/                # Experiment configuration files (YAML / JSON)
│   └── README.md           # Configuration documentation and examples
├── data_storage/           # Raw, cached, and split datasets (not tracked by git)
│   ├── raw/
│   ├── processed/
│   └── splits/
├── evaluation/             # Metric scripts and evaluation outputs
│   ├── outputs/            # predictions.json + metrics.json written here
│   └── README.md           # Evaluation reporting standards & libraries
├── models/                 # Model loaders, API wrappers, and inference helpers
│   └── README.md           # BaseModelWrapper interface & implementation guidelines
├── src/                    # Core source: preprocessing, VAD, feature extraction
│   └── README.md           # Preprocessing guidelines & VAD parameter logs
├── templates/              # Research dissection and planning documents
│   ├── New_Research_Paper_Planning_Guide.md   # Step-by-step venue-aware planning guide
│   ├── Research_Paper_Analysis_Template.md    # Blank literature review & analysis template
│   ├── DOWIS_Research_Deep_Dive.md            # Reference guide (DOWIS Spoken Instruction paper)
│   ├── SIFT50M_Research_Deep_Dive.md          # Reference guide (SIFT-50M speech LLM paper)
│   └── CLaS_Bench_Research_Deep_Dive.md        # Reference guide (CLaS-Bench multilingual steering paper)
├── .gitignore              # Excludes data, outputs, and environment files
├── CITATION.cff            # Project citation metadata (CFF format)
├── LICENSE                 # MIT License file
├── SKILL.md                # Agent routing rules & evaluation standard guidelines
├── runner.py               # Inference + evaluation execution pipeline
├── requirements.txt        # Pinned package dependencies (Python ≥ 3.10)
└── README.md               # This file
```

---

## 2. Getting Started

### Step 1: Environment Setup

Create an isolated environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 2: Running a Dry Run

Verify that the data loader, mock model, and metric evaluation initialize correctly on a single item subset:

```bash
python runner.py --dry_run --seed 42
```

Expected output: `predictions.json` and `metrics.json` are written to `evaluation/outputs/` and logged to stdout.

### Step 3: Running a Full Evaluation

Execute inference and compute metrics on a designated model and dataset:

```bash
python runner.py \
  --model <huggingface-model-id-or-local-path> \
  --dataset <dataset-name-or-path> \
  --seed 42 \
  --output_dir evaluation/outputs
```

---

## 3. Core Design Principles

1. **Decouple Prompts from Data**: Keep prompt formatting and instruction templates separate from raw dataset inputs. This enables testing the same dataset under varied prompt styles (e.g. formal, informal, short, detailed).
2. **Reproducibility Non-Negotiables**:
   - Fix **all** random seeds via `set_seed()` in `runner.py` (covers Python `random`, NumPy, and PyTorch CPU + CUDA).
   - Pin library versions in `requirements.txt` using dual-bound pins (e.g., `>=x.y.z,<a.b.0`) to prevent breaking changes while allowing patch updates.
   - Log hardware specs (GPU, VRAM, CUDA version) and preprocessing thresholds (e.g. VAD window duration, loudness thresholds).
   - Provide a single, deterministic CLI command to reproduce paper tables.
3. **Metric-First Design**: Define and implement evaluation metrics *before* modeling begins. Prioritize human-correlated metrics (e.g., CometKiwi over BLEU for MT; BERTScore over ROUGE for summarization).
4. **Venue-First Planning**: Select the target venue before drafting a single word. This informs LaTeX style packages, page budget targets (e.g., 4 pages for INTERSPEECH vs. 8 pages for CVPR), and mandatory sections (e.g., "Limitations" for ACL, "Broader Impact" for NeurIPS).
5. **Separation of Concerns**:
   - `src/` — preprocessing and feature extraction (dependency-free from model and eval modules).
   - `models/` — model wrapper loaders inheriting from `BaseModelWrapper`.
   - `evaluation/` — metric evaluation scripts reading predictions from the outputs partition.

---

## 4. Academic Templates & Workflow

This repository includes a suite of templates in the [templates/](templates/) directory to guide you from paper reading to drafting your submission:

| Template | Purpose | Key Features |
|---|---|---|
| [New_Research_Paper_Planning_Guide.md](templates/New_Research_Paper_Planning_Guide.md) | **Step-by-step guide** for planning new research papers (Mode B). | Phase-by-phase planning, **target scope & research area maps** (to prevent desk rejects), **typical submission deadlines & conference cycles** (for major AI/ML/NLP/Speech/Vision venues and specialized workshops like AfricaNLP and SACAIR), formatting and page limits, mandatory section checklists, and abstract drafting. |
| [Research_Paper_Analysis_Template.md](templates/Research_Paper_Analysis_Template.md) | **Blank template** for literature review, analysis, and replication planning (Mode A). | Venue Type tagging, reproducibility audit checklist, and venue-specific BibTeX templates (ISCA, ACL/NeurIPS, arXiv) to ensure correct metadata tracking. |
| [DOWIS_Research_Deep_Dive.md](templates/DOWIS_Research_Deep_Dive.md) | **Reference deep dive** dissecting the DOWIS (Züfle et al., 2026) paper. | Exemplar showing how to use the analysis template, complete with synthesis tables, reproducing checklist results, and 3 BibTeX citation style variants (ISCA, ACL, arXiv). |
| [SIFT50M_Research_Deep_Dive.md](templates/SIFT50M_Research_Deep_Dive.md) | **Reference deep dive** dissecting the SIFT-50M (Pandey et al., ACL 2025) paper. | Exemplar detailing Whisper-medium acoustic encoders, LoRA parameters alignment, and EvalSIFT dataset splits. |
| [CLaS_Bench_Research_Deep_Dive.md](templates/CLaS_Bench_Research_Deep_Dive.md) | **Reference deep dive** dissecting the CLaS-Bench (Gurgurov et al., 2026) paper. | Exemplar detailing cross-lingual alignment and steering representations, PCA/LDA/SAE steering methods, and the LID + BERTScore steering evaluation formula. |

> [!TIP]
> Use the associated **Research Paper Analyst Skill** (`academic-research-eval`) to automatically parse paper repos, perform literature analysis, design hypotheses, and validate submission packages.

---

## 5. Metric Quick Reference

| Task | Primary Metric | Tools / Packages | Direction | Notes & Selection Guidelines |
|---|---|---|---|---|
| **ASR** | WER | `jiwer` | ↓ | Word Error Rate baseline |
| **MT / ST** | CometKiwi | `unbabel-comet` | ↑ | Reference-free, state-of-the-art human correlation |
| **MT / ST (legacy)** | BLEU | `sacrebleu` | ↑ | N-gram match; reference-dependent; known biases |
| **Summarisation** | BERTScore | `bert-score` | ↑ | Semantic similarity; use `deberta-xlarge-mnli` |
| **Summarisation** | ROUGE | `rouge-score` | ↑ | Overlap-based; less semantic |
| **Speech Quality** | PESQ | `pesq` | ↑ | Reference-based speech quality evaluation |
| **Speech Quality** | UTMOS | `utmos` (manual install) | ↑ | MOS prediction proxy |
| **Segmentation** | Collar-F1 | `pyannote.metrics` | ↑ | Audio boundaries with tolerance (e.g. ±3s) |

---

## 6. Submission & Reproducibility Checklist

Before submitting your manuscript or releasing code/data, cross-check these items:

### ⚙️ Code & Data Reproducibility
- [ ] `requirements.txt` has dual-bound version pins (`>=x.y.z,<a.b.0`).
- [ ] Random seed is explicitly set (via `set_seed()`) and logged in logs/configs.
- [ ] GPU model, VRAM, and CUDA version are recorded.
- [ ] Preprocessing parameters (sample rates, VAD dB thresholds, frame windows) are logged.
- [ ] Dataset splits are preserved under `data_storage/splits/` with a `data_stats.json`.
- [ ] Results can be reproduced with a single command listed in the README.
- [ ] `evaluation/outputs/metrics.json` is committed or attached to the supplemental material.

### 📝 Venue & Submission Compliance
- [ ] Target venue constraints (page limit, LaTeX template, review system) are validated (see [Planning Guide Section 6.4](templates/New_Research_Paper_Planning_Guide.md#64-venue-quick-reference--formatting--requirements)).
- [ ] Mandatory sections are present (e.g., "Limitations" + "Ethics Statement" for ACL; "Broader Impact" for NeurIPS).
- [ ] Citation style is verified (e.g., natbib `\citep` for ACL/NeurIPS; numbered `[1]` for INTERSPEECH/ICASSP).
- [ ] Every reference bibtex is updated to its peer-reviewed published version (no stale arXiv preprints if published).
- [ ] Anonymous submission guidelines are followed (no preprints posted during strict ACL blackout period).
- [ ] `CITATION.cff` is present in the repository root and filled with author and project metadata.

---

## 7. Citing This Repository

If you use this template or baseline runner in your academic research, please cite the repository using the citation metadata below. Alternatively, you can use the "Cite this repository" feature provided by GitHub in the sidebar.

**BibTeX:**
```bibtex
@software{oyerinde2026academic,
  author = {Oyerinde, Samuel},
  title = {{Academic Research Template Repository}},
  month = {6},
  year = {2026},
  publisher = {GitHub},
  version = {1.0.0},
  url = {https://github.com/sam4rano/academic-research-repo}
}
```

---

## 8. License

This template repository is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
