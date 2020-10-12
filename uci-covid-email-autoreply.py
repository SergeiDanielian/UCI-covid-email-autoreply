#!/usr/bin/env python
# coding: utf-8

# read
from decouple import config
from imap_tools import MailBox, AND
from lxml import html
from urllib.parse import unquote

# reply
import smtplib
from getpass import getpass
from email.mime.text import MIMEText

# automate
from os import system, path, mkdir, getenv
from shutil import copyfile
from platform import system as sys
sys = sys()


# .env example
# SENDER=UCInetID@uci.edu
# PASSWORD=abc123
sender = config('SENDER')
password = config('PASSWORD')

receiver = 'uci@service-now.com'
subject = 'UCI Student Daily Symptom Monitoring'
content = ''

with MailBox('imap.gmail.com').login(sender, password, 'INBOX') as mailbox:
    for msg in mailbox.fetch(AND(seen=False, subject=subject)):
        for a in html.fromstring(msg.html).findall('.//a'):
            if a.text == 'Not on campus today':
                # decode subject and body from link
                subject = unquote(a.get('href').split(
                    '?')[1].split('=')[1].split('&')[0]).strip()
                content = unquote(a.get('href').split(
                    '?')[1].split('=')[2].split('&')[0]).strip()

                msg = MIMEText(content)
                msg['From'] = sender
                msg['To'] = receiver
                msg['Subject'] = subject

                server = smtplib.SMTP_SSL('smtp.gmail.com:465')
                server.login(sender, password)
                # send reply
                server.send_message(msg)
                server.quit()
