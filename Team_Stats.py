import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image

from utils import court_coordinates as cc


class Dashboard:
    def __init__(self):
        favicon = Image.open('./assests/basketball.png')
        st.set_page_config(
            page_title='BWB Team Stats',
            page_icon=favicon,
            layout='wide',
        )

        st.markdown(
            '<style> body { text-transform: uppercase; } </style>',
            unsafe_allow_html=True
        )

    def create_dashboard(self):
        leading_stats_container = st.container()
        left, mid_left, mid_right, right = st.columns(4)

        with st.sidebar:
            options = [
                'AverageJoe',
                'RiseUp',
            ]
            selected_option = st.sidebar.selectbox('League', options)

        with leading_stats_container:
            # Leading Overall Statistics
            with left:
                card_1 = st.container(border=True)
                st.subheader('Points Per Game')
                st.text('<player name>')
                st.text('<player name>')
                st.text('<player name>')

            with mid_left:
                card_2 = st.container(border=True)
                st.subheader('Field Goal PGT')
                st.text('<player name>')
                st.text('<player name>')
                st.text('<player name>')

            with mid_right:
                card_3 = st.container(border=True)
                st.subheader('3PT Leader')
                st.text('<player name>')
                st.text('<player name>')
                st.text('<player name>')

            with right:
                card_4 = st.container(border=True)
                st.subheader('Assists')
                st.text('<player name>')
                st.text('<player name>')
                st.text('<player name>')

    def game_logs(self):
        pass

    def player_comparison(self):
        pass

    def radar_graph(self):
        pass

    def heatmap(self):
        pass

def main():
    homepage = Dashboard()
    homepage.create_dashboard()

if __name__ == '__main__':
    main()
