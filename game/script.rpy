# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg_entrada = Transform("images/entrada.jpg", xysize=(1920, 1080))
image bg_escaleras = Transform("images/escaleras.jpg", xysize=(1920, 1080))
image bg_patio = Transform("images/patio.jpg", xysize=(1920, 1080))
image bg_fachadita = Transform("images/fachadita.jpg", xysize=(1920, 1080))
image bg_pasadiso = Transform("images/pasadiso.jpg", xysize=(1920, 1080))

define unknown = Character("unknown")
image unknown alberto = Transform("images/unknown_alberto.png", zoom=2.5)

define dorian = Character("Dorian")
image dorian happy = Transform("images/dorian_happy.png", zoom=0.3)
image dorian question = Transform("images/dorian_question.png", zoom=2)
image dorian pro = Transform("images/dorian_pro.png", zoom=2)
image dorian direccion = Transform("images/dorian_direccion.png", zoom=2)

define alberto = Character("Alberto")
# image alberto normal = "images/alberto_normal.png"
image alberto enojado = Transform("images/alberto_enojado.png", zoom=2)
image alberto feliz = Transform("images/alberto_feliz.png", zoom=2)

image alberto caida1 = Transform("images/caida_1.png", zoom=0.5)
image alberto caida2 = Transform("images/caida_2.png", zoom=0.5)
image alberto caida3 = Transform("images/caida_3.png", zoom=0.5)
image alberto caida4 = Transform("images/caida_4.png", zoom=0.5)
image alberto caida5 = Transform("images/caida_5.png", zoom=0.5)


define clari = Character("Clari")

image clari normal = Transform("images/clari_normal.png", zoom=0.5)
image clari feliz = Transform("images/clari_feliz.png", zoom=0.5)

define maycol = Character("Maycol")

image maycol normal = Transform("images/maycol_normal.png", zoom=2)

define jose = Character("Jose")

image jose normal = Transform("images/jose_normal.png", zoom=2)

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

    dorian "Espero que hoy me vaya todo bien."

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

    show alberto enojado
    alberto "Creo que pretendias ignorarme?"
    alberto "Respondeme!!"

    show alberto feliz

    alberto "Es broma, pero si quieres no es broma."

    hide alberto
    show dorian question

    dorian "*Creo que pretende ser gracioso, Tal vez pueda seguirle el juego. Jajaja xd"

    hide dorian
    show alberto feliz

    alberto "Que haces por aqui?, bueno lo que sea.."
    alberto "Seamos amigos :))"
    alberto "Para donde te diriges?"

    hide alberto
    show dorian question

    dorian "*Porque me lo pide de forma tan repentina?, Creo que me voy a sonrojar"

    hide dorian
    show alberto feliz

    alberto "Porque te estas comportando "
    alberto "Seamos amigos :))"
    alberto "Para donde te diriges?"

    hide alberto
    show dorian direccion
    dorian "Creo que para... alla!"

    # hide alberto
    # show dorian apuntando_direccion

    # dorian "Para alla!"

    # hide dorian
    # show alberto apuntando_direccion

    # alberto "Para alla?"

    hide dorian
    show alberto feliz
    alberto "Ahh! vale... Te dirijes hacia el patio"

    hide alberto
    show dorian happy
    dorian "Sisisis, exactamente par alla xd"

    hide dorian
    show alberto feliz

    alberto "Oh vaya, veo que eres inteligente. Elegiste el camino correcto."

    hide alberto
    show dorian pro

    dorian "Lo se, siempre lo supe!"

    show dorian question

    dorian "Pero... que hay alla? Disimulare que lose... xd"

    # hide dorian
    # show alberto pensando
    # alberto "Que extranioo es este tipo, pero bueno..."

    # hide alberto

    # scene patio
    hide dorian

    scene bg_patio

    show alberto feliz 
    alberto "No conozco este lugar... hacia donde deberia ir?"
    alberto "Hey que haces aqui?"

    hide alberto
    show maycol normal
    maycol "Hola Alberto, algo triste..."
    maycol "Mi servidor de minecraft no me corre :c"

    # hide maycol
    # show alberto feliz
    # alberto ""





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
