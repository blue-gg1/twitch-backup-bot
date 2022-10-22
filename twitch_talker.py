import os
import requests
import regex
import subprocess
from settings import twitch_channel, rss_feed_gen

print(twitch_channel)
print(rss_feed_gen)

rss_url = rss_feed_gen + twitch_channel

print(rss_url)

rss_data = requests.get(rss_url)

print(rss_data.status_code)
print(rss_data.content)

rss_data_string = str(rss_data.content)

write_rss_disk = open("feed.rss", "w")
write_rss_disk.write(rss_data_string)
write_rss_disk.close()

video_id_list = subprocess.run(["bash", "/home/rod/Documents/code/twitch-backup-bot/rss_reader.sh"])

print(type(video_id_list))
str(video_id_list)
print(type(video_id_list))

video_id_list.split(sep=None, maxsplit=-1)

for i in video_id_list:
    print(i)
