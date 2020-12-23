import dash
import dash_express as dx
import numpy as np
import plotly.express as px

app = dash.Dash(__name__)
# template = dx.templates.DbcSidebar(title="Dash Express App")
template = dx.templates.DdkSidebar(title="Dash Express App")
# template = dx.templates.DccCard(title="Dash Express App")
# template = dx.templates.FlatDiv()


@dx.parameterize(
    app,
    inputs=dict(
        figure_title="Initial Title",
        phase=(1, 10),
        amplitude=(1, 10),
    ),
    state=dict(fun=["sin", "cos", "exp"]),
    template=template,
    labels={
        "fun": "Function",
        "figure_title": "Figure Title",
        "phase": "Phase: {}",
        "amplitude": "Amplitude: {}"
    },
    optional=["fun", "phase"],
    manual=True,
)
def callback_components(fun, figure_title, phase, amplitude):
    print("fun", fun, "figure_title", figure_title, "phase", phase, "amplitude", amplitude)

    xs = np.linspace(-10, 10, 100)
    if fun is None:
        np_fn = lambda a: a
    else:
        np_fn = getattr(np, fun)

    if phase is None:
        phase = 0

    # Let parameterize infer output component
    x = xs
    y = np_fn(xs + phase) * amplitude
    return template.Graph(
        figure=px.line(x=x, y=y).update_layout(title_text=figure_title)
    )

print(template.output_containers)

app.layout = callback_components.layout

if __name__ == "__main__":
    app.run_server(debug=True, port=9033)
