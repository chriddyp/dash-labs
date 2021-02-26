import dash
import dash_core_components as dcc
import dash_express as dx

app = dash.Dash(__name__, plugins=[dx.Plugin()])
tpl = dx.templates.DbcSidebar("App Title", sidebar_columns=6)

@app.callback(
    output=tpl.markdown(),
    inputs=tpl.textarea(
        "## Heading\n",
        opts=dict(style={"width": "100%", "height": 400})
    ),
    template=tpl
)
def markdown_preview(input_text):
    return input_text

app.layout = tpl.layout(app)

if __name__ == "__main__":
    app.run_server(debug=True)
