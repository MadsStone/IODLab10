import streamlit as st
import pandas as pd
import joblib
from utils import preprocessor

def run():
    # Load the pre-trained model
    model = joblib.load(r"C:\Users\maddi\IODLabs\VS Code\IOD_Lab-10_2\model.joblib")

    st.title("Sentiment Analysis")
    st.text("Basic app to detect the sentiment of text.")
    st.text("")
    userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Input text HERE')
    st.text("")
    predicted_sentiment = ""
    if st.button("Predict"):
        # Predict sentiment
        predicted_sentiment = model.predict([userinput])[0]
        output = 'positive 👍' if predicted_sentiment == 1 else 'negative 👎'
        sentiment = f'Predicted sentiment of "{userinput}" is {output}.'
        st.success(sentiment)

if __name__ == "__main__":
    run()
