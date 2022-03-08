from django.shortcuts import render


def show_main_page(request):
    data = {
        'count': range(5),
    }
    return render(request, 'fromtemplate/Главная.html', context=data)


def show_contacts(request):
    return render(request, 'fromtemplate/Контакты.html')


def show_index(request):
    return render(request, 'fromtemplate/index.html')


def show_about_us(request):
    return render(request, 'fromtemplate/О-нас.html')
