#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Sergio Burdisso (sergio.burdisso@gmail.com)

from solidwebpush import Pusher

pusher = Pusher()

#In the previous example we created
#a new subscription for Robert. And
#therefore this should notify him too.
#(subscription was permanently stored).
pusher.notifyall("Hello World")

#NOTE: remember you can send a dict
#object too, it will be converted to
#a JSON string, like for instance:
#pusher.notifyall({
#	"title": "Hi there!",
#	"body": "Hello World"
#})

#let's wait for the notification
#to be sent before we exit by
#pressing Enter
raw_input()