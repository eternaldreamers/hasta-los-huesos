# The game starts here.

#xalign 0.1 yalign 0.5 xsize 0.8 ysize 0.8

label start:
    play music maya
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

    dorian "Waohhh!!! Que bonito dia para tryhardear!! :))"

    dorian "Espero que hoy me vaya todo bien."

    jump desconocido_aparece
    play sound bruh


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

    play sound boom volume 1.2

    show alberto enojado
    alberto "Creo que pretendias ignorarme?"

    show alberto feliz

    alberto "Es broma, pero si quieres no es broma."

    hide alberto
    show dorian question

    dorian "*Creo que pretende ser gracioso, Tal vez pueda seguirle el juego. Jajaja xd"
 
    hide dorian
    show alberto duda

    alberto "Que haces por aqui?"

    show alberto sonroja
    alberto "Quieres ser mi amigo!? Me interesas uwu"

    hide alberto
    show dorian poker
    dorian "Dando vueltas, no me ves? :v"

    show dorian emocionado
    dorian "Vengo a la GAME JAM, listo para ganar! :D"

    hide dorian
    show alberto riendo
    alberto "Jajajajajajjaaj, crees que vas a ganar?"

    hide alberto
    show dorian feliz
    dorian "Si! :D"

    hide dorian
    show alberto alegre
    alberto "Me conveciste, seamos amigos :3"
    alberto "Eres interesante."

    scene fachadita

    hide alberto
    show dorian pro
    dorian "Sisisis, siempre lo se :emoji de pro:"

    scene bg_patio

    hide dorian
    show alberto dolor
    alberto "Me duele la panza! :C"

    hide alberto
    show dorian pensando
    dorian "Sabes, ayer...."

    hide dorian
    show alberto sufriendo
    alberto "Callate, me sigue doliendo! >.<"

    show alberto alegre
    alberto "Ya, ya estoy bien :D"

    show alberto pensando
    alberto "En que eres bueno?"

    hide alberto
    show dorian feliz
    dorian "*Porque me pregunta eso? Quiere descartarme antes de tiempo?"
    
    show dorian convencido
    dorian "*Le dire que soy repro en unity, soy tan inteligente!"

    hide dorian
    show alberto feliz
    alberto "Seamos Team, aceptas? :3"

    hide alberto 
    show dorian duda
    dorian "*Porque me lo pide tan repentino? Me pone nerviso owo"
    dorian "No hay de otra, tendre que aceptar >.<"

    hide dorian
    show alberto emocionado
    alberto "Yeyyy!!!!"

    scene bg_patio

    "Camino al patio..."

    hide alberto
    show clari enojada
    clari "Donde estabas? >:v"

    hide clari
    show alberto miedo
    alberto "*Finjire que estoy arrepentido para que me perdone xd"
    alberto "Ya, ya... Me comportare >.<"

    show alberto feliz
    alberto "Mira... Traje un amigo para el team :D"

    hide alberto
    show dorian saludo
    dorian "Hola! :D"

    hide dorian
    show clari poker
    clari "Cual Hola? >:v"

    show clari duda
    clari "Porque te inscriste?"

    hide clari
    show dorian feliz
    dorian "Solo vine porque decia juegos :v"

    show dorian triste
    dorian "Y yo solo queria jugar y termine aqui"

    hide dorian
    show alberto alegre
    alberto "Tranquilo, todo va estar bien..."

    show alberto 
    alberto "Ahora que somos equipo, vamos a ganar porque..."
    alberto "Tenemos el poder de la amistad :D"

    show alberto riendo
    alberto "Y eso es mas que suficiente xdddddddddd"

    hide alberto
    show clari pensando
    clari "Entonces... que vamos a hacer para crear el juego?"
    clari "Solo nos quedan 3 horas..."

    show clari preocupada
    clari "Crees que podamos terminarlo?"

    hide clari
    show alberto emocionado
    alberto "Sisisi, solo tenemos que llenarlo de fotos y hacer que se vea epicooo!"
    alberto "Pero con cara de payasoss! xd"

    show alberto triste
    alberto "*Yo solo quiero dormir"

    show alberto emocionado
    alberto "Y si presentamos una presentacion en blanco? :D"
    
    show alberto emocionado_ultra
    alberto "Dejariamos marca y no crees!? xd"

    hide alberto
    show clari gritar
    clari "ahhhhhhhhh!! Que verguenza!!"
    clari "No quiero!! No quierooooooooooooo!!!"

    show clari emocionado
    clari "Tengo una idea..."
    clari "Y si mejor nos ponemos a videojuegar? xddddd"

    hide clari
    show dorian emocionado
    dorian "Sisis vamos a jugar minecraft"

    hide dorian
    show alberto feliz
    alberto "Acepto! :D"

    # hide clari
    # show dorian pensando
    # dorian "Entonce... Comenzemos?"

    
















    # alberto "Seamos amigos :))"
    # alberto "Para donde te diriges?"

    # hide alberto
    # show dorian question

    # dorian "*Porque me lo pide de forma tan repentina?, Creo que me voy a sonrojar"

    # hide dorian
    # show alberto feliz

    # alberto "Porque te estas comportando "
    # alberto "Seamos amigos :))"
    # alberto "Para donde te diriges?"

    # hide alberto
    # show dorian direccion
    # dorian "Creo que para... alla!"

    # hide alberto
    # show dorian apuntando_direccion

    # dorian "Para alla!"

    # hide dorian
    # show alberto apuntando_direccion

    # alberto "Para alla?"

    # hide dorian
    # show alberto feliz
    # alberto "Ahh! vale... Te dirijes hacia el patio"

    # hide alberto
    # show dorian happy
    # dorian "Sisisis, exactamente par alla xd"

    # hide dorian
    # show alberto feliz

    # alberto "Oh vaya, veo que eres inteligente. Elegiste el camino correcto."

    # hide alberto
    # show dorian pro

    # dorian "Lo se, siempre lo supe!"

    # show dorian question

    # dorian "Pero... que hay alla? Disimulare que lose... xd"

    # hide dorian
    # show alberto pensando
    # alberto "Que extranioo es este tipo, pero bueno..."

    # hide alberto

    # scene patio
    # hide dorian

    # scene bg_patio

    # show alberto feliz 
    # alberto "No conozco este lugar... hacia donde deberia ir?"
    # alberto "Hey que haces aqui?"

    # hide alberto
    # show maycol normal
    # maycol "Hola Alberto, algo triste..."
    # maycol "Mi servidor de minecraft no me corre :c"

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
