import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

english_to_wadar = {
    "turban": "pataka",
    "handkerchief": "roomaal",
    "bitter_gourd": "karalyalat",
    "wrist": "managatamoo",
    "gum": "hiradyala",
    "mustache": "misaaloo",
    "camel": "vantya",
    "water": "jalam",
    "sun": "soorajam",
    "star": "taratya",
}

english_to_urdu = {
    "hello": "سلام",
    "world": "دنیا",
    "goodbye": "الوداع",
    "please": "براہ کرم",
    "thank you": "شکریہ",
    "friend": "دوست",
    "book": "کتاب",
    "pen": "قلم",
    "water": "پانی",
    "home": "گھر",
}

english_to_sanskrit = {
    "hello": "नमस्ते",
    "world": "विश्वम्",
    "goodbye": "विदायः",
    "please": "कृपया",
    "thank you": "धन्यवादः",
    "friend": "मित्रम्",
    "book": "पुस्तकम्",
    "pen": "लेखनी",
    "water": "जलम्",
    "home": "गृहम्",
}

def translate_word():
    word = entry_word.get().lower()
    language = language_var.get()

    if language == "Wadar":
        translation = english_to_wadar.get(word, "Word Not Found")
    elif language == "Urdu":
        translation = english_to_urdu.get(word, "Word Not Found")
    elif language == "Sanskrit":
        translation = english_to_sanskrit.get(word, "Word Not Found")
    else:
        translation = "Invalid Language"

    result_label.config(text=f"Translation: {translation}")

def update_word_list():
    #Updates the list of words that can be translated based on the selected language.
    language = language_var.get()
    word_listbox.delete(0, tk.END)

    if language == "Wadar":
        words = english_to_wadar.keys()
    elif language == "Urdu":
        words = english_to_urdu.keys()
    elif language == "Sanskrit":
        words = english_to_sanskrit.keys()
    else:
        words = []

    for word in sorted(words):
        word_listbox.insert(tk.END, word)

image_path = r"C:\Users\aaron\Downloads\Leonardo_Phoenix_09_A_mesmerizing_keyframe_capturing_the_essen_0.jpg"  # Replace with your image path
cv_image = cv2.imread(image_path)
cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

root = tk.Tk()
root.title("Multi-Language Word Translator")
root.geometry("1000x750")

image = Image.fromarray(cv_image)
photo = ImageTk.PhotoImage(image)
title_label = tk.Label(root, text="Word Translator", font=("Helvetica", 28, "bold"))
title_label.pack(pady=10)

background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1) 

input_label = tk.Label(root, text="Enter a word (In English):", font=("Helvetica", 24))
input_label.pack()

entry_word = tk.Entry(root, font=("Helvetica", 12), width=20)
entry_word.pack(pady=5)

# Dropdown Menu
language_var = tk.StringVar()
language_var.set("Wadar")

language_label = tk.Label(root, text="Select Language:", font=("Helvetica", 24))
language_label.pack()

language_dropdown = ttk.Combobox(root, textvariable=language_var, values=["Wadar", "Urdu", "Sanskrit"], state="readonly")
language_dropdown.pack(pady=5)

language_dropdown.bind("<<ComboboxSelected>>", lambda event: update_word_list())

word_list_label = tk.Label(root, text="Words Available for Translation:", font=("Helvetica", 18))
word_list_label.pack(pady=5)

word_listbox = tk.Listbox(root, font=("Helvetica", 12), width=30, height=10)
word_listbox.pack(pady=5)

translate_button = tk.Button(root, text="Translate", font=("Helvetica", 24), command=translate_word)
translate_button.pack(pady=10)

result_label = tk.Label(root, text="Translation: ", font=("Helvetica", 48), fg="red",bg="black")
result_label.pack(pady=10)

root.mainloop()


