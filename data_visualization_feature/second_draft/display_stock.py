from dash import html, dcc 
import dash                  
import plotly.express as px 
import datetime as dt                
from dash.dependencies import Input, Output, State 
import requests 
import pandas as pd            
import finnhub

finnhub_client = finnhub.Client(api_key = "")

print(finnhub_client.marke)
