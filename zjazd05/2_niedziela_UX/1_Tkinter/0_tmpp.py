import PySimpleGUI as sg
import os

sg.theme('LightBlue')  # ustawienie motywu

# Definicja menu
menu_def = [
    ['Plik', ['Otwórz plik', 'Zapisz plik', '---', 'Zamknij']],
    ['Pomoc', ['O aplikacji']]
]

# ================================
# Layout dla zakładki "Operacje plikowe"
# ================================
tab_file_layout = [
    [sg.Text("Wybrany plik: brak", key="-FILE-LABEL-")],
    [sg.Button("Wybierz plik", key="-FILE-")],
    [sg.Multiline(size=(80, 15), key="-FILE-TEXT-")]
]

# ================================
# Layout dla zakładki "Widgety"
# ================================
tab_widgets_layout = [
    [sg.Text("Imię:"), sg.Input(key="-NAME-", size=(20, 1))],
    [sg.Checkbox("Zgadzam się", key="-AGREE-")],
    [sg.Text("Wybierz płeć:"),
     sg.Radio("Kobieta", "GENDER", default=True, key="-GENDER-F-"),
     sg.Radio("Mężczyzna", "GENDER", key="-GENDER-M-")],
    [sg.Text("Kraj:"), sg.Combo(["Polska", "Niemcy", "Francja", "Wielka Brytania"],
                                 default_value="Polska", key="-COUNTRY-")],
    [sg.Text("Ilość:"), sg.Spin(values=list(range(101)), initial_value=0, key="-AMOUNT-")],
    [sg.Text("Wiek:"), sg.Slider(range=(0, 100), orientation="h", size=(34, 20),
                                 key="-AGE-", default_value=0),
     sg.Text("0", key="-AGE-VALUE-")],
    [sg.Text("Postęp:"), sg.ProgressBar(max_value=100, orientation="h",
                                         size=(20, 20), key="-PROGRESS-")],
    [sg.Button("Wyświetl dane", key="-SHOW-DATA-")],
    [sg.Listbox(values=["Element 1", "Element 2", "Element 3", "Element 4"],
                size=(30, 4), key="-LIST-")]
]

# ================================
# Layout dla zakładki "Canvas"
# (używamy elementu Graph do rysowania)
# ================================
graph = sg.Graph(
    canvas_size=(400, 300),
    graph_bottom_left=(0, 0),
    graph_top_right=(400, 300),
    background_color="white",
    key="-GRAPH-"
)
tab_canvas_layout = [
    [graph]
]

# Rysowanie przykładowych kształtów na grafie
graph.draw_rectangle((50, 50), (150, 150), fill_color="red", line_color="black")
graph.draw_oval((200, 50), (300, 150), fill_color="blue", line_color="black")
graph.draw_line((50, 200), (300, 200), color="green", width=3)

# ================================
# Layout dla zakładki "Obrazki/Kolory"
# ================================
tab_images_layout = [
    [sg.Button("Wybierz obrazek", key="-IMAGE-")],
    [sg.Image(key="-IMAGE-ELEM-")],
    [sg.Button("Wybierz kolor tła", key="-COLOR-")],
    [sg.Text("Tutaj zmieni się kolor tła", size=(40, 2),
             key="-COLOR-DISPLAY-", background_color="lightgrey")]
]

# ================================
# Tworzenie grupy zakładek oraz głównego layoutu
# ================================
tab_group = sg.TabGroup([
    [sg.Tab("Operacje plikowe", tab_file_layout),
     sg.Tab("Widgety", tab_widgets_layout),
     sg.Tab("Canvas", tab_canvas_layout),
     sg.Tab("Obrazki/Kolory", tab_images_layout)]
])

layout = [
    [sg.Menu(menu_def, key="-MENU-")],
    [tab_group]
]

window = sg.Window("Zaawansowana Aplikacja PySimpleGUI", layout, finalize=True)

# Ustawienie początkowej wartości progressbara na 50%
window["-PROGRESS-"].update(current_count=50)

# ================================
# Pętla zdarzeń
# ================================
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Zamknij":
        break

    # Obsługa zdarzeń z menu
    if event == "Otwórz plik":
        file_path = sg.popup_get_file("Wybierz plik",
                                      file_types=(("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")))
        if file_path:
            window["-FILE-LABEL-"].update("Wybrany plik: " + file_path)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                window["-FILE-TEXT-"].update(content)
            except Exception as e:
                sg.popup_error("Błąd", f"Nie udało się otworzyć pliku:\n{e}")

    elif event == "Zapisz plik":
        file_path = sg.popup_get_file("Zapisz plik", save_as=True,
                                      file_types=(("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")))
        if file_path:
            try:
                content = values["-FILE-TEXT-"]
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                sg.popup("Sukces", "Plik został zapisany.")
            except Exception as e:
                sg.popup_error("Błąd", f"Nie udało się zapisać pliku:\n{e}")

    elif event == "O aplikacji":
        sg.popup("O aplikacji", "Zaawansowana Aplikacja PySimpleGUI\nPrzykład użycia wielu widgetów i funkcji.")

    # Obsługa przycisku "Wybierz plik" w zakładce "Operacje plikowe"
    elif event == "-FILE-":
        file_path = sg.popup_get_file("Wybierz plik",
                                      file_types=(("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")))
        if file_path:
            window["-FILE-LABEL-"].update("Wybrany plik: " + file_path)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                window["-FILE-TEXT-"].update(content)
            except Exception as e:
                sg.popup_error("Błąd", f"Nie udało się otworzyć pliku:\n{e}")

    # Obsługa przycisku "Wyświetl dane" w zakładce "Widgety"
    elif event == "-SHOW-DATA-":
        name = values["-NAME-"]
        agree = "Tak" if values["-AGREE-"] else "Nie"
        gender = "Kobieta" if values["-GENDER-F-"] else "Mężczyzna"
        country = values["-COUNTRY-"]
        amount = values["-AMOUNT-"]
        age = int(values["-AGE-"])
        progress_val = 50  # ustalono wartość 50% przy inicjalizacji
        data = (f"Imię: {name}\n"
                f"Zgoda: {agree}\n"
                f"Płeć: {gender}\n"
                f"Kraj: {country}\n"
                f"Ilość: {amount}\n"
                f"Wiek: {age}\n"
                f"Postęp: {progress_val}%")
        sg.popup("Dane z formularza", data)

    # Aktualizacja etykiety przy suwaku wieku
    if event == "-AGE-":
        window["-AGE-VALUE-"].update(f"{int(values['-AGE-'])}")

    # Obsługa kliknięć na elemencie Graph (zakładka "Canvas")
    if event == "-GRAPH-":
        click = values["-GRAPH-"]
        if click is not None:
            # Rysowanie małego okręgu o promieniu 5 w miejscu kliknięcia
            graph.draw_circle(click, 5, fill_color="purple", line_color="purple")

    # Obsługa przycisku "Wybierz obrazek" w zakładce "Obrazki/Kolory"
    elif event == "-IMAGE-":
        file_path = sg.popup_get_file("Wybierz obrazek",
                                      file_types=(("Pliki graficzne", "*.png;*.jpg;*.jpeg;*.gif"), ("Wszystkie pliki", "*.*")))
        if file_path:
            window["-IMAGE-ELEM-"].update(filename=file_path)

    # Obsługa przycisku "Wybierz kolor tła" w zakładce "Obrazki/Kolory"
    elif event == "-COLOR-":
        color = sg.popup_get_color()
        if color:
            window["-COLOR-DISPLAY-"].update(background_color=color)

window.close()
