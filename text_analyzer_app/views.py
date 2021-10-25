from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def analyzer(request):
    user_written_text = request.GET.get("user_given_text", "default")
    params = {"user_written_text" : user_written_text}
    return render(request, 'analyzer.html', params) 