from sanic.response import html
from jinja2 import Environment, FileSystemLoader, select_autoescape

class Template:
    def __init__(self, loader: FileSystemLoader) -> None:
        self.env = Environment(
            loader=loader
        )

    def render(self, filename: str):
        template = self.env.get_template(filename)
        return html(template.render())