from feedgen.feed import FeedGenerator

def get_description(fn):
    """
    pass the file name as a string
    """
    with open(fn) as f:
        return '\n'.join(f.readlines())


def main():
    fg = FeedGenerator()
    fg.load_extension('podcast')

    fg.id('https://www.flawcode.com/')
    fg.title('FlawCode')
    fg.author( {'name':'FlawCode','email':'0xflawcode@gmail.com'} )
    fg.link( href='https://www.flawcode.com', rel='alternate' )
    fg.logo('https://pbs.twimg.com/profile_images/774831574177067009/tuxOiOZj.jpg')
    fg.subtitle(' The other side story ')
    fg.link( href='https://www.flawcode.com', rel='self' )
    fg.language('en')

    fg.podcast.itunes_category('Technology', 'Podcasting')

    fe = fg.add_entry()
    fe.id('https://flawcode.com/episode/show/4/ep04_APL_with_Morten.mp3')
    fe.title('APL with Morten')
    fe.author( {'name':'FlawCode','email':'0xflawcode@gmail.com'} )
    fe.description(get_description("ep04_description.txt"))
    fe.link( href='https://flawcode.com/episode/show/4/', rel='alternate' )
    fe.enclosure('https://flawcode.com/episode/show/4/ep04_APL_with_Morten.mp3', 0, 'audio/mpeg')




    fg.rss_str(pretty=True)
    fg.rss_file('atom_episode4.rss')


if __name__ == "__main__":
    main()

