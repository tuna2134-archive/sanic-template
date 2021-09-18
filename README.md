# sanic-templates

## How to use sanic-template

# 1
```bash
pip install sanic-template
```

# 3
create a templates folder

# 2
```py
from sanic import Sanic
from sanic_template import template

app = Sanic("api")
template=template()

@app.route("/test")
async def html(request):
  return await template.render_template("test.html", test="a")
  
app.run(host="0.0.0.0", port=8080)
```