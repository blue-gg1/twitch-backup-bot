import os
import requests
import regex
import subprocess
from settings import twitch_channel, rss_feed_gen, date_now_string, rss_file_name

print(twitch_channel)
print(rss_feed_gen)

rss_url = rss_feed_gen + twitch_channel

print(rss_url)

rss_data = requests.get(rss_url)

# print(rss_data.status_code)
# print(rss_data.content)

rss_file_name

rss_data_string = str(rss_data.content)
write_rss_disk = open(rss_file_name, "w")
write_rss_disk.write(rss_data_string)
write_rss_disk.close()

video_id_list = subprocess.call(["bash", "/home/rod/Documents/code/twitch-backup-bot/rss_reader.sh"])
print('\r\n')
print(type(video_id_list))
print(video_id_list)

# video_id_list_str = video_id_list.stdout.splitlines()
# print(video_id_list_str)

# for i in video_id_list_str:
#     print(i)
