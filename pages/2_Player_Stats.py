import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from PIL import Image
from numpy import sin, cos, pi
from streamlit_elements import dashboard, elements, mui, html, nivo
from streamlit_extras.grid import grid



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
                dashboard.Item('heatmap_block', 4, 0, 8, 4, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('career_stats_block', 0, 5, 4, 2.4, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('season_stats_block', 0, 9, 4, 2.4, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('game_log', 4, 0, 8, 5.0, isResizable=False, isDraggable=False, moved=False),
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
                    mui.CardContent('SHOT CHART HEATMAP'),
                    sx=card_theme,
                    key='heatmap_block',
                )

                with mui.Box(sx=card_theme, key='career_stats_block'):
                    self.career_stats()

                with mui.Box(sx=card_theme, key='season_stats_block'):
                    self.season_stats()

                mui.Card(
                    mui.CardContent('GAME LOG'),
                    sx=card_theme,
                    key='game_log',
                )

    def metrics(self):
        with st.container(height=450, border=True):
            career_grid = grid(4, gap='small', vertical_align='center')
            career_grid.metric('PTS', '24.5', '.5')
            career_grid.metric('AST', '2', '-.5')
            career_grid.metric('STL', '3', '.2')
            career_grid.metric('BLK', '.2', '-.1')

            career_grid.metric('PTS', '24.5', '.5')
            career_grid.metric('AST', '2', '-.5')
            career_grid.metric('STL', '3', '.2')
            career_grid.metric('BLK', '.2', '-.1')

            career_grid.metric('PTS', '24.5', '.5')
            career_grid.metric('AST', '2', '-.5')
            career_grid.metric('STL', '3', '.2')
            career_grid.metric('BLK', '.2', '-.1')

            career_grid.metric('PTS', '24.5', '.5')
            career_grid.metric('AST', '2', '-.5')
            career_grid.metric('STL', '3', '.2')
            career_grid.metric('BLK', '.2', '-.1')

    def career_stats(self):
        career_data = {
            'pts': 15.3,
            'ast': 2.1,
            'stl': 3.1,
            'blk': 3.1,
            'orb': 5.6,
            'drb': 8.2,
            'foul': 3,
            'tur': 2,
            'fg': 6.5,
            'fg%': 45.6,
            'ft': 5.3,
            'ft%': 75.2,
            '2p': 5.7,
            '2p%': 41.6,
            '3p': 4.1,
            '3p%': 32.2,
        }
        self.grid_statistics('career statistics', career_data)

    def season_stats(self):
        season_data = {
            'pts': 25.3,
            'ast': 2.1,
            'stl': .7,
            'blk': 1.2,
            'orb': 3.6,
            'drb': 7.2,
            'foul': 4,
            'tur': 2,
            'fg': 6.5,
            'fg%': 45.6,
            'ft': 5.3,
            'ft%': 87.5,
            '2p': 6.7,
            '2p%': 51.6,
            '3p': 3.1,
            '3p%': 43.2,
        }
        self.grid_statistics('season statistics', season_data)

    def grid_statistics(self, block_title: str, data):
        html.div(
            block_title,
            css={
                'padding': '.5em .5em .5em .7em',
                'margin-left': '1em',
                'margin-right': '1.8em',
                'border-bottom': 'solid .7px #232323',
                'color': '#232323',
                'display': 'grid',
                'justify-content': 'start',
                'align-items': 'end',
                'text-transform': 'uppercase',
                'font-family': 'sans-serif',
                'font-weight': 'bold',
                'font-size': '15px',
            }
        )

        with elements('statistics_overview_dashboard'):
            BOX_CSS = {
                'p': 0,
                'display': 'flex',
                'flex-direction': 'column',
                'justify-content': 'center',
                'align-items': 'center',
                ':hover': {
                    'background': '#d4d4d4',
                }
            }

            FFI_BOX_CSS = {
                'p': 0,
                'display': 'flex',
                'radius': 3,
                'flex-direction': 'column',
                'justify-content': 'center',
                'align-items': 'center',
                'background': '#e3e3e3',
            }

            TITLE_CSS = {
                'color': '#232323',
                'font-size': 15,
            }

            FFI_TITLE_CSS = {
                # 'overflow-wrap': 'break-word',
                # 'inline-size': 110,
                'word-break': 'break-all',
                'color': '#232323',
                'font-size': 11,
                'padding-bottom': '.5em',
            }

            VALUE_CSS = {
                'color': '#101010',
                'font-size': 22,
                'font-weight': 'medium',
            }

            GAIN_DELTA_CSS = {
                'color': '#16a68e',
                'font-size': 14,
                'font-weight': 'bold',
            }

            LOSS_DELTA_CSS = {
                'color': '#ff1400',
                'font-size': 14,
                'font-weight': 'bold',
            }

            # First, build a default layout for every element you want to include in your dashboard
            layout = [
                # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
                # ROW 1
                dashboard.Item('PTS', 0, 0, .7, .5, isResizable=False, isDraggable=False, isBounded=True),
                dashboard.Item('AST', .7, 0, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('STL', 1.4, 0, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('BLK', 2.1, 0, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('EFGP', 2.8, 0, 1, .5, isResizable=False, isDraggable=False, moved=False), # FOUR FACTOR INDEX
                # ROW 2
                dashboard.Item('ORB', 0, .5, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('DRB', .7, .5, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('FOUL', 1.4, .5, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('TUR', 2.1, .5, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('TURR', 2.8, .5, 1, .5, isResizable=False, isDraggable=False, moved=False), # FOUR FACTOR INDEX
                # ROW 3
                dashboard.Item('FG', 0, 1, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('FG%', .7, 1, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('FT', 1.4, 1, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('FT%', 2.1, 1, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('ORB%', 2.8, 1, 1, .5, isResizable=False, isDraggable=False, moved=False), # FOUR FACTOR INDEX
                # ROW 4
                dashboard.Item('2P', 0, 1.5, .7, .5, isResizable=False, isDraggable=True, moved=False),
                dashboard.Item('2P%', .7, 1.5, .7, .5, isResizable=False, isDraggable=True, moved=False),
                dashboard.Item('3P', 1.4, 1.5, .7, .5, isResizable=False, isDraggable=True, moved=False),
                dashboard.Item('3P%', 2.1, 1.5, .7, .5, isResizable=False, isDraggable=False, moved=False),
                dashboard.Item('FTR', 2.8, 1.5, 1, .5, isResizable=False, isDraggable=False, moved=False), # FOUR FACTOR INDEX
            ]

            with dashboard.Grid(layout, autoSize=True, margin=[0,0], containerPadding=[0,0]):
                # ----------------- ROW 1 -----------------
                with mui.Box(key='PTS', sx=BOX_CSS):
                    mui.Box('PTS', sx=TITLE_CSS)
                    mui.Box(data['pts'], sx=VALUE_CSS)
                    mui.Box('+2.2', sx=GAIN_DELTA_CSS)

                with mui.Box(key='AST', sx=BOX_CSS):
                    mui.Box('AST', sx=TITLE_CSS)
                    mui.Box(data['ast'], sx=VALUE_CSS)
                    mui.Box('+0.6', sx=LOSS_DELTA_CSS)

                with mui.Box(key='STL', sx=BOX_CSS):
                    mui.Box('STL', sx=TITLE_CSS)
                    mui.Box(data['stl'], sx=VALUE_CSS)

                with mui.Box(key='BLK', sx=BOX_CSS):
                    mui.Box('BLK', sx=TITLE_CSS)
                    mui.Box(data['blk'], sx=VALUE_CSS)

                with mui.Box(key='EFGP', sx=FFI_BOX_CSS): # FOUR FACTOR INDEX
                    mui.Box('Effective FG%', sx=FFI_TITLE_CSS)
                    mui.Box(data['2p'], sx=VALUE_CSS)

            # ----------------- ROW 2 -----------------
            with dashboard.Grid(layout, margin=[0,0]):
                with mui.Box(key='ORB', sx=BOX_CSS):
                    mui.Box('ORB', sx=TITLE_CSS)
                    mui.Box(data['orb'], sx=VALUE_CSS)
                    mui.Box('+2.2', sx=GAIN_DELTA_CSS)

                with mui.Box(key='DRB', sx=BOX_CSS):
                    mui.Box('DRB', sx=TITLE_CSS)
                    mui.Box(data['drb'], sx=VALUE_CSS)

                with mui.Box(key='FOUL', sx=BOX_CSS):
                    mui.Box('FOUL', sx=TITLE_CSS)
                    mui.Box(data['foul'], sx=VALUE_CSS)

                with mui.Box(key='TUR', sx=BOX_CSS):
                    mui.Box('TUR', sx=TITLE_CSS)
                    mui.Box(data['tur'], sx=VALUE_CSS)

                with mui.Box(key='TURR', sx=FFI_BOX_CSS): # FOUR FACTOR INDEX
                    mui.Box('Turnover Ratio', sx=FFI_TITLE_CSS)
                    mui.Box(data['2p%'], sx=VALUE_CSS)

            # ----------------- ROW 3 -----------------
            with dashboard.Grid(layout, margin=[0,0]):
                with mui.Box(key='FG', sx=BOX_CSS):
                    mui.Box('FG', sx=TITLE_CSS)
                    mui.Box(data['fg'], sx=VALUE_CSS)

                with mui.Box(key='FG%', sx=BOX_CSS):
                    mui.Box('FG%', sx=TITLE_CSS)
                    mui.Box(data['fg%'], sx=VALUE_CSS)

                with mui.Box(key='FT', sx=BOX_CSS):
                    mui.Box('FT', sx=TITLE_CSS)
                    mui.Box(data['ft'], sx=VALUE_CSS)

                with mui.Box(key='FT%', sx=BOX_CSS):
                    mui.Box('FT%', sx=TITLE_CSS)
                    mui.Box(data['ft%'], sx=VALUE_CSS)

                with mui.Box(key='ORB%', sx=FFI_BOX_CSS): # FOUR FACTOR INDEX
                    mui.Box('Offensive Rebound %', sx=FFI_TITLE_CSS)
                    mui.Box(data['3p'], sx=VALUE_CSS)

            # ----------------- ROW 4 -----------------
            with dashboard.Grid(layout, margin=[0,0]):
                with mui.Box(key='2P', sx=BOX_CSS):
                    mui.Box('2P', sx=TITLE_CSS)
                    mui.Box(data['2p'], sx=VALUE_CSS)

                with mui.Box(key='2P%', sx=BOX_CSS):
                    mui.Box('2P%', sx=TITLE_CSS)
                    mui.Box(data['2p%'], sx=VALUE_CSS)

                with mui.Box(key='3P', sx=BOX_CSS):
                    mui.Box('3P', sx=TITLE_CSS)
                    mui.Box(data['3p'], sx=VALUE_CSS)

                with mui.Box(key='3P%', sx=BOX_CSS):
                    mui.Box('3P%', sx=TITLE_CSS)
                    mui.Box(data['3p%'], sx=VALUE_CSS)

                with mui.Box(key='FTR', sx=FFI_BOX_CSS): # FOUR FACTOR INDEX
                    mui.Box('Free Throw Ratio', sx=FFI_TITLE_CSS)
                    mui.Box(data['3p%'], sx=VALUE_CSS)

        html.div(
            '4-Factors Index: 28.5',
            css={
                'margin-bottom': '1em',
                'padding': '.5em 2em .5em .5em',
                # 'backgroundColor': '#dfdfdf',
                'color': '#232323',
                'display': 'grid',
                'justify-content': 'end',
                'align-items': 'start',
                'text-transform': 'uppercase',
                'font-family': 'sans-serif',
                'font-stlye': 'italic',
                'font-size': '14px',
            }
        )


    def radial_bar(self):
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
                padding=0.5,
                valueFormat='>-.2f',
                startAngle=-124,
                endAngle=124,
                innerRadius=0.65,
                cornerRadius=2,
                margin={'top': 20, 'right': 20, 'bottom': 20, 'left': 20},
                colors = ['#07da63', '#b4b9c7'],
                borderColor={'from': 'color', 'modifiers': {'darker': 1}},
                enableTracks=True,
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

    def radar_graph(self):
        with elements('radar_graph'):
            DATA = [
                { 'index': 'SCORING', 'TEAM': 93, 'PLAYER': 61, 'TOP': 114  },
                { 'index': 'SHOOTING', 'TEAM': 91, 'PLAYER': 37, 'TOP': 72  },
                { 'index': '3P%', 'TEAM': 91, 'PLAYER': 37, 'TOP': 72  },
                { 'index': 'ASSISTS', 'TEAM': 56, 'PLAYER': 95, 'TOP': 99  },
                { 'index': 'REBOUNDS', 'TEAM': 64, 'PLAYER': 90, 'TOP': 30  },
                { 'index': 'STEALS', 'TEAM': 119, 'PLAYER': 94, 'TOP': 103  },
                { 'index': 'TURNOVERS', 'TEAM': 119, 'PLAYER': 94, 'TOP': 103  },
                { 'index': 'PER', 'TEAM': 119, 'PLAYER': 94, 'TOP': 103  },
            ]

            nivo.Radar(
                data=DATA,
                keys=[ 'TOP', 'TEAM', 'PLAYER'],
                # colors={ 'scheme': 'paired' },
                # colors={ 'scheme': 'spectral' },
                # colors = [ '#e4364b', '#ba98f5', '#ff8c00' ],
                # colors = [ '#359982', '#9ac2ee', '#0b79b4' ],
                # colors = [ '#ffb128', '#ff8916', '#dc143c'],
                # colors = [ '#8ab8fe', '#359982', '#005ffd'],
                # colors = [ '#e7b7f4', '#9488d8', '#dc143c'],
                # colors = [ '#ffaf31', '#ff7600', '#ff398e'],
                colors = [ '#ffaf31', '#ff4655', '#008080'],
                colorBy='index',
                curve='catmullRomClosed',
                fillOpacity=0.35,
                indexBy='index',
                valueFormat='>-.2f',
                margin={ 'top': 70, 'right': 90, 'bottom': 40, 'left': 90},
                borderColor={ 'from': 'color'  },
                gridLabelOffset=15,
                enableDots=True,
                dotColor='#fff',
                dotBorderColor={'from': 'color'},
                dotBorderWidth=1,
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
                    # 'background': '#ececec',
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
