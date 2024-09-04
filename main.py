from fasthtml.common import *
# from LibreGrid.fomantic import *
import argparse
import subprocess

parser = argparse.ArgumentParser(
    prog="Fast HTML + Tailwind template",
    description="FastHTML template using Tailwind CSS for styling",
)
parser.add_argument(
    "--tailwind",
    type=bool,
    default=False,
    help="Run the Tailwind CLI build or not",
)
args = parser.parse_args()

hdrs = [

    HighlightJS(
        langs=[
            "python",
        ]
    ),
    Meta(name="description", content="LibreGrid: Free and Open Source Community Energy Management System"),
    Meta(charset="UTF-8"),
      Meta(
        name="viewport",
        content="width=device-width, initial-scale=1.0, maximum-scale=1.0",
    ),
    Link(href='css/input.css', rel='stylesheet'),
    Script(src="https://unpkg.com/htmx.org@2.0.1/dist/htmx.js"),
    Script(src="https://cdn.tailwindcss.com"),
]

app, rt = fast_app(
    pico=False,
    hdrs=fui_hdrs+hdrs,
    default_hdrs=False)

@rt('/')
def get():
    return Div(
        "Hello!", cls="font-bold text-red text-5xl")

if args.tailwind:
    subprocess.run(
        ["npx", "tailwindcss", "-i", "css/input.css", "-o", "css/output.css"]
    )

serve()
