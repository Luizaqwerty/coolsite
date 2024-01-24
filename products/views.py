from django.http import HttpResponse
from django.shortcuts import render

#new_names = ["Ishak", "Nurislam", "Ariet", "Eldar", "Asylbek", "Bek", "Aidana", "Luiza"]

#menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Авторизация']


#data_db =[
 #   {'id': 1, 'title': 'Асылбек', 'content': 'Биография Асылбека', 'is_published': True},
 #   {'id': 2, 'title': 'Луиза', 'content': 'Биография Луизы', 'is_published': True},
 #   {'id': 3, 'title': 'Нурмухаммед', 'content': 'Биография Нурмухаммеда', 'is_published': False},
#]


 #def index(request):
 #   data = {
      #  'menu': menu,
 #       'title': 'Главная страница',
      #  'posts': data_db
  #  }
  #  return render(request, "index.html", context=data)

#menu = [{'title': "О сайте", 'url_name': 'about'},
        #{'title': "Добавить статью", 'url_name': 'add_page'},
       # {'title': "Обратная связь", 'url_name': 'contact'},
       # {'title': "Войти", 'url_name': 'login'}]

#hobby=["Sleeping","Progrmming","Footbal","Reading","Vollevbal",]


#def about(reguest):
   # return render(reguest,'about.html',{"title": "о сайте"})


#def show_post(reguest, post_id):
   # return HttpResponse(f"Отображение статьи с id = {post_id}")


#def addpage(request):
   # return HttpResponse('Добавление поста')


#def contact(request):
   # return HttpResponse('Обратная связь')


 #def login(request):
 #   return HttpResponse('Авторизация')




from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Animal


new_names = ["Ishak", "Nurislam", "Ariet", "Eldar", "Asylbek", "Bek", "Aidana", "Luiza"]


def index(request):
    names = {"new_names": new_names}
    return render(request, "index.html", context=names)


hobby = ["Sleeping", "Programming", "Footbal", "Reading", "Volleybal", "Table tennis"]


def about(request):
    list_hobby = {"hooby": hobby}
    return render(request, "about.html", context=list_hobby)


def animal(request):
    animal = Animal.objects.all()
    new_animal = {"new_animal": animal}
    return render(request, "animal.html", context=new_animal)


def detail_animal(request, animal_name):
    animal = Animal.objects.filter(name=animal_name)
    new_animal = {"new_animal": animal}
    return render(request, "animal.html", context=new_animal)


def create_animal(reguest):
    if reguest.method == "POST":
        name = reguest.POST.get("name")
        age = reguest.POST.get("age")
        breed = reguest.POST.get("breed")
        animal= Animal.objects.create(
        name=name,
        age=age,
        breed=breed,
        )

        animal.save()
        return redirect("animal")


def edit_animal(reguest, animal_id):
    animal= Animal.objects.filter(id=animal_id).first()
    new_animal= {"animal": animal}
    if reguest.method == "POST":
        name=reguest.POST.get("name")
        age= reguest.POST.get("age")
        breed= reguest.POST.get("breed")
        animal = Animal.objects.create(
            name=name,
            age=age,
            breed=breed,
        )
        return redirect("animal")
    return render(redirect, "edit_animal.html",context=new_animal)
