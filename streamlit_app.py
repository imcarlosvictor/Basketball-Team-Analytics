import streamlit as st

from PIL import Image


class Dashboard:
    def __init__(self):
        favicon = Image.open("./assests/basketball.png")
        st.set_page_config(page_title="BWB Team Statistics", page_icon=favicon, layout="wide")

    def create_streamlit(self):
        # Sidebar
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
        left, mid_left, mid_right, right = st.columns(4)

        # Leading Overall Statistics
        with left:
            card_1 = st.container(border=True)
            st.subheader(":fire: Leading Scorer :fire:")

        with mid_left:
            card_2 = st.container(border=True)
            st.subheader("Most Field Goals Made")

        with mid_right:
            card_3 = st.container(border=True)
            st.subheader("Most 3PT Field Goals made")

        with right:
            card_4 = st.container(border=True)
            st.subheader("Free Throw Percentage")
