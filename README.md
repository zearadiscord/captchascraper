# captchascraper
captcha and cloudflare bypass
# Example
```
import captchascraper

data = {"name": "captchascraper","message": "captchascraper","send_message": "投稿"}

# https://www.scraperapi.com/
bypass = bypass(apikey="APIKEYHERE")

# get
bypass.get("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/")

# post
bypass.post("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",data=data)

# patch
bypass.get("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",data=data)

#delete
bypass.delete("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/")
```
