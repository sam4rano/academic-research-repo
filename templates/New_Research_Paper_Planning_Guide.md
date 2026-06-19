# New Research Paper Planning Guide

Follow these phases sequentially when planning, designing, and launching a new research project (MODE B).

---

## Phase 0: Problem Discovery & Formulation
*   **Gap Identification**: Research existing literature to ensure your idea is novel. Identify a specific deficiency in current models, datasets, or evaluation methodologies.
*   **Research Questions (RQs)**: Write 2–3 precise research questions you want your experiments to answer.
    *   *Example*: *RQ1: How does microphone noise influence the intent classification accuracy of multi-modal speech models?*

---

## Phase 1: Contribution Design
*   **Contribution Statement**: Formulate a single, high-level summary of your project's value.
    *   *Format*: *"We introduce [Name], the first [dataset/method/model] that enables [capability], demonstrating a [improvement]% performance change over prior methods."*
*   **Novelty Check**: Write down the closest 3 papers and explain exactly how your project differs.

---

## Phase 2: Dataset & System Design
*   **Collection Protocol**: If collecting data, document the quality control steps:
    *   Who are the annotators/speakers?
    *   Are prompts decoupled from task inputs?
    *   How will you normalize formats (e.g., audio sample rates, video aspect ratios)?
*   **Modality Blueprint**: Map out target inputs and expected outputs.

---

## Phase 3: Experiment Design

### 3.1 Hypothesis Matrix
*   For **every** research question (RQ), write one falsifiable hypothesis in the form:
    *   *"If [intervention], then [outcome], because [mechanism]."*

### 3.2 Baselines
*   Select at least **3 state-of-the-art** baseline models or methods for comparison.
*   Include at least one **simple/naive baseline** (e.g. majority class, identity function) as a lower bound.
*   Document each baseline's source (paper citation + Hugging Face ID or checkpoint URL).

### 3.3 Ablation Design
*   Plan ablations *before* running experiments: decide which components to remove/swap to isolate the effect of each contribution.
*   Record the ablation plan as a table: `| Ablated Component | Expected Effect | Justification |`

### 3.4 Metric Selection
*   Pick robust, standard, and **human-correlated** evaluation metrics.
*   For every task, specify: metric name, tool/library, direction (↑/↓), and what range is considered "good".
*   Use the quick reference in `SKILL.md` or `README.md` as a starting point.
*   **Avoid single-metric evaluation** — use at least 2 metrics from different families (e.g. CometKiwi + BLEU, not just BLEU).

    | Task | Metric | Tool | Direction | Human-correlated? |
    |------|--------|------|-----------|-------------------|
    | | | | ↑ / ↓ | Yes / No |

---

## Phase 4: Implementation Scaffolding
*   **Directory Structure**: Set up clean repository folders:
    ```
    project/
    ├── configs/            # Experiment config files (YAML / JSON)
    ├── data_storage/
    │   ├── raw/
    │   ├── processed/
    │   └── splits/
    ├── evaluation/
    │   └── outputs/        # Auto-created by runner.py
    ├── models/
    ├── src/
    ├── templates/
    ├── .gitignore          # Must exclude data_storage/, evaluation/outputs/, .venv/
    ├── LICENSE
    ├── runner.py
    └── requirements.txt
    ```
*   **Scaffolding Scripts**: Create skeleton scripts for loading data, wrapping inference, and calculating metrics.
*   **Verify**: Run `python runner.py --dry_run --seed 42` to confirm the end-to-end pipeline produces `evaluation/outputs/predictions.json` and `evaluation/outputs/metrics.json` without errors.

---

## Phase 5: Visualizations & Analytics Plan
*   **Table Plan**: Sketch the structure of the main evaluation tables before running experiments.
*   **Figure Plan**: Define what charts/plots will visualize results (e.g. line graph showing accuracy vs noise level).

---

## Phase 6: Paper Structure & Writing

> ⚠️ **Different venues have fundamentally different requirements.** Always identify
> your target venue **before** you start writing. The wrong template, citation style,
> or missing mandatory section will result in a desk reject.

### 6.1 Choose Your Target Venue First

Determine the venue type and look up the current year's call for papers (CFP):

| Venue Type | Examples | Typical Properties |
|-----------|----------|-------------------|
| **NLP / CL conference** | ACL, EMNLP, NAACL, EACL, COLING | ACL Anthology format, ARR review, Limitations + Ethics mandatory |
| **ML / AI conference** | NeurIPS, ICML, ICLR | NeurIPS/ICML LaTeX style, double-blind, appendix-heavy |
| **Speech conference** | INTERSPEECH, ICASSP, SLT | 4-page limit (INTERSPEECH), IEEE format (ICASSP/SLT) |
| **Vision conference** | CVPR, ECCV, ICCV | CVPR LaTeX style, supplementary material common |
| **AI general** | AAAI, IJCAI | AAAI Press format, 7+1 pages typical |
| **Journal** | TACL, JMLR, IEEE TASLP, CSL | Longer format (12–25 pages), revision rounds, no page panic |
| **Workshop** | ACL workshops, NeurIPS workshops | Often 4–6 pages, non-archival, looser formatting |
| **Preprint** | arXiv | No page limit, no review, any LaTeX style; cite as `@misc` |

### 6.2 Venue Quick Reference — Formatting & Requirements

| Requirement | ACL / EMNLP / NAACL | NeurIPS / ICML / ICLR | INTERSPEECH | ICASSP / SLT (IEEE) | AAAI | CVPR | Journal (TACL / JMLR) |
|------------|---------------------|----------------------|-------------|---------------------|------|------|----------------------|
| **LaTeX template** | `acl2024.sty` (ACL Anthology) | `neurips_2024.sty` | ISCA template | IEEE conference template | AAAI Press `.sty` | CVPR template | Venue-specific |
| **Page limit (main)** | 8 (long) / 4 (short) | 9 | 4 | 4 (+1 refs) | 7 (+1 refs) | 8 | 12–25 (varies) |
| **Appendix / supplementary** | Unlimited appendix (same PDF) | Supplementary ZIP | Not standard | 1-page supplement | 2 pages | Supplementary ZIP | Appendix in paper |
| **Citation style** | `\citep` / `\citet` (natbib) | `\citep` / `\citet` (natbib) | Numbered `[1]` | Numbered `[1]` (IEEE) | Author-year | `\cite{}` | Varies |
| **Bibliography format** | `.bbl` / ACL Anthology BibTeX | `.bbl` / natbib | ISCA `.bst` | `IEEEtran.bst` | AAAI `.bst` | Venue `.bst` | Venue `.bst` |
| **Blind review?** | Yes (ARR) | Yes | Yes | Yes | Yes | Yes | Often yes |
| **Mandatory "Limitations"** | ✅ Yes (since ACL 2023) | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Mandatory "Ethics"** | ✅ Yes (since ACL 2023) | ✅ "Broader Impact" | ❌ No | ❌ No | ✅ Yes | ❌ No | Sometimes |
| **Reproducibility checklist** | ✅ Mandatory | ✅ Mandatory | ❌ No | ❌ No | ❌ No | ❌ No | Sometimes |
| **Review system** | ACL Rolling Review (ARR) → commitment | OpenReview | CMT / internal | CMT | EasyChair / CMT | CMT | Editorial board |
| **Anonymous period** | Strict (no arXiv during review) | No restriction | No restriction | Check CFP | Check CFP | No restriction | Check CFP |

> **⚠️ Always re-read the current year's CFP.** Requirements change year to year.
> E.g., ACL 2023 introduced mandatory "Limitations" sections; NeurIPS 2023 added
> "Broader Impact" requirements that 2021 didn't have.

### 6.3 Section Outline by Venue Family

#### ACL / EMNLP / NAACL (NLP Conferences)

```
1. Introduction
2. Related Work
3. [Method / Dataset / System]       ← name by contribution type
4. Experimental Setup
   4.1 Data
   4.2 Baselines
   4.3 Evaluation Metrics
5. Results
6. Analysis / Discussion
7. Conclusion
--- (not counted in page limit) ---
Limitations                           ← MANDATORY (ACL 2023+)
Ethics Statement                      ← MANDATORY (ACL 2023+)
Acknowledgements
References
Appendix A, B, ...                    ← Unlimited (same PDF)
```

**ACL-specific edge cases:**
- **ARR (ACL Rolling Review)**: Papers are reviewed by ARR, then "committed" to a specific venue (ACL, EMNLP, NAACL). The same paper can be committed to multiple deadlines if not accepted.
- **Short vs. Long paper**: Short papers (4 pages) are *not* just a truncated long paper — they must make a focused, self-contained contribution.
- **Anonymous submission period**: Do NOT post on arXiv or social media during review. ACL has strict anonymity policies. Check the current CFP for exact dates.
- **"Findings" track**: Papers not accepted to the main conference may be offered "Findings" (published in ACL Anthology but no talk slot). This is a legitimate publication venue.
- **Citation format**: `\citet{jones2023}` for "Jones et al. (2023) showed..." and `\citep{jones2023}` for "(Jones et al., 2023)". Use `\citet` in the subject position.
- **Required Reproducibility checklist**: Must be filled out and submitted via the system.

#### NeurIPS / ICML / ICLR (ML Conferences)

```
1. Introduction
2. Related Work                       ← can be at end in NeurIPS
3. [Method / Approach / Framework]
4. Theoretical Analysis               ← if applicable
5. Experiments
   5.1 Setup
   5.2 Main Results
   5.3 Ablation Studies
   5.4 Analysis
6. Conclusion
--- (supplementary material) ---
Broader Impact Statement              ← NeurIPS strongly encouraged
Reproducibility Checklist              ← Mandatory (NeurIPS/ICML)
Appendix (proofs, extra figures)
```

**ML conference-specific edge cases:**
- **OpenReview**: NeurIPS and ICLR use OpenReview. Reviews, author responses, and final decisions are publicly visible (ICLR) or become visible after decisions (NeurIPS).
- **arXiv allowed**: Unlike ACL, most ML venues allow arXiv pre-prints during review.
- **Appendix-heavy culture**: It's common to have 20+ pages of supplementary. Reviewers are not obligated to read it, so the main paper must stand alone.
- **"Related Work" placement**: NeurIPS culture often puts Related Work at the end or in the introduction. ICML and ICLR prefer it after the introduction.
- **Theoretical contributions**: Proofs go in the appendix; state theorem + proof sketch in the main paper.
- **Negative results**: NeurIPS has a "Datasets & Benchmarks" track and has welcomed negative-result papers.

#### INTERSPEECH / ICASSP / SLT (Speech/Audio Conferences)

```
1. Introduction
2. Related Work
3. Method / Proposed System
4. Experimental Setup
   4.1 Data
   4.2 Implementation Details
5. Results and Discussion
6. Conclusion
7. References
```

**Speech conference edge cases:**
- **INTERSPEECH**: Strict **4-page** limit (references included). This forces extremely concise writing. No appendix or supplementary material is standard.
- **ICASSP (IEEE)**: **4 pages + 1 page** for references only. Uses IEEE double-column format.
- **SLT**: IEEE format, similar to ICASSP but with more focus on spoken language technology.
- **IEEE citation style**: Numbered references `[1]`, `[2]` in order of appearance. Do NOT use author-year format.
- **IEEEtran.bst**: Use this for bibliography formatting. Entries look like:
  ```bibtex
  @inproceedings{zufle2026dowis,
    author    = {Z{\"u}fle, Maike and Papi, Sara ...},
    title     = {Do What I Say: ...},
    booktitle = {Proc. INTERSPEECH 2026},
    year      = {2026},
    pages     = {1--4}
  }
  ```
- **Audio demonstrations**: INTERSPEECH and ICASSP allow linking to demo pages with audio samples. Create a GitHub Pages demo site if your paper involves audio.

#### CVPR / ECCV / ICCV (Vision Conferences)

```
1. Introduction
2. Related Work
3. Method
4. Experiments
   4.1 Datasets and Metrics
   4.2 Implementation Details
   4.3 Comparisons with State-of-the-Art
   4.4 Ablation Study
5. Conclusion
Acknowledgements
References
--- (supplementary PDF + video) ---
```

**Vision conference edge cases:**
- **Supplementary material**: Often includes a separate PDF + video. Reviewers may or may not watch the video.
- **Qualitative results**: Vision papers are expected to have visual figure comparisons (input → baseline → yours → ground truth).
- **8-page limit**: CVPR main paper is 8 pages excluding references. Tables and figures are often dense.
- **Citation format**: CVPR uses `\cite{}` with numbered references.

#### AAAI / IJCAI (General AI)

```
1. Introduction
2. Related Work
3. [Problem Formulation / Preliminaries]
4. Proposed Method
5. Experiments
6. Conclusion
Ethics Statement                      ← AAAI requires this
References
Appendix (2 pages max)
```

**AAAI-specific edge cases:**
- **7+1 format**: 7 pages content + 1 page references only. Appendix limited to 2 pages.
- **Ethics Statement**: AAAI requires an ethics statement since 2021. It does NOT count towards the page limit.
- **Reproducibility**: AAAI encourages (but doesn't mandate) a reproducibility appendix.

#### Journals (TACL, JMLR, IEEE TASLP, Computer Speech & Language)

```
1. Introduction
2. Related Work                       ← typically more thorough than conferences
3. [Method / System / Dataset]
4. Experimental Framework
5. Results
6. Discussion                         ← separate from Results
7. Conclusion
Acknowledgements
References
Appendices
```

**Journal-specific edge cases:**
- **No page panic**: Journals allow 12–25 pages. Use the space for more thorough related work, detailed analysis, and comprehensive tables.
- **Revisions**: Expect 1–3 revision rounds. Each round comes with reviewer comments to address. Write a detailed **response letter** mapping each comment to a specific change.
- **Discussion vs. Results**: Journals typically expect a separate "Discussion" section interpreting results in broader context, unlike conferences which often merge "Results and Discussion".
- **TACL**: Published in ACL Anthology but reviewed like a journal. Accepts "long-form" papers. No page limit, but typical submissions are 10–14 pages.
- **JMLR**: Focuses on machine learning theory and methodology. Longer, more formal. Published online, open access.
- **IEEE TASLP**: IEEE Transactions on Audio, Speech, and Language Processing. Uses IEEE journal format (single-column review, double-column final). Revision cycles can be 6–12 months.
- **Computer Speech & Language (CSL)**: Elsevier. Uses Elsevier LaTeX template. Impact factor matters for some institutions.

### 6.4 Citation Style Quick Reference

Different venues use different BibTeX entry types and formatting:

| Source Type | BibTeX Entry | When to Use | Key Fields |
|------------|-------------|-------------|------------|
| Conference paper | `@inproceedings` | Published in conference proceedings | `author`, `title`, `booktitle`, `year`, `pages` |
| Journal article | `@article` | Published in a peer-reviewed journal | `author`, `title`, `journal`, `year`, `volume`, `number`, `pages` |
| arXiv preprint | `@misc` or `@article` | Not yet peer-reviewed | `author`, `title`, `year`, `eprint`, `archivePrefix`, `primaryClass` |
| Workshop paper | `@inproceedings` | Published in workshop proceedings | Same as conference + workshop name in `booktitle` |
| Thesis | `@phdthesis` / `@mastersthesis` | Degree thesis | `author`, `title`, `school`, `year` |
| Dataset | `@misc` or `@dataset` | Citing a published dataset | `author`, `title`, `year`, `howpublished`, `url` |
| Software / Library | `@software` or `@misc` | Citing a tool or library | `author`, `title`, `year`, `url`, `version` |
| Book | `@book` | Published book | `author`, `title`, `publisher`, `year` |
| Book chapter | `@incollection` | Chapter in an edited book | `author`, `title`, `booktitle`, `publisher`, `year`, `pages` |
| Technical report | `@techreport` | Company / lab internal report | `author`, `title`, `institution`, `year`, `number` |

**arXiv citation edge case:**
```bibtex
% Correct arXiv citation (before peer review):
@misc{jones2024method,
  title         = {A New Method for X},
  author        = {Jones, A. and Smith, B.},
  year          = {2024},
  eprint        = {2401.12345},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}

% After publication — update to the published version:
@inproceedings{jones2024method,
  title     = {A New Method for X},
  author    = {Jones, A. and Smith, B.},
  booktitle = {Proceedings of ACL 2024},
  year      = {2024},
  pages     = {100--110}
}
```

> **Rule**: Always cite the **published version** if one exists. Citing an arXiv
> preprint when the conference/journal version is out signals that you didn't
> do a thorough literature review.

### 6.5 Mandatory & Optional Sections Checklist

Use this to avoid desk rejects by missing required sections:

| Section | ACL/EMNLP | NeurIPS/ICML | INTERSPEECH | ICASSP | AAAI | CVPR | Journal |
|---------|-----------|-------------|-------------|--------|------|------|---------|
| Abstract | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Introduction | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Related Work | ✅ | ✅ (flexible placement) | ✅ | ✅ | ✅ | ✅ | ✅ (thorough) |
| Limitations | **✅ MANDATORY** | ❌ optional | ❌ | ❌ | ❌ | ❌ | ❌ optional |
| Ethics Statement | **✅ MANDATORY** | ✅ Broader Impact | ❌ | ❌ | **✅ MANDATORY** | ❌ | Sometimes |
| Reproducibility Checklist | **✅ MANDATORY** | **✅ MANDATORY** | ❌ | ❌ | ❌ encouraged | ❌ | Sometimes |
| Acknowledgements | ✅ (after de-anonymisation) | ✅ (after de-anonymisation) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Author Contributions | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ (some journals) |
| Conflict of Interest | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ (journals) |

### 6.6 Writing Style Differences

| Dimension | Conference Paper | Journal Paper | Workshop Paper |
|-----------|-----------------|---------------|----------------|
| **Tone** | Concise, every sentence counts | More room for nuance and context | Can be exploratory, work-in-progress |
| **Related Work depth** | 0.5–1 page, focus on direct comparisons | 2–4 pages, comprehensive survey | 0.5 page, highlight key references |
| **Intro structure** | Problem → gap → contribution → outline | Problem → context → motivation → gap → contribution | Problem → early results → plan |
| **How many baselines?** | 3–5 strong baselines | 5–10+ (more comprehensive) | 1–3 |
| **Ablation expectation** | Encouraged, 1–2 key ablations | Expected, thorough | Nice to have |
| **Figure quality** | Publication-ready (vector PDF) | Publication-ready + higher DPI | Acceptable quality |
| **Self-citation** | Careful — anonymised during review | Normal — help reviewers trace your work | Normal |

### 6.7 Abstract Drafting

Write a draft abstract following this structure (adapt word count to venue):

```
[PROBLEM] — What gap exists? (1–2 sentences)
[METHOD]  — What did you do about it? (2–3 sentences)
[RESULTS] — What did you find? (1–2 sentences, with numbers)
[IMPACT]  — Why does it matter? (1 sentence)
```

**Word limits by venue:**
- ACL / EMNLP: ~200 words
- NeurIPS / ICML: ~250 words (TL;DR optional in OpenReview)
- INTERSPEECH: ~200 words
- ICASSP: ~150 words (very tight)
- AAAI: ~150 words
- Journals: ~250–350 words

---

## Phase 7: Release Preparation
*   **Dataset Card**: Create a Hugging Face README documenting data split sizes, demographics, license, and usage instructions.
*   **GitHub README**: Outline setup requirements, environment files, and a **single command** to reproduce key results.
*   **Ethics / IRB**: If the dataset involves human participants (recordings, annotations, surveys), document IRB approval or equivalent ethics review status.
*   **Citation File**: Add a `CITATION.cff` (Citation File Format) to the repository so tools like GitHub and Zenodo can auto-generate citations.
*   **Versioning**: Tag the release commit (`git tag v1.0.0`) and upload a Zenodo DOI for long-term archival.
