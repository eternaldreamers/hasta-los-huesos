label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music maya
    scene bg_entrada

    "Era una tarda muy tranquila en la universidad."

    "Quien diria que pasarian cosas interesantes en la vida de nuestro, protagonista"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dorian happy

    dorian "Waohhh!!! Que bonito dia para estudiar!! :))"

    dorian "Espero que hoy me vaya todo bien."
    play sound bruh
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
