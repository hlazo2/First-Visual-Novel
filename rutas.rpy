label Ciudad_Yelmo:
    Apz "Estamos en Ciudad Yelmo"
    menu:
        Apz "¿A dónde deberiamos ir?"
        "Visitar a Gaum el Vigoroso para conseguir el Elixir":
            jump Casa_Gaum
        "Ir a los Talleres del Gremio para fabricar el Elixir":
            jump Talleres
    Apz "Debo cumplir mi misión"
    jump Escoger_Tarea

label Puerto_Guante:
    $ Jhoras -=1
    Apz "Hemos andado por un rato, Estamos en Puerto Guante."
    Apz "Despues de buscar y preguntar, he llegado a la tienda de Tedor Osa."
    $ Jhoras -=1
    Apz "Luego de una breve dialogo, le pregunto por lo que estoy buscando."
    Tedor "Si, tengo una Fulgura."
    Apz "¿Cuanto quieres por ella?"
    Tedor "La estoy ofreciendo por 45 Bitis"
    menu:
        Apz "Me parece un precio alto ¿Qué hago?"
        "Aceptar el trato":
            jump Trato_con_Tedor

        "Seguir buscando":
            jump Trato_con_Ihim

label Minas_Bajas:
    Apz "El viaje es largo hacia Minas Bajas"
    Apz "Estamos en Minas Bajas"
    Gema "Buena fortuna visitante. ¿Qué lo ha traido hasta aqui?"
    Apz "Necesito un lingote de Duogris"
    Gema "Te lo puedo ofrecer por 45 bitis"

    menu:
        "Es demasiado. No me va a alcanzar para todo. ¿Qué hacer?"
        "Aceptar el trato con Gema":
            pass
        "Buscar otras maneras":
            jump Trato_con_Pentero

    Apz "Esta bien, acepto el trato"
    Gema "Perfecto, tenga su lingote"
    Apz "Voy a cumplir mi cometido"
    $ haveMetalDuogris = True
    jump Escoger_Tarea

label Pantanos_Denbow:
    Apz "Pantanos Denbow"
    Puk "Saludos muchacho. ¿Qué te trae por acá?"
    Apz "..."
    Apz "La paz sea contigo. Estoy buscando unos materiales que dicen pueden encontrarse aqui.

        ¿Gentilmente le pregunto con quien estoy hablando?"
    Puk "Si, si. Mi nombre es Puk. No hace falta que me digas el tuyo. Se vé que me mentirias"
    Apz "..."
    Puk "Algo me dice que buscas Fulgura Nieta o Duogris"
    Apz "¡!..."
    Puk "No has sido ni el primero ni el único, a lo largo de la vida de este Pantano"
    Puk "En fin. Tendras que ganártelos"
    jump Escoger_Tarea

label Trato_con_Tedor:
    Apz "Tedor Osa, es mucho lo que pide."
    Tedor "¡Ay amigo! Creo estar siendo justo."
    Apz "De justicia sería una rebaja de 30 bitis."
    Tedor "Se la puede llevar por 40 bitis, pero no me pida mas."
    Apz "Es mejor 35, y todos ganaríamos."
    Tedor "Está bien, {b}35{/b}. Espero ganar un cliente fiel."
    "{color=#87decd}Le das 35 bitis a Tedor.{/color}"
    $Bitis -=35
    Tedor "Bien. Por favor siga a mi hija para recoger la estatuilla. Chim, ayuda a nuestro cliente."
    Chim "Asi lo hare, Padre."
    Chim "Padre, permítame preguntar..."
    Tedor "No hay noticias. Los dioses harán su voluntad. Te ruego, no te atormentes mas."
    Tedor "... Todo ocurre por algo. Honra a tu casa haciendo lo que te digo."
    Chim "Así sea Padre.(Dirigiendose a mi) La paz sea con usted. Camine conmigo."
    "Mientras caminamos, no puedo evitar la curiosidad."
    Apz "Es bueno enterarse de las noticias, si no le importa compartirlas."
    Chim "Cierto es, pero he de decir, es cosa pequeña. Teníamos un amigo de la familia. Recibió la llamada del Dux.
    Y hubo de aceptar. 10 lunas han pasado desde su partida"
    Chim "Yo recuerdo que antes las naves traían mas noticias. Pero últimamente eso ha cambiado."
    Apz "Si. Es un asunto serio. Pero no tenga temor. Mi Gremio también fue llamado para los pertrechos.
        Nuestro trabajo es el orgullo de toda la región."
    Chim "No lo dudo. Pero mas orgullosos son los Dioses."
    "No supe como responder. Su razonamiento, sencilla e inculta, derrotó todas mis lecturas y habilidades."
    "Seguía siendo un aprendiz de pocas lunas."
    Chim "Disculpe mi cortante réplica. Poco sé yo, de este mundo nuestro. Debería aceptar su sabiduría."
    "Me mantuve en silencio. Como el agua derramada, mis ideas seguían incontrolables caminos"
    Chim "Cuando nos han pedido Fulgura, también luego han preguntado por Elixir Ambar."
    Apz "Usted me sorprende. Ha adivinado uno de mis pensamientos."
    Chim "Y otra vez le pido disculpas. No nos ha llegado."
    Apz "Esta bien. Era necesario saberlo. En todo caso, me han dicho que en la misma ciudad, hay
        alquimistas expertos en esos temas."
    Chim "Está bien informado. De entre todos,Gaum es uno de los mas habiles, si no el mejor."
    Apz "El problema con los muy habiles, es su sobre valoración."
    Chim "Si. Gaum el Vigoroso... tiene muchas habilidades. Sin embargo, cuando los del puerto hemos
        estado cerca de él, los latidos en su pecho son evidentes."

    Apz "Tiene sentido. Gaum en realidad es de las lejanas Tierras Esmeralda, como muchos \"maniales\"."
    $haveChim = True
    Chim "{color=#87decd} Si. Hace poco, pasajeros de un barco hablaban sobre gorriones regresando a ese lejano lugar.{/color}"
    Chim "No sé muy bien el significado, pero tal vez sea digno de comentar."
    Apz "Como decía, es bueno estar enterado."
    Chim "Hemos llegado."
    "Luego de un rato, Chim-Osa me trae la Fulgura Nieta."
    Chim "{color=#87decd}Tenga usted lo convenido. No puedo evitar decirle: Es un pena, al final será destruida.{color=#87decd}"
    $ haveFulguraNieta = True
    "{b=#87decd}Fulgura Nieta{/b}"

    Apz "Es por una buena causa."
    Apz "...Y yo no puedo evitar preguntarle ¿Ese amigo de su familia tenía una edad parecida a la suya?."
    Chim "Tal vez un par de años mayor. Algunos dias a su lado eran terribles. Pero en otros me hacía reir."
    Apz "Los Dioses... su voluntad es mas fuerte que la nuestra. Gracias. La paz les acompañe."
    Chim "La paz y la fortuna le acompañe."
    "Estoy en la casa de Kay"
    Apz "Volver del Puerto con el material me ha tomado {b} 2 horas {/b}."
    $Jhoras -= 2
    "Debo lograr mi objetivo."

    jump Escoger_Tarea

label Trato_con_Ihim:
    Apz "¿Donde mas puedo encontrar una Fulgura Nieta?"
    "Asi hablaba, o pensaba, preocupado. Sin casi notarlo, escuché decir:"
    Ihim "He oído que está buscando un Fulgura Nieta."
    "Una \"manial\". Algo pequeña, pero como mucha de su gente, rocosa. Y de vestimentas muy trajinadas, he de decir "
    Ihim "Yo soy una servidora en este puerto."
    Ihim "Entre mis muchos servicios, podría \"conseguir\" una. Hoy mismo la tendrá."
    Apz "Suena como una buena opción ¿Cuanto costaria su servicio?"
    Ihim "{b}10 bitis{/b}. Pero me debe esperar. Esto podría demorar."
    "Las palabras usadas me preocupan.¿Así seran todos estos servidores?"
    Apz "No se ofenda, pero lo escuchado no me tranquiliza."
    Ihim "... entiendo... Mis palabras no serán las mejores, pero son reales. Como mi gente."
    Ihim "Como yo, Ihim en el puerto."
    Ihim "Mis palabras y mi gente somos lo mismo. Hechas para servir a los Dioses, aún en tierras
    extrañas."
    Ihim "Ustedes dicen \"promesas\". Pero nosotros somos las palabras."
    "Noto la apenas contenida emoción.. pero siempre puedo decir no."
    menu:
        Apz "No confio mucho en ella, pero el precio es tentador. Debo tomar una decisión."
        "Volver con Tedor":
            Apz "Ihim. Es mi voluntad y mi palabra rechazar su servicio."
            Ihim "Así sea. Una batalla mas, como otra raya mas en mi piel."
            Ihim "Que la Diosa de la Guerra le sea favorable."
            Apz "La paz sea con Ud."
            "El tiempo pasa. Ya estoy en la tienda de Tedor."
            jump Trato_con_Tedor

        "Aceptar trato con Ihim":
            pass

    Apz "Lo admito. Mis deberes me obligan. Hágalo. Le esperare."
    Ihim "A todas las gentes y sangres, siempre algo nos obliga."
    Ihim "No se mueva de aquí. Se la traeré, pero sea paciente."

    $ isBack = True
    while isBack:
        menu:
            "Pasó 1 hora ¿Qué debo hacer?"

            "Dejar de Esperar.":
                jump Confront_Ihim
            "Seguir esperando.":
                pass
        $Jhoras -=1
        $Salud -=5
        "Ha pasado 1 hora. Me aburro y en mi cabeza chocan las ideas"
        $isBack= renpy.random.choice([True, True, False])
    Ihim "Hemos triunfado. Aquí tiene la efigie de la Diosa"
    "{color=#87decd}Fulgura Nieta{/color}"
    $ haveFulguraNieta= True
    Ihim "He acabado el servicio. Entrégueme lo acordado"
    $ Bitis-=10
    Ihim "Que los dioses le cuiden y sus palabras"
    Apz "Al fin. Ya tengo la Fulgura Nieta"
    Apz "Ahora debo regresar a la ciudad"
    "Despues de 1 hora, estoy de vuelta en la Ciudad"
    $Jhoras -=1
    jump Escoger_Tarea

label Confront_Ihim:
    "Creo que cometí un error"
    "Tal vez no me haya engañado."
    " Pero se habrá dado de que no podía cumplir"
    "Mejor regreso con Tedor"
    "Mientras voy por otro camino... ¡me encuentro con Ihim!"
    Ihim "¿Pero que es esto? ¡Yo doy mi palabra, pero no das la tuya!"
    "Sin pensar casi, trato de hablar"
    Apz "...Ihim, no podía esperarla mas. ¡Me retiro de este trato!"
    Ihim "Como sea. He perdido esta batalla, ...¡Pero tú tambien!"
    "Se aproxima rápidamente, apenas consigo ver que tiene un..."
    $Salud -= renpy.random.choice([10, 20, 30])
    "{color=#ff1515} Ihim me roza con su daga. Mi salud se reduce a [Salud]\% {/color}"
    Ihim "Adios cachorro. Tal vez en otras guerras nos veremos."
    Ihim "¡Y cuida tus palabras!"
    Apz "Me ha herido, pero no es mortal. Creo entender su propósito."
    Apz "Su estirpe tiene un sentido del honor diferente al de nosotros."
    Apz "Si descanso, podré recuperarme de este encuentro."
    Apz "Creo que aceptaré el Trato con Tedor"
    Apz "Con la mejor cara, intento llegar a un trato con el comerciante"
    jump Trato_con_Tedor

label Trato_con_Pentero:
    Apz "Ese hombre de allá me está mirando. Parece ser un esclavo"
    Pentero "Haya Paz. Escuché su necesidad de un lingote Duogris ¿Es correcto?"
    Apz "La paz sea contigo. Si tiene uno, quisiera verlo ¿Cuanto ofrece por él?"
    Pentero "Deme 20 bitis. Pero deberá venir conmigo a mi cabaña"
    Apz "De acuerdo"
    Pentero "Espera. No se puede hacer tan al descubierto.
            Y me van a pasar lista.
            Encuentrame en 1 hora a la salida de ese edificio"

    "Luego de 1 hora me encuentro con el esclavo"

    Pentero "Bien. Continuas aquí. Vamos, pero guarde distancia.
    Si alguien se acerca... diga que va a la Casa del Sol Naciente."
    Pentero "Por cierto, soy el 5R. Pero me puede llamar Pentero"
    "Tras un largo recorrido, llegamos a la cabaña"
    Pentero "Aquí lo tienes"
    Apz "Gracias Pentero. Espero esto le sirva para comprar su libertad"
    Pentero "En realidad, pensaba gastarlo en el \"Sol Naciente\"."
    Apz "Debo cumplir todas mis misiones"
    $ haveMetalDuogris = True
    jump Escoger_Tarea

label Casa_Gaum:
    "Gaum el Vigoroso. Es un personaje aquí en la Ciudad"
    "Corren historias y rumores sobre él"
    "Vino de tan lejos, para competir en el Festival de Verano"
    "En el juego de las 3 esferas, logró ser campeón. Su espectáculo, le hizo el favorito del público"
    "De eso ya han pasado muchas temporadas. Muchos Veranos."
    "Despues de eso, logro hacerse oficial en el Gremio Alquimista."
    "A los de su estirpe, no les permiten la maestría, a pesar de ser tan hábil"
    "Amado por muchos y muchas, incluido algún Dux."
    "Pero es temido e incluso odiado por otros."
    "He debido esperar un par de horas. Gaum es muy visitado."
    $Jhoras -=2
    Apz "La paz sea contigo Notable Gaum."
    Gaum "La paz sea contigo, artesano. Tus insignias son de los Artificieros"
    Apz "Soy aprendiz, Notable. En Casa de Kay Espumera"
    Gaum "Kay Espumera. La conocí cuando también era aprendiz. Debí ser mas tierno con ella.
    Ella también conmigo"
    "¿Pero como me dice estas cosas?"
    Gaum "Ja, ja, es divertido el cambio de color en tus mejillas, como fruta madurando"
    Apz "Yo... la Maestra Kay... es decir, el Gremio"
    Gaum "Perdona cachorro. A veces se me olvida dónde estoy y con quien estoy. No lo tomes a mal."
    Apz "Maese Kay, a veces habla de usted."
    Gaum "Ya, pero los veranos han pasado. Ahora estoy en otros asuntos."
    Apz "Notable... yo..."
    Gaum "Llámame Gaum, aprendiz de Kay. Lo de Vigoroso tal vez en otras circunstancias."
    Apz "Gaum, estoy aquí siguiendo los mandatos Artificieros."
    Gaum "Me lo temía. Estas temporadas parecen de un Otoño alargado"
    Apz "No quiero tomar mucho de su tiempo. Requiero de usted un Elixir Ambar"
    "Gaum me observa, en silencio. Luego gira su mirada a algún punto en el techo"
    "Despues de un rato, dificil de describir,habla."
    Gaum "Me agradaría si me dijeras el motivo de este pedido"
    Apz "Yo sigo las ordenes del Gremio."
    Gaum "¿Pero no tienes siquiera una conjetura?"
    Apz "Son conjeturas de un aprendíz."
    Gaum "Ya. Obviamente intentas ser discreto. Intentas ser un buen aprendiz."
    jump Trato_con_Gaum

label Trato_con_Gaum:
    Gaum "Yo intento ser fiel a mi origen, en esta Ciudad extraña. Te voy a decir el valor"
    Gaum "Mi Elixir Ambar vale {b}50 bitis{/b}. Te lo entregaré despues de tu aceptación"
    "Ha llegado el momento de tomar una decisión"
    menu:
        "Gracias por su tiempo. Pero no puedo llegar a ese valor":
            Gaum "Está bien cachorro. Debo atender a otras personas. Dale mis saludos a Maestra Kay."
            "Me queda la opción de hacer el elixir en los talleres"
            jump Talleres
        "Gaum, es un valor alto. Pero estoy seguro de que es justo":
            pass
        "Gaum, ¿Afectaría el valor, si añado unas palabras?" if haveChim == True:
            jump Gaum_Gorriones

    Apz "Por favor, acepte estos bitis."
    $ Bitis -=50
    Gaum "Muy bien Aprendiz, Ten esta botella de Elixir Ambar."
    $ haveElixirAmbar = True
    "{color=#87decd}Elixir Ambar{/color}"
    Gaum "Tengo otros personajes que desean mi atención. Mis mejores deseos para Kay, y para tí."
    Apz "Notable Gaum, que los Dioses lo acompañen."
    jump Escoger_Tarea

label Gaum_Gorriones:
    "Gaum, tiene una ligera sonrisa."
    Gaum "¿Acaso has pasado por el Puerto?. Esta bien. Juguemos tu juego. Habla."
    "De repente me siento frio ¿Y si mis palabras no son las indicadas?."
    "Que los Dioses me guien."
    Apz "Si... Gaum. Hay noticias de Gorriones avistado en las Tierras Esmeraldas."
    "Gaum lleva una de sus \"manos\" a su rostro. Esta conmocionado. Y otra vez el silencio."
    Gaum "Ja, ja, bien jugado cachorro. O como dicen en otras regiones: GG."
    Gaum "¡Las Tierras Verdes! ¡Algún dia he de volver! ¡Y ahora ya puedo decir que ese dia existe!"
    Gaum "Está bien. El Elixir para tí vale {b}35 Bitis{/b} ¿Quieres seguir jugando contra Gaum el Vigoroso?."
    Apz "Gaum, algún maestro me dijo que en algunos juegos, todos ganan. Gracias por cambiar su valor."
    "Gaum se acerca a un mueble de su sala. Habre un cajon del que saca una botella."
    Gaum "{b}Aqui tienes el material para el artificio {/b}"
    $ haveElixirAmbar = True
    "{color=#87decd}Elixir Ambar{/color}."
    Apz "Acepte estos {b}35{/b} bitis."
    $ Bitis-=35
    Gaum "Ha sido un buen juego. Tal vez luego debas ir a las Minas Grises"
    Apz "Tal vez, Gaum."
    Gaum "En realidad no sé que lingotes buscas. Pero conozco a algunos Elfos y Elfas de allí"
    Gaum "Como por ejemplo, Gema Azul Violeta."
    Apz "He de confesarle mi admiración por los elfos. Son criaturas hechas por maestras manos de Dioses"
    Gaum "Ja ja, te veo los latidos, aprendiz. En fin, oficiales y maestros, en eso somos iguales"
    Gaum "Como sea, escucha:"
    Gaum "{color=#87decd} Hay alquimia para el perfume de la Segunda Primavera {/color}"
    $ haveGaum = True
    Gaum "Ahora, continua por tus caminos. Debo atender a otros. Mi afecto para tu Maestra, y para tí, jugador."
    "Como fruta en maduración estoy. Y sonriente. Con algo de esfuerzo, atino a decir:"
    Apz "Que los Dioses te acompañen, Gaum."

    jump Escoger_Tarea

label Talleres:
    "Estamos en los talleres"
    Apz "Aquí podremos fabricar el Elixir Ambar"
    Apz "Es decir, tengo la receta, pero no soy experto en este arte"
    Apz "Calculo que toda la preparación me tomará 3 horas, pero podría necesitar
    varios intentos"
    Apz "O tener la fortuna de lograrlo en un solo intento"
    Apz "Llegado a cierto punto, quizá lo mejor sería dejarlo todo e ir por el otro camino"
    Apz "Manos a la obra"
    $haveFailMix = True
    while haveFailMix:
        Apz "Despues de hacer todos los pasos, no conseguimos la mezcla"
        Apz "El color no es el adecuado"
        Apz "Hemos gastado {b}3 horas.{/b}"
        Apz "Este trabajo me desgasta"
        $Jhoras-=3
        $Salud-=10
        menu:
            Apz "Tomemos una decisión"
            "Seguir probando":
                pass
            "Dejemoslo, no es nuestra habilidad":
                Apz "Creo que es hora de ir donde Gaum"
                Apz "Despues de esperar un par de horas logro ser atendido"
                jump Trato_con_Gaum

        $haveFailMix= renpy.random.choice([True, False])
    "Pasan 3 horas"
    $Jhoras-=3
    $Salud -=10
    Apz "Por fin. Hemos logrado la mezcla y el color"
    "{color=#87decd}El elixir Ambar{/color}"
    $ haveElixirAmbar = True
    jump Escoger_Tarea
