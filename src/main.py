from browser import document, ajax, html
import json
      
# ajax送信
req = ajax.Ajax()
req.open("GET", "https://randomuser.me/api/", False)
req.send()
data = json.loads(req.text)["results"][0]
document['main'] <= html.H1(f'{data["name"]["title"]}.{data["name"]["first"]} {data["name"]["last"]}')
document['main'] <= html.IMG(src=data["picture"]["medium"], alt="image")
