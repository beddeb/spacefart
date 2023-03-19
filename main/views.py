from django.shortcuts import render
import requests
import json

# Create your views here.
def main(request):
    if request.method == 'POST':
        pass

    headers = {"X-Auth-Token": "4dqv9bmm"}
    link = 'https://dt.miet.ru/ppo_it_final'
    data = json.loads(requests.get(link, headers=headers).text)
    context = {'data':data}
    return render(request, 'main/main.html', context=context)
