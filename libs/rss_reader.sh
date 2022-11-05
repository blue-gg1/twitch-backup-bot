# cat feed.rss | egrep -o "https://www.twitch.tv/videos/([0-9]{10})" | sort | uniq

grep -o -E 'https?:\/\/(www\.twitch.tv)\/videos\/([0-9]{10})' libs/feed.rss 2> /dev/null | uniq > libs/urls.rss