# Text Correction Application Using Natural Language Processing

**Team Members**:
Abhinav Mishra (2101009)
Aman Verma (2101031)
Saloni Sinha (2101179)

## Project Overview

This project is a Text Correction Application developed using Natural Language Processing (NLP) techniques. The application aims to enhance the readability and professionalism of text by providing functionalities for punctuation correction, grammar correction, and spell checking.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/abhinavmishra-0302/NLP_Project.git
   cd text-correction-app
   ```
2. Install the required packages:

   ```bash
   pip3 install -r requirements.txt
   ```
3. Download necessary NLTK corpora:

   ```bash
   python -m textblob.download_corpora
   ```
4. Open a Python shell and run the following commands:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage

1. Launch the Streamlit application:

   ```bash
   streamlit run app.py
   ```
2. Open your browser and navigate to `http://localhost:8501`.
3. Enter the text you want to correct in the input box.
4. Choose one of the correction types:

   - **Punctuation Correction**: Automatically corrects punctuation in the provided text.
   - **Grammar Correction**: Applies grammar corrections to sentences in the input text.
   - **Spell Checker**: Identifies and corrects spelling errors in the text.
5. View the corrected output displayed below the input area.

## Features

- **Punctuation Correction**: Uses a fine-tuned Transformer model to accurately insert punctuation in text.
- **Grammar Correction**: Utilizes T5 (Text-to-Text Transfer Transformer) for correcting grammatical errors in sentences.
- **Spell Checker**: Implements the TextBlob library for detecting and correcting misspelled words.

## Technologies Used

- **Python**: Programming language used for development.
- **Streamlit**: Web framework for building the application interface.
- **Transformers**: Library by Hugging Face for NLP models.
- **Happy Transformer**: Library for simplified text-to-text model handling.
- **NLTK**: Natural Language Toolkit for text processing tasks.
- **TextBlob**: Library for processing textual data.
