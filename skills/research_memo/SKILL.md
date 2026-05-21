---
name: research-memo
description: >-
  A custom agent skill to research and draft premium memos. It structures the process
  of style extraction, topic gathering, primary input analysis, multi-source research
  synthesis, outline formulation, and draft development.
---

# Research Memo Custom Skill

## Overview
This skill provides a systematic framework for conducting deep research on a specialized topic and producing a premium, operator-grade memo. It guides the agent through style alignment, topic gathering, scanning user-provided primary sources, executing target research, generating structured source-level findings, and drafting the final memo.

## Directory Structure
- `inputs/` - Primary source files (PDFs, text, etc.) provided by the user.
- `reference/` - Core structural references or style guides (e.g., *Tiger's Early 2026 AI Observations*, *Adobe - Field PM memo*).
- `docs/writing_style.md` - Synthesized style, tone, terminology, and structural rules.
- `research/` - Source-level research findings and raw extractions.
- `output/` - Final drafts and polished versions of the research memo.

## Workflow

### Step 1: Synthesize/Update Writing Style Guidelines
Check if `docs/writing_style.md` exists and is up to date with any files in the `reference/` folder. If not, analyze the references inside `reference/` to draft a style document detailing:
- **Tone**: Professional, operator-led, decisive, authoritative.
- **Structural Patterns**: Upfront summary, matrices, ranked competencies, actionable headings.
- **Style Conventions**: Define guidelines for terminology formatting, key structural highlights (explicitly avoiding horizontal separator lines "---" and developer-facing alert syntax like "[!IMPORTANT]"), and using clean standard blockquotes (starting with ">") instead.

### Step 2: Solicit Research Topics
Ask the user for the specific research topics or focal areas to cover in the memo. This ensures the research is targeted and fully aligned with their interests.

### Step 3: Scan Primary Source Inputs
Look in the `inputs/` folder for any manuals, PDFs, or files placed by the user. These represent the primary, highly trusted source material. If files exist:
- Extract key sections, tables, and frameworks.
- Ground all core arguments of the memo in these inputs first.

### Step 4: Perform Web & API Research
For each topic, perform targeted web searches and query specialized APIs (e.g., standard search, science/literature search if applicable).
For every key source identified, create a dedicated markdown file in `research/` with the filename matching the source (e.g., `research/palantir_fde.md`). Each file must use the following format:
1. **Source Citation**: Direct URL, title, or filename.
2. **Short Summary**: A concise 2-3 sentence overview of the source's main point.
3. **Raw Relevant Excerpts**: The original, verbatim text sections or quotes containing the crucial data points, metrics, and arguments.

### Step 5: Formulate & Align on Memo Outline
Ask the user to provide an outline for the research memo, or present a proposed outline based on the research findings for their feedback. Do not proceed to drafting until the outline is finalized.

### Step 6: Draft the Memo
Synthesize all findings from the `research/` folder and draft the final memo inside the `output/` directory (e.g., `output/AI_FDE_Memo_Draft.md`). The draft must strictly follow the tone, structural patterns, and terminology in `docs/writing_style.md`. Ensure that formatting artifacts such as separator lines (---) and visual alert callout flags (e.g., [!IMPORTANT], [!NOTE]) are avoided entirely in favor of a clean, premium executive layout with simple blockquotes (>) for highlighting profile definitions or key takeaways.

### Step 7: Export the Memo
Export the final draft markdown file to Word (DOCX) and PDF formats using the scripts inside `skills/scripts/`. Always run the export scripts using the markdown name (e.g. `output/memo.md` dynamically exports to `output/memo.docx` and `output/memo.pdf` in the same directory). Do NOT overwrite the reference source of truth files (such as `output/20260520_FDE_Evolution_Memo_vSHARED.docx`).

## Common Mistakes
- **Hype and Buzzwords**: Avoid speculative or overly promotional marketing language. Stick to clear, operator-grade insights.
- **Vague Citations**: In the research phase, always save exact source URLs or names along with the raw verbatim excerpts. Do not summarize from memory.
- **Unstructured Drafting**: Skipping Step 5 (Outline approval) leading to poorly organized or disjointed drafts.
- **Overwriting Source of Truth Files**: Always verify that you are exporting with the markdown name as output (e.g., `memo.docx` / `memo.pdf`) to protect client-shared reference versions.
