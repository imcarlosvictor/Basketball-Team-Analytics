import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

from utils import court_coordinates as cc


class GameStatisticsDashboard:
    def __init__(self):
        st.set_page_config(layout="wide")

    def create_sidebar(self):
        # Sidebar
        with st.sidebar:
            options = [
                'AverageJoe',
                'RiseUp',
            ]
            selected_option = st.sidebar.selectbox("League", options)

            if selected_option == 'AverageJoe':
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
            elif selected_option == 'RiseUp':
                with st.sidebar:
                    options = [
                        'Season 2',
                    ]
                    selected_option = st.sidebar.selectbox("Season", options)

                with st.sidebar:
                    options = [
                        "Game 1  | BWB vs. --",
                        "Game 2  | BWB vs. --",
                        "Game 3  | BWB vs. --",
                        "Game 4  | BWB vs. --",
                        "Game 5  | BWB vs. --",
                        "Game 6  | BWB vs. --",
                        "Game 7  | BWB vs. --",
                        "Game 8  | BWB vs. --",
                    ]
                    selected_option = st.sidebar.selectbox("Game", options)

    def plot_basketball_court(self):
        container_bg = """
            <style>
                [id="scene"] {
                    background-color: #101010;
                }
                [class="user-select-none svg-container"] {
                    background-color: #101010;
                }
            </style>
        """
        st.markdown(container_bg, unsafe_allow_html=True)


        court_container = st.container(border=False)
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
                           'court': '#dedede',
                           'hoop': '#e47041'
                },
                markers=False,
            )

            fig.update_traces(line=dict(width=3), hovertemplate=None, hoverinfo='skip', showlegend=False)
            fig.update_xaxes(gridcolor='#e8ecf2')
            fig.update_yaxes(gridcolor='#e8ecf2')
            fig.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                scene_aspectmode="data",
                height=600,
                scene_camera=dict(
                    eye=dict(x=1.3, y=0, z=0.5)
                ),
                scene=dict(
                    xaxis=dict(title='', showticklabels=False, showgrid=False),
                    yaxis=dict(title='', showticklabels=False, showgrid=False),
                    # Hardwood hexcode (#fee1bd, #e3c9b1, #f1c38e)
                    zaxis=dict(title='',  showticklabels=False, showgrid=False, showbackground=True, backgroundcolor='#292929'),
                ),
                legend=dict(
                    yanchor='bottom',
                    y=0.05,
                    x=0.2,
                    xanchor='left',
                    orientation='h',
                    font=dict(size=15, color='black'),
                    bgcolor='white',
                    title='',
                    itemsizing='constant'
                ),
                legend_traceorder="reversed"
            )

            # # Remove axis values
            # fig.update_traces(hovertemplate=None, hoverinfo='skip', showlegend=False)
            # fig.update_xaxes(visible=False)
            # fig.update_yaxes(visible=False)

            # # Update camera
            # camera = dict(
            #     eye=dict(x=1.3, y=0, z=0.1)
            # )
            # fig.update_layout(scene_camera=camera)

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
    game_stats.plot_basketball_court()
    game_stats.create_dashboard()

main()
