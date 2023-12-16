from pytube import YouTube
from sys import argv
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("tvoje matka")
window.geometry("800x500")
window.iconbitmap("C:/Users/bures/Desktop/Programování/favicon1.ico")

window.columnconfigure((0, 1, 2, 3), weight=1)
window.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

def ytDown():
    odkaz = mp4.get()
    yt = YouTube(odkaz)
    yd = yt.streams.get_highest_resolution()
    yd.download('/Users/bures/Downloads')

def ytDownmp3():
    odkaz = mp3.get()
    yt = YouTube(odkaz)
    yd = yt.streams.filter(only_audio=True).first()
    yd.download('/Users/bures/Downloads')


uvodni = tk.Label(window, text="Vítejte v Youtube downloaderu", font=("Calibri", 45), bg="red", fg="white")
uvodni.grid(row=0, column=0, columnspan=4, sticky="nswe")

mp4otazka = tk.Label(window, text="Vložte odkaz na video, které chcete stáhnout v mp4 formátu", font=("Calibri", 24), bg="lightgrey", fg="black")
mp4otazka.grid(row=1, column=0, columnspan=4, sticky="nswe")
mp4 = tk.Entry(window, font=("Calibri", 20), bg="white", fg="darkblue", cursor="xterm", justify="center")
mp4.grid(row=2, column=0, columnspan=4, sticky="nsew")
mp3otazka = tk.Label(window, text="Vložte odkaz na video, které chcete stáhnout v mp3 formátu", font=("Calibri", 24), bg="lightgrey", fg="black")
mp3otazka.grid(row=3, column=0, columnspan=4, sticky="nswe")
mp3= tk.Entry(window, font=("Calibri", 20), bg="white", fg="darkblue", cursor="xterm", justify="center")
mp3.grid(row=4, column=0, columnspan=4, sticky="nsew")

tlacitko = tk.Button(window, text=" Stáhnout \nmp4", command=ytDown, font=("Calibri", 20), bg="lightblue", cursor="hand2")
tlacitko.grid(row=5, column=0, columnspan=2)
tlacitko = tk.Button(window, text=" Stáhnout \nmp3", command=ytDownmp3, font=("Calibri", 20), bg="lightblue", cursor="hand2")
tlacitko.grid(row=5, column=2, columnspan=4)


window.mainloop()

#pip install auto-py-to-exe  -stáhnu convertor na exe soubor
#auto-py-to-exe     -udělám si z toho exe soubor