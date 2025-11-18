import dash
from dash import html, dcc

dash.register_page(__name__, path='/', name= 'Inicio')

layout = html.Div(children=[
    #Contenedor izquierdo
    html.Div(children=[
    html.H2("Presentación", className="title"),
    dcc.Markdown("""
        Mi nombre es Sachy Yajayra, estudiante de la carrera de Computación Científica en la Universidad Nacional 
        Mayor de San Marcos. Me apasiona el análisis de datos, la programación orientada a soluciones científicas 
        y el desarrollo de algoritmos eficientes para problemas complejos.
        Este dashboard ha sido desarrollado con el objetivo de presentar de manera clara y organizada los resultados de 
        mis análisis, facilitando la interpretación de datos y la toma de decisiones basadas en evidencia. A través 
        de este trabajo, busco demostrar rigor académico, capacidad de síntesis y compromiso con la excelencia en la
        investigación científica computacional.
    """, mathjax=True),
], className="content left"),

    # Contenido derecho
html.Div(children=[
    html.H2("Imagen", className="title"),
    html.Img(
        src="assets/images/images1.jpeg",  # Sin la barra inicial
        style={
            'height': '350px', 
            'width': '100%',
            'object-fit': 'contain',
            'border': '1px solid red'  # Para debug
        },
        alt="Descripción de la imagen"
    )
], className="content right")

], className="page-container")