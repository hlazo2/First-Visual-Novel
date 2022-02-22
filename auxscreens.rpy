#Probando poner un panel
default reftip=""

screen my_hud:
    frame:
        xalign 0.5
        yalign 0.0
        hbox:
            spacing 40
            text "Tiempo: [Jhoras] horas"
            text "Salud: [Salud] %"
            text "Dinero: [Bitis] Bitis"

screen control_salud():
    $a = min(100, Salud+10)
    $b = min(100, Salud+20)
    frame:
        xalign 0.9
        yalign 0.8
        hbox:
            textbutton "Comer":
                tooltip "Salud +10, bitis -10"
                if Salud>=100 or Bitis<=9:
                    tooltip "Ya no puedes usar esto"
                    action NullAction()
                else:
                    action Confirm(
                        "Comer",
                        [SetVariable("Salud", a), SetVariable("Bitis", Bitis-10)],
                        NullAction()
                    )
            textbutton "Descansar":
                tooltip "Salud +20, horas -4"
                if Salud >= 100 or Jhoras <=3:
                    tooltip "Ya no puedes usar esto"
                    action NullAction()
                else:
                    action Confirm(
                        "Descansar",
                        [SetVariable("Salud", b), SetVariable("Jhoras", Jhoras-4)],
                        NullAction()
                    )
                #action [SetVariable("Salud", Salud+20), SetVariable("Jhoras", Jhoras-4)]
            textbutton "Seguir":
                action Return()
                tooltip "Salud +0, Horas +0 bitis +0"
            $ tooltip = GetTooltip()
    if tooltip:
        hbox:
            xalign 0.9
            yalign 0.9
            text "[tooltip]"
