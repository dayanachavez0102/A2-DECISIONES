import flet as ft

def main(page: ft.Page):
    page.title = "Quiz de Animales 🐾"
    page.window_width = 420
    page.window_height = 720
    page.bgcolor = "#E3F2FD"

    estado = {"actual": "inicio"}

    # Widgets
    titulo = ft.Text(
        "¿Cuánto sabes de animales?", 
        size=24, 
        weight="bold", 
        color="#1565C0",  # Azul fuerte
        text_align="center"
    )

    texto = ft.Text("", size=18, text_align="center", color="black")
    imagen = ft.Image(src="", width=280, height=180, fit=ft.ImageFit.CONTAIN, visible=False)

    btn_si = ft.ElevatedButton("Sí", bgcolor="#2E7D32", color="white", width=120)
    btn_no = ft.ElevatedButton("No", bgcolor="#C62828", color="white", width=120)
    btn_reset = ft.TextButton("Reiniciar", icon=ft.Icons.REFRESH, style=ft.ButtonStyle(color="#1565C0"))

    botones = ft.Row(
        [btn_si, btn_no],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    # --- Funciones de flujo ---
    def mostrar_inicio():
        estado["actual"] = "inicio"
        page.bgcolor = "#E3F2FD"
        texto.value = "🐶 ¿Te gustan los animales?"
        imagen.src = "dog.png"
        imagen.visible = True
        btn_si.visible = True
        btn_no.visible = True
        page.update()

    def p2_si():
        estado["actual"] = "p2_si"
        texto.value = "🐱 ¿Prefieres gatos antes que perros?"
        imagen.src = "cat.png"
        page.update()

    def p2_no():
        estado["actual"] = "p2_no"
        texto.value = "😢 ¿Entonces no te gustan los animales?"
        imagen.src = "sad.png"
        page.update()

    def p3_gato():
        estado["actual"] = "p3_gato"
        texto.value = "🐯 ¿Te gustan los felinos salvajes?"
        imagen.src = "tiger.png"
        page.update()

    def p3_perro():
        estado["actual"] = "p3_perro"
        texto.value = "🐕 ¿Te gustan los perritos guardianes?"
        imagen.src = "guard_dog.png"
        page.update()

    def p4_tigre():
        estado["actual"] = "p4_tigre"
        texto.value = "🦁 ¿Entonces también amas a los leones?"
        imagen.src = "lion.png"
        page.update()

    def p4_perro_guardian():
        estado["actual"] = "p4_perro_guardian"
        texto.value = "🐕‍🦺 ¿Y también los perros de compañía?"
        imagen.src = "dog_companion.png"
        page.update()

    # Finales
    def final_bueno():
        estado["actual"] = "final_bueno"
        texto.value = "🌎 ¡Eres un verdadero amante de los animales!"
        imagen.src = "happy_animals.png"
        page.bgcolor = "#C8E6C9"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def final_medio():
        estado["actual"] = "final_medio"
        texto.value = "🤔 Te gustan algunos animales, pero no todos..."
        imagen.src = "meh.png"
        page.bgcolor = "#FFF59D"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def final_malo():
        estado["actual"] = "final_malo"
        texto.value = "🚫 No eres muy fan de los animales..."
        imagen.src = "angry_cat.png"
        page.bgcolor = "#FFCDD2"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    # Decisiones
    def on_si(e):
        if estado["actual"] == "inicio": p2_si()
        elif estado["actual"] == "p2_si": p3_gato()
        elif estado["actual"] == "p2_no": final_malo()
        elif estado["actual"] == "p3_gato": p4_tigre()
        elif estado["actual"] == "p3_perro": p4_perro_guardian()
        elif estado["actual"] == "p4_tigre": final_bueno()
        elif estado["actual"] == "p4_perro_guardian": final_bueno()

    def on_no(e):
        if estado["actual"] == "inicio": p2_no()
        elif estado["actual"] == "p2_si": p3_perro()
        elif estado["actual"] == "p2_no": final_malo()
        elif estado["actual"] == "p3_gato": final_medio()
        elif estado["actual"] == "p3_perro": final_medio()
        elif estado["actual"] == "p4_tigre": final_medio()
        elif estado["actual"] == "p4_perro_guardian": final_medio()

    def on_reset(e): mostrar_inicio()

    btn_si.on_click = on_si
    btn_no.on_click = on_no
    btn_reset.on_click = on_reset

    # Layout
    page.add(
        ft.Container(
            content=ft.Column(
                [titulo, texto, imagen, botones, btn_reset],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                expand=True
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )

    mostrar_inicio()

ft.app(target=main)
