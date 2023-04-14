import os

import gspread
import pandas as pd
import requests
import telegram
import datetime
import pandas as pd
import gspread
import matplotlib.pyplot as plt

from flask import Flask, request
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account
from tchan import ChannelScraper
from bcb import sgs
from datetime import datetime, date
from datetime import date, timedelta


EMAIL_KEY_FILE = os.environ["EMAIL_KEY_FILE"]

app = Flask(__name__)

def enviar_email():
    data_atual = datetime.date.today()
    corpo_email = f"""
        <b>Olá, Boa noite. Eu sou uma versão do <a href="https://web.telegram.org/z/#6252592956">@dados_do_bc_bot.</a><br>Se você recebeu esse email, é porque está inscrito para ter acesso à cotação diária de diferentes moedas.</b>
        <br><br>Aqui vai algumas das notícias de hoje:\
        <br><br>{dolar_processo()}\
        <br><br>{euro_processo()}\
        <br><br>{dolar_canadense_processo()}\
        <br><br>{libra_processo()}\
        """

    msg = email.message.Message()
    msg['Subject'] = "Cotações Econômicas"
    msg['From'] = 'fernandoluizfb@gmail.com'
    msg['To'] = 'fernandoluizfb@gmail.com'
    password = os.environ.get('EMAIL_KEY_FILE')
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()

@app.route('/webhook', methods=['POST'])
def process_webhook():
    data = request.json
    
    # Chama a função de envio de e-mail quando receber um webhook
    enviar_email()
    
    return 'Webhook recebido com sucesso.'

if __name__ == '__main__':
    app.run()
