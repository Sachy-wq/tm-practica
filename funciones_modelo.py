def modelo_logistico(P0=100, r=0.03, K=1000, t_max=50):
    import numpy as np
    import plotly.graph_objects as go

    t = np.linspace(0, t_max, 200)
    P = (K * P0 * np.exp(r * t)) / (K + P0 * (np.exp(r * t) - 1))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=P, mode='lines', name='Crecimiento Logístico'))
    fig.update_layout(
        xaxis_title="Tiempo (t)",
        yaxis_title="Población P(t)",
        template="plotly_white"
    )
    return fig
