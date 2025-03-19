import streamlit as st

from streamlit_extras.grid import grid
from streamlit_elements import dashboard, elements, mui, html, nivo


class NivoGraphs:
    def line_graph(self):
        with elements('line_graph'):
            data = [
                {
                    'id': 'turnovers',
                    'data': [
                        { 'x': 'game 1', 'y': 0 },
                        { 'x': 'game 2', 'y': 0 },
                        { 'x': 'game 3', 'y': 1 },
                        { 'x': 'game 4', 'y': 0 },
                        { 'x': 'game 5', 'y': 0 },
                        { 'x': 'game 6', 'y': 2 },
                        { 'x': 'game 7', 'y': 4 },
                        { 'x': 'game 8', 'y': 0 },
                        { 'x': 'game 9', 'y': 0 },
                        { 'x': 'game 10', 'y': 0 },
                        { 'x': 'game 11', 'y': 0 },
                        { 'x': 'game 12', 'y': 0 },
                        { 'x': 'game 13', 'y': 2 },
                        { 'x': 'game 14', 'y': 0 },
                    ]
                },
                {
                    'id': 'steals',
                    'data': [
                        { 'x': 'game 1', 'y': 0 },
                        { 'x': 'game 2', 'y': 2 },
                        { 'x': 'game 3', 'y': 1 },
                        { 'x': 'game 4', 'y': 0 },
                        { 'x': 'game 5', 'y': 0 },
                        { 'x': 'game 6', 'y': 0 },
                        { 'x': 'game 7', 'y': 1 },
                        { 'x': 'game 8', 'y': 0 },
                        { 'x': 'game 9', 'y': 0 },
                        { 'x': 'game 10', 'y': 0 },
                        { 'x': 'game 11', 'y': 0 },
                        { 'x': 'game 12', 'y': 1 },
                        { 'x': 'game 13', 'y': 2 },
                        { 'x': 'game 14', 'y': 2 },
                    ]
                },
                {
                    'id': 'blocks',
                    'data': [
                        { 'x': 'game 1', 'y': 0 },
                        { 'x': 'game 2', 'y': 2 },
                        { 'x': 'game 3', 'y': 1 },
                        { 'x': 'game 4', 'y': 0 },
                        { 'x': 'game 5', 'y': 0 },
                        { 'x': 'game 6', 'y': 1 },
                        { 'x': 'game 7', 'y': 1 },
                        { 'x': 'game 8', 'y': 0 },
                        { 'x': 'game 9', 'y': 0 },
                        { 'x': 'game 10', 'y': 0 },
                        { 'x': 'game 11', 'y': 0 },
                        { 'x': 'game 12', 'y': 0 },
                        { 'x': 'game 13', 'y': 2 },
                        { 'x': 'game 14', 'y': 0 },
                    ]
                },
                {
                    'id': 'assists',
                    'data': [
                        { 'x': 'game 1', 'y': 3 },
                        { 'x': 'game 2', 'y': 2 },
                        { 'x': 'game 3', 'y': 2 },
                        { 'x': 'game 4', 'y': 4 },
                        { 'x': 'game 5', 'y': 2 },
                        { 'x': 'game 6', 'y': 3 },
                        { 'x': 'game 7', 'y': 1 },
                        { 'x': 'game 8', 'y': 0 },
                        { 'x': 'game 9', 'y': 0 },
                        { 'x': 'game 10', 'y': 2 },
                        { 'x': 'game 11', 'y': 1 },
                        { 'x': 'game 12', 'y': 0 },
                        { 'x': 'game 13', 'y': 2 },
                        { 'x': 'game 14', 'y': 4 },
                    ]
                },
                {
                    'id': 'rebounds',
                    'data': [
                        { 'x': 'game 1', 'y': 3 },
                        { 'x': 'game 2', 'y': 7 },
                        { 'x': 'game 3', 'y': 10 },
                        { 'x': 'game 4', 'y': 11 },
                        { 'x': 'game 5', 'y': 7 },
                        { 'x': 'game 6', 'y': 9 },
                        { 'x': 'game 7', 'y': 4 },
                        { 'x': 'game 8', 'y': 6 },
                        { 'x': 'game 9', 'y': 5 },
                        { 'x': 'game 10', 'y': 10 },
                        { 'x': 'game 11', 'y': 5 },
                        { 'x': 'game 12', 'y': 3 },
                        { 'x': 'game 13', 'y': 12 },
                        { 'x': 'game 14', 'y': 8 },
                    ]
                },
                {
                    'id': 'points',
                    'data': [
                        { 'x': 'game 1', 'y': 3 },
                        { 'x': 'game 2', 'y': 0 },
                        { 'x': 'game 3', 'y': 12 },
                        { 'x': 'game 4', 'y': 15 },
                        { 'x': 'game 5', 'y': 17 },
                        { 'x': 'game 6', 'y': 4 },
                        { 'x': 'game 7', 'y': 6 },
                        { 'x': 'game 8', 'y': 10 },
                        { 'x': 'game 9', 'y': 12 },
                        { 'x': 'game 10', 'y': 4 },
                        { 'x': 'game 11', 'y': 6 },
                        { 'x': 'game 12', 'y': 6 },
                        { 'x': 'game 13', 'y': 0 },
                        { 'x': 'game 14', 'y': 12 },
                    ]
                },
            ]

            nivo.line(
                data=data,
                margin={
                    'top': 50,
                    'right':30,
                    'bottom':50,
                    'left':60
                },
                xscale={'type': 'point'},
                yscale={
                    'type': 'linear',
                    'min': 'auto',
                    'max': 'auto',
                    # 'stacked': true,
                    'reverse': False,
                },
                yformat='',
                axistop=None,
                axisright=None,
                axisbottom={
                    'ticksize':5,
                    'tickpadding':5,
                    'tickrotation':-35,
                    'legend':'',
                    'legendoffset':52,
                    'legendposition':'middle',
                    'truncatetickat':0,
                },
                axisleft={
                    'ticksize': 5,
                    'tickpadding': 5,
                    'tickrotation': 0,
                    'legendoffset': -40,
                    'legendposition': 'middle',
                    'truncatetickat': 0,
                },
                colors={'scheme': 'paired'},
                pointsize=9,
                pointcolor={'from': 'color', 'modifiers': []},
                pointborderwidth=2,
                pointbordercolor={'theme': 'background', 'modifiers': []},
                enablepointlabel=True,
                pointlabel='y',
                pointlabelyoffset=-12,
                areaopacity=0.25,
                isinteractive=True,
                usemesh=True,
                debugmesh=True,
                enableslices='x',
                enabletouchcrosshair=True,
                legends=[
                    {
                        'anchor': 'top',
                        'direction': 'row',
                        'justify': False,
                        'translatex': 18,
                        'translatey': -37,
                        'itemsspacing': 0,
                        'itemdirection': 'left-to-right',
                        'itemwidth': 80,
                        'itemheight': 20,
                        'itemopacity': 0.75,
                        'symbolsize': 12,
                        'symbolshape': 'square',
                        'symbolbordercolor': 'rgba(0,0,0,.5)',
                        'effects': [
                            {
                                'on': 'hover',
                                'style': {
                                    'itembackground': '#dfdfdf',
                                    'itemopacity': 1,
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
                colors = [ '#ffaf31', '#ff4655', '#5d5ef4'],
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
                    # 'background': '#ececec',
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

        # Update figure with new parameters
        # plt.xlim(-300,300)
        # plt.ylim(-50,450)
        plt.xlim(-250,350)
        plt.ylim(-50,450)
        # plt.xlim(-250,250)
        # plt.ylim(-50,430)

        img_base64 = self.plot_to_base64(plt)
        # st.pyplot(plt) # Plot shot chart

        with elements("plotly_box"):
            mui.Box(
                html.Img(src=f'data:image/png;base64,{img_base64}'),
                sx={
                    "width": "100%",
                    "height": "100%",
                    "backgroundColor": "#efefef",
                    "margin": "0",
                    # "opacity": ".3"
                }
            )

    def plot_to_base64(self, fig):
        buf = BytesIO()
        fig.savefig(buf, format="png", bbox_inches='tight')
        buf.seek(0)
        return base64.b64encode(buf.read()).decode('utf-8')
