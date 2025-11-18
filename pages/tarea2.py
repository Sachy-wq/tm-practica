import dash
from dash import html, dcc, Input, Output, State, callback
import plotly.graph_objects as go
from funciones_modelo import modelo_logistico  # ← importamos la función

# Registrar la página
dash.register_page(__name__, path='/pagina4', name='Página 4')

# Figura inicial vacía
fig = go.Figure()

layout = html.Div([
    html.Div([
        html.H2("Modelo logístico con funciones separadas", className="title"),

        html.Div([
            html.Label("Población inicial P(0):"),
            dcc.Input(id="input-p0", type="number", value=200, className="input-field")
        ], className="input-group"),

        html.Div([
            html.Label("Tasa de crecimiento (r):"),
            dcc.Input(id="input-r", type="number", value=0.04, className="input-field")
        ], className="input-group"),

        html.Div([
            html.Label("Capacidad de carga (K):"),
            dcc.Input(id="input-k", type="number", value=1500, className="input-field")
        ], className="input-group"),

        html.Div([
            html.Label("Tiempo máximo (t):"),
            dcc.Input(id="input-t", type="number", value=100, className="input-field")
        ], className="input-group"),

        html.Button("Generar gráfico", id="btn-generar4", className="btn-generar")
    ], className="content left"),

    html.Div([
        html.H2("Gráfica del modelo logístico", className="title"),
        dcc.Graph(
            id="grafica-modelo4",
            figure=fig,
            style={'height': '350px', 'width': '100%'}
        )
    ], className="content right")
], className="page-container")


@callback(
    Output("grafica-modelo4", "figure"),
    Input("btn-generar4", "n_clicks"),
    State("input-p0", "value"),
    State("input-r", "value"),
    State("input-k", "value"),
    State("input-t", "value"),
    prevent_initial_call=False
)
def actualizar_grafico(n_clicks, p0, r, k, t_max):
    # Llamamos a la función desde el otro script
    t, P = modelo_logistico(p0, r, k, t_max)

    # Crear trazos
    trace_p = go.Scatter(x=t, y=P, mode='lines+markers', name='P(t)', line=dict(color='blue'))
    trace_k = go.Scatter(x=[0, t_max], y=[k, k], mode='lines', name='K', line=dict(color='red', dash='dot'))

    fig = go.Figure(data=[trace_p, trace_k])
    fig.update_layout(
        title="Modelo Logístico (función externa)",
        xaxis_title="Tiempo (t)",
        yaxis_title="Población P(t)",
        plot_bgcolor='white'
    )
    return fig
