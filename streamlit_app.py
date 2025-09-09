import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from components.layout import criar_layout
from components import callbacks

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)

app.title = "💧 Sistema de Análise de Perdas"
server = app.server

# Layout completo
app.layout = criar_layout()

# Registrar callbacks
callbacks.registrar_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)
