import customtkinter
import keyboard
from threading import Thread

from main import start

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("300x150")
customtkinter.set_default_color_theme('dark-blue')

app.resizable(False, False)
app.title('KlickBot')

def update_status(status):
    status_label.configure(text=status)
    app.update()  # Erzwinge die GUI-Aktualisierung

def startVisual():
    update_status("Loading...")  # Zeige 'Loading...' an, wenn der KlickBot gestartet wird
    # Hier fügst du den Code ein, der den KlickBot startet
    t = Thread(target=start)  # Führe start() in einem separaten Thread aus
    t.start()
    t.join()  # Warte darauf, dass der Thread beendet wird
    # Nachdem der KlickBot beendet ist, rufe update_status("Done") auf
    update_status("Done")

# Use CTkButton instead of tkinter Button
upperText = customtkinter.CTkLabel(master=app, text='Startet nach 3s')
upperText.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Starte KlickBot", command=startVisual)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

status_label = customtkinter.CTkLabel(master=app, text='', text_color='white')  # Empty label for displaying status
status_label.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

app.mainloop()
