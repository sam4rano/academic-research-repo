# Multi-Paper / Experiment Comparison Tracker
> Use this to track and compare multiple papers, models, or experiment runs side by side.
> Derived from DOWIS evaluation design.

---

## PART 1: PAPER COMPARISON TABLE

Use this when you're surveying the field before writing a new paper.

| | Paper A | Paper B | Paper C | **Your Work** |
|---|---------|---------|---------|--------------|
| **Title** | | | | |
| **Year** | | | | |
| **Task(s)** | | | | |
| **Language(s)** | | | | |
| **Data** | | | | |
| **Model(s)** | | | | |
| **Primary Metric** | | | | |
| **Best Score** | | | | |
| **Prompt Modality** | Text/Speech | | | |
| **Prompt Diversity** | # styles | | | |
| **Human Evaluation?** | Y/N | | | |
| **Code Public?** | Y/N | | | |
| **Dataset Public?** | Y/N | | | |
| **Key Limitation** | | | | |
| **What we improve** | | | | |

---

## PART 2: EXPERIMENT RUN TRACKER

Use this to track individual experiment runs as you iterate.

| Run ID | Model | Task | Language | Prompt Type | Modality | Metric | Score | Notes |
|--------|-------|------|----------|------------|----------|--------|-------|-------|
| run_001 | | | | | | WER ↓ | | |
| run_002 | | | | | | | | |
| run_003 | | | | | | | | |

---

## PART 3: ABLATION TRACKER

| Component Removed | Effect on Metric | Δ vs Baseline | Conclusion |
|-------------------|-----------------|--------------|------------|
| | | | |
| | | | |

---

## PART 4: PER-LANGUAGE RESULTS GRID

Fill in for each language and condition. Inspired by DOWIS Table 1 / Figure 1.

| Language | Resource Level | Text Score | Speech Score | Gap (Text − Speech) | Direction |
|----------|---------------|------------|-------------|----------------------|-----------|
| en | High | | | | |
| de | High | | | | |
| it | High | | | | |
| fr | High | | | | |
| es | High | | | | |
| pt | Medium | | | | |
| nl | Medium | | | | |
| sv | Medium | | | | |
| cs | Medium | | | | |
| ru | Medium | | | | |
| hu | Low | | | | |
| **AVG** | — | | | | |

---

## PART 5: PROMPT STYLE RESULTS

| Task | Basic | Formal | Informal | Detailed | Short | Best Style | Worst Style |
|------|-------|--------|---------|---------|-------|-----------|------------|
| | | | | | | | |
| | | | | | | | |

---

## PART 6: MODEL COMPARISON

| Task | Metric | Model A | Model B | Model C | Winner |
|------|--------|---------|---------|---------|--------|
| ASR | WER ↓ | | | | |
| MT | CometKiwi ↑ | | | | |
| ST | CometKiwi ↑ | | | | |
| SQA | BERTScore ↑ | | | | |
| TSUM | BERTScore ↑ | | | | |
| SSUM | BERTScore ↑ | | | | |
| ACHAP | Collar-F1 ↑ | | | | |
| TTS | UTMOS ↑ | | | | |
| S2ST | CometKiwi ↑ | | | | |

---

## PART 7: DATASET COMPARISON

| | Dataset A | Dataset B | DOWIS | **Your Dataset** |
|---|----------|----------|-------|-----------------|
| **Tasks** | | | 9–11 | |
| **Languages** | | | 11–12 | |
| **Total rows** | | | 1,320 | |
| **Audio hours** | | | 3h17m | |
| **Human recorded?** | | | ✅ | |
| **Parallel modalities?** | | | ✅ | |
| **Prompt styles** | | | 5 | |
| **License** | | | CC-BY | |
| **Public?** | | | ✅ | |

---

## PART 8: FIGURE PLANNING SHEET

| Figure | Type | X-axis | Y-axis | Grouped by | Caption Draft | Status |
|--------|------|--------|--------|-----------|--------------|--------|
| Fig 1 | Bar | | | | | ☐ Draft ☐ Final |
| Fig 2 | Heatmap | | | | | ☐ Draft ☐ Final |
| Fig 3 | Line | | | | | ☐ Draft ☐ Final |
| Table 1 | — | — | — | — | | ☐ Draft ☐ Final |
| Table 2 | — | — | — | — | | ☐ Draft ☐ Final |

---

## PART 9: PAPER WRITING TRACKER

| Section | Owner | Status | Word Count | Notes |
|---------|-------|--------|-----------|-------|
| Abstract | | ☐ Not started ☐ Draft ☐ Final | | Write last |
| Introduction | | ☐ Not started ☐ Draft ☐ Final | | Write first |
| Related Work | | ☐ Not started ☐ Draft ☐ Final | | |
| Dataset / Method | | ☐ Not started ☐ Draft ☐ Final | | |
| Experiments | | ☐ Not started ☐ Draft ☐ Final | | |
| Analysis | | ☐ Not started ☐ Draft ☐ Final | | |
| Conclusion | | ☐ Not started ☐ Draft ☐ Final | | |
| References | | ☐ Not started ☐ Draft ☐ Final | | |
| Appendix | | ☐ Not started ☐ Draft ☐ Final | | |

---

## PART 10: SUBMISSION CHECKLIST

| Item | Status | Notes |
|------|--------|-------|
| Paper formatted for venue | ☐ | |
| Abstract ≤ word limit | ☐ | |
| Author list finalised | ☐ | |
| Contributions clearly stated | ☐ | |
| All claims have citations or evidence | ☐ | |
| Limitations section included | ☐ | |
| Ethical considerations addressed | ☐ | |
| arXiv preprint uploaded | ☐ | |
| Dataset released with license | ☐ | |
| Code repository made public | ☐ | |
| Evaluation scripts included | ☐ | |
| README with reproduction instructions | ☐ | |
| BibTeX citation provided | ☐ | |

---

*Multi-Paper Comparison Tracker v1.0 | Research Skill Suite | Modelled on DOWIS (Züfle et al., 2026)*
