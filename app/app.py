import sanic_ext
from sanic import Sanic

from app import views


def main(
    port=8080
):
  app = Sanic('app-name')
  
  app.extend(config=sanic_ext.Config(
    templating_path_to_templates='templates',
    templating_enable_async=False
  ))
  app.ext.environment.lstrip_blocks = True
  app.ext.environment.trim_blocks = True

  app.static('/favicon.ico', 'static/favicon.ico', name="favicon")
  app.static('/static', 'static', name="static")

  views.add_views(app)

  app.run(host="0.0.0.0", port=port, single_process=True, debug=True, motd=False)


