from django.shortcuts import render
from django.http import HttpResponse 
import datetime, pytz

# Welcome page
def home(request):
    return render(request, "home.html")

# Users list page
def users_list(request):
    users = [
        {"full_name": "Aibek Mannapov", "age": 19},
        {"full_name": "Temirlan Maratuly", "age": 25}
    ]
    return render(request, "users.html", {"users": users})

# City time page
def city_time(request):
    cities = {
        "Almaty": "Asia/Almaty",
        "Calgary": "America/Edmonton",
        "Moscow": "Europe/Moscow",
        "UTC": "UTC",
    }
    selected = request.GET.get("city", "UTC")

    # текущее время в UTC
    utc_now = datetime.datetime.now(pytz.utc)
    # переводим в выбранную зону
    tz = pytz.timezone(cities[selected])
    now = utc_now.astimezone(tz)

    return render(request, "city_time.html", {
        "time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "cities": cities,
        "selected": selected
    })

# Counter page
counter = 0
def counter_view(request):
    global counter
    if "inc" in request.GET:
        counter += 1
    if "reset" in request.GET:
        counter = 0
    return render(request, "counter.html", {"counter": counter})
