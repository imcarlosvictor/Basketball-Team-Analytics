import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from PIL import Image
from numpy import sin, cos, pi
from streamlit_elements import dashboard, elements, mui, html, nivo



class PlayerStatisticsDashboard:
    def __init__(self):
        favicon = Image.open('./assests/basketball.png')
        st.set_page_config(
            page_title='Player Stats',
            page_icon=favicon,
            layout='wide',
        )
        # Uppercase all text
        st.markdown(
            '<style> body { text-transform: uppercase; } </style>',
            unsafe_allow_html=True
        )

    def create_sidebar(self):
        # Sidebar
        with st.sidebar:
            options = [
                'AverageJoe',
                'RiseUp',
            ]
            selected_option = st.sidebar.selectbox('League', options)

        with st.sidebar:
            options = [
                'Season 1',
            ]
            selected_option = st.sidebar.selectbox('Season', options)

        with st.sidebar:
            options = [
                'David',
                'Josh',
                'Jake',
                'Noel',
                'John',
                'James',
                'Marcus',
                'Ricky',
                'Harry',
                'Jeff',
            ]
            selected_option = st.sidebar.selectbox('Player', options)

    def create_dashboard(self):
        self.dashboard_elements()

    def dashboard_elements(self):
        card_theme = {
            'backgroundColor': '#e5e5e5',
            'font-family': 'sans-serif',
            'color': '#252525',
        }

        with elements('dashboard'):
            # First, build a default layout for every element you want to include in your dashboard
            layout = [
                # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
                dashboard.Item('radar_graph', 0, 0, 4, 4, isResizable=True, isDraggable=True, moved=False),
                dashboard.Item('shot_attempts_vs_made_block', 4, 0, 8, 4, isResizable=True, isDraggable=True, moved=False),
                dashboard.Item('overall_stat_block', 0, 5, 2, 5, isResizable=True, isDraggable=True, moved=False),
                dashboard.Item('last_game_stat_block', 2, 5, 2, 5, isResizable=True, isDraggable=True, moved=False),
                dashboard.Item('heatmap_block', 4, 5, 8, 5, isResizable=True, isDraggable=True, moved=False),
            ]

            mui.Box(
                'Player Name',
                sx={
                    'color': '#252525',
                    'opacity': '0.1',
                    'text-transform': 'uppercase',
                    'font-family': 'sans-serif',
                    'font-weight': 'bold',
                    'font-size': '150px',
                }
            )

            with dashboard.Grid(layout):
                with mui.Box(sx=card_theme, key='radar_graph'):
                    self.radar_graph()

                mui.Card(
                    mui.CardContent('ATTEMPTS vs. MAKES (Field Goals) PER GAME'),
                    sx=card_theme,
                    key='shot_attempts_vs_made_block',
                )

                mui.Card(
                    mui.CardContent('CAREER STATS'),
                    sx=card_theme,
                    key='overall_stat_block',
                )

                mui.Card(
                    mui.CardContent('PREVIOUS GAME STATS'),
                    sx=card_theme,
                    key='last_game_stat_block',
                )

                mui.Card(
                    mui.CardContent('SHOT CHART HEATMAP'),
                    sx=card_theme,
                    key='heatmap_block',
                )

    def career_stats(self):
        '''Career overall stats.'''

        with elements('nested_children'):
            with mui.Paper:
                with mui.Typography:
                    html.p('hellow world')
                    html.p('bye world')

    def last_game_stats(self):
        '''Most recent game.'''
        pass

    def radar_graph(self):
        with elements('nivo_charts'):
            DATA = [
                { 'index': 'SCORING', 'PLAYER': 93, 'TEAM': 61, 'TOP': 114  },
                { 'index': 'SHOOTING', 'PLAYER': 91, 'TEAM': 37, 'TOP': 72  },
                { 'index': '2P%', 'PLAYER': 91, 'TEAM': 37, 'TOP': 72  },
                { 'index': '3P%', 'PLAYER': 91, 'TEAM': 37, 'TOP': 72  },
                { 'index': 'ASSISTS', 'PLAYER': 56, 'TEAM': 95, 'TOP': 99  },
                { 'index': 'REBOUNDS', 'PLAYER': 64, 'TEAM': 90, 'TOP': 30  },
                { 'index': 'STEALS', 'PLAYER': 119, 'TEAM': 94, 'TOP': 103  },
                { 'index': 'TURNOVERS', 'PLAYER': 119, 'TEAM': 94, 'TOP': 103  },
            ]

            nivo.Radar(
                data=DATA,
                keys=[ 'PLAYER', 'TEAM', 'TOP'],
                # colors = [ '#6c45fe', '#faa000', '#dc143c' ],
                # colorBy='index',
                colors={ 'scheme': 'paired' },
                fillOpacity=0.35,
                indexBy='index',
                valueFormat='>-.2f',
                margin={ 'top': 70, 'right': 80, 'bottom': 40, 'left': 80  },
                borderColor={ 'from': 'color'  },
                gridLabelOffset=15,
                enableDots=True,
                # enableDotLabel=False,
                # dotLabel='value',
                # dotSize=18,
                # dotColor={ 'from': 'color' },
                # dotBorderColor={ 'from': 'inherit' },
                # dotBorderWidth=2,
                # dotLabelYOffset=-8,
                motionConfig='wobbly',
                legends=[
                    {
                        'anchor': 'top-left',
                        'direction': 'column',
                        'translateX': -50,
                        'translateY': -40,
                        'itemWidth': 80,
                        'itemHeight': 20,
                        'itemTextColor': '#252525',
                        'symbolSize': 12,
                        'symbolShape': 'circle',
                        'effects': [
                            {
                                'on': 'hover',
                                'style': {
                                    'itemTextColor': '#6c45fe'
                                }
                            }
                        ]
                    }
                ],
                theme={
                    'textColor': '#252525',
                    'tooltip': {
                        'container': {
                            'color': '#252525',
                        }
                    },
                    'gridColor': '#000',
                }
            )

    def shot_chart_heatmap(self):
        pass




def main():
    player_stats = PlayerStatisticsDashboard()
    player_stats.create_sidebar()
    player_stats.create_dashboard()

main()
