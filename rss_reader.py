import os
import requests
import regex
from settings import twitch_video_regex


load_rss = open("feed.rss" , "r")
rss_content = load_rss.read()
print(twitch_video_regex)


print(regex.search(twitch_video_regex, rss_content))
# print(regex.findall(pattern, string)(twitch_video_regex, rss_content))



# urls_only = regex.match(twitch_video_regex, load_rss.read())
# print(urls_only)


# print(load_rss.read().find(twitch_video_regex))