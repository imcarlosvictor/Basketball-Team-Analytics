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
            'backgroundColor': '#efefef',
            'font-family': 'sans-serif',
            'color': '#252525',
        }

        with elements('dashboard'):
            # First, build a default layout for every element you want to include in your dashboard
            layout = [
                # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
                dashboard.Item('radar_graph', 0, 0, 4, 4, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('shot_attempts_vs_made_block', 4, 0, 8, 4, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('career_stats_block', 0, 5, 2, 6, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('season_stats_block_1', 2, 5, 2, 2, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('heatmap_block', 4, 5, 8, 6, isResizable=False, isDraggable=False, moved=False),
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
                    mui.CardContent('LAST GAME EXCEL HEATMAP'),
                    sx=card_theme,
                    key='shot_attempts_vs_made_block',
                )

                mui.Card(
                    mui.CardContent('CAREER STATS'),
                    sx=card_theme,
                    key='career_stats_block',
                )

                with mui.Box(sx=card_theme, key='season_stats_block_1'):
                    with elements('block'):
                        mui.Typography('Season Stats', variant='h6')
                        self.career_stats()
                        self.career_stats()
                        self.career_stats()

                mui.Card(
                    mui.CardContent('SHOT CHART HEATMAP'),
                    sx=card_theme,
                    key='heatmap_block',
                )

    def career_stats(self):
        '''Career overall stats.'''

        with elements('radial_chart'):
            DATA = [
                { "id": "Player",
                    "data": [
                        { "x": "PPG", "y": 23.3 },
                        { "x": "cap", "y": 6.7 },
                    ]
                }
            ]

            nivo.RadialBar(
                data=DATA,
                # width=275,
                # height=250,
                padding=0.5,
                valueFormat='>-.2f',
                startAngle=-124,
                endAngle=124,
                innerRadius=0.65,
                cornerRadius=2,
                margin={'top': 20, 'right': 20, 'bottom': 20, 'left': 20},
                colors = ['#07da63', '#b4b9c7'],
                # colors = [ '#07da63', '#f5c512', '#e5e5e5'],
                # colors = [ '#1eb281', '#f3e05e', '#dc143c', '#e5e5e5'],
                # colorBy='index',
                # colors={'scheme': 'red_yellow_green'},
                borderColor={'from': 'color', 'modifiers': {'darker': 1}},
                enableTracks=True,
                # tracksColor='#e3e3e3',
                enableRadialGrid=False,
                enableCircularGrid=False,
                radialAxisStart=None,
                circularAxisOuter=None,
                motionConfig='molasses',
                transitionMode='startAngle',
                layers=[
                    'grid',
                    'tracks',
                    'bars',
                    'labels',
                    'legends',
                    {
                        'type': 'custom',
                        'render': {
                            'x': .5,
                            'y': .5,
                            'text': 'PPG',
                            'textAlign': 'center',
                            'dominantBaseline': 'central',
                            'style': {
                                'fontSize': 26,
                                'fontWeight': 'bold',
                                'fill': '#232323',
                            }
                        }
                    }
                ]
            )


    def last_game_stats(self):
        '''Most recent game.'''
        pass

    def radar_graph(self):
        with elements('radar_graph'):
            DATA = [
                { 'index': 'SCORING', 'TEAM': 93, 'PLAYER': 61, 'TOP': 114  },
                { 'index': 'SHOOTING', 'TEAM': 91, 'PLAYER': 37, 'TOP': 72  },
                { 'index': '2P%', 'TEAM': 91, 'PLAYER': 37, 'TOP': 72  },
                { 'index': '3P%', 'TEAM': 91, 'PLAYER': 37, 'TOP': 72  },
                { 'index': 'ASSISTS', 'TEAM': 56, 'PLAYER': 95, 'TOP': 99  },
                { 'index': 'REBOUNDS', 'TEAM': 64, 'PLAYER': 90, 'TOP': 30  },
                { 'index': 'STEALS', 'TEAM': 119, 'PLAYER': 94, 'TOP': 103  },
                { 'index': 'TURNOVERS', 'TEAM': 119, 'PLAYER': 94, 'TOP': 103  },
            ]

            nivo.Radar(
                data=DATA,
                keys=[ 'TOP', 'TEAM', 'PLAYER'],
                # colors={ 'scheme': 'paired' },
                # colors={ 'scheme': 'spectral' },
                # colors = [ '#e4364b', '#ba98f5', '#ff8c00' ],
                # colors = [ '#359982', '#9ac2ee', '#0b79b4' ],
                colors = [ '#8ab8fe', '#79bbac', '#005ffd'],
                # colors = [ '#8ab8fe', '#359982', '#005ffd'],
                colorBy='index',
                curve='catmullRomClosed',
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
                dotColor='#fff',
                dotBorderColor={'from': 'color'},
                dotBorderWidth=1,
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
                                    'itemTextColor': '#dc143c'
                                }
                            }
                        ]
                    }
                ],
                theme={
                    'background': '#ececec',
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
