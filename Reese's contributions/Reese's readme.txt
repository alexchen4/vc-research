========================================================
VC COI Research — End-to-End Processing Pipeline
========================================================

***this is a brief readme generated with help from ChatGPT to aid in replication from my coding
produced on 8-18-2025
last edited 8-18-2025
***


Goal:
Convert incorporation PDFs → clean text → batch LLM extraction → 
aggregate structured outputs for analysis and replication.

--------------------------------------------------------
Repository Structure
--------------------------------------------------------

/Code
    pdf_convert.ipynb
    spellchecker.ipynb
    makebatch.ipynb
    download_outs.ipynb
    postprocessing.ipynb

/batch1, /batch2, ...                # Input PDFs by group
/batch1_text_readable                # OCR-readable text
/batch1_text_unreadable              # OCR-unreadable text
/batch1_spellcheck                   # Spell-checked text

/batches/batch1, /batches/batch2, ...   # JSONL request batches for OpenAI
/downloaded_batches/                    # Downloaded batch outputs + final CSV
    combined_extracted_data.csv

--------------------------------------------------------
Prerequisites
--------------------------------------------------------

- Python 3.10+
- Jupyter Notebook or Lab
- pytesseract (Tesseract 5+ with language packs, e.g., eng)
- OpenAI API access and key

Setup Example:
    python -m venv .venv
    source .venv/bin/activate    # Windows: .venv\Scripts\activate
    pip install pytesseract
    export OPENAI_API_KEY=...    # Windows (Powershell): $env:OPENAI_API_KEY="..."

--------------------------------------------------------
Pipeline Overview
--------------------------------------------------------

1. Convert PDFs → text (OCR)
2. Spell-check & clean text
3. Build API batches (.jsonl) & submit
4. Download batch outputs (.jsonl)
5. Append all outputs → one CSV

Each step is a standalone notebook and can be re-run independently.

--------------------------------------------------------
Step 1 — PDF OCR
--------------------------------------------------------

Notebook: Code/pdf_convert.ipynb
Input: batch1, batch2, ...
Output:
    - batch1_text_readable/*.txt
    - batch1_text_unreadable/*.txt

Notes:
    - OCR threshold = 0.7
        • 30% weight: English vocab coverage
        • 70% weight: Tesseract confidence
    - Files below threshold go into *_unreadable folders.

--------------------------------------------------------
Step 2 — Spell-check
--------------------------------------------------------

Notebook: Code/spellchecker.ipynb
Input: batch1_text_readable/*.txt
Output: batch1_spellcheck/*.txt

Notes:
    - Normalizes quotes, hyphens, and spacing
    - Fixes common OCR artifacts
    - No QC logs produced

--------------------------------------------------------
Step 3 — Make Batches for OpenAI
--------------------------------------------------------

Notebook: Code/makebatch.ipynb
Input: batch1_spellcheck/*.txt
Output: batches/batch1/batch_*.jsonl (request files)

Notes:
    - Groups text files into JSONL batch requests
    - Submits to OpenAI API
    - Includes custom ID fields for later merging

--------------------------------------------------------
Step 4 — Download Batch Outputs
--------------------------------------------------------

Notebook: Code/download_outs.ipynb
Input: OpenAI batch job IDs
Output: downloaded_batches/batch_*_out.jsonl

Notes:
    - Polls and retrieves completed outputs
    - Saves JSONL outputs for each batch
    - No QC artifacts/logs produced

--------------------------------------------------------
Step 5 — Post-processing & Append
--------------------------------------------------------

Notebook: Code/postprocessing.ipynb
Input: downloaded_batches/*.jsonl
Output: downloaded_batches/combined_extracted_data.csv

Notes:
    - Parses JSONL into flat CSV
    - Expands nested fields (e.g., preferred stock terms)
    - Stores verbatim quotes from source documents
    - Final column list/schema not documented yet

--------------------------------------------------------
Re-running the Whole Pipeline
--------------------------------------------------------

You can run notebooks manually in order or automate with Papermill:

    pip install papermill

    papermill Code/pdf_convert.ipynb Code/_out/pdf_convert.out.ipynb
    papermill Code/spellchecker.ipynb Code/_out/spellchecker.out.ipynb
    papermill Code/makebatch.ipynb Code/_out/makebatch.out.ipynb
    papermill Code/download_outs.ipynb Code/_out/download_outs.out.ipynb
    papermill Code/postprocessing.ipynb Code/_out/postprocessing.out.ipynb

--------------------------------------------------------
Quality Checks
--------------------------------------------------------

Currently not implemented. Suggested checks include:
    - OCR QC: confidence/coverage logs
    - Spell-check QC: replacement counts
    - Batch QC: error/retry logs
    - Parse QC: “Uncertain” rates and schema validation

--------------------------------------------------------
Reproducibility Notes
--------------------------------------------------------

- Pin Python + package versions in requirements.txt (not yet created)
- Save run logs if possible (not currently implemented)
- Version control the prompt used for OpenAI batches
- Do not commit API keys

--------------------------------------------------------
FAQ
--------------------------------------------------------

Q: Why do some CSVs contain “â€œ” artifacts?
A: Ensure UTF-8 encoding; normalize quotes during spell-check.

Q: What if PDFs won’t OCR well?
A: Adjust DPI (300–400), tweak Tesseract settings, or place 
   outputs in *_unreadable folders for separate handling.

--------------------------------------------------------
License & Data Access
--------------------------------------------------------

License not yet specified.
Data is proprietary and should not be committed to public repos.
