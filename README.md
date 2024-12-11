# VC-Research

## Overview
The **VC-Research** project automates text extraction and quality assessment for PDF files containing venture capital-related data. Utilizing Optical Character Recognition (OCR) with Tesseract and various data processing techniques, this project categorizes files based on readability to streamline data analysis workflows.

## Environment Setup

### Requirements
- **Python Version**: 3.12.7

### Key Libraries
- **OCR Engine**: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – Recognizes text within images.
- **PDF to Image Conversion**: [`pdf2image`](https://pypi.org/project/pdf2image/) – Converts PDF pages to images for OCR processing.
- **OCR Wrapper**: [`pytesseract`](https://pypi.org/project/pytesseract/) – Python wrapper for Tesseract, facilitating text and confidence score extraction.
- **Data Processing**: `pandas`, `numpy` – Used for organizing, analyzing, and storing extracted text metrics.
- **Natural Language Processing**: [`nltk`](https://www.nltk.org/) – Utilizes the English vocabulary corpus to verify and correct OCR-extracted text.
- **Parallel Processing**: `concurrent.futures` – Enables concurrent OCR tasks, significantly reducing processing time for large PDF batches.


## Directory Structure
- **/Batch1**: Contains the raw PDF files to be processed.
- **/Batch1_text_readable**: Stores extracted text files classified as readable.
- **/Batch1_text_unreadable**: Stores extracted text files classified as unreadable.
- **/Batch2**: Contains the raw PDF files to be processed.
- **/Batch2_text_readable**: Stores extracted text files classified as readable.
- **/Batch2_text_unreadable**: Stores extracted text files classified as unreadable.