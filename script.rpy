# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mako")

image mako neutral = "mako_neutral.jpeg"


# The game starts here.

label start:
    scene bg room
    show mako neutral

    m "SQWAK SQWAK"
    m "HELLO"
    m "HELLOOOO"

    menu:
        "GO INTO IT":
            "we are going to go into it"
            m "here we go"
            jump wentintoit
        "GET OUTTA HERE":
            m "ok"

    label wentintoit:
        m "yo s"

    return
