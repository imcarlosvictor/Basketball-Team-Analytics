import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

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

            # with left:
            #     options = ['Average Joe', 'RiseUp']
            #     selection = st.pills('League', options, selection_mode='single', default='Average Joe')

            # with middle:
            #     options = ['1', '2', '3']
            #     selection = st.pills('Season', options, selection_mode='single', default='1')

            with left:
                options = ['Average Joe', 'RiseUp']
                selection = st.segmented_control("League", options, selection_mode="single", default='Average Joe')

            with middle:
                options = ['1', '2', '3']
                selection = st.segmented_control("Season", options, selection_mode="single", default='1')

            st.markdown('#####') # Margin bottom space

    def create_dashboard(self):
        self.season_selection()

        leading_stats_container = st.container()
        col_1, col_2, col_3, col_4, col_5, col_6 = st.columns(6)

        with leading_stats_container:
            # Leading Overall Statistics
            st.markdown('###### Team Leaders')

            with col_1:
                with st.container(border=True):
                    st.markdown('### Points')
                    st.text('<player name>')

            with col_2:
                with st.container(border=True):
                    st.markdown('### FG%')
                    st.text('<player name>')

            with col_3:
                # card_2 = st.container(border=True)
                with st.container(border=True):
                    st.subheader('Rebounds')
                    st.text('<player name>')

            with col_4:
                with st.container(border=True):
                    st.subheader('Assists')
                    st.text('<player name>')

            with col_5:
                with st.container(border=True):
                    st.subheader('Steals')
                    st.text('<player name>')

            with col_6:
                with st.container(border=True):
                    st.subheader('Blocks')
                    st.text('<player name>')

        self.player_table_stats()
        self.shooting_table_stats()


    def game_logs(self):
        pass

    def player_comparison(self):
        pass

    def player_table_stats(self):
        # Data
        sample_data = self.sample_data()
        df = pd.DataFrame.from_records(sample_data)

        # Container for tables
        container = st.container(border=False)
        with container:
            st.write('###### Player Stats')

            # Player tables
            st.dataframe(df, width=100000)
            self.player_table_heatmap(df)

    def player_table_heatmap(self, df):
        heatmap = df.style.format(precision=1).background_gradient(cmap='Wistia')
        st.dataframe(heatmap, width=100000)

    def shooting_table_stats(self):
        # Data
        sample_data = self.sample_data()
        df = pd.DataFrame.from_records(sample_data)

        # Container for tables
        container = st.container(border=False)
        with container:
            st.write('###### Shooting Stats')

            # Player tables
            st.dataframe(df, width=100000)
            self.shooting_table_heatmap(df)


    def shooting_table_heatmap(self, df):
        heatmap = df.style.format(precision=1).background_gradient(cmap='Wistia')
        st.dataframe(heatmap, width=100000)

    def sample_data(self):
        sample_data = [{
            'Name': 'Liesa McMinn',
            'GP': 23,
            'PTS': 21.3,
            'OR': 5.3,
            'DR': 2.2,
            'REB': 8.4,
            'AST': 1.3,
            'STL': 1.1,
            'BLK': 2.7,
            'TO': 0.8,
        }, {
            'Name': 'Augusta Yansons',
            'GP': 23,
            'PTS': 12.3,
            'OR': 1.2,
            'DR': 4.2,
            'REB': 5.4,
            'AST': 3.5,
            'STL': 3.3,
            'BLK': 2.7,
            'TO': 3.0,
        }, {
            'Name': 'Errick Lingner',
            'GP': 23,
            'PTS': 12.3,
            'OR': 1.2,
            'DR': 4.2,
            'REB': 7.4,
            'AST': 1.5,
            'STL': 1.3,
            'BLK': 0.8,
            'TO': 5.1,
        }, {
            'Name': 'Suki Roderham',
            'GP': 23,
            'PTS': 10.3,
            'OR': 3.2,
            'DR': 0.2,
            'REB': 3.0,
            'AST': 0.9,
            'STL': 1.0,
            'BLK': 3.1,
            'TO': 0.2,
        }, {
            'Name': 'Tarrah Gatehouse',
            'GP': 23,
            'PTS': 12.3,
            'OR': 1.2,
            'DR': 4.2,
            'REB': 5.4,
            'AST': 3.5,
            'STL': 1.3,
            'BLK': 2.7,
            'TO': 3.0,
        }, {
            'Name': 'Roland Goane',
            'GP': 23,
            'PTS': 12.3,
            'OR': 1.2,
            'DR': 4.2,
            'REB': 5.4,
            'AST': 3.5,
            'STL': 1.3,
            'BLK': 2.7,
            'TO': 3.0,
        }, {
            'Name': 'Trude Greenham',
            'GP': 23,
            'PTS': 12.3,
            'OR': 1.2,
            'DR': 4.2,
            'REB': 5.4,
            'AST': 3.5,
            'STL': 1.3,
            'BLK': 2.7,
            'TO': 3.0,
        }] 

        return sample_data


def main():
    homepage = Dashboard()

if __name__ == '__main__':
    main()
