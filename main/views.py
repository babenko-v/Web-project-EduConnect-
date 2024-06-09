from django.shortcuts import render

def main_index(request):
    return render(request, "main/main_page.html")

def about(request):
    return render(request, "main/about_us.html")