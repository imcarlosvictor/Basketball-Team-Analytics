import base64
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

import sample_data

from PIL import Image
from io import BytesIO
from numpy import sin, cos, pi
from streamlit_extras.grid import grid
from streamlit_elements import dashboard, elements, mui, html, nivo
from streamlit_extras.stylable_container import stylable_container

from modules.basketball_court import draw_court
from modules.nivo_graphs import NivoGraphs



class PlayerStatisticsDashboard:
    def __init__(self):
        favicon = Image.open('./assests/basketball.png')
        st.set_page_config(
            page_title='Player Stats',
            page_icon=favicon,
            layout='wide',
        )
        # Uppercase all text
        st.markdown('<style> body { text-transform: uppercase; } </style>', unsafe_allow_html=True)
        with st.container():
            self.create_dashboard()

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

    def season_selection(self):
        with st.container(border=False):
            league = ''
            season = ''
            player = ''
            # Season
            left, middle, right = st.columns(3, vertical_alignment="bottom")
            with left:
                options = ['Average Joe', 'RiseUp']
                league = st.segmented_control("League", options, selection_mode="single", default='Average Joe')

            with middle:
                options = ['1', '2', '3']
                season = st.segmented_control("Season", options, selection_mode="single", default='1')

            # Players
            col1, col2 = st.columns([2,1])
            with col1:
                option_map = {
                    0: 'David Perez',
                    1: 'Josh',
                    2: 'Jake',
                    3: 'Noel Ramos',
                    4: 'John',
                    5: 'James Perez',
                    6: 'Marcus',
                    7: 'Ricky',
                    8: 'Harry',
                    9: 'Jeff',
                    10: 'James',
                    11: 'Marcus',
                    12: 'Ricky',
                    14: 'Harry',
                }

                selection = st.pills(
                        "Players",
                        options=option_map.keys(),
                        format_func=lambda option: option_map[option],
                        selection_mode="single",
                    
                )
                st.write(
                        "Your selected option: "
                        f"{None if selection is None else option_map[selection]}"
                    
                )
            st.markdown('#####') # Margin bottom space

        return league, season, player


    def create_dashboard(self):
        league, season, player = self.season_selection()

        card_theme = {
            # 'background-color': '#f0f1f6',
            'background-color': '#f5f9fa',
            'font-family': 'sans-serif',
            'color': '#252525',
            'border-radius': '.3em',
        }

        left_coloumn_card_theme = {
            'padding': '.5em',
            # 'backgroundColor': '#efefef',
            # 'backgroundColor': '#f0f1f6',
            'backgroundColor': '#f5f9fa',
            'backdrop-filter': 'blur(32px)',
            'font-family': 'sans-serif',
            'color': '#252525',
            # 'max-width': '600px',
            'border-radius': '5px',
        }

        with st.container():
            with elements('dashboard'):
                # First, build a default layout for every element you want to include in your dashboard
                layout = [
                    # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
                    dashboard.Item('radar_graph', 0, 0, 4, 4, isResizable=False, isDraggable=False, moved=False),
                    dashboard.Item('line_graph', 4, 0, 8, 4, isResizable=False, isDraggable=False, moved=False),
                ]

                mui.Box(
                    f'{player}',
                    sx={
                        'backgroundColor': '#f8f8f8',
                        'backdrop-filter': 'blur(32px)',
                        'color': '#252525',
                        'opacity': '0.1',
                        'text-transform': 'uppercase',
                        'font-family': 'sans-serif',
                        'font-weight': 'bold',
                        'font-size': '150px',
                    }
                )

                with dashboard.Grid(layout):
                    with mui.Box(sx=left_coloumn_card_theme, key='radar_graph'):
                        self.radar_graph()

                    with mui.Box(sx=card_theme, key='line_graph'):
                        self.line_graph()

        with st.container():
            col1, col2 = st.columns([1,2])
            with col1:
                self.season_stats()
                self.career_stats()
            with col2:
                self.create_game_log()

    def collect_data(self):
        player_sample_data = sample_data.player_sample_data()
        player_stats = pd.DataFrame.from_records(player_sample_data)

        shooting_sample_data = sample_data.shooting_sample_data()
        shooting_stats = pd.DataFrame.from_records(shooting_sample_data)

        return player_stats, shooting_stats

    def create_game_log(self):
        # Data
        player_stats_df, shooting_stats_df = self.collect_data()
        # Container for tables
        container = st.container(border=False)
        with container:
            # Player tables
            st.dataframe(player_stats_df, width=100000)

    def season_stats(self):
        data = {
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

        with st.container(border=True):
            st.markdown('###### Season Stats')
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric(label='PTS', value=data['pts'], delta=+2.2, delta_color='normal')
                st.metric(label='ORB', value=data['orb'], delta=+2.2, delta_color='normal')
                st.metric(label='FG', value=data['fg'], delta=+2.2, delta_color='normal')
                st.metric(label='2P', value=data['2p'], delta=+2.2, delta_color='normal')
            with col2:
                st.metric(label='AST', value=data['ast'], delta=+2.2, delta_color='normal')
                st.metric(label='DRB', value=data['drb'], delta=+2.2, delta_color='normal')
                st.metric(label='FG%', value=data['fg'], delta=+2.2, delta_color='normal')
                st.metric(label='2P%', value=data['2p%'], delta=+2.2, delta_color='normal')
            with col3:
                st.metric(label='STL', value=data['stl'], delta=+2.2, delta_color='normal')
                st.metric(label='FOUL', value=data['foul'], delta=+2.2, delta_color='normal')
                st.metric(label='FT', value=data['ft'], delta=+2.2, delta_color='normal')
                st.metric(label='3P', value=data['3p'], delta=+2.2, delta_color='normal')
            with col4:
                st.metric(label='BLK', value=data['blk'], delta=+2.2, delta_color='normal')
                st.metric(label='TUR', value=data['tur'], delta=+2.2, delta_color='normal')
                st.metric(label='FT%', value=data['ft%'], delta=+2.2, delta_color='normal')
                st.metric(label='3P%', value=data['3p%'], delta=+2.2, delta_color='normal')
            with col5:
                st.metric(label='Effective FG%', value=5.7, delta=+2.2, delta_color='normal')
                st.metric(label='Turnover Ratio', value=41.6, delta=+2.2, delta_color='normal')
                st.metric(label='ORB %', value=4.1, delta=+2.2, delta_color='normal')
                st.metric(label='FT Ratio', value=32.2, delta=+2.2, delta_color='normal')

    def career_stats(self):
        data = {
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

        st.markdown(
            """
                <style>
                    [data-testid="stMetricLabel"] {
                        font-size: 12px;
                            
                    }
                        
                    [data-testid="stMetricValue"] {
                        font-size: 25px;
                            
                    }
                </style>
            """, unsafe_allow_html=True
            )

        with st.container(border=True):
            st.markdown('###### Career Stats')
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric(label='PTS', value=data['pts'], delta=+2.2, delta_color='normal')
                st.metric(label='ORB', value=data['orb'], delta=+2.2, delta_color='normal')
                st.metric(label='FG', value=data['fg'], delta=+2.2, delta_color='normal')
                st.metric(label='2P', value=data['2p'], delta=+2.2, delta_color='normal')
            with col2:
                st.metric(label='AST', value=data['ast'], delta=+2.2, delta_color='normal')
                st.metric(label='DRB', value=data['drb'], delta=+2.2, delta_color='normal')
                st.metric(label='FG%', value=data['fg'], delta=+2.2, delta_color='normal')
                st.metric(label='2P%', value=data['2p%'], delta=+2.2, delta_color='normal')
            with col3:
                st.metric(label='STL', value=data['stl'], delta=+2.2, delta_color='normal')
                st.metric(label='FOUL', value=data['foul'], delta=+2.2, delta_color='normal')
                st.metric(label='FT', value=data['ft'], delta=+2.2, delta_color='normal')
                st.metric(label='3P', value=data['3p'], delta=+2.2, delta_color='normal')
            with col4:
                st.metric(label='BLK', value=data['blk'], delta=+2.2, delta_color='normal')
                st.metric(label='TUR', value=data['tur'], delta=+2.2, delta_color='normal')
                st.metric(label='FT%', value=data['ft%'], delta=+2.2, delta_color='normal')
                st.metric(label='3P%', value=data['3p%'], delta=+2.2, delta_color='normal')
            with col5:
                st.metric(label='Effective FG%', value=5.7, delta=+2.2, delta_color='normal')
                st.metric(label='Turnover Ratio', value=41.6, delta=+2.2, delta_color='normal')
                st.metric(label='ORB %', value=4.1, delta=+2.2, delta_color='normal')
                st.metric(label='FT Ratio', value=32.2, delta=+2.2, delta_color='normal')

    def line_graph(self):
        with elements('line_graph'):
            DATA = [
                {
                    'id': 'Turnovers',
                    'data': [
                        { 'x': 'Game 1', 'y': 0 },
                        { 'x': 'Game 2', 'y': 0 },
                        { 'x': 'Game 3', 'y': 1 },
                        { 'x': 'Game 4', 'y': 0 },
                        { 'x': 'Game 5', 'y': 0 },
                        { 'x': 'Game 6', 'y': 2 },
                        { 'x': 'Game 7', 'y': 4 },
                        { 'x': 'Game 8', 'y': 0 },
                        { 'x': 'Game 9', 'y': 0 },
                        { 'x': 'Game 10', 'y': 0 },
                        { 'x': 'Game 11', 'y': 0 },
                        { 'x': 'Game 12', 'y': 0 },
                        { 'x': 'Game 13', 'y': 2 },
                        { 'x': 'Game 14', 'y': 0 },
                    ]
                },
                {
                    'id': 'Steals',
                    'data': [
                        { 'x': 'Game 1', 'y': 0 },
                        { 'x': 'Game 2', 'y': 2 },
                        { 'x': 'Game 3', 'y': 1 },
                        { 'x': 'Game 4', 'y': 0 },
                        { 'x': 'Game 5', 'y': 0 },
                        { 'x': 'Game 6', 'y': 0 },
                        { 'x': 'Game 7', 'y': 1 },
                        { 'x': 'Game 8', 'y': 0 },
                        { 'x': 'Game 9', 'y': 0 },
                        { 'x': 'Game 10', 'y': 0 },
                        { 'x': 'Game 11', 'y': 0 },
                        { 'x': 'Game 12', 'y': 1 },
                        { 'x': 'Game 13', 'y': 2 },
                        { 'x': 'Game 14', 'y': 2 },
                    ]
                },
                {
                    'id': 'Blocks',
                    'data': [
                        { 'x': 'Game 1', 'y': 0 },
                        { 'x': 'Game 2', 'y': 2 },
                        { 'x': 'Game 3', 'y': 1 },
                        { 'x': 'Game 4', 'y': 0 },
                        { 'x': 'Game 5', 'y': 0 },
                        { 'x': 'Game 6', 'y': 1 },
                        { 'x': 'Game 7', 'y': 1 },
                        { 'x': 'Game 8', 'y': 0 },
                        { 'x': 'Game 9', 'y': 0 },
                        { 'x': 'Game 10', 'y': 0 },
                        { 'x': 'Game 11', 'y': 0 },
                        { 'x': 'Game 12', 'y': 0 },
                        { 'x': 'Game 13', 'y': 2 },
                        { 'x': 'Game 14', 'y': 0 },
                    ]
                },
                {
                    'id': 'Assists',
                    'data': [
                        { 'x': 'Game 1', 'y': 3 },
                        { 'x': 'Game 2', 'y': 2 },
                        { 'x': 'Game 3', 'y': 2 },
                        { 'x': 'Game 4', 'y': 4 },
                        { 'x': 'Game 5', 'y': 2 },
                        { 'x': 'Game 6', 'y': 3 },
                        { 'x': 'Game 7', 'y': 1 },
                        { 'x': 'Game 8', 'y': 0 },
                        { 'x': 'Game 9', 'y': 0 },
                        { 'x': 'Game 10', 'y': 2 },
                        { 'x': 'Game 11', 'y': 1 },
                        { 'x': 'Game 12', 'y': 0 },
                        { 'x': 'Game 13', 'y': 2 },
                        { 'x': 'Game 14', 'y': 4 },
                    ]
                },
                {
                    'id': 'Rebounds',
                    'data': [
                        { 'x': 'Game 1', 'y': 3 },
                        { 'x': 'Game 2', 'y': 7 },
                        { 'x': 'Game 3', 'y': 10 },
                        { 'x': 'Game 4', 'y': 11 },
                        { 'x': 'Game 5', 'y': 7 },
                        { 'x': 'Game 6', 'y': 9 },
                        { 'x': 'Game 7', 'y': 4 },
                        { 'x': 'Game 8', 'y': 6 },
                        { 'x': 'Game 9', 'y': 5 },
                        { 'x': 'Game 10', 'y': 10 },
                        { 'x': 'Game 11', 'y': 5 },
                        { 'x': 'Game 12', 'y': 3 },
                        { 'x': 'Game 13', 'y': 12 },
                        { 'x': 'Game 14', 'y': 8 },
                    ]
                },
                {
                    'id': 'Points',
                    'data': [
                        { 'x': 'Game 1', 'y': 3 },
                        { 'x': 'Game 2', 'y': 0 },
                        { 'x': 'Game 3', 'y': 12 },
                        { 'x': 'Game 4', 'y': 15 },
                        { 'x': 'Game 5', 'y': 17 },
                        { 'x': 'Game 6', 'y': 4 },
                        { 'x': 'Game 7', 'y': 6 },
                        { 'x': 'Game 8', 'y': 10 },
                        { 'x': 'Game 9', 'y': 12 },
                        { 'x': 'Game 10', 'y': 4 },
                        { 'x': 'Game 11', 'y': 6 },
                        { 'x': 'Game 12', 'y': 6 },
                        { 'x': 'Game 13', 'y': 0 },
                        { 'x': 'Game 14', 'y': 12 },
                    ]
                },
            ]

            nivo.Line(
                data=DATA,
                margin={
                    'top': 50,
                    'right':30,
                    'bottom':50,
                    'left':60
                },
                xScale={'type': 'point'},
                yScale={
                    'type': 'linear',
                    'min': 'auto',
                    'max': 'auto',
                    # 'stacked': True,
                    'reverse': False,
                },
                yFormat='',
                axisTop=None,
                axisRight=None,
                axisBottom={
                    'tickSize':5,
                    'tickPadding':5,
                    'tickRotation':-35,
                    'legend':'',
                    'legendOffset':52,
                    'legendPosition':'middle',
                    'truncateTickAt':0,
                },
                axisLeft={
                    'tickSize': 5,
                    'tickPadding': 5,
                    'tickRotation': 0,
                    'legendOffset': -40,
                    'legendPosition': 'middle',
                    'truncateTickAt': 0,
                },
                colors={'scheme': 'paired'},
                pointSize=9,
                pointColor={'from': 'color', 'modifiers': []},
                pointBorderWidth=2,
                pointBorderColor={'theme': 'background', 'modifiers': []},
                enablePointLabel=True,
                pointLabel='y',
                pointLabelYOffset=-12,
                areaOpacity=0.25,
                isInteractive=True,
                useMesh=True,
                debugMesh=True,
                enableSlices='x',
                enableTouchCrosshair=True,
                legends=[
                    {
                        'anchor': 'top',
                        'direction': 'row',
                        'justify': False,
                        'translateX': 18,
                        'translateY': -37,
                        'itemsSpacing': 0,
                        'itemDirection': 'left-to-right',
                        'itemWidth': 80,
                        'itemHeight': 20,
                        'itemOpacity': 0.75,
                        'symbolSize': 12,
                        'symbolShape': 'square',
                        'symbolBorderColor': 'rgba(0,0,0,.5)',
                        'effects': [
                            {
                                'on': 'hover',
                                'style': {
                                    'itemBackground': '#dfdfdf',
                                    'itemOpacity': 1,
                                }
                            }
                        ]
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
                # colors = [ '#e7b7f4', '#9488d8', '#dc143c'],
                colors = [ '#ffaf31', '#ff4655', '#5c00ff'],
                colorBy='index',
                curve='catmullRomClosed',
                fillOpacity=0.35,
                indexBy='index',
                valueFormat='>-.2f',
                margin={'top': 70, 'right': 90, 'bottom': 40, 'left': 90},
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
                    'textColor': '#252525',
                    'tooltip': {
                        'container': {
                            'color': '#252525',
                        }
                    },
                    'gridColor': '#000',
                }
            )

    def heatmap(self):
        # Plotting
        # fig, ax = plt.subplots(figsize=(6.1,5.4))
        # fig, ax = plt.subplots(figsize=(5.25,4.4))
        # draw_court(ax, outer_lines=True)
        plt.figure(figsize=(5.25,4.4))
        draw_court(outer_lines=True)
        # st.pyplot(plt) # Plot shot chart

        # Update figure with new parameters
        plt.xlim(-260,320)
        plt.ylim(-50,430)

        img_base64 = self.plot_to_base64(plt)

        with elements("plotly_box"):
            mui.Box(
                html.Img(src=f'data:image/png;base64,{img_base64}'),
                sx={
                    "max-width": "100%",
                    "height": "100%",
                    "margin": "0",
                }
            )

    def plot_to_base64(self, fig):
        buf = BytesIO()
        fig.savefig(buf, format="png", bbox_inches='tight')
        buf.seek(0)
        return base64.b64encode(buf.read()).decode('utf-8')




def main():
    player_stats = PlayerStatisticsDashboard()


main()
