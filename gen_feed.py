from feedgen.feed import FeedGenerator

def get_description():
    with open("ep01_description.txt") as f:
        return '\n'.join(f.readlines())

def main():
    fg = FeedGenerator()
    fg.load_extension('podcast')

    fg.id('https://www.flawcode.com/ep01_deep_learning_with_vijay.mp3')
    fg.title('FlawCode')
    fg.author( {'name':'FlawCode','email':'0xflawcode@gmail.com'} )
    fg.link( href='https://www.flawcode.com', rel='alternate' )
    fg.logo('https://pbs.twimg.com/profile_images/774831574177067009/tuxOiOZj.jpg')
    fg.subtitle(' The other side story ')
    fg.link( href='https://www.flawcode.com/atom.xml', rel='self' )
    fg.language('en')

    fg.podcast.itunes_category('Technology', 'Podcasting')
    fe = fg.add_entry()
    fe.id('https://www.flawcode.com/ep01_deep_learning_with_vijay.mp3')
    fe.title('Deep Learning with Vijay')
    fe.author( {'name':'FlawCode','email':'0xflawcode@gmail.com'} )
    fe.link( href='https://flawcode.com/index.html', rel='alternate' )
    fe.description(get_description())
    fe.enclosure('https://www.flawcode.com/ep01_deep_learning_with_vijay.mp3', 0, 'audio/mpeg')

    fg.rss_str(pretty=True)
    fg.rss_file('atom.rss')


if __name__ == "__main__":
    main()
