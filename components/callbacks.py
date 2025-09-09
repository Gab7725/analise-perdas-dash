from dash import Input, Output

def registrar_callbacks(app):
    @app.callback(
        Output('live-update', 'children'),
        Input('interval-component', 'n_intervals')
    )
    def update_metrics(n):
        return f"Sistema atualizado {n} vezes"
