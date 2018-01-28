define m = Character("Mako", who_color="#eee66e")
define c = Character("Chacha", who_color="#de6a99")
define j = Character("Juice", who_color="#9cd847")
define s = Character("Soda", who_color="#e4af7a")
define w = Character("Whiskey", who_color="#6191e8")

define fade = Fade(0.5, 0.5, 0.5)

image mako neutral = "mako_neutral.png" # doesn't use commas, uses !
image chacha neutral = "chacha_neutral.png" # regular speech, use of ellipses
image juice neutral = "juice_neutral.png" # no punctuation but has auto-caps letters. Short sentences
image soda neutral = "soda_neutral.png" # keyboard smashes and uses multi !
image whiskey neutral = "whiskey_neutral.png" # lower case but sometimes caps for emphasis

image phone mako = "phone_mako_orange.png"
image phone chacha = "phone_chacha.png"
image phone juice = "phone_juice.png"
image phone soda = "phone_soda.png"
image phone whiskey = "phone_whiskey.png"

image bg bedroom = "bg_bedroom.png"
image bg shop = "bg_shop.png"
image bg chathyme = "bg_chathyme.png"
image bg meme = "bg_bedroom_meme.png"

################################################################################
label start:
    $ pointsChacha = 0
    $ pointsSoda = 0
    $ pointsWhiskey = 0

    jump group_chat

    scene bg bedroom with fade
    "\[ \"...just finish that with a slice of fresh lime - and there you have it. Delicious egg stir-fry with rice noodles!\" \["
    show mako neutral with dissolve
    m "(Uggghh how is it already 9 PM)"
    m "(Did I just watch recipe videos for 6 hours straight?)"
    m "(I can't even cook that well!)"
    m "(Although...no one can cook like Jordan Lambsey.)"
    "\[ RIBBIT \[ RIBBIT \["
    m "(oh, my phone...Juice is messaging me!)"
    jump tag_yourself

################################################################################
label tag_yourself:
    show phone juice at right with easeinright
    show mako neutral at left with easeinleft
    j "MAKO. i found another one of those 'tag yourself' memes"
    j "which one are you? i am definitely tom"
    scene bg meme

    menu:
        "(Press H to show/hide options)"
        "Tom":
            $ pointsWhiskey += 1
            $ pointsChacha += 1
            $ pointsSoda += 1
            scene bg bedroom
            show mako neutral at left
            show phone juice at right
            m "Juice we've been friends since forever ago. I'm def Tom"
            j "Hey me too"
        "Burgos":
            $ pointsSoda += 2
            scene bg bedroom
            show mako neutral at left
            show phone juice at right
            m "i'm burgos lol I can never figure out what gifts to buy people"
            j "Yeah I love burgos. And I love burgers"
        "Chrispy":
            $ pointsChacha += 2
            scene bg bedroom
            show mako neutral at left
            show phone juice at right
            m "extreme chrispy. i CANNOT have people wearing shoes indoors"
            j "Yeah. Why do people do that?"
        "Spudina":
            $ pointsWhiskey += 2
            scene bg bedroom
            show mako neutral at left
            show phone juice at right
            m "spudina. when i sleep, i SLEEP."
            j "did I wake u up just now by texting u a meme"
            m "you woke me up from "

    j "i wonder who our other friends would be"
    j "have you talked to any of them recently?"

    menu:
        "I've been meaning to...":
            $ pointsSoda += 1
            m "I've tried to get in touch with them, but I've been so busy..."
            m "(you weren't busy, you were JUST WATCHING Jordan Lambsey)"
            j "Were you watching food videos again"
            m "Okay yeah. I was"
        "I was busy watching videos":
            $ pointsWhiskey += 1
            $ pointsChacha += 1
            m "Nope...I've holed myself up in my room tbh"
            j "OK glad you're being honest mako."

    m "I should ask Soda, Whiskey, and Chacha how they're doing"
    j "we should all do something together before the summer ends"
    j "it'll be the last time we see each other for a long time"
    j "maybe a picnic"
    m "oh...that would be a great idea!"
    m "(ok, gotta message the group)"
    jump group_chat

################################################################################
label group_chat:
    scene bg bedroom with fade
    show mako neutral at left with easeinleft
    show phone mako at right with easeinright

    m "yo poops"
    show phone whiskey
    w "sup mako"
    m "me and juice were thinking about a picnic get together tomorrow!"
    show phone juice
    j "Yep. Beach picnic"
    j "I will bring juice"
    m "i want to see everyone one last time before the end of summer!"
    show phone whiskey
    w "the beach sounds far but i'm ALWAYS down for food"
    w "count me IN"
    show phone chacha
    c "ahhh...that sounds so fun!"
    c "but I'll be busy with work and school tmrw...so I'm not sure"

    menu:
        "Come anyway!":
            m "chacha you should try to make it anyway"
            m "it won't be the same without you!"
            c "sorry...I'll see how much studying I can cram tonight..."
        "We'll miss you":
            $ pointsChacha += 1
            m "noooo chacha"
            m "promise you'll see us before summer ends tho!"
            c "aww...I'll try...!"

    show phone whiskey
    w "chacha you should come anyway. college can wait til later"
    w "i mean it's college PREP, not even college lol"
    show phone chacha
    c "I also had a shift at Chathyme til 4"
    show phone whiskey
    w "it's the SUMMER! don't waste it stressing about school stuff lol"
    show phone chacha
    c "(Chacha is typing...)"

    menu:
        m "(Oh fluff maybe I should say something)"
        "Reschedule?":
            $ pointsChacha += 2
            m "uhh! maybe we can just reschedule to next week!"
            show phone whiskey
            w "I'm going out of town with my family then"
            show phone juice
            j "My juice is going to expire"
            show phone chacha
            c "I'll probably still be busy...but I appreciate it Mako"
            m "awww feathers"
        "Cut that out, Whiskey!":
            $ pointsChacha += 2
            m "hey come on whiskey! it's ok if she's busy"
            show phone whiskey
            w "yeah i know, i'm just saying lol"
        "(Just listen)":
            $ pointsWhiskey += 1
            # TODO

    show phone chacha
    c "I'll let everyone know later if I can make it tmrw. I need to finish studying tonight"
    m "OK!"
    c "if I can't make it, have fun"
    show phone whiskey
    w "we'll try"
    m "(oh...poor Chacha! I hope she doesn't overwork herself)"
    show phone soda
    s "HEY GUYS sry I was busy at the jungle gym!!!"
    show phone juice
    j "Hi Soda"
    show phone soda
    s "my friend told me they had new monkey bars at the gym. so I spent FOREVER looking for them"
    s "I asked the guy there and he was like uhhhh we only have pull up bars"
    s "it took me an hour before I realized my friend meant MONKEY ENERGY bars. like that vegan protein bar brand"
    m "SODA OMG"
    show phone whiskey
    w "classic soda"
    show phone soda
    s "yeah uhhh what'd I miss here"
    m "we were trying to make plans for a picnic tomorrow and get Chacha to come"
    show phone soda
    s "OH WORD!!!"
    s "I'll go out first thing tomorrow to buy some stuff"
    m "soda you're the best!"

################################################################################
label morning:
    scene bg bedroom with fade
    show phone mako with dissolve
    "\[ SQWAK \[ SQWAK \[ SQWAK \[" with vpunch
    hide phone with dissolve
    show mako neutral with dissolve

    menu:
        m "(Ugghh...it's 7 AM)"
        "Wake up right now":
            m "(OK, I'm waking up! Rise and shine, Mako!!)"
            m "(And don't close y...your...eyes...)"
            hide mako with easeoutbottom
            scene bg bedroom with fade
            show phone mako with dissolve
            "\[ SQWAK \[ SQWAK \[ SQWAK \[" with vpunch
            hide phone with dissolve
            show mako neutral with dissolve
            m "(I OVERSLEPT UNTIL 10 AM AGAIN)" with vpunch
            m "(This is why I don't get the worm.)"
        "Snooze":
            m "(I know myself well. I can't get up this early)"
            m "(Goodnight Mako.)"
            hide mako with easeoutbottom
            scene bg bedroom with fade
            show mako neutral with dissolve
            m "(Ahh, 10 AM...a proper time to wake up)"
            m "(The early bird can keep that worm. Who needs worms?)"

    show phone mako at right with easeinright
    show mako neutral at left with easeinleft
    "\[ OOK \[ OOK \["
    m "(Perfect timing.)"
    show phone soda
    s "hey mako! went out to get some stuff for tonight. if u need anything meet me at the grocery store in 30"
    m "(30 minutes?! Better get ready fast)" with vpunch
    hide phone soda with dissolve
    hide mako with easeoutright

################################################################################
label shop_soda:
    scene bg shop with fade
    show mako neutral with dissolve
    m "(OK, I should review everything I need to buy today.)"
    m "(I'll need some {color=#f48}cutlery{/color} for everyone...)"
    m "(Probably a nice {color=#f48}blanket{/color} to sit on...)"
    m "(Some...{color=#f48}balloons{/color} for decoration!)"
    m "(And {color=#f48}chicken{/color} to make my stirfry...)"
    m "(That should be good for now.)"
    m "(Soda said to meet him at the front. Where'd that monkey run off to?)"
    m "(Oh, I think I see him!)"
    m "SODA! \[" with vpunch
    show mako at left with move
    show soda neutral at right with moveinright
    s "Hey Makooo."
    s "Sorry, I said I'd be at the entrance but then I got really carried away by the fruit aisle."
    s "They're doing a two-for-one sale on bananas."
    s "TWO. FOR ONE." with vpunch
    m "Oh! That's bananas."

################################################################################
label bananas:
    s "Mako, did you know there's a proper way to peel bananas?"

    menu:
        s "Apparently, you DON'T peel bananas by the stem."
        "Why not peel the stem?":
            $ pointsSoda += 1
            m "Oh, how come? I thought the stem made peeling easier."
            s "Right. But if you DON'T peel it, the stem makes it easy to hold the banana while you eat that final last bite."
            s "Crazy, huh? Do it the hard way first and it's easier later."
            m "Huh!"
        "I knew that already!":
            m "Yeah I heard that one before! You pinch the other end and then hold onto the stem."
            s "Ah! I didn't think you were a banana bird."
            m "I don't really like bananas, I just watch TONS of food videos online."

    # TODO
    s ""
    m "Let's find the picnic stuff before we forget!"
    s "Oh yeah! I already went ahead and picked out some {color=#f48}cutlery{/color}, a {color=#f48}blanket{/color}..."
    s "Even some {color=#f48}chicken{/color} for that stirfry you said you'd make."
    m "Wow Soda, you're the best!"
    s "Anything else before we head out?"

    menu:
        "Bananas":
            m "Oh yeah, we definitely need some bananas."
            s "Really?? This is my lucky day."
            s "We can buy TWICE AS MANY because they're HALF OFF!"
            m "Yeah!!"
        "Balloons":
            m "Yeah, I thought balloons would be a really nice touch."

    s "By the way, the birthday cake should be ready in two hours."
    m "...Huh?"
    s "The birthday cake? For Chacha's party tonight?"
    m "..."
    s "..."
    m "Chacha's birthday was 3 months ago, today was just a get-together"
    s "Ohhh"
    s "OHHHHHHHhh my gosh I'm sorry"
    s "I thought it was like a surprise party and we were trying to get Chacha to come."
    m "Hooooowww did this happen."

    menu:
        "This is hilarious":
            m "This is honestly kind of funny."
            s "Yeah?"
            m "Yeah! I mean now we have cake."
        "I should've been more clear":
            m "Ahhh I can't believe I let that happen! I wasn't clear enough."
            s "Mako it's my bad, really!"
            m "Well, are you still going to pick up that cake?"
            s "Might as well, now."

################################################################################
label talk_chacha:
    scene bg chathyme with fade
    show mako neutral with dissolve
    m "(Good job Mako! You actually went out of the house and did some stuff today.)"
    m "(Before I go home, I'll stop by Chathyme and see how Chacha's doing)"
    show mako neutral at left with move
    show chacha neutral at right with moveinright
    c "Hey, welcome to Chathyme!"
    c "OH! Hi Mako!" with vpunch
    m ""

    c "I don't think I'll be able to come tonight..."
    c "I still have a ton of work to do."
    m "It's OK."

    menu:
        "You should take a break, anyway":
            m "Even if you can't make it, I think you should take a break from studying."
            c "Yeah! That's why I'm working the shift at Chathyme right now."
            m "No, I mean a REAL break! Like, some time for yourself."
            c "Oh...how do you mean?"
            menu:
                "Find time to just relax":
                    m "You just need to put aside time to recharge yourself."
                    m "Like sometimes I'll just watch videos for HOURS, and kinda just drown out the world."
                    c "I don't know, Mako, it feels like time I could just spend ACTUALLY doing stuff..."
                    m "Maybe, but when I take breaks, I can do important stuff "
                    c "..."
                    c "Yeah..."
                    c "I guess I've been really hard on myself. I'm sure I studied well already, at this point I'm just pushing myself too far."
                    m "Yeah! Don't force yourself to work past your limit!"
                    m "And hey, if you can't make it tonight, that's totally cool. We would just like it if you did, that's all."
                    c ""
                "Find something new to do":
                    m ""

################################################################################
label talk_whiskey:
    m "hey whiskey"
    w "mako!! good idea with the picnic" with vpunch
    m "yes! same"
    m "just checking what you're bringing tomorrow"
    w "oh darn, were we supposed to bring food?"
    m "kinda yeah"
    m "I was planning to make some chicken stir fry for everyone BUT LIKE will it even turn out good?? WHO KNOWS!!"
    w "I would eat your stirfry mako. there's no bottom limit for what I'd eat"
    w "so hmmm food to bring..."
    w "maybe I'll buy some mackerel? Chacha isn't coming so I won't have to bring as much"

    menu:
        "I'm going to talk to her about that":
            m "actually..."

return
