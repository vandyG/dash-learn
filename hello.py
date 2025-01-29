from dash import Dash, html, dash_table, dcc
import pandas as pd
from pprint import pformat
import plotly.express as px


def main() -> Dash:
    # Incorporate data
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
    # print(df.head())
    # print(pformat(df.to_dict(orient="records")))

    app = Dash()
    app.layout = [
        html.Div(children="Hello World!"),
        dash_table.DataTable(data=df.to_dict("records"), page_size=10),
        dcc.Graph(figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg")),
    ]

    return app


if __name__ == "__main__":
    main().run(debug=True)
