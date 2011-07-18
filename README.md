telstar
========

Simple-as-possible, personal link shortener with Bottle and Redis. Uses Redis' INCR function for an interesting change from the usual BASE and random stuff. 

Requires: 
 
* [Redis](http://github.com/antirez/redis "Redis")
* [Bottle](http://github.com/defnull/bottle "Bottle")
* [redis-py](http://github.com/andymccurdy/redis-py "redis-py")

telstar is directly inspired by Dave Jeffery's tinchy, Leah Culver's tinytinyurl, and also by Cake's song Daria (which was playing in the couple of minutes when telstar was written).

to run
---------

With the deps installed and a running redis-server on localhost, `python telstar.py` will start the telstar web interface on `localhost`. Point your browser
to `http://localhost:8080/` and start shortening links.

author: Ted Nyman
license: MIT

