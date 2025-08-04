import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

from PIL import Image
from utils import court_coordinates as cc
from matplotlib.colors import ListedColormap
from streamlit_extras.stylable_container import stylable_container
from modules.basketball_court import draw_court

from modules.team_leaders import *

# from mplbasketball import Court
# from mplbasketball.utils import transform


class GameStatisticsDashboard:
    def __init__(self):
        favicon = Image.open('./assests/basketball.png')
        st.set_page_config(
            page_title='Game Report',
            page_icon=favicon,
            layout='wide',
        )
        # Uppercase all text
        st.markdown('<style> body { text-transform: uppercase; } </style>', unsafe_allow_html=True)
        self.create_game_stat_dashboard()

    def create_game_stat_dashboard(self):
        self.create_filter_search()
        self.embedded_video_slider()
        self.create_game_summary()
        self.create_tabs()
        # self.plot_basketball_court()
        # self.plot_shot_chart()

    def create_tabs(self):
        tab1, tab2, tab3 = st.tabs(['Box Score', 'Team Stats', 'Shot Chart',])
        with tab1:
            create_team_leaders_table()
            self.create_home_team_stats()
            self.create_away_team_stats()
        with tab2:
            self.create_team_stats_dataframe()

    def create_filter_search(self):
        with st.container():
            user_choice = ''
            col1, col2, col3 = st.columns(3)
            with col1:
                league = st.selectbox(
                    'League',
                    (
                        'AverageJoes',
                        'RiseUp',
                    ),
                    index=None,
                )
            with col2:
                season = st.selectbox(
                    'Season',
                    (
                        'Winter 2024',
                        'Summer 2025',
                    ),
                    index=None,
                )
            with col3:
                game = st.selectbox(
                    'Game',
                    (
                        'Game 1: ABG',
                        'Game 2: CL Warriors',
                    ),
                    index=None,
                )

        st.divider()

    def embedded_video_slider(self):
        """From filter search, find the video on youtube page."""

        VIDEO_URL = 'https://www.youtube.com/watch?v=ZQ1dfAVO910'
        with st.expander('Game'):
            st.video(VIDEO_URL)
            
    def create_game_summary(self):
        with st.container():
            col1, col2, col3 = st.columns([2,1,2])

            with col1:
                st.text('Bros w/ Benefits')
                st.write("""<style>
                    [data-testid='stVerticalBlock']
                    [data-testid='stVerticalBlockBorderWrapper']:nth-child(1) {
                        width: 100%;
                        height: 100%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }

                    [data-testid='stVerticalBlockBorderWrapper'] 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stHorizontalBlock'] 
                    [data-testid='stColumn']:nth-child(1) {
                        display: grid;
                        justify-content: right;
                        align-items: end;
                    }

                    [data-testid='stVerticalBlockBorderWrapper'] 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stHorizontalBlock'] 
                    [data-testid='stColumn']:nth-child(1) 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stElementContainer']:nth-child(1) 
                    [data-testid='stText'] {
                        font-size: 30px;
                        font-weight: bold;
                        text-align: right;
                    }
                    </style>""", unsafe_allow_html=True)

            with col2:
                st.text('36-28')
                st.write("""<style>
                    [data-testid='stVerticalBlock']
                    [data-testid='stVerticalBlockBorderWrapper']:nth-child(1) {
                        width: 100%;
                        # height: 100%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }

                    [data-testid='stVerticalBlockBorderWrapper'] 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stHorizontalBlock'] 
                    [data-testid='stColumn']:nth-child(2) {
                        display: grid;
                        justify-content: center;
                        align-items: end;
                    }

                    [data-testid='stVerticalBlockBorderWrapper'] 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stHorizontalBlock'] 
                    [data-testid='stColumn']:nth-child(2) 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stElementContainer']:nth-child(1) 
                    [data-testid='stText'] {
                        font-size: 50px;
                        font-weight: bold;
                    }
                    </style>""", unsafe_allow_html=True)

            with col3:
                st.text('CL Warriors')
                st.write("""<style>
                    [data-testid='stVerticalBlock']
                    [data-testid='stVerticalBlockBorderWrapper']:nth-child(1) {
                        width: 100%;
                        height: 100%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }

                    [data-testid='stVerticalBlockBorderWrapper'] 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stHorizontalBlock'] 
                    [data-testid='stColumn']:nth-child(3) {
                        display: grid;
                        justify-content: left;
                        align-items: end;
                    }

                    [data-testid='stVerticalBlockBorderWrapper'] 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stHorizontalBlock'] 
                    [data-testid='stColumn']:nth-child(3) 
                    [data-testid='stVerticalBlock'] 
                    [data-testid='stElementContainer']:nth-child(1) 
                    [data-testid='stText'] {
                        font-size: 30px;
                        font-weight: bold;
                        text-align: left;
                    }
                    </style>""", unsafe_allow_html=True)

        with st.container():
            data = pd.DataFrame(
                {
                    '': ['Bros w/ Benefits', 'CL Warriors'],
                    'Half 1': [10, 13],
                    'Half 2': [26, 15],
                    'Total': [36, 28],
                }
            )

            # Center table header and data 
            s1 = dict(selector='th', props=[('text-align', 'center')])
            s2 = dict(selector='td', props=[('text-align', 'center')])
            table = data.style.set_table_styles([s1, s2]).to_html()

            # Hide unique key upon table creation
            st.markdown("""
                <style>
                    table td {
                            text-align: left;
                    }

                    table td:nth-child(1) {
                            display: none
                    }

                    table th:nth-child(1) {
                            display: none
                    }
                </style>
            """, unsafe_allow_html=True)
           
            st.write("""<style>
                [data-testid='stVerticalBlock']
                [data-testid='stVerticalBlockBorderWrapper']:nth-child(3) {
                    width: 100%;
                    height: 100%;
                    display: grid;
                    justify-content: center;
                    align-items: start;
                }

                [data-testid='stVerticalBlock']
                [data-testid='stVerticalBlockBorderWrapper']:nth-child(3)
                [data-testid='stVerticalBlock'] {
                    height: 100%;
                    display: flex;
                    align-items: start;
                }

                [data-testid='stVerticalBlock']
                [data-testid='stVerticalBlockBorderWrapper']:nth-child(3)
                [data-testid='stVerticalBlock'] 
                [data-testid='stElementContainer']:nth-child(2) {
                    background: blue;
                    height: 100%;
                    position: static;
                    top: 0;
                }

                [data-testid='stVerticalBlock']
                [data-testid='stVerticalBlockBorderWrapper']:nth-child(3)
                [data-testid='stVerticalBlock']
                [data-testid='stElementContainer']:nth-child(2) 
                [data-testid='stMarkdown'] {
                    width: 100%;
                    height: 100%;
                    display: grid;
                    justify-content: center;
                    align-items: start;
                }
                </style>""", unsafe_allow_html=True)
            st.write(f'{table}', unsafe_allow_html=True)

    def create_home_team_stats(self):
        # TABLE
        player_stats_df, shooting_stats_df = collect_data()
        # Container for tables
        container = st.container(border=False)
        with container:
            # Player tables
            on = st.toggle('Home Team Heatmap (BwB)')
            if on:
                # HEATMAP
                custom_colors = ['#ffdfbe', '#ffd1ad', '#ffc39b', '#ffb58a' ,'#ffa778', '#ff9967']
                custom_cmap = ListedColormap(custom_colors)
                heatmap = player_stats_df.style.format(precision=1).background_gradient(cmap=custom_cmap)
                st.dataframe(heatmap, width=100000)
            else:
                st.dataframe(player_stats_df, width=100000)

    def create_away_team_stats(self):
        # TABLE
        player_stats_df, shooting_stats_df = collect_data()
        # Container for tables
        container = st.container(border=False)
        with container:
            # Player tables
            on = st.toggle('Away Team Heatmap')
            if on:
                # HEATMAP
                custom_colors = ['#ffdfbe', '#ffd1ad', '#ffc39b', '#ffb58a' ,'#ffa778', '#ff9967']
                custom_cmap = ListedColormap(custom_colors)
                heatmap = player_stats_df.style.format(precision=1).background_gradient(cmap=custom_cmap)
                st.dataframe(heatmap, width=100000)
            else:
                st.dataframe(player_stats_df, width=100000)

    def plot_shot_chart(self):
        # Initialize Court object
        origin = 'bottom-left'
        court_type = 'fiba'
        court = Court(origin=origin)
        fig, ax = plt.subplots(1, 4)

        # Simulate some data
        n_pts = 100
        x_1 = np.random.uniform(0, 94, size=n_pts)
        y_1 = np.random.uniform(0, 50, size=n_pts)

        x_2 = np.random.uniform(0, 94, size=n_pts)
        y_2 = np.random.uniform(0, 50, size=n_pts)

        # On the first subplot, plot the data as is
        court.draw(ax[0], )
        ax[0].scatter(x_1, y_1, s=5, c='tab:blue')
        ax[0].scatter(x_2, y_2, s=5, c='tab:orange')

        x_1_hl, y_1_hl = transform(x_1, y_1, fr='h', to='hl', origin=origin, court_type='fiba')
        x_2_hr, y_2_hr = transform(x_2, y_2, fr='h', to='hr', origin=origin, court_type='fiba')
        court.draw(ax[1], )
        ax[1].scatter(x_1_hl, y_1_hl, s=5, c='tab:blue')
        ax[1].scatter(x_2_hr, y_2_hr, s=5, c='tab:orange')

        # x_1_vd, y_1_vd = transform(x_1_hl, y_1_hl, fr='hl', to='vd', origin=origin, court_type=court_type)
        # court.draw(ax[2], orientation='vd')
        # ax[2].scatter(x_1_vd, y_1_vd, s=5, c='tab:blue')

        # x_2_vu, y_2_vu = transform(x_2_hr, y_2_hr, fr='hl', to='vu', origin=origin, court_type=court_type)
        # court.draw(ax[3], orientation='vu')
        # ax[3].scatter(x_2_vu, y_2_vu, s=5, c='tab:orange')

    def plot_basketball_court(self):
        container_bg = '''
            <style>
                [id='scene'] {
                    background-color: #ececec;
                }
                [class='user-select-none svg-container'] {
                    background-color: #ececec;
                }
            </style>
        '''
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
                           'court': '#232323',
                           'hoop': '#e47041'
                },
                markers=False,
            )
            fig.update_traces(line=dict(width=3), hovertemplate=None, hoverinfo='skip', showlegend=False)
            fig.update_xaxes(gridcolor='#e8ecf2')
            fig.update_yaxes(gridcolor='#e8ecf2')
            fig.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
                scene_aspectmode='data',
                height=600,
                scene_camera=dict(
                    eye=dict(x=1.3, y=0, z=0.5)
                ),
                scene=dict(
                    xaxis=dict(title='', showticklabels=False, showgrid=False),
                    yaxis=dict(title='', showticklabels=False, showgrid=False),
                    # Court background hexcode (#fee1bd, #f4f0e6,  #f6e3c8, #c9b7ab, #cfcfcf, #777777, #87939f)
                    zaxis=dict(title='',  showticklabels=False, showgrid=False, showbackground=True, backgroundcolor='#f4f0e6'),
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
                legend_traceorder='reversed'
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

    def create_team_stats_dataframe(self):
        col1, col2, col3 = st.columns([2,4,2])

        with col1:
            self.display_team_leaders()

        with col2:
            df = pd.DataFrame(
                {
                    'Bros w/ Benefits': [
                        'FG',
                        'FG %',
                        '3PT',
                        '3PT %',
                        'FT',
                        'FT %',
                        'Rebounds',
                        'OFF Rebounds',
                        'DEF Rebounds',
                        'Assists',
                        'Steals',
                        'Blocks',
                        'Turnovers',
                        'Fouls',
                    ],
                    '': [
                        'FG',
                        'FG %',
                        '3PT',
                        '3PT %',
                        'FT',
                        'FT %',
                        'Rebounds',
                        'OFF Rebound',
                        'DEF Rebound',
                        'Assists',
                        'Steals',
                        'Blocks',
                        'Turnovers',
                        'Fouls',
                    ],
                    'CL Warriors': [
                        'FG',
                        'FG %',
                        '3PT',
                        '3PT %',
                        'FT',
                        'FT %',
                        'Rebounds',
                        'OFF Rebounds',
                        'DEF Rebounds',
                        'Assists',
                        'Steals',
                        'Blocks',
                        'Turnovers',
                        'Fouls',
                    ]
                }
            )
            
            df_styled = df.style.set_table_styles(
                [
                    {
                        'selector': 'th',
                        'props': [
                            ('background-color', '#ffb975'),
                        ]
                    },
                    {
                        'selector': 'td, th',
                        'props':[
                            ('border', 'none'),
                            ('text-align', 'center'),
                            ('width', '30%'),
                            ('height', '30px'),
                        ]
                    }
                ]
            )
            
            st.write(df_styled.to_html(), unsafe_allow_html=True)

        with col3:
            self.display_team_leaders()

    def display_team_leaders(self):
        # TODO: set data to their respective team box scores
        data = get_team_leader_stats()
        team_leader_container = st.container()
        col1, col2 = st.columns(2, gap='large')

        st.write(
            """
                <style>
                    [data-testid="stMetricDelta"] svg {
                    display: none;
            }
                </style>
            """,
            unsafe_allow_html=True,
        )

        with team_leader_container:
            with col1:
                with st.container(border=False):
                    st.metric(
                        label='**points**', 
                        value=f'{data["leading_PTS_stat"]}', 
                        delta=f'{data["PTS_leader"]}',
                        delta_color='inverse',
                    )
                st.markdown('######')
                with st.container(border=False):
                    st.metric(
                        label='**rebounds**', 
                        value=f'{data["leading_REB_stat"]}', 
                        delta=f'{data["REB_leader"]}',
                        delta_color='inverse',
                    )
                st.markdown('######')
                with st.container(border=False):
                    st.metric(
                        label='**steals**', 
                        value=f'{data["leading_STL_stat"]}', 
                        delta=f'{data["STL_leader"]}',
                        delta_color='inverse',
                    )
            with col2:
                with st.container(border=False):
                    st.metric(
                        label='**FG%**', 
                        value=f'{data["leading_FG_stat"]}', 
                        delta=f'{data["FG_leader"]}',
                        delta_color='inverse',
                    )
                st.markdown('######')
                with st.container(border=False):
                    st.metric(
                        label='**assists**', 
                        value=f'{data["leading_AST_stat"]}', 
                        delta=f'{data["AST_leader"]}',
                        delta_color='inverse',
                    )
                st.markdown('######')
                with st.container(border=False):
                    st.metric(
                        label='**blocks**', 
                        value=f'{data["leading_BLK_stat"]}', 
                        delta=f'{data["BLK_leader"]}',
                        delta_color='inverse',
                    )

        st.markdown('######')

def main():
    game_stats = GameStatisticsDashboard()


main()