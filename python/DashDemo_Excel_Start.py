# Dash demo 
# Tue Hellstern

# Import
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Data import
Excel_file = 'data/northwind_data.xlsx'
Top5Products = pd.read_excel(Excel_file, "Top5Products")
CategorySale = pd.read_excel(Excel_file, "CategorySale")

# Create charts
def top5_products():
    fig = px.pie(Top5Products, values='Total', names='ProductName', title='Top 5 Products')
    return fig  

def categorysale():
    fig = px.bar(CategorySale, x='CategoryName', y='Total', title='Category Sales')
    return fig

# Initialize the App
app = dash.Dash()

# Flatly theme
app = dash.Dash(external_stylesheets = [dbc.themes.FLATLY],)

body_app = dbc.Container([
    
    dbc.Row([
        # 1 column
        dbc.Col(
            dcc.Graph(id = 'top5products', figure = top5_products()),
            style = {'height':'400px'}),
         
        # 2 column
        dbc.Col(
            dcc.Graph(id = 'top5customers', figure = categorysale()),
            style = {'height':'400px'}),         
    ])

],fluid = True)  # Using Fluid   

# Dash
app.layout = html.Div(id = 'parent', children = [body_app])

if __name__ == "__main__":
    app.run_server()