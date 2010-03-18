"""
telstar | Personal link shortener with Bottle and Redis. Unless you are creating over 100,000 links for yourself, this beyond dead-simple and quick Redis increment function should do nicely.

telstar is directly inspired by davej's tinchy, Leah Culver's TinyTinyUrl, and also by Cake's song Daria (during which telstar was written)

author: Ted Nyman
license: MIT

"""

from bottle import route, run, request, redirect
import redis

r = redis.Redis()

#your site's domain. in the newer versions of Bottle, you can just use request.url instead.
BASEURL = "http://localhost:8080/"

@route('/')
def index():
    return """
<head>
<title>telstar</title>
<style type="text/css">
h1{color:orange; font-family: Helvetica, Arial;}
</style>
</head>

<h1>telstar link shortener</h1>
<form method="post">
<input type="text" name="url" />
<input type="submit" value="Let's get small!" />
</form>
"""
 
@route('/', method='POST')
def make_small_url():
    big_url = request.POST.get('url', '').strip()
    if big_url[:7] == "http://":
        small_id = r.incr("url:all")
        small_id = str(small_id)
        set_big_url = r.set(big_url, small_id)
	set_small_url = r.set(small_id, big_url)
        small_url = BASEURL + small_id
        return 'Your small url is: <a href="{0}">{0}</a>'.format(small_url)
    else:
        return 'Dude, that is not a legit URL. It needs to start with <strong>http:// </strong><a href="/">Get real.</a>'
  
@route('/:small_id')
def redirect_to_big_url(small_id):
    if r.get(small_id) == None:
        return "Yah, that's not a valid short ID."
    else:
        big_url =  r.get(small_id) 
        redirect(big_url)
    
run(host='localhost', port=8080)

