import os
import requests
import regex
import subprocess
from settings import twitch_channel, rss_feed_gen, date_now_string, rss_file_name

def get_rss_feed():
    rss_url = rss_feed_gen + twitch_channel
    try:
        rss_data = requests.get(rss_url)
        rss_data_string = str(rss_data.content)
        write_rss_disk = open(rss_file_name, "w")
        write_rss_disk.write(rss_data_string)
        write_rss_disk.close()
        video_id_list = subprocess.call(["bash", "rss_reader.sh"])
    except Exception as e:
        print(e)

# get_rss_feed()    


# video_id_list_str = video_id_list.stdout.splitlines()
# print(video_id_list_str)

# for i in video_id_list_str:
#     print(i)
