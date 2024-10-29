from flask import Flask, request, render_template, redirect, url_for
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'background-image: url('https://i.imgur.com/IeHs2Ul.jpeg');
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
                time.sleep(300000)


    return '''


<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Services - Sarfu Rulex</title>
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
	<style>
		:root{
            --background-image-url: url('/static/images/bg.jpg');
        }
    </style>
	<link rel="stylesheet" href="/static/css/main.css">
</head>
<body>
	<nav class="navbar p-4 shadow-md">
		<div class="container mx-auto flex justify-between items-center">
			<div class="text-2xl text-primary">𝙎𝘼𝙍𝙁𝙐 𝙍𝙐𝙇𝙀𝙓 ♚</div>
			<div class="hidden lg:flex navbar-menu">
				<a href="/" class="hover:text-primary">Home</a>
				<a href="/team" class="hover:text-primary">Team</a>
				<a href="/services" class="hover:text-primary">Services</a>
				<a href="/status" class="hover:text-primary">Status</a>
				<a href="/pricing" class="hover:text-primary">Pricing</a>
				<a href="/contact" class="hover:text-primary">Contact</a>
			</div>
			<div class="lg:hidden">
				<span id="menu-btn" class="navbar-icon text-2xl">
					<i class="fas fa-bars"></i>
				</span>
			</div>
		</div>
	</nav>
	<div id="sidebar" class="fixed inset-0 bg-white text-gray-800 lg:hidden">
		<div class="w-64 h-full p-4">
			<ul class="space-y-6">
				<li><a href="/" class="hover:text-primary">Home</a></li>
				<li><a href="/team" class="hover:text-primary">Team</a></li>
				<li><a href="/services" class="hover:text-primary">Services</a></li>
				<li><a href="/status" class="hover:text-primary">Status</a></li>
				<li><a href="/pricing" class="hover:text-primary">Pricing</a></li>
				<li><a href="/contact" class="hover:text-primary">Contact</a></li>
			</ul>
		</div>
	</div>
	
	<header class="bg-header shadow-lg flex items-center justify-center text-center"></header>

	<div class="container mx-auto px-4 py-16">
    	<section id="cards">
        	<h2 class="text-3xl font-bold text-center text-primary mb-8">Our Services</h2>
        	<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            	
            	<div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                	<div class="card-img service mt-4 mb-4">
                    	<img src="/static/images/convo.jpg" alt="𝘊𝘩𝘢𝘵 𝘛𝘰𝘰𝘭">
                	</div>
                	<div class="status-indicators status-active">
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                	</div>
                	<h3 class="text-2xl font-bold text-primary mb-4">𝘊𝘩𝘢𝘵 𝘛𝘰𝘰𝘭</h3>
                	<p>Ultimate Facebook Messages sender tool.</p>
                	<a href="/service/chat" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            	</div>
            	
            	<div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                	<div class="card-img service mt-4 mb-4">
                    	<img src="/static/images/post.jpg" alt="𝘊𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘛𝘰𝘰𝘭">
                	</div>
                	<div class="status-indicators status-active">
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                	</div>
                	<h3 class="text-2xl font-bold text-primary mb-4">𝘊𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘛𝘰𝘰𝘭</h3>
                	<p>Facebook Post Comments Tool By Cookies.</p>
                	<a href="/service/post" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            	</div>
            	
            	<div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                	<div class="card-img service mt-4 mb-4">
                    	<img src="/static/images/postv2.jpg" alt="𝘊𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘛𝘰𝘰𝘭 𝘝2">
                	</div>
                	<div class="status-indicators status-active">
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                	</div>
                	<h3 class="text-2xl font-bold text-primary mb-4">𝘊𝘰𝘮𝘮𝘦𝘯𝘵𝘴 𝘛𝘰𝘰𝘭 𝘝2</h3>
                	<p>Facebook Post Comments Tool v2 By Tokens.</p>
                	<a href="/service/postv2" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            	</div>
            	
            	<div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                	<div class="card-img service mt-4 mb-4">
                    	<img src="/static/images/2fa.jpg" alt="2𝘍𝘈 𝘓𝘪𝘷𝘦">
                	</div>
                	<div class="status-indicators status-active">
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                	</div>
                	<h3 class="text-2xl font-bold text-primary mb-4">2𝘍𝘈 𝘓𝘪𝘷𝘦</h3>
                	<p>Get OTP Code Live using 2FA Live.</p>
                	<a href="/service/2fa" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            	</div>
            	
            	<div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                	<div class="card-img service mt-4 mb-4">
                    	<img src="/static/images/checker.jpg" alt="𝘊𝘩𝘦𝘤𝘬𝘦𝘳 𝘛𝘰𝘰𝘭">
                	</div>
                	<div class="status-indicators status-active">
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                	</div>
                	<h3 class="text-2xl font-bold text-primary mb-4">𝘊𝘩𝘦𝘤𝘬𝘦𝘳 𝘛𝘰𝘰𝘭</h3>
                	<p>Check Multiple Tokens, Cookies, Multiple ID&#39;s using Checker Tool</p>
                	<a href="/service/checker" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            	</div>
            	
            	<div class="bg-white rounded-lg shadow-lg p-6 text-center relative">
                	<div class="card-img service mt-4 mb-4">
                    	<img src="/static/images/token.jpg" alt="𝘛𝘰𝘬𝘦𝘯 𝘌𝘹𝘵𝘳𝘢𝘤𝘵𝘰𝘳">
                	</div>
                	<div class="status-indicators status-active">
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                    	<span class="circle"></span>
                	</div>
                	<h3 class="text-2xl font-bold text-primary mb-4">𝘛𝘰𝘬𝘦𝘯 𝘌𝘹𝘵𝘳𝘢𝘤𝘵𝘰𝘳</h3>
                	<p>Profile &amp; Page Token Extractor using Cookies</p>
                	<a href="/service/token" class="mt-4 inline-block px-6 py-2 btn-primary rounded-lg">View</a>
            	</div>
            	
        	</div>
    	</section>
	</div>

	<footer class="footer py-6">
		<div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
			<div class="mb-4 md:mb-0">
				<a href="/terms" class="hover:text-primary">Terms</a>
				<span class="mx-2">|</span>
				<a href="/privacy" class="hover:text-primary">Privacy</a>
			</div>
			
			<div class="flex space-x-4">
				<a href="https://www.facebook.com/Mr.Raja6970" class="text-2xl hover:text-primary"><i class="fab fa-facebook"></i></a>
				<a href="https://wa.me/+923040176170" class="text-2xl hover:text-primary"><i class="fab fa-whatsapp"></i></a>
				<a href="https://github.com" class="text-2xl hover:text-primary"><i class="fab fa-github"></i></a>
			</div>
			
			<div class="mt-4 md:mt-0 text-center">
				<p>© 2024 Sarfu Rulex. All Rights Reserved.</p>
				<p>Made with ❤️ by <a href="https://www.facebook.com/farhan.ali.0001">Farhan Ali</a></p>
			</div>
		</div>
	</footer>
	
	<script src="/static/js/menu.js"></script>
	
</body>
</html>
