# VC-Research

## Overview
The **VC-Research** project automates text extraction and quality assessment for PDF files containing venture capital-related data. Utilizing Optical Character Recognition (OCR) with Tesseract and various data processing techniques, this project categorizes files based on readability to streamline data analysis workflows.

## ⚙️ Environment Setup

### Python Version

- **Python 3.12.7**

### Key Libraries

| Category                  | Library                | Purpose                                                                 |
|---------------------------|------------------------|-------------------------------------------------------------------------|
| OCR Engine                | `Tesseract`            | Recognizes text from scanned PDF images                                |
| PDF to Image Conversion   | `pdf2image`            | Converts PDF pages to images                                           |
| OCR Wrapper               | `pytesseract`          | Python wrapper for Tesseract                                           |
| Data Processing           | `pandas`, `numpy`      | Stores, analyzes, and filters extracted text                           |
| NLP & Tokenization        | `nltk`, `re`           | Tokenizes sentences and extracts key phrases                           |
| Sentence Embedding        | `sentence-transformers`| Embeds and ranks sentence similarity                                   |
| Model Training            | `torch`, `scikit-learn`| Fine-tuning sentence transformers and evaluating results               |
| Parallel Processing       | `concurrent.futures`   | Accelerates large-batch OCR processing                                 |

## Directory Structure
├── liquidation.ipynb                        # Main ML notebook for sentence classification and property extraction
├── pdf_convert.ipynb                        # Converts raw PDFs into readable/unreadable .txt files via OCR
├── Extracted Sentences - Batch 1.csv        # Annotated sentence-property training set
├── requirements.txt                         # Environment dependencies
├── data/
│   ├── Batch1/                              # Raw venture capital-related PDFs
│   ├── Batch1_text_readable/                # Text files extracted from machine-readable or high-quality OCR
│   ├── Batch1_text_unreadable/              # Low-confidence or failed OCR outputs
│   ├── Batch2/                              # New batch of raw PDF files for processing
│   ├── Batch2_text_readable/                # Readable text outputs from Batch 2
│   ├── Batch2_text_unreadable/              # Unreadable or noisy outputs from Batch 2
│   └── outputs/                             # Intermediate CSVs, final structured outputs, model embeddings, etc.
├── models/
│   └── fine_tuned_bert/                     # Optional: Folder for saving fine-tuned model checkpoints
├── utils/
│   ├── extraction.py                        # Rule-based and semantic extraction functions
│   ├── labeling.py                          # Utilities to annotate or identify relevant sentences
│   └── training.py                          # BERT model training pipeline
└── README.md                                # You're here!
