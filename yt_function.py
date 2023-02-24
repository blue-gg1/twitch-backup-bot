import os
import requests
import regex
import subprocess
import sys
import time
from libs.settings import rss_feed_gen, date_now_string, yt_rss_file_name
from libs.secrets import bot_name, tele_chatID, tele_api_token
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
        write_rss_disk = open(rss_file_name, "w")
        write_rss_disk.write(rss_data_string)
        write_rss_disk.close()
        # take the full rss and only get the urls
        video_id_list = subprocess.call(["bash", "libs/rss_reader.sh"])
    except Exception as e:
        print(e)

# get_rss_feed() 


# define the function
def send_to_telegram(message):
    # build the URL with the secret API key
    apiURL = f'https://api.telegram.org/bot{tele_api_token}/sendMessage'
    try:
        # send the request 
        response = requests.post(apiURL, json={'chat_id': tele_chatID, 'text': message})
        # tell me what happened 
        print(response.status_code)
        print(response.text)
    except Exception as e:
        print(e)

# take_file = open('urls.rss' , 'r')
# print(take_file.readlines())
# for i in take_file.readlines():
#     print(i)
#     send_to_telegram('/VideoDownloadBot '+i)
#     time.sleep(1)

# with open('urls.rss') as url_list:
#     lines = url_list.readlines()
#     print(lines)
#     print(lines.type)
#     send_to_telegram(lines)
# bash is king
# subprocess.run(["bash", "/home/rod/Documents/code/twitch-backup-bot/rss_reader.sh"])
# load_rss = open(rss_file_name, "r")
# rss_content = load_rss.read()
# print(rss_content)
# NewsFeed = feedparser.parse(rss_content)
# entry = NewsFeed.entries[1]
# print(entry.keys())
# print(entry['link'])
# print(twitch_video_regex
# working function, but the list is fucked
# load_rss = open(rss_file_name, "r")
# rss_content = load_rss.read()
# print(twitch_video_regex)
# urls_only = regex.findall(twitch_video_regex, rss_content, flags=0)
# write_file = open("video_urls.txt","w")
# write_file.write(str(urls_only))
# write_file.close()

# print(regex.search(twitch_video_regex, rss_content))
# print(regex.findall(twitch_video_regex, rss_content))

# loop that does not work
# for i in urls_only:
#     print(i)
#     write_file = open("video_urls.txt","w")
#     write_file.write(str(i))
# write_file.close()

# regex that did not work
# rss_findings = regex.findall(twitch_video_regex, rss_content)
# uniq = list(dict.fromkeys(rss_findings))
# for i in uniq:
#     print(i)
# print(regex.findall(pattern, string)(twitch_video_regex, rss_content))
# urls_only = regex.match(twitch_video_regex, load_rss.read())
# print(urls_only)
# print(load_rss.read().find(twitch_video_regex))