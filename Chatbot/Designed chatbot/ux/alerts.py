import tkinter as tk
import os
from pathlib import Path

ASSETS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def center_window(window, width=300, height=100):
    window.update_idletasks()
    # TODO: Center the window on the screen (with the formulas)
    
    # TODO: Set the window icon
    # Ensure you have a code_sinaia_logo.ico file in the same directory
    # use relative_to_assets to get the path
    
    
    # focus on window
    window.focus_force()

#MODEL: alert window for empty message
def empty_message_alert():
    alert = tk.Toplevel()
    alert.title("Alert")
    alert.configure(bg="#ff0015")
    center_window(alert)
    alert_label = tk.Label(alert, text="Please enter a message.", bg="#f8d7da", fg="#ff0019", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#ff0019")
    ok_button.pack(pady=10)

#MODEL: alert window for success messages
def save_success_alert():
    alert = tk.Toplevel()
    alert.title("Success")
    alert.configure(bg="#d4edda")    
    alert_label = tk.Label(alert, text="History saved successfully.", bg="#d4edda", fg="#155724", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#c3e6cb", fg="#155724")
    ok_button.pack(pady=10)
    
    #TODO: center window
    center_window(alert)
    
#TODO: Create alert windows for success load 
def load_success_alert():
    alert = tk.Toplevel()
    alert.title("Success")
    alert.configure(bg="#d4edda")
    alert_label = tk.Label(alert, text="History loaded successfully.", bg="#d4edda", fg="#155724", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#c3e6cb", fg="#155724")
    ok_button.pack(pady=10)
    
    #TODO: center window
    

#TODO: Create alert window for success clear
def clear_success_alert():
    alert = tk.Toplevel()
    
    #TODO: create alert and center it
    
    alert_label = tk.Label(alert, text="Chat cleared successfully.", bg="#d4edda", fg="#155724", font=("Helvetica", 12))
    alert_label.pack(expand=True)

#TODO: Create alert for no history found
def no_history_alert():
    alert = tk.Toplevel()
    
    #TODO: create alert and center it
    
    alert_label = tk.Label(alert, text="No chat history found.", bg="#f8d7da", fg="#ff0019", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    
def json_decode_error_alert():
    alert = tk.Toplevel()
    alert.title("Error")
    alert.configure(bg="#f8d7da")
    center_window(alert)
    alert_label = tk.Label(alert, text="Error decoding JSON.", bg="#f8d7da", fg="#721c24", font=("Helvetica", 12))
    alert_label.pack(expand=True)
    ok_button = tk.Button(alert, text="OK", command=alert.destroy, bg="#f5c6cb", fg="#721c24")
    ok_button.pack(pady=10)