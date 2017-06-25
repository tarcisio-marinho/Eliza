#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho

import speech_recognition as sr

def reconhecer():
    rec = sr.Recognizer()
    with sr.Microphone() as fala:
        frase = rec.listen(fala)
    frase = rec.recognize_google(frase,language='pt')
    frase = frase.lower()
    return frase
