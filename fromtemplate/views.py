from django.shortcuts import render


def show_main_page(request):
    return render(request, 'fromtemplate/Главная.html')


def show_contacts(request):
    return render(request, 'fromtemplate/Контакты.html')


def show_index(request):
    return render(request, 'fromtemplate/index.html')


def show_about_us(request):

    return render(request, 'fromtemplate/О-нас.html')
