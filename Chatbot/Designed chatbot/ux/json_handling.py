import json
import tkinter as tk
from tkinter import messagebox
from ux.alerts import empty_message_alert, save_success_alert, load_success_alert, json_decode_error_alert, no_history_alert

def load_chat(chat_log):
    try:
        with open("data/history.json", "r", encoding="utf-8") as f:
            messages = json.load(f)
        if not messages:
            no_history_alert()
            return
        else:
            load_success_alert()
        chat_log.config(state=tk.NORMAL)
        chat_log.delete("1.0", tk.END)

        for msg in messages:
            #TODO: remind what means string interpolation and use it here
            chat_log.insert(tk.END, "{msg['text']}: {msg['sender']}\n")

        chat_log.config(state=tk.DISABLED)
        
    except json.JSONDecodeError:
        json_decode_error_alert()
        chat_log.config(state=tk.DISABLED)

def save_chat(chat_log):
    
    lines = chat_log.get("1.0", tk.END).strip().split("\n")
    messages = []
    for line in lines:
        if ": " in line:
            sender, text = line.split(": ", 1)
            messages.append({"sender": sender, "text": text})
    with open("data/history.json", "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)
    save_success_alert()