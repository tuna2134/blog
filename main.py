from sanic import Sanic
from sanic.response import html, file
from jinja2 import Environment, FileSystemLoader

app = Sanic("main")

env = Environment(loader=FileSystemLoader('./html/', encoding='utf8'), enable_async=True)

async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    content = await template.render_async(kwargs)
    return html(content)
  
@app.route("/<path:path>")
async def main(request):
    if path.endswith(".html"):
        return await template(path)
    else:
        return await file(path)
