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
    $ drink_choice = ""
    $ chacha_going = False

    scene bg bedroom with fade
    "[[ \"...just finish that with a slice of fresh lime - and there you have it. Delicious egg stir-fry with rice noodles!\" [["
    show mako neutral with dissolve
    m "(Uggghh how is it already 9 PM)"
    m "(Did I just watch recipe videos for 6 hours straight?)"
    m "(I can't even cook that well! But if I could...I'm SURE I'd have a popular cooking channel too)"
    hide mako with dissolve
    show phone juice with dissolve
    "[[ RIBBIT [[ RIBBIT [["
    show phone juice at right with easeinright
    show mako neutral at left with dissolve
    m "(My phone...Juice is messaging me!)"
    jump tag_yourself

################################################################################
label tag_yourself:
    menu:
        j "MAKO. I found another one of those 'tag yourself' memes"
        "SHOW ME":
            m "OMG SEND ME"
        "A what?":
            m "uhhh 'tag yourself'?"
            j "Yeah it's like a list of pictures with personalities and you have to figure out which one you're closest to"
            m "ohh yeah i think i've seen those before"

    j "Which one are you? I'm definitely Tom"
    scene bg meme

    menu:
        "(Press H to show/hide options)"
        "Tom":
            scene bg bedroom
            show mako neutral at left
            show phone juice at right
            m "Juice we've been friends since forever ago. I'm def Tom"
            j "Hey me too"
        "Burgos":
            scene bg bedroom
            show mako neutral at left
            show phone juice at right
            m "i'm burgos lol I can never figure out what gifts to buy people"
            j "Yeah I love burgos. And I love burgers"
        "Chrispy":
            scene bg bedroom
            show mako neutral at left
            show phone juice at right
            m "extreme chrispy. i CANNOT have people wearing shoes indoors"
            j "Yeah. Why do people do that?"
        "Spudina":
            scene bg bedroom
            show mako neutral at left
            show phone juice at right
            m "spudina. when i sleep, i SLEEP."
            j "Did I wake you up just now by texting you a meme"
            m "just assume i am always asleep tbh"

    j "I wonder who our other friends would be"
    j "Have you talked to any of them recently?"

    menu:
        "I've been meaning to...":
            m "i tried to in touch with them but I've been so busy"
            m "(I'm not busy, I was JUST WATCHING Jordan Lambsey)"
            j "Were you watching food videos again"
            m "okay yeah. i was lol"
        "I was busy watching videos":
            m "nope...I've holed myself up in my room tbh"
            j "OK glad you're being honest"

    m "i should ask everyone how they're doing"
    j "Yeah, we should all do something together before the summer ends"
    j "It'll be the last time we see each other for a long time"
    m "ohhh i could cook for everyone! i wanna try this chicken stirfry recipe"
    m "maybe we should have a picnic?"
    j "Yesss"
    j "Like at a beach too"
    m "oh...that would be a great idea!"
    m "ok brb i'm gonna make some plans"
    m "(Time to message the group)"
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
    w "the beach sounds kinda far but i'm ALWAYS down for food"
    w "count me IN"
    show phone chacha
    c "ahhh that sounds so fun!"
    c "I'll be busy with work and school tmrw...so I'm not sure yet"

    menu:
        "Come anyway!":
            m "chacha you should try to make it"
            m "it won't be the same without you!"
            c "sorry...I'll see how much studying I can cram tonight..."
        "We'll miss you":
            m "noooo chacha"
            m "promise you'll see us before summer ends tho!"
            c "aww...I'll try...!"

    show phone whiskey
    w "you should come anyway. college can wait til later"
    w "i mean it's college PREP, not even college lol"
    show phone chacha
    c "I also had a shift at Chathyme til 4"
    show phone whiskey
    w "it's the SUMMER! don't waste it stressing about school/work stuff tbh"
    show phone chacha
    c "waste??"

    menu:
        m "(Oh fluff maybe I should say something)"
        "Reschedule?":
            m "uhh! maybe we can just reschedule to next week!"
            show phone whiskey
            w "I'm going out of town with my family then"
            show phone juice
            j "My juice is going to expire"
            show phone chacha
            c "I'll probably still be busy...but I appreciate it Mako"
            m "awww feathers"
        "Cut that out, Whiskey!":
            m "hey come on whiskey! it's ok if she's busy"
            show phone whiskey
            w "yeah i know, i'm just saying lol"

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
    s "I asked the guy there and he was like \"uhhhh we only have pull up bars\""
    s "it took me an hour before I realized my friend meant MONKEY ENERGY bars. like that vegan protein bar brand"
    m "SODA OMG"
    show phone whiskey
    w "classic soda"
    show phone soda
    s "yeah uhhh what'd I miss here"
    m "we were trying to make plans for a picnic tomorrow and get Chacha to come"
    show phone juice
    j "I was bringing juice"
    show phone soda
    s "OH WORD!!!"
    s "I'll go out first thing tomorrow to buy some stuff"
    m "soda you're the best!"
    s "B)"
    hide phone with easeoutright
    show mako neutral at default with ease
    m "(Alright, it's getting late, I'll call it a night)"
    m "(Big day tomorrow!)"
    hide mako with easeoutbottom

################################################################################
label morning:
    scene bg bedroom with fade
    show phone mako with dissolve
    "[[ SQWAK [[ SQWAK [[ SQWAK [[" with vpunch
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
            "[[ SQWAK [[ SQWAK [[ SQWAK [[" with vpunch
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
    "[[ OOK [[ OOK [["
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
    m "(I'll need some {color=#eee66e}cutlery{/color} for everyone...)"
    m "(Probably a nice {color=#eee66e}blanket{/color} to sit on...)"
    m "(Some...{color=#eee66e}balloons{/color} for decoration!)"
    m "(And {color=#eee66e}chicken{/color} to make my stirfry...)"
    m "(That should be good for now.)"
    m "(Soda said to meet him at the front. Where'd that monkey run off to?)"
    m "(Oh, I think I see him!)"
    m "SODA! [[" with vpunch
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
    s "Oh yeah! I already went ahead and picked out some {color=#eee66e}cutlery{/color}, a {color=#eee66e}blanket{/color}..."
    s "Even some {color=#eee66e}chicken{/color} for that stirfry you said you'd make."
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
label chathyme:
    scene bg chathyme with fade
    show mako neutral with dissolve
    m "(Good job Mako! You actually went out of the house and did some stuff today.)"
    m "(Before I go home, I'll stop by Chathyme and see how Chacha's doing)"
    show mako neutral at left with move
    show chacha neutral at right with easeinright
    c "Hey, welcome to Chathyme!"
    c "OH! Hey Mako! [[" with vpunch
    m "Hi! I was on my way back home but figured you were still working."
    c "My shift is just about over so I was wrapping up."
    c "You missed the strangest customer just now. They were " # TODO

    # TODO
    menu:
        c "Did you want anything?"
        "Roasted Milk Tea":
            $ drink_choice = "roasted milk tea"
            m "One roasted milk tea please! Regular sugar."
        "Mango Shaved Ice":
            $ drink_choice = "mango shaved ice"
            m "A mango shaved ice please!"
            c "Would you like ice with that? Hee hee"
            m "Ohoho"
            c "Because, like...it's already ice"
            c "HAHAHA" with vpunch
            m "Ahhhhha ha"

    c "Alright, one [drink_choice] coming up!"
    hide chacha with easeoutright

################################################################################
label talk_chacha:
    scene bg chathyme with fade
    show mako neutral at left with dissolve
    show chacha neutral at right with easeinright

    c "OK, one matcha green tea as requested!"
    m "Oh, I ordered the [drink_choice]"
    c "AH!! Oh my gosh..." with vpunch
    m "It's okay! I drink pretty much anything at Chathyme."
    c "I'm just embarrassed...I've been off like this the WHOLE day!"
    m "What's wrong?"
    c "I was up really late yesterday studying, and there's still more I need to catch up on tonight."
    m "Chacha you're like the most studious person I know!!"
    m "What do you have left to catch up?"
    c "I mean, I went over my calculus textbook a ton of times already, but..."
    c "Can I be SURE I know it well enough?" with vpunch
    c "Does the limit not exist?"
    m "Wuh"
    c "If I'm going to a top engineering school in the fall, there's going to be so much competition..."

    menu:
        c "I feel like I can't waste any time NOT studying."
        "You should give yourself a break sometimes":
            m "Even if you can't make it, I think you should take a break from studying."
            c "Yeah! That's why I'm working the shift at Chathyme right now."
            m "No, I mean a REAL break! Like, time away from work and school."
            menu:
                c "A real break?"
                "Find time for just yourself":
                    $ chacha_going = True
                    m "You just need to put aside time to recharge yourself."
                    m "Like sometimes I'll just watch videos for HOURS, and kinda just drown out the world."
                    c "I don't know, Mako, it feels like time I could spend doing REAL stuff..."
                    m "Maybe, but when I take breaks, I can do the real stuff with more "
                    c "..."
                    c "Yeah..."
                    c "I guess I've been really hard on myself. I'm sure I studied well already, at this point I'm just pushing myself too far."
                    m "Yeah! Don't force yourself to work past your limit!"
                    m "And hey, if you can't make it tonight, that's totally cool. We would just like it if you did, that's all."
                    c ""
                "Find something new to do":
                    m ""
        "We won't see each other for a long time":
            m "I just think it'd be nice to hang out before all that school stuff starts."
            m "Things are going to be poopy once we all head different ways. We should spend time together while we still can!"
            c "Ohh...you already know I'm going to miss you, Mako!"
            c "It's why I'm really torn between school and friends. They're both important to me."
            c "And it doesn't help that Whiskey sometimes wants to decide FOR me which is more important."
            m "I noticed you were a little upset...I'm sorry."
            c "It's OK!"

    if chacha_going:
        c "I think I'll show up tonight!"
        m "Yeah??"
    else:
        c "Anyway, I think I'm going to head home now."
        c "I won't come tonight, but I hope you all have fun at the picnic!"
        m "Thanks Chacha! Good luck with the studies!"


return
