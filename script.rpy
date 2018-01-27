define m = Character("Mako")
define c = Character("Chacha")
define j = Character("Juice")
define s = Character("Soda")
define w = Character("Whiskey")

image mako neutral = "mako_neutral.jpeg"

image bg room = "background.jpg"

label start:
    $ pointsChacha = 0
    $ pointsSoda = 0
    $ pointsWhiskey = 0

    scene bg room with fade
    show jordan lambsey with dissolve

    "...and just finish that with a fresh lime - and you've got yourself a delicious egg stir fry with rice noodles!"

    show mako neutral with moveinright
    m "(Uggghh)"
    m "(Did I just watch recipe videos for 6 hours straight?)"
    m "(I can't even cook that well!!!)"
    m "(Although...no one can cook like Jordan Lambsey.)"
    "*RIBBIT* *RIBBIT*"
    m "(Oh, my phone...Juice is messaging me!)"
    jump tag_yourself

label tag_yourself:
    show juice text at left with moveinleft
    show mako neutral at right with move
    j "MAKO. Which one of these are you, I am definitely Tom"

    menu:
        "Brago: buys great presents for wrong people":
            $ pointsSoda += 2
            m "I'm Brago lol I can never figure out what gifts to buy people!!"
            j "yeah I love Brago I love burgers"
        "Chrispy: huge brother":
            $ pointsChacha += 2
            m "not sure what 'Huge Brother' means but I'm PRETTY SURE that's me"
            j "I don't know about huge brother haha"
        "Spudina: down to le earth":
            $ pointsWhiskey += 2
            m "Spudina!! I think I'm pretty easy going"
            j "That potato makes me want some fries"
        "Tom: always ur friend":
            $ pointsWhiskey += 1
            $ pointsChacha += 1
            $ pointsSoda += 1
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
    m "(ok, gotta message thr group)"
    jump group_chat

label group_chat:
    show mako neutral at left
    show juice neutral at left
    show chacha neutral at right
    show soda neutral at right
    show whiskey neutral at right

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
            m "aw Chacha you should try to make it anyway"
            m "it won't be the same without you :("
            c "I'm already really behind on studying so I really don't know if I can"
            c "sorry Mako"
            m "aw don't be Chacha"
        "OK, good luck studying :(":
            $ pointsChacha += 1
            m "that's too bad, but good luck with your prep exams"
            c "thanks!! Just need to go through 6 more chapters and an essay before tonight and I'll be on track"

    w "Chacha you should come anyway! College can come later"
    w "Uhh, I mean, College PREP can come later"
    c "I wish, but I really need to catch up while it's still summmer"
    w "but summer is FOR hanging out. and this is the last one we'll get."
    w "why waste it by studying?"
    c "..."

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

    c "I'll let you know tomorrow. I really need to finish this chapter tonight"
    m "OK!"
    c "have fun..."
    c "(Chacha has left the conversation)"
    m "(it...sounded like Whiskey hurt her feelings a bit)"
    s "HEY GUYS sorry I was busy at the jungle gym, working on the monkey bars"
    s "I might have broke the bars. and the Monkeys."
    s "What'd I miss"
    m "we were trying to make plans for a picnic and get Chacha to come"
    s "OH WORD!!!"
    s "I'll go out first thing tomorrow to buy some stuff"
    m "soda you're the best"

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

label talk_soda:

return
