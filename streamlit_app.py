import streamlit as st


class Dashboard:
    def __init__(self):
        st.set_page_config(layout="wide")

    def create_streamlit(self):
        with st.sidebar:
            options = [
                'Season 1',
            ]
            selected_option = st.sidebar.selectbox("Season", options)

        with st.sidebar:
            options = [
                'Game 1 | BWB vs. Venoms',
                "Game 2 | BWB vs. ABG",
                "Game 3 | BWB vs. GoEasy",
            ]
            selected_option = st.sidebar.selectbox("Game", options)

        with st.sidebar:
            options = [
                'David',
                'Noel',
            ]
            selected_option = st.sidebar.selectbox("Player", options)


