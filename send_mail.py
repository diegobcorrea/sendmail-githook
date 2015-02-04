#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import libraries
import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re, sys, os
	

# Get the git log --stat entry of the new commit
log = check_output(['git', 'log', '-1', 'HEAD', '--pretty=format:%s'])

# Check if last git log has "@.... "
matchObj = re.match( r'(\@(.*?)\s)', log )

if matchObj:
   	# print "matchObj.group(2) : ", matchObj.group(2)
   	# Users data in array
   	addresses = [
   		['aperalta', 'Alejandro', 'Alejandro Peralta <aperalta@peruwayna.com>'],
   		['ddumst', 'Diego', 'Diego Becerra <ddumst@gmail.com>']
   	]

   	sendTo = matchObj.group(2)
   	# Create new array for "@all"
   	mails = []

   	i = 0
   	length = len(addresses)

   	while (i < length):
   		if sendTo == addresses[i][0]:
	   		selectAddres = addresses[i][2]
	   		mails.append(addresses[i][2])
	   		name = addresses[i][1]
	   		break
	   	else:
	   		mails.append(addresses[i][2])
	   		selectAddres = ", ".join(mails)
			name = 'Equipo'
	   	
   		i = i + 1
	   	
	# print selectAddres
	# print name

	# Specifying the from and to addresses
	fromaddr = ('Diego Becerra Correa <ddumst@gmail.com>')
	toaddrs  = selectAddres
	subject = (log)
	# Writing the message (this message will appear in the email)
	message = """\
		<div class='content'>
			<p>Hola %s,</p>
			<p>Ya se subieron los cambios al sitio de producción, pueden verlos acá:</p>
			<ul>
				<li><a href='http://book-a-class.com/admin-panel'>Panel de Administración</a></li>
				<li><a href='http://book-a-class.com/sistema-de-reservas'>Sistema de Reservas</a></li>
				<li><a href='http://book-a-class.com/modulo-profesor'>Modulo de Profesor</a></li>
			</ul>
		</div>
	""" %(name)

	# Gmail Login

	username = 'ddumst@gmail.com'
	password = getpass.getpass("Password: ")

	# Sending the mail  
	# Server Smtp & Port Smtp
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	# User credentials
	server.login(username,password)

	# Header mail
	header = MIMEMultipart()
	header['Subject'] = subject
	header['From'] = fromaddr
	header['To'] = toaddrs

	# Type message
	message = MIMEText(message, 'html', 'utf-8') 
	header.attach(message)

	# Send mail and close conection
	server.sendmail(fromaddr, mails, header.as_string())
	server.quit()
else:
   	print "No match!!"