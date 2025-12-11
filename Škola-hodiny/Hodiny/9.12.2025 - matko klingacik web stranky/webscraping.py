import requests as rq

page = rq.get("https://www.sme.sk/")

print(page.text)
