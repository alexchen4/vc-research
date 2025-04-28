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
```
├── liquidation.ipynb                  # Main notebook for information extraction using ML
├── pdf_convert.ipynb                  # Notebook for OCR conversion of PDFs to .txt
├── Extracted Sentences - Batch 1.csv  # Labeled dataset of sentences tagged with property types
├── requirements.txt                   # Python dependencies for the project
├── README.md                          # Project documentation

├── data/
│   ├── Batch1/                        # Raw PDF files (Batch 1)
│   ├── Batch1_text_readable/         # Text files from readable PDFs (Batch 1)
│   ├── Batch1_text_unreadable/       # Text files from unreadable PDFs (Batch 1)
│   ├── Batch2/                        # Raw PDF files (Batch 2)
│   ├── Batch2_text_readable/         # Text files from readable PDFs (Batch 2)
│   ├── Batch2_text_unreadable/       # Text files from unreadable PDFs (Batch 2)
│   └── outputs/                      # Folder for intermediate files and final extracted data

├── models/
│   └── fine_tuned_bert/              # Checkpoints for fine-tuned BERT model (if used)

└── utils/
    ├── extraction.py                 # Functions for extracting key fields from text
    ├── labeling.py                   # Sentence labeling tools for creating training data
    └── training.py                   # Fine-tuning pipeline for BERT sentence transformer
```
