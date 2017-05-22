from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
	if (request.session.get('gold') == None): # if the count = None, set count to 0 (this is useful for our first navigation to /)
		request.session['gold'] = 0
	if (request.session.get('message') == None):
		request.session['message'] = ''
	if (request.session.get('building') == None):
		request.session['building'] = ''
	return render(request, 'first_app/index.html')

def process_money(request):
	if request.method == 'POST':
		request.session['building'] = request.POST['building']
		if request.session['building'] == 'farm':
			farmgold = random.randrange(10, 21)
			request.session['gold'] += farmgold
			request.session['message'] += 'Earned ' + str(farmgold) + ' from the farm! (' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')<br>'
		elif request.session['building'] == 'cave':
			cavegold = random.randrange(5, 11)
			request.session['gold'] += cavegold
			request.session['message'] += 'Earned ' + str(cavegold) + ' from the cave! (' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')<br>'
		elif request.session['building'] == 'house':
			housegold = random.randrange(2, 6)
			request.session['gold'] += housegold
			request.session['message'] += 'Earned ' + str(housegold) + ' from the house! (' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')<br>'
		elif request.session['building'] == 'casino':
			randnum = random.randrange(0,11)
			casinogold = random.randrange(0, 51);
			if (randnum > 7):
				request.session['gold'] += casinogold;
				request.session['message'] += 'Earned ' + str(casinogold) + ' from the casino! (' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')<br>'
			else:
				if request.session['gold'] < casinogold:
					request.session['gold'] = 0
				else:
					request.session['gold'] -= casinogold;
				request.session['message'] += 'Entered a casino and lost ' + str(casinogold) + ' golds... Ouch.. (' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ')<br>'

	return redirect('/')