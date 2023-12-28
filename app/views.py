from jinja2_fragments.sanic import render
from sanic import Request, Sanic


def add_views(app: Sanic):
  @app.get("/")
  async def get_index(request: Request):
    return await render(
      "index.html", 
      context={}
    )
  
