from fasthtml.common import *
from LibreGrid.fomantic import *

hdrs = [
    HighlightJS(
        langs=[
            "python",
        ]
    ),
    Meta(name="description", content="LibreGrid: Free and Open Source Community Energy Management System"),
    Link(href='/assets/styles.css', rel='stylesheet'),
    Script(src="https://unpkg.com/htmx.org@2.0.1/dist/htmx.js"),
]

app, rt = fast_app(hdrs=fui_hdrs+hdrs, default_hdrs=False)

@rt('/')
def get():
    return Div(
        HeroSegment(
            "LibreGrid",
            "Power to the people, literally.",
        ),
        VerticalStripeSegment(
            Grid(
                Div(
                    H2("Decentralize power, amplify impact."),
                    P("We are coding the future of energy management, together."),
                cls="row")
            ),
        ),
        cls="pusher")
serve()
