import streamlit as st
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from graphs import plot_reviews_by_stars, plot_average_star_by_category, plot_average_star_by_insurer, plot_number_of_reviews_by_insurer, plot_categories_by_insurer

# Load data
df_en = pd.read_csv('data/df_assurance_en_prepro.csv')
df_fr = pd.read_csv('data/df_assurance_fr_prepro.csv')

# Load models
senti_model_name = "tabularisai/multilingual-sentiment-analysis"
senti_tokenizer = AutoTokenizer.from_pretrained(senti_model_name)
senti_model = AutoModelForSequenceClassification.from_pretrained(senti_model_name).to('cpu')
senti_model.eval()

subject_model_name = 'facebook/bart-large-mnli'
subject_classifier = pipeline("zero-shot-classification", model=subject_model_name, device=-1)

# Define functions
def sentiment_pipeline(texts):
    inputs = senti_tokenizer(texts, return_tensors="pt", truncation=True, padding=True, max_length=512).to('cpu')
    with torch.no_grad():
        outputs = senti_model(**inputs)
        probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
        sentiment = torch.argmax(probabilities, dim=-1).tolist()
    senti_rescale = [int(senti + 1) for senti in sentiment]  # convert to 1-5 scale like stars
    return senti_rescale

def subject_pipeline(reviews, lang='en', threshold=0.5):
    labels_fr = ["Prix", "Couverture", "Inscription", "Service Client", "Traitement des Sinistres", "Annulation", "Autres"]
    labels_en = ["Pricing", "Coverage", "Enrollment", "Customer Service", 'Claims Processing', 'Cancellation', 'Others']
    labels = labels_fr if lang == 'fr' else labels_en
    resp = subject_classifier(reviews, labels[:-1])  # exclude 'Others' label
    subjects, scores = [], []
    for r in resp:
        if max(r['scores']) <= threshold:
            subjects.append(labels[-1])
        else:
            subjects.append(r['labels'][0])
    return subjects

# Streamlit app
st.title('NLP Project 2 - Streamlit App')

lang = st.selectbox('Select Language', ['en', 'fr'])
df = df_en if lang == 'en' else df_fr

tab1, tab2 = st.tabs(["Analysis", "Graphs"])

with tab1:
    st.write(f"Displaying data for language: {lang}")

    if st.checkbox('Show raw data'):
        st.write(df.head())

    st.subheader('Sentiment Analysis')
    sample_reviews = df.sample(5)[f'avis_{lang}'].tolist()
    sentiments = sentiment_pipeline(sample_reviews)
    for review, sentiment in zip(sample_reviews, sentiments):
        st.write(f"Review: {review}")
        st.write(f"Predicted Sentiment (1-5): {sentiment}")
        st.write("---")

    st.subheader('Subject Classification')
    subjects = subject_pipeline(sample_reviews, lang=lang)
    for review, subject in zip(sample_reviews, subjects):
        st.write(f"Review: {review}")
        st.write(f"Predicted Subject: {subject}")
        st.write("---")

with tab2:
    st.subheader('Graphs')
    plot_reviews_by_stars(df)
    plot_average_star_by_category(df)
    plot_average_star_by_insurer(df)
    plot_number_of_reviews_by_insurer(df)
    plot_categories_by_insurer(df)