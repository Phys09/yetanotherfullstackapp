from dash import html, dcc 
import dash 
import plotly.express as px 
import datetime as dt                 
from dash.dependencies import Input, Output, State 
import requests  
import pandas as pd             

stock = px.data.stocks('TSLA')
stock.reset_index(inplace=True)
print(stock.head())


app = dash.Dash("Stock")

app.layout = html.Div(children = [html.H1("Stock Visualization", style = {'textAlign': 'center', 'font-size': 26}), 
                                  html.Div(
                                      html.Div([
                                          html.H2('Select Stock: ', style = {'margin-right': '2em'}), 
                                          dcc.RadioItems([
                                              {'label': "Google", 'value': 'GOOG'}, 
                                              {'label': 'Apple', 'value': 'AAPL'}, 
                                              {"label": "Amazon", 'value': 'AMZN'}, 
                                              {'label': 'Facebook', 'value': 'FB'}, 
                                              {'label': 'Netflix', 'value': 'NFLX'}, 
                                              {'label': 'Microsoft', 'value': 'MSFT'}], value = 'GOOG', id = 'stock_name', inline=True),
                                          html.Div([
                                              html.Div([], id = 'plot1')
                                          ])
                                        ])
                                  )])

@app.callback(Output(component_id='plot1', component_property="children"),
              Input(component_id="stock_name", component_property="value"))

def stock_display(stock_name):
    stock = px.data.stocks(stock_name)
    stock.reset_index(inplace=True)
    figure = px.line(stock, x = 'date', y = stock_name)
    
    return dcc.Graph(figure = figure) 


if __name__ == '__main__':
    app.run_server(debug=True)