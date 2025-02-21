import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from PIL import Image
from numpy import sin, cos, pi
from streamlit_elements import dashboard, elements, mui, html



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

    def dashboard_elements(self):
        with elements('player_name'):
            mui.Box(
                'Player Name',
                sx={
                    'margin': '0px',
                    'padding': '0px',
                    'color': '#232323',
                    'text-transform': 'uppercase',
                    'font-family': 'sans-serif',
                    'font-weight': 'bold',
                    'font-size': '90px',
                }
            )

        card_theme = {
            'backgroundColor': '#9f9f9f',
            'backdrop-filter': 'blur(60px)',
            'opacity': '0.7',
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

            with dashboard.Grid(layout):
                mui.Card(
                    mui.CardContent('RADAR GRAPH'),
                    sx=card_theme,
                    key='radar_graph',
                )

                mui.Card(
                    mui.CardContent('ATTEMPTS vs. MAKES (Field Goals) PER GAME'),
                    sx=card_theme,
                    key='shot_attempts_vs_made_block',
                )

                mui.Card(
                    mui.Typography('CAREER STATS'),
                    mui.CardContent('23'),
                    sx=card_theme,
                    key='overall_stat_block',
                )

                mui.Card(
                    mui.Typography('PREVIOUS GAME STATS'),
                    mui.CardContent('999'),
                    sx=card_theme,
                    key='last_game_stat_block',
                )

                mui.Card(
                    mui.CardContent('SHOT CHART HEATMAP'),
                    sx=card_theme,
                    key='heatmap_block',
                )

    def shot_chart_heatmap(self):
        pass

    def degree_to_radian(self, degrees):
        return degrees*pi/180

    def draw_circular_gauge(self, degree_start, degree_end, annotation_text, r=1.0, padding=0.2, tick_length=0.02):
        radian_start, radian_end = self.degree_to_radian(degree_start), self.degree_to_radian(degree_end)
        theta = np.linspace(radian_start,radian_end,5000)
        x = r * cos(theta)
        y = r * sin(theta)
        fig = go.Figure()

        # draw the gauge bar
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode='markers',
            marker_symbol='circle',
            marker_size=20,
            hoverinfo='skip'
        ))

        # draw the inside radial border
        for r_outer in [r-padding,r+padding]:
            fig.add_shape(
                type='circle',
                xref='x', yref='y',
                x0=-r_outer, y0=-r_outer, x1=r_outer, y1=r_outer,
                line_color='white',
            )
            tick_theta = np.linspace(pi,-pi,13)
            tick_labels = np.linspace(0,330,12)
            tick_start_x, tick_end_x = (r+padding)*cos(tick_theta), (r+padding+tick_length)*cos(tick_theta)
            tick_start_y, tick_end_y = (r+padding)*sin(tick_theta), (r+padding+tick_length)*sin(tick_theta)
            tick_label_x, tick_label_y = (r+padding+0.04+tick_length)*cos(tick_theta), (r+padding+0.04+tick_length)*sin(tick_theta)

            # add ticks
            for i in range(len(tick_theta)):
                # add text in the center of the plot
                fig.add_trace(go.Scatter(
                    x=[0], y=[0],
                    mode='text',
                    text=[annotation_text],
                    textfont=dict(size=30),
                    textposition='middle center',
                    hoverinfo='skip'
                ))

            # get rid of axes, ticks, background
            fig.update_layout(
                showlegend=False,
                xaxis_range=[-1.5,1.5], yaxis_range=[-1.5,1.5],
                xaxis_visible=False, xaxis_showticklabels=False,
                yaxis_visible=False, yaxis_showticklabels=False,
                template='plotly_white',
                width=800, height=800

            )
            return fig



def main():
    player_stats = PlayerStatisticsDashboard()
    player_stats.create_sidebar()
    player_stats.create_dashboard()

main()
