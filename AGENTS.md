# AI Forward Deployed Engineering (FDE) Memo Project

Welcome to the AI FDE Memo project. This project is dedicated to researching and drafting a comprehensive, premium memo on AI Forward Deployed Engineering, analyzing the role, responsibilities, evolution, and best practices of FDEs in the AI era.

## Project Structure
- `AGENTS.md` - Primary coordination document for AI agents, outlining project structure, documentation guidelines, and architectural boundaries.
- `.gitignore` - Standard ignore configuration for python environments, local IDE settings, and temp directories.
- `LICENSE` - Standard MIT License containing terms of reuse and distribution.
- `docs/` - General project documentation and guidelines.
  - `docs/writing_style.md` - Tone, structural patterns, and formatting guidelines for writing premium memos, synthesized from reference files.
- `inputs/` - Folder for the user to place primary source files (PDFs, text files, etc.) for target research.
- `output/` - Contains the final output documents, drafts, and rendered versions of the memo.
  - `output/outline.md` - The structured outline of the AI Forward Deployed Engineering memo.
  - `output/memo.md` - The full 5-6 page AI Forward Deployed Engineering memo draft, covering all six sections from the outline.
- `reference/` - Source materials, reference PDFs, articles, and documentation.
  - `reference/2026 AI Observations.pdf` - PDF document containing recent 2026 observations on AI engineering.
  - `reference/Adobe - Field PM memo.pdf` - PDF document containing Adobe's memo on Field Product Management, which serves as a structural reference.
- `research/` - Research notes, literature reviews, and synthesized findings about AI forward deployed engineering.
  - `research/palantir_fde.md` - Research on Palantir's FDE team structure (Deltas, Echos, Devs), purpose, roles, and profiles.
  - `research/c3_ai_fde.md` - Research on C3 AI's FDE team structure (FDEs, FDDSs, AI Solution Managers), purpose, and profiles.
  - `research/openai_fde.md` - Research on OpenAI's FDE evolution, Applied Engineering, and the newly formed OpenAI Deployment Company in May 2026.
  - `research/anthropic_fde.md` - Research on Anthropic's Applied AI FDE structure, Solutions Architects, and Enterprise Foundations.
  - `research/google_cloud_fde.md` - Research on Google Cloud's FDE team, Applied AI integration, and key differences vs. Solutions Engineering.
  - `research/palantir_delta_jd.md` - Job description for Palantir FDE ("Delta").
  - `research/palantir_echo_jd.md` - Job description for Palantir Deployment Strategist ("Echo").
  - `research/c3_ai_fde_jd.md` - Job description for C3 AI Forward Deployed Engineer (FDE).
  - `research/c3_ai_fdds_jd.md` - Job description for C3 AI Forward Deployed Data Scientist (FDDS).
  - `research/c3_ai_ai_solution_manager_jd.md` - Job description for C3 AI AI Solution Manager.
  - `research/openai_fde_jd.md` - Job description for OpenAI Forward Deployed Engineer (FDE).
  - `research/openai_ai_deployment_manager_jd.md` - Job description for OpenAI AI Deployment Manager (Technical Success Group).
  - `research/anthropic_fde_jd.md` - Job description for Anthropic Forward Deployed Engineer (FDE).
  - `research/anthropic_solutions_architect_jd.md` - Job description for Anthropic Solutions Architect (SA).
  - `research/google_cloud_fde_jd.md` - Job description for Google Cloud Forward Deployed Engineer (FDE).
  - `research/google_cloud_ai_consultant_jd.md` - Job description for Google Cloud AI Consultant (PSO).
- `skills/` - Custom skills and utilities for compiling and exporting draft memos.
  - `skills/research_memo/` - Custom skill outlining the end-to-end memo research and drafting workflow.
    - `skills/research_memo/SKILL.md` - Detailed workflow instructions and guidelines.
  - `skills/scripts/` - Script utilities for document conversions and reading.
    - `skills/scripts/export_docx.py` - Python script to compile and export the memo into DOCX format using the markdown name by default.
    - `skills/scripts/export_pdf.py` - Python script to compile and export the memo into PDF format using the markdown name by default.
    - `skills/scripts/read_docx.py` - Python script to parse and extract text from DOCX format to stdout or files.
    - `skills/scripts/read_pdf.py` - Python script to parse and extract text from PDF format to stdout or files.


## Workflow and Guidelines
1. **Research & Synthesis**: Process reference PDFs, search literature, and document core findings in `research/`.
2. **Drafting**: Create incremental drafts of the FDE memo inside `output/` following `docs/writing_style.md`.
3. **Refining & Reviewing**: Edit, structure, and polish the memo to high professional standards.
