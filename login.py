from fasthtml.common import *
from fh_frankenui.components import *

hdrs = (Script(src="https://cdn.tailwindcss.com"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
        Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js"),
        Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css") )

app,rt = fast_app(hdrs=hdrs,default_hdrs=False)

@rt('/')
def get():
    return Card(
            UkInput('Email',    'email',   placeholder='m@example.com'),
            UkInput('Password', 'Password',placeholder='Password',     type='Password'),
            header=(UkH3('Create an account'),P(cls=TextT.muted_sm)('Enter your email below to create your account')),
            footer=UkButton(cls=(UkButtonT.primary,'w-full'))('Create Account'),
            body_cls='space-y-4 py-0')

serve()
