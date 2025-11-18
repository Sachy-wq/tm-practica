import dash
from dash import html, dcc, callback, Output, Input, State
import numpy as np
import plotly.graph_objects as go
from scipy.integrate import odeint  # ← NECESARIO

#PAGINA 6

dash.register_page(__name__, path='/pagina6', name='Modelo SIR')

layout = html.Div([
    html.Div([ 
        html.H2("Modelo SIR - Epidemiología", className="title"),

        html.Div([ 
            html.Label("Población Total (N): "),
            dcc.Input(id="input-N", type="number", value=1000, className="input-field")
        ], className="input-group"),

        html.Div([ 
            html.Label("Tasa de transmisión (β): "),
            dcc.Input(id="input-beta", type="number", value=0.3, step=0.01, className="input-field")
        ], className="input-group"),
        
        html.Div([ 
            html.Label("Tasa de recuperación (γ): "),
            dcc.Input(id="input-ganma", type="number", value=0.1, step=0.01, className="input-field")
        ], className="input-group"),

        html.Div([ 
            html.Label("Infectados iniciales: "),
            dcc.Input(id="input-I0", type="number", value=1, className="input-field")
        ], className="input-group"),

        html.Div([ 
            html.Label("Tiempo de simulación:"),
            dcc.Input(id="input-tiempo", type="number", value=100, className="input-field")
        ], className="input-group"),

        html.Button("Simular Epidemia", id="btn-simular", className="btn-generar"),

    ], className="content left"),

    html.Div([
        html.H2("Evolución de la Epidemia", className="title"),
        dcc.Graph(id="grafica-sir", style={"height":"450", "width":"100%"}),
        html.Div(id='info-campo')
    ], className="content right")
], className="page-container")


## MODELO SIR ###
def modelo_sir(y, tiempo, beta, ganma, N):
    S, I, R = y

    dS_dt = -beta * S * I / N
    dI_dt = beta * S * I / N - ganma * I
    dR_dt = ganma * I

    return [dS_dt, dI_dt, dR_dt]


@callback(
    Output("grafica-sir", "figure"),
    Input("btn-simular", "n_clicks"),
    State("input-N", "value"),
    State("input-beta", "value"),
    State("input-ganma", "value"),
    State("input-I0", "value"),
    State("input-tiempo", "value")
)
def simular_sir(n_clicks, N, beta, ganma, I0, tiempo_max):

    S0 = N - I0
    R0_inicial = 0
    y0 = [S0, I0, R0_inicial]
    
    t = np.linspace(0, tiempo_max, 200)

    try:
        solucion = odeint(modelo_sir, y0, t, args=(beta, ganma, N))
        S, I, R = solucion.T
    except:
        S = np.full_like(t, S0)
        I = np.full_like(t, I0)
        R = np.full_like(t, R0_inicial) 

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=t, y=S, 
        mode='lines', 
        name='Susceptibles (S)', 
        line=dict(color='blue', width=2),
    ))

    fig.add_trace(go.Scatter(
        x=t, y=I,   
        mode='lines',
        name='Infectados (I)',
        line=dict(color='red', width=2),
    ))

    fig.add_trace(go.Scatter(
        x=t, y=R,   
        mode='lines',
        name='Recuperados (R)',
        line=dict(color='green', width=2),
    ))  

    fig.update_layout(
        title=dict(
            text = "<b>Evolución del Modelo SIR</b>",
            x=0.5, font=dict(size=15, color="darkblue")
        ),
        xaxis_title="tiempo(días)",
        yaxis_title="Número de personas",
        paper_bgcolor="lightcyan",
        plot_bgcolor="white",
        font=dict(family="Outfit", size=12),
        legend=dict(
            orientation="h", 
            yanchor="bottom",
            y=1.02, 
            xanchor="right",
            x=0.5
        ),
        margin=dict(l=40, r=40, t=60, b=40)   # ← AQUÍ FALTABA LA COMA
    )

    return fig
