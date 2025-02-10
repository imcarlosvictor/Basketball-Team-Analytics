import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image

from utils import court_coordinates as cc


class GameStatisticsDashboard:
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

    def build_court(self):
        court_container = st.container(border=True)
        with court_container:
            court = cc.CourtCoordinates()
            court_lines_df = court.get_court_lines()
            fig = px.line_3d(
                data_frame=court_lines_df,
                x='x',
                y='y',
                z='z',
                line_group='line_group',
                color='color',
                color_discrete_map={
                           'court': '#fff',
                           'hoop': '#e47041'
                },
                markers=False,
            )
            # Remove axis values
            fig.update_traces(hovertemplate=None, hoverinfo='skip', showlegend=False)
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_yaxes(visible=False, showticklabels=False)
            # Plot court
            st.plotly_chart(fig, use_container_width=True)

    def create_dashboard(self):
        leading_stats_container = st.container(border=True)
        left, mid_left, mid_right, right = st.columns(4)

        # Leading Overall Statistics
        with left:
            card_1 = st.container(border=True)
            st.subheader("Top Scorer")

        with mid_left:
            card_2 = st.container(border=True)
            st.subheader("Most Field Goals Made")

        with mid_right:
            card_3 = st.container(border=True)
            st.subheader("Most 3PT Field Goals made")

        with right:
            card_4 = st.container(border=True)
            st.subheader("Free Throw Percentage")


def main():
    game_stats = GameStatisticsDashboard()
    game_stats.create_sidebar()
    game_stats.build_court()
    game_stats.create_dashboard()

main()
