﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg_entrada = Transform("images/entrada.jpg", xysize=(1920, 1080))
image bg_escaleras = Transform("images/escaleras.jpg", xysize=(1920, 1080))
image bg_patio = Transform("images/patio.jpg", xysize=(1920, 1080))

define unknown = Character("unknown")
image unknown alberto = "images/unknown_alberto.png"

define dorian = Character("Dorian")
image dorian happy = Transform("images/dorian_happy.png", zoom=0.3)
image dorian question = "images/dorian_question.png"

define alberto = Character("Alberto")
# image alberto normal = "images/alberto_normal.png"
image alberto enojado = "images/alberto_enojado.png"

image alberto caida1 = "images/caida_1.png"
image alberto caida2 = "images/caida_2.png"
image alberto caida3 = "images/caida_3.png"
image alberto caida4 = "images/caida_4.png"
image alberto caida5 = "images/caida_5.png"

# The game starts here.

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

    show dorian happy

    dorian "Waohhh!!! Que bonito dia para estudiar!! :))"

    dorian "Este es mi nuevo inicio"

    dorian "Se que podre cumplir todo mis suenios aqui, estoy muy emocioado!!"

    jump desconocido_aparece


label desconocido_aparece:
    scene bg_escaleras

    show unknown alberto

    unknown "Hey tu! Espera!!"

    menu:
        "Que decision vas a tomar?"

        "Ignorar":
            hide unknown
            show dorian question
            dorian "Alguien me esta hablando?, debio ser mosca!"
            jump aceptar_desconocido

        "Aceptar":
            hide unknown
            show dorian question
            dorian "Creo que escucho a alguien!"
            jump aceptar_desconocido

label aceptar_desconocido: 

    hide dorian

    show alberto caida1

    "piuu..."

    show alberto caida2

    "pumm..."

    show alberto caida3

    "pammm..."

    show alberto caida4

    "crashhh...!!"

    "Creo que pretendias ignorarme?"

    show alberto enojado

    alberto "Respondeme!!"

    show alberto feliz

    alberto "Es broma, pero si quieres no es broma."

    hide alberto
    show dorian pensando

    dorian "*Creo que pretende ser gracioso?, Tal vez pueda seguirle el juego."

    hide dorian
    show alberto feliz

    alberto "Pareces alguien interesante"
    alberto "Seamos amigos :))"
    alberto "Para donde te diriges?"

    hide alberto
    show dorian apuntando_direccion

    dorian "Para alla!"

    hide dorian
    show alberto apuntando_direccion

    alberto "Para alla?"

    hide alberto
    show dorian apuntando_direccion

    dorian "Sisisis, exactamente par alla xd"

    hide dorian
    show alberto feliz

    alberto "Oh vaya, veo que eres inteligente. Elegiste el camino correcto."

    hiden alberto
    show dorian posicion_pro

    dorian "Lo se, siempre lo supe!"

    show dorian pensando

    dorian "Pero... que hay alla? Disimulare que lose... xd"

    hide dorian
    show alberto pensando
    alberto "Que extranioo es este tipo, pero bueno..."

    hide alberto

    scene patio

    "Alberto con muchas hambre, decidi en buscar de algo de comer..."

    show alberto pensando 
    alberto "No conozco este lugar... hacia donde deberia ir?"

    #Aparece un men salvaje cayendose de las escaleras
    #Quien sera?
    #Se levanta y dice: "Hola, vi que eres nuevo aqui"
    #Alberto: Pareces alguien interesantes
    #Alberto: Seamos amigos :))
    #Albeto: Para donde te diriges?
    #Dorian: Para alla!
    #Alberto: Para alla?
    #Dorian: Sisisisi, exactamete para alla
    #alberto: Oh vaya, veo que eres inteligente, elegiste el camino correcto.
    #Dorian: Siempre lo supe
    #Dorian: Pero... Que alla>
    #Dorian: Disumulare que lo se...

    # Dorian se va lentamente a  una direccion desconocida, sin sabes cual sera su destino

    #Alberto: Que extranio ese tipo, pero bueno... 


    #Alberto con muchas hambre, decidi en buscar de algo de comer...

    #Alberto: No conozco este lugar... hacia donde deberia ir?

    #[Opciones] : Izquierda, Derecha

    #Elegir izquierda

    #Maycol: Hey hey hey!! a donde crees que vas?
    #Alberto:  Dejame pasar, tengo muchas hambre!


    # +++++++++

    #Maycol:  Claro, puedes pasar por aqui *Mientras sonrie sadicamente
    #Alberto: Escaquita su brazo 
    #Maycol: Tan gozuuu!!
    #Maycol: Veo que eres alguien habilidozo
    #Maycol: Es interesante este suceso, estaba buscando a alguien como tu
    #maycol: Necesito encontrar a una chica perdida y para ellos, me informron
    #maycol: Que Josep conoce su paradero
    #Alberto: Y si no quiero hacerlo?
    #MAycol: Como que no!?








    return
