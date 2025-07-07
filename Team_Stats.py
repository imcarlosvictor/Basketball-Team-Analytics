import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import sample_data

from PIL import Image
from utils import court_coordinates as cc
from streamlit_option_menu import option_menu
from streamlit_card import card


class Dashboard:
    def __init__(self):
        favicon = Image.open('./assests/basketball.png')
        st.set_page_config(
            page_title='BWB Team Stats',
            page_icon=favicon,
            layout='wide',
            initial_sidebar_state = 'collapsed',
        )
        st.markdown(
            '<style> body { text-transform: uppercase; } </style>',
            unsafe_allow_html=True
        )

        # self.create_sidebar()
        self.create_dashboard()

    def season_selection(self):
        with st.container(border=False):
            left, middle, right = st.columns(3, vertical_alignment="bottom")
            with left:
                options = ['Average Joe', 'RiseUp']
                selection = st.segmented_control("League", options, selection_mode="single", default='Average Joe')

            with middle:
                options = ['1', '2', '3']
                selection = st.segmented_control("Season", options, selection_mode="single", default='1')

            st.markdown('#####') # Margin bottom space

    def create_dashboard(self):
        self.season_selection()
        self.create_team_leaders_table()
        self.create_player_table_stats()
        self.create_shooting_table_stats()

    def collect_data(self):
        player_sample_data = sample_data.player_sample_data()
        player_stats = pd.DataFrame.from_records(player_sample_data)

        shooting_sample_data = sample_data.shooting_sample_data()
        shooting_stats = pd.DataFrame.from_records(shooting_sample_data)

        return player_stats, shooting_stats

    def get_team_leader_stats(self):
        player_stats_df, shooting_stats_df = self.collect_data()

        data = {
            'PTS_leader': '',
            'leading_PTS_stat': 0,
            'FG_leader': '',
            'leading_FG_stat': 0,
            'REB_leader': '',
            'leading_REB_stat': 0,
            'AST_leader': '',
            'leading_AST_stat': 0,
            'STL_leader': '',
            'leading_STL_stat': 0,
            'BLK_leader': '',
            'leading_BLK_stat': 0,
        }

        shooting_stat_list = shooting_stats_df.to_dict(orient='records')
        for dict_item in shooting_stat_list:
            if dict_item['FG%'] > data['leading_FG_stat']:
                data['leading_FG_stat'] = dict_item['FG%']
                data['FG_leader'] = dict_item['Name']

        player_stat_list = player_stats_df.to_dict(orient='records')
        for dict_item in player_stat_list:
            if dict_item['PTS'] > data['leading_PTS_stat']:
                data['leading_PTS_stat'] = dict_item['PTS']
                data['PTS_leader'] = dict_item['Name']

            if dict_item['REB'] > data['leading_REB_stat']:
                data['leading_REB_stat'] = dict_item['REB']
                data['REB_leader'] = dict_item['Name']

            if dict_item['AST'] > data['leading_AST_stat']:
                data['leading_AST_stat'] = dict_item['AST']
                data['AST_leader'] = dict_item['Name']

            if dict_item['STL'] > data['leading_STL_stat']:
                data['leading_STL_stat'] = dict_item['STL']
                data['STL_leader'] = dict_item['Name']

            if dict_item['BLK'] > data['leading_BLK_stat']:
                data['leading_BLK_stat'] = dict_item['BLK']
                data['BLK_leader'] = dict_item['Name']

        return data

    def create_team_leaders_table(self):
        data = self.get_team_leader_stats()

        leading_stats_container = st.container()
        col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)

        # CSS to hide delta arrow
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

        with leading_stats_container:
            # Leading Overall Statistics
            st.markdown('###### Team Leaders')

            with col_1:
                with st.container(border=False):
                    st.metric(
                        label='**points**', 
                        value=f'{data["leading_PTS_stat"]}', 
                        delta=f'{data["PTS_leader"]}',
                        delta_color='inverse',
                    )
            with col_2:
                with st.container(border=False):
                    st.metric(
                        label='**FG%**', 
                        value=f'{data["leading_FG_stat"]}', 
                        delta=f'{data["FG_leader"]}',
                        delta_color='inverse',
                    )
            with col_3:
                # card_2 = st.container(border=True)
                with st.container(border=False):
                    st.metric(
                        label='**rebounds**', 
                        value=f'{data["leading_REB_stat"]}', 
                        delta=f'{data["REB_leader"]}',
                        delta_color='inverse',
                    )
            with col_4:
                with st.container(border=False):
                    st.metric(
                        label='**assists**', 
                        value=f'{data["leading_AST_stat"]}', 
                        delta=f'{data["AST_leader"]}',
                        delta_color='inverse',
                    )
            with col_5:
                with st.container(border=False):
                    st.metric(
                        label='**steals**', 
                        value=f'{data["leading_STL_stat"]}', 
                        delta=f'{data["STL_leader"]}',
                        delta_color='inverse',
                    )
            with col_6:
                with st.container(border=False):
                    st.metric(
                        label='**blocks**', 
                        value=f'{data["leading_BLK_stat"]}', 
                        delta=f'{data["BLK_leader"]}',
                        delta_color='inverse',
                    )

        st.markdown('######')

    def player_comparison(self):
        pass

    def create_player_table_stats(self):
        # Data
        player_stats_df, shooting_stats_df = self.collect_data()
        # Container for tables
        container = st.container(border=False)
        with container:
            # Player tables
            on = st.toggle('Player Stats Heatmap')
            if on:
                self.player_table_heatmap(player_stats_df)
            else:
                st.dataframe(player_stats_df, width=100000)

    def create_shooting_table_stats(self):
        # Data
        player_stats_df, shooting_stats_df = self.collect_data()
        # Container for tables
        container = st.container(border=False)
        with container:
            # Player tables
            on = st.toggle('Shooting Stats Heatmap')
            if on:
                self.shooting_table_heatmap(shooting_stats_df)
            else:
                st.dataframe(shooting_stats_df, width=100000)

    def player_table_heatmap(self, df):
        # heatmap = df.style.format(precision=1).background_gradient(cmap='Wistia')
        heatmap = df.style.format(precision=1).background_gradient(cmap='summer')
        st.dataframe(heatmap, width=100000)

    def shooting_table_heatmap(self, df):
        # heatmap = df.style.format(precision=1).background_gradient(cmap='Purples')
        heatmap = df.style.format(precision=1).background_gradient(cmap='Wistia')
        st.dataframe(heatmap, width=100000)



def main():
    homepage = Dashboard()

if __name__ == '__main__':
    main()
