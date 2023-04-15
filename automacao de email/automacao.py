import csv
from datetime import *
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

arq_clientes = 'csv_clientes.csv'
arq_template = 'template.txt'

sender_email = 'email do remetente'
sender_password = 'senha do email do remetente'




s = smtplib.SMTP(host = 'host smtp do email do remetente', port = '587')
s.starttls()
s.login(sender_email, sender_password)

print("login feito!")

def leitura_template(filename):
    with open(filename, 'r', encoding='utf-8') as arq_template:
        conteudo_template = arq_template.read()
    print('leitura feita!')
    return Template(conteudo_template)


def identifica_clientes(filename):
    emails_p_enviar = []
    nomes_p_enviar =  []

    with open(filename, encoding='utf-8') as arquivo_ref:
    
        tabela = csv.reader(arquivo_ref, delimiter=',')

        print('tabela lida')
    
        for l in tabela:
            emails_p_enviar.append(l[0])
            nomes_p_enviar.append(l[1])
    
    return emails_p_enviar, nomes_p_enviar    

def envia_emails(lista_emails, lista_clientes, texto_email):
    for email, nome in zip(lista_emails, lista_clientes):
        msg = MIMEMultipart()

        mensagem = texto_email.substitute(PERSON_NAME = nome.title())

        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = 'Email automatizado'

        msg.attach(MIMEText(mensagem, 'plain'))

        s.send_message(msg)

        print('email enviado para ', nome)

        del msg     

def main():
    
    texto_email = leitura_template(arq_template)
    lista_emails, lista_clientes = identifica_clientes(arq_clientes)

    envia_emails(lista_emails, lista_clientes, texto_email)

main()