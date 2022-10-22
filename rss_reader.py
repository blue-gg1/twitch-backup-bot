import os
import requests
import regex
from settings import twitch_video_regex


load_rss = open("feed.rss" , "r")
# print(load_rss.read())

print(twitch_video_regex)

urls_only = regex.match(twitch_video_regex, load_rss.read())
print(urls_only)


# print(load_rss.read().find(twitch_video_regex))