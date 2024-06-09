import sys
import customtkinter as ctk
import keyboard
from threading import Thread, Event
import pyautogui
from main import start, offset_y, offset_x

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("350x150")
ctk.set_default_color_theme('dark-blue')

app.resizable(False, False)
app.title('KlickBot')

stop_event = Event()

def update_status(status):
    status_label.configure(text=status)
    app.update()  # Force GUI update

def updateCoordinates():
    selected_index = print_selected_value()
    global offset_x, offset_y
    if selected_index == 'Laptop - 15.6 Zoll':
        offset_x += 0
        offset_y += 0
    elif selected_index == '24 Zoll (Standard)':
        offset_x += 50
        offset_y += 70
    elif selected_index == '27 Zoll':
        offset_x += 480
        offset_y += 490
    print("Updated coordinates: x =", offset_x, ", y =", offset_y)
    return offset_x, offset_y

def startVisual():
    update_status("Loading...")  # Show 'Loading...' when KlickBot starts
    t = Thread(target=run_start, args=(offset_x, offset_y))  # Pass the offsets as arguments
    t.start()
# move mouse with force to the top left corner to stop the bot

def run_start(offset_x, offset_y):
    try:
        start(offset_x, offset_y)  # Your start function here
        if not stop_event.is_set():
            update_status("Done")  # Update status to 'Done' after KlickBot finishes
    except pyautogui.FailSafeException:
        update_status("Run Again")
def on_escape(event=None):
    stop_event.set()  # Signal the thread to stop
    sys.exit()  # Exit the application

def print_selected_value():
    selected_index = combo.current()
    print("Selected index:", selected_index)
    return selected_index



# items = ('Laptop - 15.6 Zoll', '24 Zoll (Standard)', '27 Zoll' )
combo = ctk.CTkComboBox(app, width=150, values=['Laptop - 15.6 Zoll', '24 Zoll (Standard)', '27 Zoll'], corner_radius=8, state='readonly')
combo.place(rely=0.2, relx=0.5, anchor=ctk.CENTER)
combo.set('choose Screen')


# Use CTkButton instead of tkinter Button
upperText = ctk.CTkLabel(master=app, text='Startet nach 3s')
upperText.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Starte KlickBot", command=startVisual)
button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

status_label = ctk.CTkLabel(master=app, text='', text_color='white')  # Empty label for displaying status
status_label.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)
app.bind("<Escape>", on_escape)  # Bind Escape key to on_escape function


app.mainloop()
