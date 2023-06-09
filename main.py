from tkinter import *
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize Tkinter
window = Tk()
window.title("Language Translator")
window.geometry('300x408')
# Load the background image
background_img = PhotoImage(file="mic2.png")

# Create a label with the background image
background_label = Label(window, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a Canvas widget
canvas = Canvas(window, width=300, height=408, highlightthickness=0, bg='#0a1020', bd=0)
canvas.pack()

# A tuple containing all the language and codes of the language will be detected
dic = ('afrikaans', 'af', 'albanian', 'sq',
       'amharic', 'am', 'arabic', 'ar',
       'armenian', 'hy', 'azerbaijani', 'az',
       'basque', 'eu', 'belarusian', 'be',
       'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
       'bg', 'catalan', 'ca', 'cebuano',
       'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)',
       'zh-tw', 'corsican', 'co', 'croatian', 'hr',
       'czech', 'cs', 'danish', 'da', 'dutch',
       'nl', 'english', 'en', 'esperanto', 'eo',
       'estonian', 'et', 'filipino', 'tl', 'finnish',
       'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
       'gl', 'georgian', 'ka', 'german',
       'de', 'greek', 'el', 'gujarati', 'gu',
       'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
       'hi', 'hmong', 'hmn', 'hungarian',
       'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
       'id', 'irish', 'ga', 'italian',
       'it', 'japanese', 'ja', 'javanese', 'jw',
       'kannada', 'kn', 'kazakh', 'kk', 'khmer',
       'km', 'korean', 'ko', 'kurdish (kurmanji)',
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian',
       'lt', 'luxembourgish', 'lb',
       'macedonian', 'mk', 'malagasy', 'mg', 'malay',
       'ms', 'malayalam', 'ml', 'maltese',
       'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
       'mn', 'myanmar (burmese)', 'my',
       'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
       'pashto', 'ps', 'persian', 'fa',
       'polish', 'pl', 'portuguese', 'pt', 'punjabi',
       'pa', 'romanian', 'ro', 'russian',
       'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
       'serbian', 'sr', 'sesotho', 'st',
       'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
       'slovak', 'sk', 'slovenian', 'sl',
       'somali', 'so', 'spanish', 'es', 'sundanese',
       'su', 'swahili', 'sw', 'swedish',
       'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
       'te', 'thai', 'th', 'turkish',
       'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
       'ug', 'uzbek', 'uz',
       'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba',
       'yo', 'zulu', 'zu')

# Function to capture voice
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...", fg="white", bg='#0a1020')
        window.update()
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        status_label.config(text="Recognizing...", fg="white", bg='#0a1020')
        window.update()
        query = r.recognize_google(audio, language='en-in')
        return query
    except Exception as e:
        status_label.config(text="Please try again.", fg="white", bg='#0a1020')
        window.update()
        return None

# Function to handle translation
def translate_text():
    query = take_command()
    while query is None:
        query = take_command()

    # Display "Select language"
    status_label.config(text="Select language", fg="white", bg='#0a1020')
    window.update()

    def destination_language():
        to_lang = take_command()
        while to_lang is None:
            to_lang = take_command()
        to_lang = to_lang.lower()
        return to_lang

    to_lang = destination_language()

    while to_lang not in dic:
        status_label.config(text="Language is currently not available. Please input another language.", fg="white", bg='#0a1020')
        window.update()
        to_lang = destination_language()

    to_lang = dic[dic.index(to_lang) + 1]

    # Translating the text
    translator = Translator()
    text_to_translate = translator.translate(query, dest=to_lang)
    text = text_to_translate.text

    # Converting text to speech
    speak = gTTS(text=text, lang=to_lang, slow=False)
    speak.save("captured_voice.mp3")

    # Playing the translated speech
    playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')

    # Displaying the translated text
    result_label.config(text=text)
    window.update()

# Create a frame for the button at the bottom
button_frame = Frame(window)
button_frame.pack(side=BOTTOM, pady=20)

# GUI elements
title_label = Label(canvas, text="Language Translator", font=("Arial", 16), fg="white", bg='#0a0c18')
title_label.pack(pady=20)

translate_button = Button(button_frame, text="Translate", command=translate_text, font=("Arial", 14))
translate_button.pack()

status_label = Label(canvas, text="", fg="white", bg='#0a1020')
status_label.pack()

result_label = Label(canvas, text="", fg="white", bg='#0a1020')
result_label.pack()

# Run the GUI
window.mainloop()
