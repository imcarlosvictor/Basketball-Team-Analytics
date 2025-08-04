import streamlit as st
import pandas as pd

import sample_data


def collect_data():
        player_sample_data = sample_data.player_sample_data()
        player_stats = pd.DataFrame.from_records(player_sample_data)

        shooting_sample_data = sample_data.shooting_sample_data()
        shooting_stats = pd.DataFrame.from_records(shooting_sample_data)

        return player_stats, shooting_stats

def get_team_leader_stats():
        player_stats_df, shooting_stats_df = collect_data()

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

def create_team_leaders_table():
    data = get_team_leader_stats()

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
        st.markdown('###### Game Leaders')

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