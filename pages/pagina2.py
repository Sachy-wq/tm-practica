import dash
from dash import html, dcc
import plotly.graph_objects as go
import numpy as np

##########################################################

P0 = 100  # Población inicial
r = 0.03  # Tasa de crecimiento
K = 1000  # Capacidad de carga (nuevo parámetro)
t = np.linspace(0, 300, 100)  # Más puntos para una curva suave

# Función de crecimiento logístico (con capacidad de carga)
p_logistic = (K * P0 * np.exp(r * t)) / (K + P0 * (np.exp(r * t) - 1))

# Función de crecimiento exponencial (para comparación)
p_exponential = P0 * np.exp(r * t)

# Crear trazas para ambas curvas
trace_logistic = go.Scatter(
    x=t,
    y=p_logistic,
    mode='lines',
    line=dict(
        color='blue',
        width=3
    ),
    name='Crecimiento Logístico',
    hovertemplate='t: %{x:.1f}<br>P(t): %{y:.1f}<extra></extra>'
)

trace_exponential = go.Scatter(
    x=t,
    y=p_exponential,
    mode='lines',
    line=dict(
        dash='dash',
        color='red',
        width=2
    ),
    name='Crecimiento Exponencial',
    hovertemplate='t: %{x:.1f}<br>P(t): %{y:.1f}<extra></extra>'
)

# Línea de capacidad de carga
trace_capacity = go.Scatter(
    x=t,
    y=[K] * len(t),
    mode='lines',
    line=dict(
        dash='dot',
        color='green',
        width=2
    ),
    name=f'Capacidad de Carga (K={K})',
    hovertemplate='Capacidad de Carga: %{y:.0f}<extra></extra>'
)

# Crear la figura
fig = go.Figure(data=[trace_exponential, trace_logistic, trace_capacity])

fig.update_layout(
    title=dict(
        text='<b>Crecimiento Poblacional: Exponencial vs Logístico</b>',
        font=dict(
            size=18,
            color='darkblue'
        ),
        x=0.5,
        y=0.93
    ),
    xaxis_title='Tiempo (t)',
    yaxis_title='Población P(t)',
    margin=dict(l=40, r=40, t=60, b=40),
    paper_bgcolor='lightgray',
    plot_bgcolor='white',
    font=dict(
        family='Arial',
        size=12,
        color='black'
    ),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01,
        bgcolor='rgba(255,255,255,0.8)'
    )
)

fig.update_xaxes(
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    zeroline=True, zerolinewidth=1, zerolinecolor='black',
    showline=True, linecolor='black', linewidth=1,
)

fig.update_yaxes(
    showgrid=True, gridwidth=1, gridcolor='lightgray',
    zeroline=True, zerolinewidth=1, zerolinecolor='black',
    showline=True, linecolor='black', linewidth=1,
)

##########################################################

dash.register_page(__name__, path='/pagina2', name='Página 2')

layout = html.Div(children=[
    # Contenedor izquierdo
    html.Div(children=[
        html.H2("Crecimiento de la población y capacidad de carga", className="title"),
        dcc.Markdown("""
        ## Modelo de Crecimiento Logístico
        
        En la naturaleza, el crecimiento poblacional no puede ser exponencial indefinidamente debido 
        a limitaciones de recursos, espacio y otros factores. El **modelo logístico** incorpora 
        el concepto de **capacidad de carga (K)**, que representa el tamaño máximo de población 
        que el ambiente puede sostener.
        
        La ecuación diferencial del modelo logístico es:
        
        $$\\frac{dP}{dt} = rP \\left(1 - \\frac{P}{K}\\right)$$
        
        Donde:
        - $P(t)$: Población en el tiempo $t$
        - $r$: Tasa de crecimiento intrínseca ($r = 0.03$)
        - $K$: Capacidad de carga ($K = 1000$)
        - $P_0$: Población inicial ($P_0 = 100$)
        
        La solución de esta ecuación es:
        
        $$P(t) = \\frac{K P_0 e^{rt}}{K + P_0(e^{rt} - 1)}$$
        """, mathjax=True),
        
        dcc.Markdown("""
        ## Comparación con Crecimiento Exponencial
        
        - **Crecimiento Exponencial** (línea roja): 
          $$P(t) = P_0 e^{rt}$$
          Crece indefinidamente sin límites.
        
        - **Crecimiento Logístico** (línea azul): 
          Se aproxima asintóticamente a la capacidad de carga $K$.
        
        - **Línea verde punteada**: Representa la capacidad de carga $K = 1000$.
        """, mathjax=True),
    ], className="content left"),

    # Contenido derecho
    html.Div(children=[
        html.H2("Comparación de Modelos Poblacionales", className="title"),
        dcc.Graph(
            figure=fig,
            style={'height': '500px', 'width': '100%'}
        ),
        
        html.Div(children=[
            html.H3("Parámetros del Modelo"),
            html.P(f"Población inicial (P₀): {P0}"),
            html.P(f"Tasa de crecimiento (r): {r}"),
            html.P(f"Capacidad de carga (K): {K}"),
        ], style={'margin-top': '20px', 'padding': '15px', 'background-color': '#f0f0f0', 'border-radius': '5px'})
    ], className="content right")

], className="page-container")