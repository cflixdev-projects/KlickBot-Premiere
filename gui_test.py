import sys
import customtkinter
import keyboard
from threading import Thread, Event
from main import start

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("300x150")
customtkinter.set_default_color_theme('dark-blue')

app.resizable(False, False)
app.title('KlickBot')

stop_event = Event()

def update_status(status):
    status_label.configure(text=status)
    app.update()  # Force GUI update

def startVisual():
    update_status("Loading...")  # Show 'Loading...' when KlickBot starts
    # Here you add the code that starts the KlickBot
    t = Thread(target=run_start)  # Run start() in a separate thread
    t.start()

def run_start():
    start()  # Your start function here
    if not stop_event.is_set():
        update_status("Done")  # Update status to 'Done' after KlickBot finishes

def on_escape(event=None):
    stop_event.set()  # Signal the thread to stop
    sys.exit()  # Exit the application

# Use CTkButton instead of tkinter Button
upperText = customtkinter.CTkLabel(master=app, text='Startet nach 3s')
upperText.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Starte KlickBot", command=startVisual)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

status_label = customtkinter.CTkLabel(master=app, text='', text_color='white')  # Empty label for displaying status
status_label.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
app.bind("<Escape>", on_escape)  # Bind Escape key to on_escape function

app.mainloop()
