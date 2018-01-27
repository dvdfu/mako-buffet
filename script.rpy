define m = Character("Mako")
define c = Character("Chacha")
define j = Character("Juice")
define s = Character("Soda")
define w = Character("Whiskey")

image mako neutral = "mako_neutral.jpeg"

label start:
    scene bg room
    show jordan lambsey

    "...and just finish that with a fresh lime - and you've got yourself a delicious egg stir fry with rice noodles!"

    show mako neutral
    m "(Uggghh)"
    m "(Did I just watch recipe videos for 6 hours straight?)"
    m "(I can't even cook that well!!!)"
    m "(Although...no one can cook like Jordan Lambsey.)"
    "*RIBBIT* *RIBBIT*"
    m "(Oh, my phone...Juice is messaging me!)"

    show juice text at left
    show mako neutral at right
    j "MAKO. Which one of these are you, I am definitely Tom"

    menu:
        "Brago: buys great presents for wrong people":
            m "I'm Brago lol I can never figure out what gifts to buy people!!"
            j "yeah I love Brago I love burgers"
        "Chrispy: huge brother":
            m "not sure what 'Huge Brother' means but I'm PRETTY SURE that's me"
            j "I don't know about huge brother haha"
        "Spudina: down to le earth":
            m "Spudina!! I think I'm pretty easy going"
            j "That potato makes me want some fries"
        "Tom: always ur friend":
            m "Juice we've been friends since forever ago. I'm def Tom"
            j "Yeah me too"

    j "I wonder who our other friends would be"
    j "Have you talked to any of them recently?"

    menu:
        "I've been meaning to...":
            m "I've tried to get in touch with them, but I've been so busy..."
            m "(you weren't busy, you were JUST WATCHING Jordan Lambsey)"
            j "Were you watching food videos again"
            m "Okay yeah"
        "I was busy watching videos":
            m "Nope...I've holed myself up in my room tbh"
            j "OK glad you're being honest lol"

    j "we should all do something together before the summer ends"
    m "oh...that would be a great idea!"

    scene bg group


    return
