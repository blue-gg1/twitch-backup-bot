import os
import requests
import regex
import subprocess
import sys
# from libs.settings import rss_feed_gen, rss_file_name_twitch, twitch_channel_list, rss_feed_gen_yt
from settings import rss_feed_gen, rss_file_name_twitch, twitch_channel_list, rss_feed_gen_yt

# define the function
def get_twitch_rss_feed(twitch_channel):
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
        write_rss_disk = open(rss_file_name_twitch, "a")
        write_rss_disk.write(rss_data_string)
        write_rss_disk.close()
        # take the full rss and only get the urls
        video_id_list = subprocess.call(["bash", "libs/rss_reader.sh"])
    except Exception as e:
        print(e)

# define the function
def get_yt_rss_feed(yt_channel):
    # build the url from the given data
    rss_url = rss_feed_gen_yt + yt_channel
    print(rss_url)
    try:
        # tell me what you are doing 
        print(rss_url)
        print(yt_channel)
    #     # get the rss feed
        rss_data = requests.get(rss_url)
        rss_data_string = str(rss_data.content)
        print(rss_data.status_code)
    #     # write the rss feed to disk
        write_rss_disk = open(rss_file_name, "a") # fix me
        write_rss_disk.write(rss_data_string)
        write_rss_disk.close()
    #     # take the full rss and only get the urls
    #     # video_id_list = subprocess.call(["bash", "libs/rss_reader.sh"])
    except Exception as e:
        print(e)

get_yt_rss_feed('UCGaVdbSav8xWuFWTadK6loA')
