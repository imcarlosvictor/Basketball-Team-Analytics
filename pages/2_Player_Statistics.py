import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image



class PlayerStatisticsDashboard:
    def __init__(self):
        st.set_page_config(layout="wide")

    def create_sidebar(self):
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

    def heatmap(self):
        pass

    def create_dashboard(self):
        left, mid_left, mid_right, right = st.columns(4)

        ovr_ppg_container = st.container(border=True)
        ovr_assists_container = st.container(border=True)
        ovr_rebounds_container = st.container(border=True)
        with left:
            with ovr_ppg_container:
                st.subheader("Point Per Game")

            with ovr_assists_container:
                st.subheader("Field Goal PGT")

            with ovr_rebounds_container:
                st.subheader("Field Goal PGT")

        ppg_container = st.container(border=True)
        assists_container = st.container(border=True)
        rebounds_container = st.container(border=True)
        with mid_left:
            with ppg_container:
                st.subheader("Point Per Game")

            with assists_container:
                st.subheader("Field Goal PGT")

            with rebounds_container:
                st.subheader("Field Goal PGT")




def main():
    player_stats = PlayerStatisticsDashboard()
    player_stats.create_sidebar()
    player_stats.create_dashboard()

main()
