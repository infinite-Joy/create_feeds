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
    fg.link( href='https://www.flawcode.com/atom.rss', rel='self' )
    fg.language('en')

    fg.podcast.itunes_category('Technology', 'Podcasting')
    fe = fg.add_entry()
    fe.id('https://www.flawcode.com/episode/show/1/ep01_deep_learning_with_vijay.mp3')
    fe.title('Deep Learning with Vijay')
    fe.author( {'name':'FlawCode','email':'0xflawcode@gmail.com'} )
    fe.link( href='https://www.flawcode.com/episode/show/1/index.html', rel='alternate' )
    fe.description(get_description("ep01_description.txt"))
    fe.enclosure('https://www.flawcode.com/episode/show/1/ep01_deep_learning_with_vijay.mp3', 0, 'audio/mpeg')

    fe = fg.add_entry()
    fe.id('https://www.flawcode.com/episode/show/2/ep02_venture_capitalism_with_abishek_and_debanjoli.mp3')
    fe.title('Venture Capitalism With Abishek and Debanjoli')
    fe.author( {'name':'FlawCode','email':'0xflawcode@gmail.com'} )
    fe.description(get_description("ep02_description.txt"))
    fe.link( href='https://flawcode.com/index.html', rel='alternate' )
    fe.enclosure('https://www.flawcode.com/episode/show/2/ep02_venture_capitalism_with_abishek_and_debanjoli.mp3', 0, 'audio/mpeg')




    fg.rss_str(pretty=True)
    fg.rss_file('atom_episode2_003.rss')


if __name__ == "__main__":
    main()
