# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Apz =Character("Yo, aprendiz", color="cc7311")
define Kay = Character("Kay Espumera")

define Gaum = Character("Gaum El Vigoroso")
define Ihim = Character("Ihim en el Puerto")
define Gema = Character("Gema Azul Violeta")
define Pentero = Character("5r")
define Puk = Character("Puk Silvador")
define Chim = Character("Chim Osa")
define Tedor = Character("Tedor Osa")
define test = "probando"
default Jhoras = 72
default Salud = 80
default Bitis = 100
default haveFulguraNieta = False
default haveElixirAmbar = False
default haveMetalDuogris = False
default haveChim = False
default haveGaum = False

init python:

    def myfunc():
        test = "la función myfunc"
        return test

# The game starts here.

label start:
    scene bg room
    show character
    show screen my_hud
    $test= min(5,4)
    "Esto es una prueba de min(5,4) {b}[test]{/b}"

    call screen control_salud

    jump Que_Hacer

label Presenta_Kay:
    # These display lines of dialogue.
    "Ha empezado el día, en Ciudad Yelmo"
    "En la casa de La Maestra Kay Espumera, ella está algo preocupada"
    "La podemos verla hablar a uno de sus alumnos"
    Kay "Escúchame, ha llegado el momento de que hagas una tarea importante"
    Apz "¿De qué se trata maestra?"
    Kay "Tal vez no estés totalmente preparado, pero la situación lo exije"
    Kay "Yo estoy ocupada atendiendo otros deberes, los cuales me obligan a ser discreta"
    Kay "¡La Ciudad nos reclama!...¡El Gremio Artificiero nos necesita!"
    Kay "Iré directo al grano. Debes conseguirme estos 3 materiales:"
    Kay "   -	Un lingote de Metal Duogris \n
            -	Un frasco de Elixir Ambar \n
            -	Una Fulgura Nieta \n
            "
    Kay "Presta atención, estos materiales debes darmelos a mi... "
    Kay "... en 3 dias (72 horas). Te entrego 100 bitis, para facilitar su obtención "
    Kay "Repasa lo que te enseñado. Así te será mas sencillo conseguirlos"
    Kay "Debes ser discreto. No eres cualquier aldeano"
    Kay "¡Perteneces al Gremio Artificiero de Ciudad Yelmo!"
    Kay "...bueno ... aunque solo seas un aprendiz de algunas lunas"
    Kay "Tu misión empieza aquí ¡Repasa lo enseñado se quieres conseguirlo!"
    Kay "¡¡En Marcha!!"
    jump Que_Hacer

label Que_Hacer:
    menu:
        Apz "¿Qué hacer?:"
        "Repasar lo que sabemos":
            jump Repaso
        "Escoger la tarea":
            jump Escoger_Tarea

label Repaso:

    Apz "Esto es lo que sé de los materiales"
    menu:
        "Los Materiales"
        "Fulgura Nieta":
            jump Sobre_Fulgura_Nieta

        "Elixir Ambar":
            jump Sobre_Elixir_Ambar

        "Metal Duogris":
             jump Sobre_Metal_Duogris

        "Regresar a \"¿Qué hacer?\"":
            jump Que_Hacer

label Escoger_Tarea:
    menu:
        Apz "Hacia donde ir"
        "Ir al Puerto por Fulgura Nieta" if haveFulguraNieta == False:
            jump Puerto_Guante

        "Ir a las Minas Bajas" if haveMetalDuogris == False:
            jump Minas_Bajas

        "Ir a los Pantanos Denbow" if (haveFulguraNieta and  haveMetalDuogris) == False:
            jump Pantanos_Denbow

        "Buscar en Ciudad Yelmo" if haveElixirAmbar == False:
            jump Ciudad_Yelmo

        "Entregar Materiales a Maestra Kai" if haveFulguraNieta and  haveMetalDuogris and haveElixirAmbar == True:
            jump Completada_Mision
        "Repasar Nuestro Conocimiento":
            jump Que_Hacer
label Completada_Mision:
    "Hemos tenido exito"
    return()





    # This ends the game.
