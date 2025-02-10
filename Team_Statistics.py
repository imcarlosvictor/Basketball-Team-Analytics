import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image

from utils import court_coordinates as cc


class Dashboard:
    def __init__(self):
        favicon = Image.open('./assests/basketball.png')
        st.set_page_config(
            page_title='BWB Team Statistics',
            page_icon=favicon,
            layout='wide',
        )

    def create_dashboard(self):
        leading_stats_container = st.container()
        left, mid_left, mid_right, right = st.columns(4)

        with leading_stats_container:
            # Leading Overall Statistics
            with left:
                card_1 = st.container(border=True)
                st.subheader('Leading Scorer')

            with mid_left:
                card_2 = st.container(border=True)
                st.subheader('Most Field Goals Made')

            with mid_right:
                card_3 = st.container(border=True)
                st.subheader('Most 3PT Field Goals made')

            with right:
                card_4 = st.container(border=True)
                st.subheader('Free Throw Percentage')




def main():
    homepage = Dashboard()
    homepage.create_dashboard()

if __name__ == '__main__':
    main()
