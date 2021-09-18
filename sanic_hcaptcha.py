try:
  import aiohttp
  from jinja2 import Template
  import json
except ImportError:
  raise ImportError("Missing dependencies")

class hcaptcha:
  def __init__(self, secret_key=None, site_key=None):
    self.secret_key=secret_key
    self.site_key=site_key

  @property
  def get_code(self):
    html="""
    <script src="https://hcaptcha.com/1/api.js" async defer></script>
    <div class="h-captcha" data-sitekey={{sitekey}}></div>"""
    template = Template(html)
    html2 = template.render(sitekey=self.site_key)
    return html2

  async def verify(self, request):
    rjson={
       "secret": self.secret_key,
       "response": request.form["h-captcha-response"]
    }
    async with aiohttp.ClientSession() as session:
      async with session.post("https://hcaptcha.com/siteverify", data=rjson) as response:
        data=json.loads(await response.text())
        print(data)
        if data["success"] == True:
          return True
        else:
          return False
