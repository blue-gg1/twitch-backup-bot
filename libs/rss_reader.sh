# cat feed.rss | egrep -o "https://www.twitch.tv/videos/([0-9]{10})" | sort | uniq

# python regex is hell. bash is king
# grep -o -E 'https?:\/\/(www\.twitch.tv)\/videos\/([0-9]{10})' libs/feed.rss 2> /dev/null | uniq > libs/urls.rss
# grep -o -E 'https?:\/\/(www\.twitch.tv)\/videos\/([0-9]{9})' libs/feed.rss 2> /dev/null | uniq > libs/urls.rss
grep -o -E 'https?:\/\/(www\.twitch.tv)\/videos\/([0-9]{8,})' libs/feed_twitch.rss 2> /dev/null | sort | uniq > libs/urls.rss