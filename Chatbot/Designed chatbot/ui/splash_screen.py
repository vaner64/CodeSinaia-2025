import tkinter as tk
from .main_app import open_app

def open_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)
    
    splash_width = 400
    splash_height = 200
    
    #TODO: set splash screen size and position 
    
    
    splash.configure(bg="#333333")
    label = tk.Label(splash, text="Welcome to Chatbot!", font=("Helvetica", 24), fg="white", bg="#333333")
    label.pack(expand=True)

    def close_splash():
        splash.destroy()
        open_app()
        
    splash.after(3000, close_splash)
    splash.mainloop()