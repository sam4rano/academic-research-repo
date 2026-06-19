# Research Paper Analysis Template
> **Template version:** 1.0 | Derived from DOWIS methodology (arXiv:2603.09881)
> Fill in each section. Delete guidance text (in *italics*) before finalising.

---

## PAPER IDENTITY

| Field | Value |
|-------|-------|
| **Title** | |
| **Authors** | |
| **Venue / ArXiv** | *(Full venue name, e.g. "ACL 2025", "NeurIPS 2024", "INTERSPEECH 2026")* |
| **Venue Type** | *(NLP conf / ML conf / Speech conf / Vision conf / AI conf / Journal / Workshop / Preprint)* |
| **Year** | |
| **Domain** | *(e.g. NLP / Computer Vision / Speech / Multimodal)* |
| **License** | *(Dataset/Code license if applicable)* |
| **Code Repo** | |
| **Dataset** | |
| **My Reading Date** | |
| **Relevance to My Work** | *(High / Medium / Low — one sentence on why)* |

---

## 1. PROBLEM STATEMENT

### 1.1 The Core Problem
*In 2–3 sentences: what fundamental problem does this paper address? Frame it as a gap between what exists and what is needed.*

> [Write here]

### 1.2 Why Now?
*What made this problem tractable or urgent at the time of publication? (new hardware, new dataset, new model capability, etc.)*

> [Write here]

### 1.3 Prior Work Limitations

| Prior Work | Limitation |
|------------|-----------|
| | |
| | |
| | |

*Tip: These become your "Related Work" section when writing your own paper.*

### 1.4 Research Questions
*List the specific questions this paper sets out to answer (usually 2–4):*

1. RQ1:
2. RQ2:
3. RQ3:

---

## 2. KEY CONTRIBUTIONS

*What did this paper give the world? Be precise — "a dataset" is vague; "the first multilingual human-recorded spoken prompt dataset spanning 9 tasks and 11 languages" is precise.*

1.
2.
3.
4.

---

## 3. METHOD / SYSTEM DESIGN

### 3.1 High-Level Approach
*One paragraph describing what the system/method does:*

> [Write here]

### 3.2 Step-by-Step Pipeline

*List each step in the exact order the authors follow. For each step, note the input, transformation, and output.*

| Step | Input | Transformation | Output |
|------|-------|----------------|--------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### 3.3 Key Design Decisions & Justifications

*For each design choice, explain what it is and why the authors made it:*

| Decision | Rationale |
|----------|-----------|
| | |
| | |
| | |

### 3.4 Architecture / System Diagram
*Sketch or describe the system architecture here. Use ASCII or describe in prose.*

```
[Input] → [Component A] → [Component B] → [Output]
                ↕
          [Data Store]
```

---

## 4. DATASET

### 4.1 Dataset Overview

| Dimension | Value |
|-----------|-------|
| **Name** | |
| **Size** | *(rows, files, hours, tokens, etc.)* |
| **Languages** | |
| **Domains** | |
| **License** | |
| **Splits** | *(train / dev / test + sizes)* |
| **Public?** | |

### 4.2 Collection Process
*How was the data collected? Manual annotation, crowdsourcing, web scraping, human recording, synthesis?*

> [Write here]

### 4.3 Dataset Schema / Fields

| Field Name | Type | Description |
|------------|------|-------------|
| | | |
| | | |

### 4.4 Statistics (fill in numbers from the paper)

> [Tables, figures, or bullet points of dataset statistics]

### 4.5 Quality Control
*How did the authors ensure data quality? What were the annotator qualifications? Was there an inter-annotator agreement check?*

> [Write here]

---

## 5. EXPERIMENTS

### 5.1 Baselines & Models

| Model / Baseline | Description | Role in Experiments |
|------------------|-------------|---------------------|
| | | |
| | | |

### 5.2 Experimental Variables

| Variable | Type | Values |
|----------|------|--------|
| *(e.g. prompt modality)* | *(independent)* | *(text / speech)* |
| *(e.g. language)* | *(independent)* | *(en / de / it ...)* |
| *(e.g. prompt style)* | *(independent)* | *(basic / formal ...)* |
| *(e.g. performance score)* | *(dependent)* | *(WER / BERTScore ...)* |

### 5.3 Hardware & Compute

| Resource | Detail |
|----------|--------|
| GPU | |
| Batch size | |
| Inference params | |
| Training time | *(if applicable)* |

### 5.4 Evaluation Metrics

| Task | Metric | Tool/Library | Direction | Notes |
|------|--------|-------------|-----------|-------|
| | | | ↑ / ↓ | |
| | | | ↑ / ↓ | |
| | | | ↑ / ↓ | |

*For each metric, note: (a) what it measures, (b) its known limitations, (c) whether it correlates with human judgement.*

---

## 6. RESULTS

### 6.1 Main Results

*Copy the key results table(s) from the paper, or summarise in your own words.*

> [Table or summary here]

### 6.2 Key Findings

*For each finding, state it plainly and note the evidence:*

1. **Finding 1:** [State the finding] → Evidence: [metric / table / figure]
2. **Finding 2:** [State the finding] → Evidence: [metric / table / figure]
3. **Finding 3:** [State the finding] → Evidence: [metric / table / figure]

### 6.3 Ablation Studies

| Ablated Component | Effect on Performance | Conclusion |
|-------------------|-----------------------|------------|
| | | |
| | | |

### 6.4 Error Analysis
*What kinds of errors does the system make? Are there failure modes or edge cases?*

> [Write here]

---

## 7. ANALYSIS (Paper's Own Deeper Dive)

### 7.1 What sub-analyses did the paper run?

> [Describe — e.g. "compared male vs female speaker prompts across 5 tasks"]

### 7.2 Figures / Visualisations

*For each figure in the paper, describe what it shows and why it matters:*

| Figure # | What It Shows | Key Takeaway |
|----------|---------------|--------------|
| | | |
| | | |
| | | |

### 7.3 Surprising or Counterintuitive Results
*What results went against the authors' (or your) expectations?*

> [Write here]

---

## 8. STRENGTHS

*What does this paper do particularly well? Consider: novelty, rigour, clarity, reproducibility, practical impact.*

1.
2.
3.
4.

---

## 9. WEAKNESSES & LIMITATIONS

*What does the paper not address? What could have been done differently?*

1.
2.
3.
4.

*Note: These become candidate research questions for your follow-up work.*

---

## 10. RELEVANCE TO MY RESEARCH

### 10.1 Direct Applicability

*How can I use this paper's methods, data, or findings directly in my own work?*

> [Write here]

### 10.2 Inspirations

*What new ideas does this paper spark for my own research?*

1.
2.
3.

### 10.3 What I Would Do Differently

*If I were extending or replicating this paper, what changes would I make?*

> [Write here]

### 10.4 Citations I Need to Follow Up

*Papers in the reference list that I should also read:*

- [ ]
- [ ]
- [ ]

---

## 11. RELATED WORK MAP

*Where does this paper sit in the broader literature? Build a mini-taxonomy:*

```
Research Area: [e.g. Speech LLM Evaluation]
│
├── Text-only evaluation benchmarks
│   ├── [Paper A]
│   └── [Paper B]
│
├── Spoken evaluation benchmarks
│   ├── [This paper: DOWIS]
│   └── [Other]
│
└── Synthesis-based evaluation
    └── [Other]
```

---

## 12. REPRODUCIBILITY CHECKLIST

| Item | Status | Notes |
|------|--------|-------|
| Code publicly available | ✅ / ❌ / ⚠️ | *(Link to repo)* |
| Dataset publicly available | ✅ / ❌ / ⚠️ | *(Link to dataset; note license restrictions)* |
| All hyperparameters reported | ✅ / ❌ / ⚠️ | *(learning rate, batch size, epochs, temperature, etc.)* |
| Hardware/compute budget reported | ✅ / ❌ / ⚠️ | *(GPU model, VRAM, total GPU-hours)* |
| Random seeds reported | ✅ / ❌ / ⚠️ | *(Seed value + how many runs averaged)* |
| Evaluation scripts provided | ✅ / ❌ / ⚠️ | *(Can I rerun their eval with one command?)* |
| Pre-trained model weights released | ✅ / ❌ / ⚠️ | *(HuggingFace ID, Zenodo DOI, or "not released")* |

**Venue-specific reproducibility requirements:**

| Venue | Reproducibility Requirement |
|-------|----------------------------|
| ACL / EMNLP (2023+) | Mandatory reproducibility checklist submitted with the paper |
| NeurIPS (2023+) | Mandatory reproducibility checklist in supplementary |
| ICML | Encouraged but not mandatory |
| INTERSPEECH / ICASSP | No formal checklist; but reviewers check for it |
| AAAI | Encouraged reproducibility appendix (2 pages max) |
| Journals | Varies; some require code/data availability statements |

---

## 13. HOW TO CITE THIS PAPER

### 13.1 Determine the Correct BibTeX Entry Type

| Published Where? | Use This Entry Type |
|-----------------|--------------------|
| Conference proceedings (ACL, NeurIPS, INTERSPEECH, CVPR, etc.) | `@inproceedings` |
| Journal (TACL, JMLR, IEEE TASLP, CSL, etc.) | `@article` |
| arXiv preprint (not yet peer-reviewed) | `@misc` |
| Workshop (ACL workshop, NeurIPS workshop, etc.) | `@inproceedings` |
| Dataset release | `@misc` or `@dataset` |
| PhD / Master's thesis | `@phdthesis` / `@mastersthesis` |

### 13.2 BibTeX Templates by Venue Type

**Conference paper** (ACL, EMNLP, NeurIPS, INTERSPEECH, CVPR, etc.):
```bibtex
@inproceedings{key2025,
  title     = {},
  author    = {},
  booktitle = {Proceedings of [Conference Full Name] [Year]},
  year      = {},
  pages     = {},
  publisher = {},
  url       = {},
  doi       = {}
}
```

**Journal article** (TACL, JMLR, IEEE TASLP, etc.):
```bibtex
@article{key2025,
  title   = {},
  author  = {},
  journal = {},
  year    = {},
  volume  = {},
  number  = {},
  pages   = {},
  doi     = {}
}
```

**arXiv preprint** (not yet published at a venue):
```bibtex
@misc{key2025,
  title         = {},
  author        = {},
  year          = {},
  eprint        = {2501.12345},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}
```

**Workshop paper:**
```bibtex
@inproceedings{key2025,
  title     = {},
  author    = {},
  booktitle = {Proceedings of the [N]th Workshop on [Topic] at [Conference]},
  year      = {},
  pages     = {},
  url       = {}
}
```

### 13.3 Common Citation Pitfalls

| Pitfall | Why It's Wrong | Fix |
|---------|---------------|-----|
| Citing arXiv when published version exists | Signals incomplete literature review | Always use the published version |
| Missing `booktitle` for conference papers | BibTeX will render incorrectly | Always include full proceedings name |
| Using `@article` for conference papers | Wrong entry type; confuses readers | Use `@inproceedings` for conferences |
| Inconsistent author name format | BibTeX may generate wrong short names | Use "Last, First and Last, First" consistently |
| Missing `pages` field | Some styles require it; looks incomplete | Add page numbers if available |
| Citing a retracted/withdrawn paper | Ethical and scientific concern | Always check paper status before citing |

---

## 14. MY OVERALL RATING

| Dimension | Score (1–5) | Comment |
|-----------|-------------|---------|
| Novelty | | |
| Technical Rigour | | |
| Clarity of Writing | | |
| Reproducibility | | |
| Practical Impact | | |
| **Overall** | | |

---

## 15. RAW NOTES

*Free-form space for notes while reading:*

> [Paste your notes here as you read the paper]

---

*Template by: Research Skill Suite v1.0 | Modelled on DOWIS (Züfle et al., 2026)*
