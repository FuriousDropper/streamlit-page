from textblob import TextBlob
import streamlit as st
from deep_translator import GoogleTranslator

# function to calculate subjectivity
def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity


# function to calculate polarity
def getPolarity(review):
    return TextBlob(review).sentiment.polarity


# function to analyze the reviews
def analysis(score, language):
    if language == "English":
        if score < 0:
            return 'Negative'
        elif score == 0:
            return 'Neutral'
        else:
            return 'Positive'
    elif language == "Français/French":
        if score < 0:
            return 'Négative'
        elif score == 0:
            return 'Neutre'
        else:
            return 'Positive'


# function to analyze the reviews #Fine-grain
def analysis2(score, language):
    if language == "Français/French":
        if score < -0.7:
            return 'Très négative'
        elif score < 0:
            return 'Négative'
        elif score == 0:
            return 'Neutre'
        elif score > 0.7:
            return 'Très positive'
        elif score > 0:
            return 'Positive'
    elif language == "English":
        if score < -0.7:
            return 'Very Negative'
        elif score < 0:
            return 'Negative'
        elif score == 0:
            return 'Neutral'
        elif score > 0.7:
            return 'Very Positive'
        elif score > 0:
            return 'Positive'


with st.sidebar:
    sb = st.selectbox("Choose your language", ("English", "Français/French"))
if sb == "English":
    st.title("Analize the sentiment of your sentence")

    sentence = st.text_input("Your sentence")

    if st.button("Analyze"):
        subj = getSubjectivity(sentence)
        pol = getPolarity(sentence)
        sentiment = analysis2(pol, "English")
        st.write(sentiment)

if sb == "Français/French":
    st.title("Analyser les sentiments de votre phrase")

    sentence = st.text_input("Votre phrase")

    translated = GoogleTranslator(source='auto', target='en').translate(text=sentence)

    if st.button("Analyser"):
        subj = getSubjectivity(translated)
        pol = getPolarity(translated)
        sentiment = analysis2(pol, "Français/French")
        st.write(sentiment)

