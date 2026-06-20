# SIFT-50M Research Deep Dive

This document serves as a complete paper analysis and reproducibility checklist for the SIFT-50M paper (Pandey et al., ACL 2025).

---

## Paper & Repository Metadata
*   **Paper Title**: SIFT-50M: A Large-Scale Multilingual Dataset for Speech Instruction Fine-Tuning
*   **Authors**: Prabhat Pandey, Rupak Vignesh Swaminathan, K V Vijay Girish, Arunasish Sen, Jian Xie, Grant P. Strimel, Andreas Schwarz (Amazon)
*   **Conference/Journal**: ACL 2025 (Annual Meeting of the Association for Computational Linguistics)
*   **Venue Type**: NLP / CL Conference
*   **Citation Style**: Author-Year (natbib `\citep` / `\citet`)
*   **Page Limit**: 8 pages of content (excluding references/appendices)
*   **arXiv ID / Link**: [arxiv.org/abs/2504.09081](https://arxiv.org/abs/2504.09081)
*   **ACL Anthology Link**: [aclanthology.org/2025.acl-long.xxx](https://aclanthology.org/)

---

## 1. Abstract & Core Contribution
*   **Problem Statement**: Most existing speech datasets focus strictly on paired audio and task-specific targets (such as transcripts for ASR), lacking the instruction-following context needed to train Spoken Large Language Models (SLLMs) to follow arbitrary instructions.
*   **Core Contribution/Solution**: The authors introduce **SIFT (Speech Instruction Fine-Tuning)**, a massive 50-million-example dataset spanning 5 languages and 14,000 hours of speech. They leverage standard LLMs alongside specialized expert models to annotate/generate complex instruction sets (controlling parameters like gender, accent, speaking rate, noise levels, and distortion).
*   **Key Findings**:
    *   Using SIFT-50M, they train **SIFT-LLM**, which beats existing open-source speech-text LLMs on instruction-following benchmarks while remaining competitive on foundational ASR tasks.
    *   They introduce **EvalSIFT**, a standardized benchmark specifically designed to assess speech instruction-following.

---

## 2. Dataset & Data Loader Pipeline
*   **Dataset Schema**:
    *   *Inputs*: Speech signals (audio) accompanied by text instructions.
    *   *Speech Dimensions annotated*: Accent, age, gender, pitch, speaking rate, room characteristics, noise levels, distortion, and word alignment.
    *   *Languages*: 5 languages.
    *   *Size*: 50 Million instruction-response examples (14K hours of total audio).

---

## 3. Evaluated Models & Inference Configuration
*   **Model Baselines**: Evaluated against current state-of-the-art open-source speech-text LLMs (e.g., Whisper-LLaMA variants, Speech-LLaMA baselines).
*   **Proposed Model**: **SIFT-LLM** (Speech Instruction Fine-Tuned LLM).

---

## 4. Metric Functions & Evaluation Pipeline

| Task | Metric | Tool / Package | Direction | Focus |
|---|---|---|---|---|
| **Automatic Speech Recognition (ASR)** | WER | `jiwer` | ↓ | Baseline transcript accuracy |
| **Speech Instruction Following** | EvalSIFT Score | Custom Benchmark | ↑ | Accuracy of following spoken constraints |

---

## 5. BibTeX Citation

**For ACL anthology venues (natbib format):**
```bibtex
@inproceedings{pandey2025sift,
  title     = {{SIFT}-50{M}: A Large-Scale Multilingual Dataset for Speech Instruction Fine-Tuning},
  author    = {Pandey, Prabhat and Swaminathan, Rupak Vignesh and Girish, K. V. Vijay and Sen, Arunasish and Xie, Jian and Strimel, Grant P. and Schwarz, Andreas},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  year      = {2025},
  publisher = {Association for Computational Linguistics},
  url       = {https://arxiv.org/abs/2504.09081}
}
```

**Before official publication (cite as arXiv preprint):**
```bibtex
@misc{pandey2025sift,
  title         = {{SIFT}-50{M}: A Large-Scale Multilingual Dataset for Speech Instruction Fine-Tuning},
  author        = {Prabhat Pandey and Rupak Vignesh Swaminathan and K. V. Vijay Girish and Arunasish Sen and Jian Xie and Grant P. Strimel and Andreas Schwarz},
  year          = {2025},
  eprint        = {2504.09081},
  archivePrefix = {arXiv},
  primaryClass  = {eess.AS}
}
```
