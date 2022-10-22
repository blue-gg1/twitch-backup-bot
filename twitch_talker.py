import os
import requests
import regex
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