import os
import requests
import regex
import subprocess
import sys
from libs.settings import rss_feed_gen, date_now_string, rss_file_name, twitch_channel_list
# from settings import twitch_channel, rss_feed_gen, date_now_string, rss_file_name

# define the function
def get_rss_feed(twitch_channel):
    # build the url from the given data
    rss_url = rss_feed_gen + twitch_channel
    try:
        # tell me what you are doing 
        print(rss_url)
        print(twitch_channel)
        # get the rss feed
        rss_data = requests.get(rss_url)
        rss_data_string = str(rss_data.content)
        print(rss_data.status_code)
        # write the rss feed to disk
        write_rss_disk = open(rss_file_name, "a")
        write_rss_disk.write(rss_data_string)
        write_rss_disk.close()
        # take the full rss and only get the urls
        video_id_list = subprocess.call(["bash", "libs/rss_reader.sh"])
    except Exception as e:
        print(e)

# get_rss_feed() 