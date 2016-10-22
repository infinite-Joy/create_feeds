# create_feeds
To generate feeds for playerfm and possibly other platforms

# to get the item

cat rssfile | tr "\n" "|" | grep -o '<item>.*</item>' | sed 's/\(<item>\|<\/item>\)//g' | sed 's/|/\n/g'


add item and change the last build date
