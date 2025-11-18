import dash
from dash import html, dcc, callback, Output, Input, State
import numpy as np
import plotly.graph_objects as go

# === REGISTRO DE PÁGINA ===
dash.register_page(__name__, path='/pagina8', name='covid-19')

layout = html.Div([ 
    html.Div([
        html.H2("Dashboard Covid 19", className="title"),

        html.Div([
            html.Label("Seleccione el país: "),
            dcc.Dropdown(
                id="dropdown-pais",
                options=[
                    {"label": "Perú", "value": "Peru"},
                    {"label": "México", "value": "Mexico"},
                    {"label": "Estados Unidos", "value": "USA"},
                    {"label": "Canada", "value": "Canada"},
                ],
                value="Peru",
                className="dropdown-field",
                style={"width": "100%"}
            )
        ], className="input-group"),

        html.Div([ 
            html.Label("Días historicos"),
            dcc.Dropdown( 
                id="dropdown-dias-covid",
                options=[
                    {"label": "30 días", "value": 30},
                    {"label": "60 días", "value": 60},
                    {"label": "90 días", "value": 90},
                    {"label": "120 días", "value": 120},
                    {"label": "Todo el histórico", "value": "all"},
                ],
                value=30,
                className="input-field",
                style={"width": "100%"}
            )
        ], className="input-group"),

        html.Button("Actualizar Datos", id="btn-actualizar", className="btn-generar"),

        html.Div(
            id="info-actualizado-covid",
        )
    ], className="content left"),

    html.Div([ 
        html.H2("Estadísticas en tiempo real", className="title"),

        html.Div([
            html.Div([
            html.H4("Total de Casos", style={'color':'#1976d2'}),
            html.H3(id="total-casos", style={'color':'#0b3661'})
        ], style={
            'backgroundColor': '#e3f2fd',
            'padding': '10px',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '5px'
        }),

        html.Div([ 
            html.H4("Casos nuevos", style={'color':"#ffaa00"}),
            html.H3(id="total-casos", style={'color':"#ef9f0b"})
        ], style={
            'backgroundColor': '#e3f2fd',
            'padding': '10px',
            'borderRadius': '10px',
            'textAlign': 'center',
            'margin': '5px'
        }),

        html.Div([ 
            html.H4("Total de muertes", style={'color':"#1635ff"}),
            html.H3(id="total-muertes", style={'color':"#050aff"})
        ], style={
            'backgroundColor': '#e3f2fd',
            'padding': '10px',
            'borderRadius': '10px',
            'textAlign': 'center',
            'margin': '5px'
        }),

        html.Div([ 
            html.H4("Recuperados", style={'color':"#2dff0d"}),
            html.H3(id="total-recuperados", style={'color':"#fefe0a"})
        ], style={
            'backgroundColor': '#e3f2fd',
            'padding': '10px',
            'borderRadius': '10px',
            'textAlign': 'center',
            'margin': '5px'
        })
        ], style={'display': 'flex'})

    ])
])