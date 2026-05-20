# AI Forward Deployed Engineering — Research Memo

> **A premium practitioner memo on the rise, evolution, and strategy of AI Forward Deployed Engineering.**  
> Covering Palantir, C3 AI, OpenAI, Anthropic, and Google Cloud — with a framework for the ideal FDE team and operating model.

---

## Overview

This repository contains the full research and drafting pipeline for a comprehensive memo on **AI Forward Deployed Engineering (FDE)** — one of the fastest-growing and least-understood functions in enterprise AI.

The memo analyzes the FDE landscape across five market leaders, surfaces the unresolved organizational and economic tensions these teams face, and proposes a framework for the ideal FDE pod structure and operating model.

**Primary Audience:** Enterprise AI leaders, GTM executives, and technical founders evaluating or building FDE capabilities.

---

## The Memo

📄 **[Read the full memo →](output/memo.md)**

The memo covers six sections:

| # | Section | Description |
|---|---------|-------------|
| 1 | **Origins & Definition** | The integration-and-outcomes gap; Palantir's historical blueprint; the Build-Prove-Generalize loop |
| 2 | **Competitive Landscape** | Five deployment models compared: Palantir, C3 AI, OpenAI, Anthropic, Google Cloud |
| 3 | **Foreseeable Challenges** | The pricing/profitability dilemma; the failure of engineering-only pods |
| 4 | **The Ideal FDE Pod** | The three-role model: Strategist, Engineer, Data Scientist |
| 5 | **The Ideal Operating Model** | Three operating imperatives: model-agnosticism, open-source portability, output-based pricing |

---

## Repository Structure

```
fde-memo/
├── AGENTS.md                        # AI agent coordination & architectural guidelines
├── README.md                        # This file
│
├── docs/
│   └── writing_style.md             # Tone, structure, and formatting guidelines
│
├── inputs/                          # Drop source PDFs or text files here for research
│
├── output/
│   ├── outline.md                   # Structured memo outline
│   └── memo.md                      # ✅ Final memo draft (6 sections, ~5,000 words)
│
├── reference/
│   ├── 2026 AI Observations.pdf     # Recent 2026 observations on AI engineering
│   └── Adobe - Field PM memo.pdf    # Structural reference: Adobe's Field PM memo
│
├── research/                        # Per-company research notes and job description analyses
│   ├── palantir_fde.md
│   ├── c3_ai_fde.md
│   ├── openai_fde.md
│   ├── anthropic_fde.md
│   ├── google_cloud_fde.md
│   ├── palantir_delta_jd.md
│   ├── palantir_echo_jd.md
│   ├── c3_ai_fde_jd.md
│   ├── c3_ai_fdds_jd.md
│   ├── c3_ai_ai_solution_manager_jd.md
│   ├── openai_fde_jd.md
│   ├── openai_ai_deployment_manager_jd.md
│   ├── anthropic_fde_jd.md
│   ├── anthropic_solutions_architect_jd.md
│   ├── google_cloud_fde_jd.md
│   └── google_cloud_ai_consultant_jd.md
│
├── skills/
│   ├── research_memo/
│   │   └── SKILL.md                 # End-to-end memo research & drafting workflow
│   └── scripts/
│       ├── export_docx.py           # Export memo to DOCX
│       └── export_pdf.py            # Export memo to PDF
│
└── tmp/                             # Temporary scripts and logs (not committed)
```

---

## Exporting the Memo

The memo can be exported to **DOCX** or **PDF** using the included scripts. Ensure dependencies are installed first:

```powershell
uv sync
```

### Export to DOCX

```powershell
uv run python skills/scripts/export_docx.py
```

### Export to PDF

```powershell
uv run python skills/scripts/export_pdf.py
```

Output files will be written to the `output/` directory.

---

## Workflow

```
inputs/          →   research/        →   output/outline.md   →   output/memo.md
(source PDFs)        (synthesized          (structured plan)       (final draft)
                      notes per company)
```

1. **Research & Synthesis** — Source materials in `reference/` and `inputs/` are analyzed; findings are documented in `research/` as per-company notes and job description breakdowns.
2. **Outlining** — Core themes and section structure are organized in `output/outline.md`.
3. **Drafting** — The full memo is written to `output/memo.md` following the style guide in `docs/writing_style.md`.
4. **Exporting** — The memo is compiled into a distributable format (DOCX/PDF) via `skills/scripts/`.

---

## Key Findings (TL;DR)

- The 2026 AI market is a **deployment competition**, not a model competition.
- FDE teams comprise **30–40% of total headcount** at deployment-native companies.
- No company has credibly solved the **FDE pricing and profitability dilemma**.
- The minimum viable FDE pod requires **three roles**: Strategist, Engineer, and Data Scientist.
- The ideal operating model is **open-source, model-agnostic, and priced on outputs** — not headcount.

---

*Research current as of May 2026.*
