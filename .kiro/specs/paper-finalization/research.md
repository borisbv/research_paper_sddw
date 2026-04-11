# Research and Discovery: Paper Finalization

## Conversion Tool: Pandoc
- **Version:** 3.9 (Installed).
- **Core Command:** 
  ```bash
  pandoc paper/manuscript_es.md -o paper/manuscript_es.docx --citeproc --bibliography=references/references.bib --csl=references/apa.csl --metadata-file=paper/metadata.yaml
  ```
- **CSL File:** Required `apa.csl` (APA 7th Edition) to be downloaded from Zotero repository.
- **Figures:** MD format `![Caption](path)` is required for automatic integration in DOCX.

## Translation Strategy
- **Tool:** `scientific-writing` skill + `generalist` agent for batch translation.
- **Style:** Academic English, preserving technical terms (*User Experience*, *Design Thinking*, *Thematic Analysis*).
- **Consolidation:** Sections will be translated individually and then merged into `manuscript_en.md`.

## Metadata Enrichment
- `paper/metadata.yaml` needs to be updated with `figureTitle`, `tableTitle`, and cross-ref templates if `pandoc-crossref` is used.
- For simple integration, captions will be hardcoded in the consolidated MD.

## Implementation Risks
| Risk | Mitigation |
| :--- | :--- |
| **CSL Missing** | Auto-download `apa.csl` using `web_fetch` or a simple `curl`. |
| **Image Paths** | Use relative paths from the root to ensure Pandoc finds `figures/*.jpg`. |
| **Translation Bias** | Use `scientific-critical-thinking` to review translated conclusions. |
