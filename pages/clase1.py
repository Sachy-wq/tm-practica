import dash
from dash import html, dcc

dash.register_page(__name__, path='/pagina1', name= 'Página 1')

layout = html.Div([
    html.Div("Bienvenido a la página 1"),
])