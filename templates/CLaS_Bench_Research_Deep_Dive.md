# CLaS-Bench Research Deep Dive (Reference Guide)

This document serves as a complete paper analysis and reproducibility checklist for the CLaS-Bench (Gurgurov et al., 2026) paper.

---

## Paper & Repository Metadata
*   **Paper Title**: CLaS-Bench: A Cross-Lingual Alignment and Steering Benchmark
*   **Authors**: Daniil Gurgurov, Yusser Al Ghussin, Tanja Baeumel, Cheng-Ting Chou, Patrick Schramowski, Marius Mosbach, Josef van Genabith, Simon Ostermann
*   **Conference/Journal**: arXiv Preprint / ACL 2026
*   **Venue Type**: NLP / CL Conference (ACL format)
*   **Citation Style**: Author-Year (natbib `\citep` / `\citet` format)
*   **Page Limit**: 8 pages of content (excluding references/appendices)
*   **arXiv ID / Link**: [arxiv.org/abs/2601.08331](https://arxiv.org/abs/2601.08331)
*   **GitHub Repository**: [github.com/d-gurgurov/CLaS-Bench](https://github.com/d-gurgurov/CLaS-Bench)

---

## 1. Abstract & Core Contribution
*   **Problem Statement**: Language steering (manipulating internal representation hidden states during inference) is a promising and lightweight alternative to prompting or fine-tuning for cross-lingual adaptation. However, there has been no standardized benchmark or evaluation protocol to measure the trade-off between language control and semantic preservation across steering methods.
*   **Core Contribution/Solution**:
    1.  **CLaS-Bench**: The first standardized parallel question-answer benchmark spanning **32 languages** with 70 parallel questions per language (manually verified by native speakers).
    2.  **Multilingual Steering Evaluation**: Compares 7 steering methods (DiffMean, Probe-based vectors, Linear Discriminant Analysis (LDA), PCA, Language Activation Probability Entropy (LAPE) neurons, Sparse Autoencoders (SAEs), and prompting baselines).
    3.  **Unified Metric**: Combines Language Forcing Success (LFS) and Semantic Relevance into a single **Harmonic-Mean Steering Score**.
*   **Key Findings**:
    *   **DiffMean** (residual stream manipulation) achieves the highest average steering score (84.5%), significantly outperforming explicit prompting (67.7%).
    *   Prompting frequently fails for target languages like Tibetan, Farsi, and English (where the model ignores the instruction), whereas activation steering forces compliance.
    *   Language-specific hidden structures cluster by language family (e.g., Romance, Germanic, Slavic) and emerge predominantly in mid-to-later layers (layers 16–32).

---

## 2. Dataset & Data Loader Pipeline
*   **Dataset Schema**:
    *   *Source prompts ($x_s$)*: 70 open-ended parallel questions translated into 32 languages.
    *   *Target answer ($y_t$)*: Evaluated response forced into target language $t \in \mathcal{L}$.
    *   *Data Collection*: Translated from English via Google Translate API and proofread/corrected by native speaker annotators with backgrounds in computer science or linguistics.
*   **Steering Activations dataset**:
    *   Tokens used to compute vectors: 10M tokens per language from the **CulturaX** dataset (for DiffMean and LAPE) or 100K-500K tokens (for covariance-based methods like PCA/LDA).

---

## 3. Evaluated Models & Inference Configuration
*   **Evaluated Backbones**:
    *   `Llama-3.1-8B-Instruct`
    *   `Aya-Expanse-8B`
*   **Steering Intervention Configurations**:
    1.  **DiffMean ($\vec{\Delta}$)**: Adds the difference in activation means between target language $t$ and source/other languages to the residual stream:
        $$h'_l = h_l + \alpha (\boldsymbol{\mu}_{\text{tgt}} - \boldsymbol{\mu}_{\text{other}})$$
    2.  **LAPE (Neuron-based)**: Sets activations of language-selective MLP/attention neurons to target averages.
    3.  **Probes (Residual Stream)**: Adds weights ($\mathbf{w}_l$) of a binary classifier trained to separate target and negative language activations.
    4.  **LDA Vectors ($\mathbf{v}_l$)**: Uses Linear Discriminant Analysis to project activations onto the vector maximizing class separability.
    5.  **Sparse Autoencoder (SAE-DM)**: Steering features inside sparse autoencoder latent space (evaluated at layers 4, 12, 18, 20, and 25).

---

## 4. Metric Functions & Evaluation Pipeline

The steering capability is evaluated along two orthogonal dimensions, combined via a **Harmonic Mean**:

$$\text{Steering Score} = 2 \times \frac{\text{LFS} \times \text{SemPres}}{\text{LFS} + \text{SemPres}}$$

*   **Language Forcing Success (LFS)**: Measured using the **FastText Language Identification (LID)** classifier on the generated output to verify if the output matches target language $t$.
*   **Semantic Preservation (SemPres)**: Measured using **BERTScore F1** (normalized/scaled) comparing the steered output $y_t$ with reference parallel answers in language $t$ to ensure the answer's meaning is preserved.

---

## 5. Synthesis, Gaps & Next Steps

| Dimension | Detail |
|---|---|
| **Limitations identified by paper** | Varying data scales used to compute vectors (10M for DiffMean vs 100K for LDA); SAE evaluations limited to layers with public checkpoint availability; base models not evaluated. |
| **Open gaps (your read)** | The benchmark evaluates only single-turn steering; does not evaluate steering persistence in long-form generation (whether the model drifts back to English). |
| **Actionable next steps** | (1) Test steering persistence on paragraphs/long text; (2) Create steering vectors for low-resource African languages (e.g. Swahili, Zulu) using CulturaX segments. |

---

## 6. Reproducibility Checklist

| Item | Status | Notes |
|---|---|---|
| Code publicly available | ✅ | Hosted at `github.com/d-gurgurov/CLaS-Bench`. |
| Dataset publicly available | ✅ | Parallel questions files committed to the GitHub repo. |
| Evaluation models | ✅ | Standard Llama-3.1-8B-Instruct and Aya-Expanse-8B. |
| Evaluation pipeline | ✅ | Evaluated using standard FastText LID and BERTScore. |

---

## 7. BibTeX Citation

**For peer-reviewed conference publication:**
```bibtex
@inproceedings{gurgurov2026clas,
  title     = {{CLaS}-Bench: A Cross-Lingual Alignment and Steering Benchmark},
  author    = {Gurgurov, Daniil and Ghussin, Yusser Al and Baeumel, Tanja and Chou, Cheng-Ting and Schramowski, Patrick and Mosbach, Marius and van Genabith, Josef and Ostermann, Simon},
  booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},
  year      = {2026},
  publisher = {Association for Computational Linguistics},
  url       = {https://arxiv.org/abs/2601.08331}
}
```

**For arXiv pre-prints:**
```bibtex
@misc{gurgurov2026clas,
  title         = {{CLaS}-Bench: A Cross-Lingual Alignment and Steering Benchmark},
  author        = {Daniil Gurgurov and Yusser Al Ghussin and Tanja Baeumel and Cheng-Ting Chou and Patrick Schramowski and Marius Mosbach and Josef van Genabith and Simon Ostermann},
  year          = {2026},
  eprint        = {2601.08331},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}
```
