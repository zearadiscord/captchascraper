import requests



def get(url,apikey,headers=None,**kwargs):
      return requests.get(f"http://api.scraperapi.com?api_key={apikey}&url=" + url + "&keep_headers=True",**kwargs)
      
def post(url,apikey,data,**kwargs):
      return requests.post(f"http://api.scraperapi.com?api_key={apikey}&url=" + url + "&keep_headers=True",data=data,**kwargs)
      
def put(url,apikey,**kwargs):
      return requests.put(f"http://api.scraperapi.com?api_key={apikey}&url=" + url + "&keep_headers=True",**kwargs)
def patch(url,apikey,data,**kwargse):
      return requests.patch(f"http://api.scraperapi.com?api_key={apikey}&url=" + url + "&keep_headers=True",data=data,**kwargs)

def delete(url,apikey,**kwargs):
      return requests.delete(f"http://api.scraperapi.com?api_key={apikey}&url=" + url + "&keep_headers=True",**kwargs)
