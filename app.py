 # pip3 install -r requirements.py
# python -m textblob.download_corpora
# open python in terminal and write this 
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from happytransformer import HappyTextToText, TTSettings
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
import re
import string

# Load the models with caching to optimize loading
@st.cache_resource
def load_punctuation_model():
    tokenizer = AutoTokenizer.from_pretrained("oliverguhr/fullstop-punctuation-multilang-large")
    model = AutoModelForTokenClassification.from_pretrained("oliverguhr/fullstop-punctuation-multilang-large")
    return pipeline('ner', model=model, tokenizer=tokenizer)

@st.cache_resource
def load_grammar_model():
    return HappyTextToText("T5", "vennify/t5-base-grammar-correction")

# Initialize models
punctuation_model = load_punctuation_model()
happy_tt = load_grammar_model()

# Streamlit UI
st.title("Text Correction Application")

# Input text
text_input = st.text_area("Enter text to correct:", "")

# Define buttons for each correction type
if st.button("Punctuation Correction"):
    if text_input:
        # Punctuation Correction
        processed_text = punctuation_model(text_input)
        punctuation_corrected_text = ''.join([i['word'].replace('▁', ' ') + i['entity'].replace('0', '') for i in processed_text])

        # Display punctuation-corrected text
        st.subheader("Punctuation Corrected Text:")
        st.write(punctuation_corrected_text)
    else:
        st.warning("Please enter some text for punctuation correction.")

if st.button("Grammar Correction"):
    if text_input:
        # Grammar Correction
        text_tokenize = sent_tokenize(text_input)  # Tokenize input into sentences
        args = TTSettings(num_beams=5, min_length=1)

        # Process each sentence through the grammar correction model
        processed_text = []
        for sentence in text_tokenize:
            modeled_text = happy_tt.generate_text(sentence, args=args)
            processed_text.append(modeled_text.text)

        # Combine the grammar-corrected sentences
        grammar_corrected_text = " ".join(processed_text)

        # Display grammar-corrected text
        st.subheader("Grammar Corrected Text:")
        st.write(grammar_corrected_text)
    else:
        st.warning("Please enter some text for grammar correction.")

if st.button("Spell Checker"):
    if text_input:
        # Spell Checker
        # Remove punctuation for spell-checking
        unpunc_model = re.compile("[" + re.escape(string.punctuation) + "]")
        unpunc_text = unpunc_model.sub("", text_input)

        # Tokenize the text into words and correct each word's spelling
        tokenize_text = word_tokenize(unpunc_text)
        processed_text = [str(TextBlob(word).correct()) for word in tokenize_text]

        # Combine the spell-corrected words back into a single text
        spell_corrected_text = " ".join(processed_text)

        # Display spell-corrected text
        st.subheader("Spell Corrected Text:")
        st.write(spell_corrected_text)
    else:
        st.warning("Please enter some text for spell correction.")