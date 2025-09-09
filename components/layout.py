from dash import html
import dash_bootstrap_components as dbc

def criar_layout():
    return dbc.Container([
        html.H1("💧 Sistema de Análise de Perdas", className="text-center my-4"),
        dbc.Card([
            dbc.CardBody([
                html.H3("🚀 Sistema em Funcionamento!"),
                html.P("Seu dashboard foi carregado com sucesso!"),
                html.P("Configure os componentes específicos do seu sistema.")
            ])
        ]),
        dcc.Interval(id='interval-component', interval=60000, n_intervals=0)
    ], fluid=True)
