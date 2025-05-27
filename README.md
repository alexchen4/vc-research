# VC-Research

## Overview  
**VC-Research** is an end-to-end pipeline for converting PDF certificates and related venture-capital documents into structured data. It combines:

- **OCR & Readability Classification**: Converts scanned PDFs to text and labels pages as “readable” or “unreadable” using Tesseract, pytesseract, and a composite confidence/readability score   
- **Basic Field Extraction**: Pulls out high-level metadata (Company Name, Date, Document Type, Preferred Stocks, Priority Order, Liquidation Value) from plain-text files via regex and SpaCy NER   
- **Document-Level Classification**: Trains a RandomForest classifier (TF-IDF + BERT embeddings) to detect which documents mention liquidation preferences   
- **Sentence-Level Tagging**: Fine-tunes a Sentence-Transformer and SciBERT model to tag and extract the exact sentences containing each key property   

---

## 🚀 Quickstart

1. **Clone the repository**  
   ```bash
   git clone https://github.com/alexchen4/vc-research.git
   cd vc-research
2. **Create & activate a Python 3.12.7 virtual environment**
    ```bash
    python3.12 -m venv venv
    source venv/bin/activate
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
4. **Launch notebooks in this order:**
    ```bash
    pdf_convert.ipynb
    time_series.ipynb
    liquidation.ipynb
    certificate_extraction.ipynb

## 📂 Repository Structure
```
vc-research/
├── pdf_convert.ipynb                  # OCR → text conversion + readability classification
├── time_series.ipynb                  # Basic metadata extraction pipeline
├── liquidation.ipynb                  # Doc-level classification & sentence tagging
├── certificate_extraction.ipynb       # Token-classification for exact field spans
├── Extracted Sentences - Batch 1.csv  # Heuristically labeled sentences (Batch 1)
├── Extracted_Information.csv          # Initial ML-extracted info summary
├── requirements.txt                   # Pinned Python dependencies
└── README.md                          # This file

data/
├── Batch1/                            # Raw PDF files (Batch 1)
├── Batch1_text_readable/              # OCR-readable `.txt` (Batch 1)
├── Batch1_text_unreadable/            # OCR-unreadable `.txt` (Batch 1)
├── Batch2/                            # Raw PDF files (Batch 2)
├── Batch2_text_readable/              # OCR-readable `.txt` (Batch 2)
├── Batch2_text_unreadable/            # OCR-unreadable `.txt` (Batch 2)
└── outputs/                           # Excel/CSV summaries & intermediates

models/
└── fine_tuned_bert/                   # Checkpoints & artifacts for BERT models

utils/
├── extraction.py                      # Regex & SpaCy NER extractors
├── labeling.py                        # Heuristic sentence-labeling tools
└── training.py                        # Fine-tuning scripts for transformers
```

## 🛠️ Environment & Dependencies
- Python: 3.12.7
- Key Libraries:
    - OCR & Imaging: pdf2image, pytesseract
    - NLP & Tokenization: nltk, spacy, sentence-transformers
    - ML & Deep Learning: scikit-learn, torch, transformers
    - Data Handling: pandas, numpy
    - Parallelism: concurrent.futures
See requirements.txt for full version details.

## 📝 Notebooks & Workflows
| Notebook                          | Description                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **pdf\_convert.ipynb**            | Converts PDFs → images → text; computes OCR confidence & word coverage; sorts into readable/unreadable |
| **time\_series.ipynb**            | Reads plain-text files and extracts core fields into a master DataFrame                                |
| **liquidation.ipynb**             | Builds TF-IDF + BERT features; trains & evaluates a RandomForest to flag liquidation-preference docs   |
| **certificate\_extraction.ipynb** | Fine-tunes SciBERT for BIO token-classification to pinpoint exact character spans for each field       |
