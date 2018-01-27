define m = Character("Mako")
define c = Character("Chacha")
define j = Character("Juice")
define s = Character("Soda")
define w = Character("Whiskey")

image mako neutral = "mako_neutral.png"
image mako phone = "mako_phone_orange.png"
image chacha neutral = "chacha_neutral.png"
image juice neutral = "juice_neutral.png"
image juice phone = "juice_phone.png"
image soda neutral = "soda_neutral.png"
image whiskey neutral = "whiskey_neutral.png"

image bg room = "background.jpg"

label start:
    $ pointsChacha = 0
    $ pointsSoda = 0
    $ pointsWhiskey = 0

    scene bg room with fade
    "\[ \"...and just finish that with a fresh lime - and you've got yourself a delicious egg stir fry with rice noodles!\" \["
    show mako neutral with dissolve
    m "(Uggghh)"
    m "(Did I just watch recipe videos for 6 hours straight?)"
    m "(I can't even cook that well!!!)"
    m "(Although...no one can cook like Jordan Lambsey.)"
    "\[ RIBBIT \[ RIBBIT \[" with vpunch
    m "(Oh, my phone...Juice is messaging me!)"
    jump tag_yourself

label tag_yourself:
    show juice phone at right with moveinright
    show mako neutral at left with move
    j "MAKO. i found another one of those 'tag yourself' memes"
    j "which one is you?"
    hide juice with dissolve
    show memes at right with dissolve
    j "i am definitely tom"

    menu:
        "Brago":
            $ pointsSoda += 2
            hide memes with dissolve
            show juice phone at right with dissolve
            m "I'm brago lol I can never figure out what gifts to buy people!!"
            j "yeah I love brago. I love burgers"
        "Chrispy":
            $ pointsChacha += 2
            hide memes with dissolve
            show juice phone at right with dissolve
            m "not sure what 'Huge Brother' means but I'm PRETTY SURE that's me"
            j "I don't know about huge brother haha"
        "Spudina":
            $ pointsWhiskey += 2
            hide memes with dissolve
            show juice phone at right with dissolve
            m "Spudina!! I think I'm pretty easy going"
            j "That potato makes me want some fries"
        "Tom":
            $ pointsWhiskey += 1
            $ pointsChacha += 1
            $ pointsSoda += 1
            hide memes with dissolve
            show juice phone at right with dissolve
            m "Juice we've been friends since forever ago. I'm def Tom"
            j "Yeah me too"

    j "I wonder who our other friends would be"
    j "Have you talked to any of them recently?"

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

label group_chat:
    show mako neutral at left with move
    show juice neutral at left with move
    show chacha neutral at right with dissolve
    show soda neutral at right with dissolve
    show whiskey neutral at right with dissolve

    m "yo poops"
    w "sup mako"
    m "me and Juice were thinking about a picnic get-together tomorrow"
    j "yes. picnic"
    j "I will bring juice"
    m "I want to see everyone one last time before the end of summer"
    w "Food is always a good idea"
    w "count me in tomorrow"
    c "ahhh...that sounds so fun!"
    c "but, I might be too busy. I have to study for my college prep exams next week"

    menu:
        "Come anyway!":
            $ pointsWhiskey += 1
            m "(I don't want to sound pushy, but...I want Chacha to come!)"
            m "Chacha you should try to make it anyway"
            m "it won't be the same without you"
            c "I'm already really behind on studying so I really don't know if I can."
            c "sorry Mako"
            m "aw, don't be Chacha"
        "OK, good luck studying :(":
            $ pointsChacha += 1
            m "that's too bad, but good luck with your prep exams"
            c "thanks!! Just need to go through 6 more chapters and an essay before tonight and I'll be on track"

    w "Chacha you should come anyway! College can come later"
    w "Uhh, I mean, College PREP can come later"
    c "I wish, but I really need to catch up while it's still summmer"
    w "but summer is FOR hanging out. and this is the last one we'll get."
    w "why waste it by studying?"
    c "waste??"

    menu:
        "(Say something)":
            $ pointsChacha += 2
            m "uhh. maybe we can just reschedule to next week!"
            w "I'm going out of town with my family later"
            j "My juice is going to expire"
            c "I'll probably still be busy...but I appreciate it Mako"
            m "awww feathers"
        "(Just listen)":
            $ pointsWhiskey += 1
            m "(I don't want to step on any toes here...)"
            w "yeah...it seems like a waste of a good time to relax"
            c "there is never time to relax!!" with vpunch
            c "anyway"

    c "I'll let you know later if I can make it tomorrow. I really need to finish this chapter tonight"
    m "OK!"
    c "if I can't make it, have fun..."
    c "(Chacha went offline)"
    m "(oh...poor Chacha)"
    s "HEY GUYS sorry I was busy at the jungle gym, working on the monkey bars"
    s "I might have broke the bars. and the Monkeys."
    s "What'd I miss"
    m "we were trying to make plans for a picnic and get Chacha to come"
    s "OH WORD!!!"
    s "I'll go out first thing tomorrow to buy some stuff"
    m "soda you're the best"
    m "I'll come with you tomorrow"

label morning:
    scene bg room with fade
    "\[ SQWAK SQWAK SQWAK \[" with vpunch
    show mako neutral with dissolve
    m "(ugghh my alarm...it's 7 AM)"

    menu:
        "Wake up right now":
            m "(OK! I'm waking up! Rise and shine, Mako!!)"
            m "(and don't close y...your...eyes...)"
            hide mako with moveoutbottom
            show bg room with fade
            "\[ SQWAK SQWAK SQWAK \[" with vpunch
            show mako neutral with dissolve
            m "(I OVERSLEPT UNTIL 10 AM AGAIN)" with vpunch
            m "(This is why I don't get the worm.)"
        "Snooze":
            m "(I know myself well. I can't get up this early)"
            m "(goodnight)"
            hide mako with moveoutbottom
            show bg room with fade
            show mako neutral with dissolve
            m "(ahh, 10 AM...a proper time to wake up)"
            m "(the early bird can keep that worm. Who needs worms?)"


label shop_soda:
    show mako neutral with dissolve
    m "(OK, I should review everything I need to buy today.)"
    m "(I'll need some {color=#f48}cutlery{/color} for everyone...)"
    m "(Probably a nice {color=#f48}blanket{/color} to sit on...)"
    m "(Some...{color=#f48}balloons{/color} for decoration!)"
    m "(And {color=#f48}chicken{/color} to make my stirfry...)"
    m "(That should be good for now.)"
    m "(Soda said he'd be at the entrance. Where'd that monkey run off to?)"
    m "(Oh, I think I see him!)"
    m "SODA! \[" with vpunch
    show mako at left with move
    show soda neutral at right with moveinright
    s "Hey Makooo."
    s "Sorry, I said I'd be at the entrance but then I got really carried away by the fruit aisle."
    s "They're doing a half-off sale on bananas."
    s "HALF. OFF." with vpunch
    m "Oh! That's bananas."
    s "Mako, did you know there's a proper way to peel bananas?"
    s "Apparently, you DON'T peel at the end with the stem."

    menu:
        "Why not peel the stem?":
            $ pointsSoda += 1
            m "Oh, how come? The stem made it easier to peel."
            s "Right, right, but if you DON'T peel it, the stem makes it easier to HOLD!"
            s "Crazy right? Do it the hard way first and it's easier later."
            m "Huh!"
        "I knew that already!":
            m "Yeah I heard that one before!"
            s "Ah! I didn't think you were a banana bird."
            m "I'm more of a clementine bird! But I know my foods."

    m "Anyway, let's find the picnic stuff!"
    s "Oh yeah! I already went ahead and picked out some {color=#f48}cutlery{/color}, a {color=#f48}blanket{/color}..."
    s "Even some {color=#f48}chicken{/color} for that stirfry you said you'd make."
    m "Wow Soda, you're the best!"
    s "Anything else before we head out?"

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


label talk_chacha:

return
