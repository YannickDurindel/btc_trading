#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 17:21:29 2022

@author: yannick
"""

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "yannick.durindel@gmail.com"  # Enter your address
receiver_email = "yannick.durindel@gmail.com"  # Enter receiver address
password = "Pyfgcrl8!"
message = """\
Subject: Feedback from the bot !

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)