try:
  from jinja2 import Environment, FileSystemLoader, select_autoescape
  import asyncio
  from sanic.response import html
except ImportError:
  raise ImportError("Missing dependencies")

class template:
  async def render_template(self, file_name, **content):
    env = Environment(loader=FileSystemLoader('./templates/', encoding='utf8'))
    template = env.get_template(file_name)
    e=template.render(**content)
    return html(e)