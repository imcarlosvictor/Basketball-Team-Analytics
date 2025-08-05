import pandas as pd
import streamlit as st


def create_play_by_play_summary():
    with st.container():
        half_1_df = pd.DataFrame(
            [
                {'time': '12:34', 'Player': 'Mark', 'Play': '3', 'BWB': '10', 'CLW': '19'},
                {'time': '12:34', 'Player': 'Mark', 'Play': '3', 'BWB': '10', 'CLW': '19'},
                {'time': '12:34', 'Player': 'Mark', 'Play': '3', 'BWB': '10', 'CLW': '19'},
                {'time': '12:34', 'Player': 'Mark', 'Play': '3', 'BWB': '10', 'CLW': '19'},
                {'time': '12:34', 'Player': 'Mark', 'Play': '3', 'BWB': '10', 'CLW': '19'},
            ]
        )

        half_2_df = pd.DataFrame(
            [
                {'time': '12:34', 'Player': 'Mark', 'Play': '3', 'BWB': '10', 'CLW': '19'},
                {'time': '12:34', 'Player': 'Mark', 'Play': '3', 'BWB': '10', 'CLW': '19'},
            ]
        )


        tab1, tab2 = st.tabs(['1st Half', '2nd Half'])
        with tab1:
            new_df = style_dataframe(half_1_df)
            st.write(new_df.to_html(), unsafe_allow_html=True)
        with tab2:
            new_df = style_dataframe(half_2_df)
            st.write(new_df.to_html(), unsafe_allow_html=True)

def style_dataframe(dataframe_to_style):
    styled_df = dataframe_to_style.style.set_table_styles(
        [
            {
                'selector': 'th',
                'props': [
                    ('background-color', '#c7cbe0'),
                ]
            },
            {
                'selector': 'td, th',
                'props':[
                    ('padding', '.4em'),
                    ('border', 'none'),
                    ('text-align', 'center'),
                    ('width', '25%'),
                    ('height', '30px'),
                ]
            }
        ]
    )

    return styled_df
