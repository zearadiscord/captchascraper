# captchascraper
captcha and cloudflare bypass
# Example
```py
import captchascraper

data = {"name": "captchascraper","message": "captchascraper","send_message": "投稿"}

apikey

# get
captchascraper.get("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey)

# post
captchascraper.post("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey,data=data)

# patch
captchascraper.get("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey,data=data)

#delete
captchascraper.delete("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey)
```
# 使い方
`$ pip install captchascraper`
```py
import captchascraper

print(captchascraper.get("https://google.com").status_code)
```
