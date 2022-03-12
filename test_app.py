import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
#from plotly.offline import plot

# external JavaScript files
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = ['https://github.com/plotly/dash-app-stylesheets/blob/1564e52057ea20b6c23a4047d3d9261fc793f3af/dash-analytics-report.css']


test_app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
test_app.title = 'Test_App'

colors = { 'background': '#111111','text':'#7FDBFF'}

df = pd.DataFrame({"Country":['US','Canada','Africa','UK'],"x":[1,2,3,4], "SF":[4,1,2,5], "Montreal":[2,4,5,6]})

fig = px.bar(df,x="x",y=["SF","Montreal"],barmode="group")
fig1 = px.scatter(df, x="x", y=["SF","Montreal"],
                 size='Montreal')
test = '2020-12-01'
max_rows=len(df)
ahsh=df.drop_duplicates(subset=['Country'],keep='first')
qqwe=df.drop_duplicates(subset=['Montreal'],keep='first')
ahsh1=ahsh['Country']
qqwe=qqwe['Montreal']
qqwe=qqwe.to_numpy()
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color = colors['text'])
fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color = colors['text'])


def generate_table(dataframe, max_rows=max_rows):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(0, max_rows)]
    ) 


test_app.layout = html.Div(style={'backgroundColor':colors['background']},children=[html.Div(children=[
    html.H2(children='Hello Dash',style={'textAlign':'left','color':colors['text']}),
    html.Div(children='''Dash: A Web application framework for python.''',style={'textAlign':'right','color':colors['text']}),
    html.Div(children=test,style={'textAlign':'right','color':colors['text'],'fontSize':18}),
    html.Div(children='Graph Overview',style={'textAlign':'Left','color':colors['text'],'padding':16}),
    html.Div(children = [
                        dcc.Graph(id = 'example-graph',figure=fig),
                        html.Div(children='This is a test',style={'backgroundColor':colors['text'],'textAlign':'center','color':'orange','fontSize':12,'padding':20}),
                        html.Div(children=test,style={'textAlign':'center','color':'red','fontSize':18}),
                        dcc.Graph(id = 'example-scatter',figure=fig1),
                        html.Div(children='This is a test',style={'textAlign':'center','color':colors['text'],'fontSize':12,'padding':20}),
                        html.Div(children=test,style={'textAlign':'center','color':colors['text'],'fontSize':18}),   
                        ],style = {'columnCount':2}),
    html.Div(children=[
            generate_table(df)
            ],style={'textAlign':'center','color':colors['text'],'fontSize':10}),
    html.Div(children=[
            html.Div(children='Country',style={'textAlign':'center','color':'red','fontSize':18}),
            dcc.Dropdown(id='country',options=[{'label':i,'value':i} for i in ahsh1],multi=True,style={'backgroundColor':colors['background'],'textAlign':'center','color':'red'}),
            html.Div(children='Montreal',style={'textAlign':'center','color':'red','fontSize':18}),
            dcc.Dropdown(id='montreal',options=[{'label':i,'value':i} for i in qqwe],multi=True,style={'backgroundColor':colors['background'],'textAlign':'center','color':'red','width':'50%'}),
            html.Div([generate_table(df)],style={'textAlign':'center','color':colors['text'],'fontSize':10}),dcc.Graph(id = 'example-scatter1',figure=fig1),dcc.Graph(id = 'example-scatter2',figure=fig1),dcc.Graph(id = 'example-scatter3',figure=fig1)
            ],style = {'columnCount':3})
])
])

if __name__ == '__main__':
    test_app.run_server(host='0.0.0.0',debug=True,port=8081)