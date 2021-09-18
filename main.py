from sanic import Sanic
from sanic_template import template
from sanic.response import *
from sanic_hcaptcha import hcaptcha
import os

app = Sanic("api")
template=template()
hcaptcha=hcaptcha(secret_key=os.getenv("secret_key"),site_key=os.getenv("site_key"))
   
@app.route("/")
async def main(request):
  return text("君は何もないところに来てしまった")

@app.route("/test")
async def html(request):
  return await template.render_template("test.html", test="a", hcaptcha=hcaptcha.get_code)

@app.post("/submit")
async def submit(request):
  if await hcaptcha.verify(request):
    return text("111")
  else:
    return text("失敗")
  
app.run(host="0.0.0.0", port=8080)