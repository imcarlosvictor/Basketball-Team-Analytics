import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import sample_data

from PIL import Image
from utils import court_coordinates as cc
from matplotlib.colors import ListedColormap
from streamlit_option_menu import option_menu
from streamlit_card import card

from modules.team_leaders import *

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
        create_team_leaders_table()
        self.create_player_table_stats()
        self.create_shooting_table_stats()

    def player_comparison(self):
        pass

    def create_player_table_stats(self):
        # Data
        player_stats_df, shooting_stats_df = collect_data()
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
        player_stats_df, shooting_stats_df = collect_data()
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
        # custom_colors = ['#ffdfbe', '#ffd1ad', '#ffc39b', '#ffb58a' ,'#ffa778', '#ff9967']
        custom_colors = ['#f0d1f2', '#e7c3e8', '#deb5de', '#d4a7d3' ,'#db99c9']
        custom_cmap = ListedColormap(custom_colors)
        heatmap = df.style.format(precision=1).background_gradient(cmap=custom_cmap)
        st.dataframe(heatmap, width=100000)

    def shooting_table_heatmap(self, df):
        custom_colors = ['#ffa9a9', '#ff9997', '#ff8986', '#ff7974', '#ff6962']
        custom_cmap = ListedColormap(custom_colors)
        heatmap = df.style.format(precision=1).background_gradient(cmap=custom_cmap)
        st.dataframe(heatmap, width=100000)



def main():
    homepage = Dashboard()

if __name__ == '__main__':
    main()
