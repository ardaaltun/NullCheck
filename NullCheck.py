import tkinter as tk
from tkinter import filedialog
import json
import os
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("sa")
        self.master.geometry("200x100")
        self.master.geometry("+100+100")
        self.master.resizable(False,False)
        # Create label to display file name
        self.filename_label = tk.Label(self.master, text="")
        self.filename_label.pack()

        # Create button to open file dialog
        self.open_button = tk.Button(self.master, text="JSON Dosyasi", command=self.open_file)
        self.open_button.pack()

    def open_file(self):
        # Open file dialog and get selected file name
        filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            # Display file name in label
            name = os.path.split(filename)
            self.filename_label.config(text=name[1])
            # Read contents of JSON file
            with open(filename, "r", encoding='utf-8-sig') as f:
                data = json.load(f)
            # Display contents of JSON file in new window
##            self.display_json(data['tr'])
            
                self.display_json(data)

    def display_json(self, json_data):
        # Create new window to display JSON data
        new_window = tk.Toplevel(self.master)
        new_window.title("JSON Data")
        new_window.geometry("600x400")
        # Create text box to display JSON data
        json_textbox = tk.Text(new_window)
        json_textbox.pack()
        # Insert JSON data into text box
        for i in json_data['en']:
            if(i['value'] is None and i['speechFileName'] is None):
                json_textbox.insert(tk.END, "en value & mp3  --> " + json.dumps(i['id']) + '\n')
            elif(i['value'] is None):
                json_textbox.insert(tk.END, "en sadece value --> " + json.dumps(i['id']) + '\n')
            elif(i['speechFileName'] is None):
                 json_textbox.insert(tk.END, "en sadece mp3  --> " + json.dumps(i['id']) + '\n')
        for i in json_data['es']:
            if(i['value'] is None and i['speechFileName'] is None):
                json_textbox.insert(tk.END, "es value & mp3  --> " + json.dumps(i['id']) + '\n')
            elif(i['value'] is None):
                json_textbox.insert(tk.END, "es sadece value --> " + json.dumps(i['id']) + '\n')
            elif(i['speechFileName'] is None):
                 json_textbox.insert(tk.END, "es sadece mp3  --> " + json.dumps(i['id']) + '\n')
        

root = tk.Tk()
app = App(root)
root.mainloop()
