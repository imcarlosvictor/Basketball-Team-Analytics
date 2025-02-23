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
            'backgroundColor': '#b9b9b9',
            'backdrop-filter': 'blur(60px)',
            'opacity': '.8',
            'font-family': 'sans-serif',
            'color': '#262626',
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
                    'color': '#484848',
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
        with elements("nivo_charts"):
            DATA = [
                { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114  },
                { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72  },
                { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99  },
                { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30  },
                { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103  },
            ]

            nivo.Radar(
                data=DATA,
                keys=[ "chardonay", "carmenere", "syrah"  ],
                indexBy="taste",
                valueFormat=">-.2f",
                margin={ "top": 70, "right": 80, "bottom": 40, "left": 80  },
                borderColor={ "from": "color"  },
                gridLabelOffset=36,
                dotSize=10,
                dotColor={ "theme": "background"  },
                dotBorderWidth=2,
                motionConfig="wobbly",
                legends=[
                    {
                        "anchor": "top-left",
                        "direction": "column",
                        "translateX": -50,
                        "translateY": -40,
                        "itemWidth": 80,
                        "itemHeight": 20,
                        "itemTextColor": "#232323",
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemTextColor": "#6b47e3"
                                }
                            }
                        ]
                    }
                ],
                theme={
                    "background": "#bbbbbb",
                    "textColor": "#232323",
                    "tooltip": {
                        "container": {
                            "background": "#bbbbbb",
                            "color": "#232323",
                        }
                    }
                }
            )

    def shot_chart_heatmap(self):
        pass




def main():
    player_stats = PlayerStatisticsDashboard()
    player_stats.create_sidebar()
    player_stats.create_dashboard()

main()
