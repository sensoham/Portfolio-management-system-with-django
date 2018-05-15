from django.shortcuts import render

def index(request):
	return render(request, 'mainpage/home.html')
	
def contact(request):
	return render(request, 'mainpage/basic.html', {'content': ['For getting in touch with me, please send an email', 'soham11235@gmail.com/soham11235@yahoo.in']})
