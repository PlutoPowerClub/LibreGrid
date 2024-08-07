from fasthtml.common import *
from fomantic import *

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

app, rt = fast_app(hdrs=fui_hdrs+hdrs)

@rt('/')
def get():
    return HeroSegment(
        "LibreGrid",
        "Free and Open Source Community Energy Management System",
    )
serve()
