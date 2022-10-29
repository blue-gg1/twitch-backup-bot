import os
import requests
import regex
import subprocess
from settings import twitch_video_regex, twitch_video_id_regex, rss_file_name

# subprocess.run(["bash", "/home/rod/Documents/code/twitch-backup-bot/rss_reader.sh"])


load_rss = open(rss_file_name, "r")
rss_content = load_rss.read()
print(twitch_video_regex)

print(regex.search(twitch_video_regex, rss_content))
print(regex.findall(twitch_video_regex, rss_content))

urls_only = regex.findall(twitch_video_regex, rss_content)
print(urls_only)


# rss_findings = regex.findall(twitch_video_regex, rss_content)
# uniq = list(dict.fromkeys(rss_findings))


# for i in uniq:
#     print(i)


# print(regex.findall(pattern, string)(twitch_video_regex, rss_content))
# urls_only = regex.match(twitch_video_regex, load_rss.read())
# print(urls_only)
# print(load_rss.read().find(twitch_video_regex))