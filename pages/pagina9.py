import dash
from dash import html, dcc, callback, Output, Input, State
import requests
import plotly.graph_objects as go

dash.register_page(__name__, path="/pagina9", name="Economía Mundial")

# ----------- LAYOUT ----------------
layout = html.Div([

    # ================= PANEL IZQUIERDO ==================
    html.Div([
        html.H2("Dashboard Economía (PIB Mundial)", className="title"),

        html.Div([
            html.Label("Seleccione el país:"),
            dcc.Dropdown(
                id="dropdown-pais-econ",
                options=[
                    {"label": "Perú", "value": "PER"},
                    {"label": "México", "value": "MEX"},
                    {"label": "Argentina", "value": "ARG"},
                    {"label": "Chile", "value": "CHL"},
                    {"label": "Colombia", "value": "COL"},
                    {"label": "Brasil", "value": "BRA"},
                    {"label": "Estados Unidos", "value": "USA"},
                ],
                value="PER",
                style={"width": "100%"}
            )
        ], className="input-group"),

        html.Div([
            html.Label("Rango de años:"),
            dcc.Dropdown(
                id="dropdown-years",
                options=[
                    {"label": "2010 - 2023", "value": "2010:2023"},
                    {"label": "2000 - 2023", "value": "2000:2023"},
                    {"label": "1990 - 2023", "value": "1990:2023"},
                    {"label": "1980 - 2023", "value": "1980:2023"}
                ],
                value="2010:2023",
                style={"width": "100%"}
            )
        ], className="input-group"),

        html.Button("Actualizar Datos", id="btn-econ", className="btn-generar"),
        html.Div(id="info-econ")

    ], className="content left"),

    # ================= PANEL DERECHO ==================
    html.Div([
        html.H2("Indicadores Económicos", className="title"),

        html.Div([

            html.Div([
                html.H4("Último PIB registrado (USD)"),
                html.H3(id="gdp-ultimo", style={"color": "#0b3661"})
            ], style={
                "backgroundColor": "#e3f2fd",
                "padding": "10px",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "5px"
            }),

            html.Div([
                html.H4("Año del último dato"),
                html.H3(id="gdp-year", style={"color": "#0b3661"})
            ], style={
                "backgroundColor": "#e3f2fd",
                "padding": "10px",
                "borderRadius": "5px",
                "textAlign": "center",
                "margin": "5px"
            }),

        ], style={"display": "flex"}),

        dcc.Graph(id="grafica-econ", style={"height": "450px", "width": "100%"})

    ], className="content right")

], className="page-container")


# --------- API WORLD BANK ----------
def obtener_pib(country_code, rango):
    url = f"https://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json&per_page=500&date={rango}"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data
    except:
        return None


# -------- CALLBACK ------------
@callback(
    Output("gdp-ultimo", "children"),
    Output("gdp-year", "children"),
    Output("grafica-econ", "figure"),
    Output("info-econ", "children"),
    Input("btn-econ", "n_clicks"),
    State("dropdown-pais-econ", "value"),
    State("dropdown-years", "value"),
    prevent_initial_call=True
)
def actualizar_dashboard(n, pais, years):

    datos = obtener_pib(pais, years)

    if not datos or len(datos) < 2:
        fig = go.Figure()
        fig.add_annotation(text="Error al cargar datos", x=0.5, y=0.5, showarrow=False)
        return "N/A", "N/A", fig, "Error al obtener datos."

    registros = datos[1]

    años = [r["date"] for r in registros][::-1]
    valores = [r["value"] if r["value"] else 0 for r in registros][::-1]

    ultimo_valor = valores[-1]
    ultimo_año = años[-1]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=años,
        y=valores,
        mode="lines+markers",
        name="PIB (USD)",
        line={"width": 3}
    ))

    fig.update_layout(
        title="PIB Total (USD)",
        xaxis_title="Año",
        yaxis_title="Dólares"
    )

    return (
        f"${ultimo_valor:,.0f}" if ultimo_valor else "N/A",
        ultimo_año,
        fig,
        f"Datos actualizados para {pais}"
    )
