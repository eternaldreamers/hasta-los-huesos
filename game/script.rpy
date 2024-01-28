# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg_entrada = "images/entrada.jpg"
image bg_patio = "images/patio.jpg"

define dorian = Character("Dorian")
image dorian happy = "images/dorian_happy.png"

define alberto = Character("Alberto")


# The game starts here.

transform dorian_happy_size:
    zoom 0.5
    xalign 0.5
#xalign 0.1 yalign 0.5 xsize 0.8 ysize 0.8

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_entrada

    "Era una tarda muy tranquila en la universidad."

    "Quien diria que pasarian cosas interesantes en la vida de nuestro, protagonista"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dorian happy at dorian_happy_size with dissolve#

    dorian "Waohhh!!! Que bonito dia para estudiar!! :))"

    dorian "Es te es mi nuevo inicio"

    dorian "Se que podre cumplir todo mis suenios aqui, estoy muy emocioado!!"


    "Mientras nuestro protagonista caminaba hacia la busqueda de su clase..."



    # These display lines of dialogue.


    # This ends the game.

    return
