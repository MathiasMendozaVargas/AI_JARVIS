###################
# IMPORT PACKAGES
###################
from random import randint


# Functions
def getQuote():
    quote = [
        '<p>Listen to your client, take into consideration all of their input, weigh the options, study the details, know the target audience, and then, if necessary, ignore all of it and design what you think will work best.  </p>\n\n- Von R. Glitschka',
        '<p>In design man becomes what he is.<br />\nAnimals have language and perception as well,<br />\nbut they do not design.  </p>\n\n- Otl Aicher',
        '<p>Life beats down and crushes the soul, and art reminds you that you have one.  </p>\n\n- Stella Adler',
        '<p>Graphic design is the design of highly disposable items... It all winds up in the garbage.  </p>\n\n- Karrie Jacobs',
        '<p>Designers tend to overvalue differentiation and originality. We are taught this in design school. The best solutions are created ex nihilo, break new ground, resemble nothing else in the world. Everyone wants to stand out, or else what is the point? But this is not true. Most people do not want to stand out. They want to fit in. More precisely, they want to fit in with the people they like, or want to be like.</p>\n\n- Michael Bierut',
        '<p>The ability to change on a dime is one thing small teams have by default that big teams can never have. This is where the big guys envy the little guys. What might take a big team in a huge organization weeks to change may only take a day in a small, lean organization. That advantage is priceless.</p>\n\n- Andrew Hunt',
        'The greatest glory in living lies not in never falling, but in rising every time we fall. \n\n- Nelson Mandela',
        "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. \n\n- Steve Jobs",
        "It is during our darkest moments that we must focus to see the light. \n\n- Aristotle",
        "It’s fine to celebrate success but it is more important to heed the lessons of failure. \n\n- Bill Gates",
        "The biggest risk is not taking any risk… In a world that’s changing really quickly, the only strategy that is guaranteed to fail, is not taking risks. \n\n- Mark Zuckerberg",
        "If you're competitor-focused, you have to wait until there is a competitor doing something. Being customer-focused allows you to be more pioneering. \n\n- Jeff Bezos",
        "The problem is that at a lot of big companies, process becomes a substitute for thinking. You're encouraged to behave like a little gear in a complex machine. Frankly, it allows you to keep people who aren't that smart, who aren't that creative. \n\n- Elon Musk",
        "Stay hungry, stay foolish! \n\n- Steve Jobs",
        "Any sufficiently advanced technology is equivalent to magic. \n\n- Sir Arthur C.Clarke",
        "Just because something doesn’t do what you planned it to do doesn’t mean it’s useless. \n\n- Thomas Edison",
        "When something is important enough, you do it even if the odds are not in your favor. \n\n- Elon Musk",
        '<p>There is nothing glamorous in what I do. I am a working man. Perhaps I am luckier than most in that I receive considerable satisfaction from doing useful work which I, and sometimes others, think is good.</p>\n\n- Saul Bass',
        "If you get up in the morning and think the future is going to be better, it is a bright day. Otherwise, it's not. \n\n- Elon Musk",
        "I could either watch it happen or be a part of it. \n\n- Elon Musk",
        '<p>If you find an element of your interface requires instructions, then you need to redesign it.  </p>\n\n- Dan Rubin',
        "If you go back a few hundred years, what we take for granted today would seem like magic-being able to talk to people over long distances, to transmit images, flying, accessing vast amounts of data like an oracle. These are all things that would have been considered magic a few hundred years ago. \n\n- Elon Musk",
        '<p>Do not stare at a blank page for too long, be bold, and make the first incisive stroke. The rest will come naturally.   </p>\n\n- James Kingman',
        "Failure is an option here. If things are not failing, you are not innovating enough. \n\n- Elon Musk",
        "Get busy living or get busy dying. \n\n- Stephen King",
        "Those who dare to fail miserably can achieve greatly. \n\n- John F. Kennedy",
        "If you want to live a happy life, tie it to a goal, not to people or things. \n\n- Albert Einstein",
        "The successful warrior is the average man, with laser-like focus. \n\n- Bruce Lee",
        "The whole secret of a successful life is to find out what is one’s destiny to do, and then do it. \n\n- Henry Ford",
        "We are what we repeatedly do; excellence, then, is not an act but a habit. \n\n- Aristotle",
        "The big lesson in life, baby, is never be scared of anyone or anything. \n\n- Frank Sinatra",
        "The person who reads too much and uses his brain too little will fall into lazy habits of thinking. \n\n- Albert Einstein",
        "Every child is an artist, the problem is staying an artist when you grow up. \n\n- Pablo Picasso",
        "You must be the change you wish to see in the world. \n\n- Gandhi",
        "Creativity is just connecting things. When you ask creative people how they did something, they feel a little guilty because they didn’t really do it, the just saw something. It seemed obvious to them after a while. \n\n- Steve Jobs"]
    x = randint(0, 35)
    quote = quote[x]

    quote = quote.replace("<p>", "")
    quote = quote.replace("</p>", "")
    if "<br " in quote:
        quote = quote.replace("<br ", "")
        quote = quote.replace("/>", "")

    return quote

