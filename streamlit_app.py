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
                "Game 1  | BWB vs. Venoms",
                "Game 2  | BWB vs. ABG",
                "Game 3  | BWB vs. GoEasy",
                "Game 4  | BWB vs. --",
                "Game 5  | BWB vs. --",
                "Game 6  | BWB vs. --",
                "Game 7  | BWB vs. --",
                "Game 8  | BWB vs. --",
                "Game 9  | BWB vs. --",
                "Game 10 | BWB vs. --",
                "Game 11 | BWB vs. --",
                "Game 12 | BWB vs. --",
                "Game 13 | BWB vs. --",
                "Game 14 | BWB vs. --",
            ]
            selected_option = st.sidebar.selectbox("Game", options)

        with st.sidebar:
            options = [
                "Team Overall",
                "David",
                "Noel",
                "Josh",
                "Jake",
                "John",
                "James",
                "Marcus",
                "Ricky",
                "Harry",
                "Jeff",
            ]
            selected_option = st.sidebar.selectbox("Player", options)

        leading_stats_container = st.container(border=True)
        col_1, col_2, col_3, col_4 = st.columns(4)

        with col_1:
            card_1 = st.container(border=True)
            st.subheader(":fire: Leading Scorer :fire:")

        with col_2:
            card_2 = st.container(border=True)
            st.subheader("Most Field Goals Made")

        with col_3:
            card_3 = st.container(border=True)
            st.subheader("Most 3PT Field Goals made")

        with col_4:
            card_4 = st.container(border=True)
            st.subheader("Free Throw Percentage")
