from textblob import TextBlob
import streamlit as st


# function to calculate subjectivity
def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity


# function to calculate polarity
def getPolarity(review):
    return TextBlob(review).sentiment.polarity


# function to analyze the reviews
def analysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'


# function to analyze the reviews #Fine-grain
def analysis2(score):
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

st.title("Analize the sentiment of your sentence")

sentence = st.text_input("Your sentence")

if st.button("Analyze"):
    subj = getSubjectivity(sentence)
    pol = getPolarity(sentence)
    sentiment = analysis2(pol)
    st.write(sentiment)




