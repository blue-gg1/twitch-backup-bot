import os
import requests
import regex
import subprocess
import feedparser
from settings import twitch_video_regex, twitch_video_id_regex, rss_file_name
from secrets import bot_name, tele_api
def send_to_telegram(message):

    apiToken = '5082654068:AAF7quCLZ4xuTq2FBdo3POssdJsM_FRHwTs'
    chatID = '515382482'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Hello from Python!")


with open('urls.rss') as url_list:
    lines = url_list.readlines()
    print(lines)
    print(bot_name+tele_api)




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