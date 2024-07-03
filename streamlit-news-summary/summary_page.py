import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from NewSummary import allNews
from Text_Summarization import summarizer


def show_summary_page():
    # Create a text input box for the URL
    url = st.text_input('Enter the URL')

    # Create a button for the search action
    if st.button('Search'):
        try:
            news_title, news = allNews(url)
            summary, doc, scores_df, len_doc, lens_summary = summarizer(news)
            st.title(news_title)
            st.write(summary)
            df2 = pd.DataFrame()

            #st.dataframe(pd.DataFrame.from_dict({""" Serialization of dataframe to Arrow table was unsuccessful due to: ('Could not convert The Supreme Court on Wednesday declined to entertain former Jharkhand chief minister Hemant Soren’s plea seeking interim bail on money laundering charges in a land scam-related case to campaign for the Lok Sabha elections, saying his bail plea was pending before the trial court when he approached the apex court seeking the relief""": 1, 'b': 'foobar'}, orient='index'))

            first_column_series = scores_df.iloc[:, 0]
            first_column_series = first_column_series.astype(str)
            scores = scores_df.iloc[:, 1]
            df_combined = pd.concat([first_column_series, scores], axis=1)
            st.dataframe(df_combined)

        except Exception as e:
            st.write(f"An error occurred: {e}")

        