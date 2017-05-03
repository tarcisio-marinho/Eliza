#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import smtplib
import socket
import re


def envia_email(email):

    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()

        # Email e senha da Eliza, por favor não utilizar #
        smtp.login('elizabot123@gmail.com','boteliza123')

        de = 'elizabot123@gmail.com'
        para = [email]
        msg = """From: %s
To: %s
Subject: Oi, tenho novidades!

teste email""" % (de, ', '.join(para))

        smtp.sendmail(de, para, msg)
        smtp.quit()
        print('Email enviado')

    except smtplib.SMTPRecipientsRefused:
        print('Erro ao enviar, email inválido')
    except socket.gaierror:
        print('Erro ao enviar, sem conexão')


teste='tarcisio_marinho09@hotmail.com'
padrao=re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',teste)

if(padrao==[]):
    print('O digitado não é válido como email')

else:
    envia_email(teste)
