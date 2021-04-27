import requests as http

url = 'http://localhost:3000/hooks/6Jzwu8exYbmaYnFho/RwYRSLQacMrXEB59NcfMtG5PkpZ9pfxAEqx4Zx3Br49rga4Z'
r = http.post(url, headers={'Content-Type': 'application/json'}, json={
    "text": "Example message",
    "attachments": [
        {
            "title": "Rocket.Chat",
            "title_link": "https://rocket.chat",
            "text": "Rocket.Chat, the best open source chat",
            "image_url": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F7cede7c66bd4ecfc352a368933ede52a0e099981.jpg&refer=http%3A%2F%2Fi2.hdslb.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1622023692&t=0d140072cb53c0d5e2d21e180d0237bf",
            "color": "#764FA5"}
    ]})

print(r.json())
