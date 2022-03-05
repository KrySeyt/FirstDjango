from django.shortcuts import HttpResponse, render


def show_main_page(request):
    return render(request, 'TestApp/index.html')


def request_response(request):
    return HttpResponse("This is request page")
