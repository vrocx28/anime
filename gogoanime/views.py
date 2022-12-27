import os
import re

import requests
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from lxml import html

from .forms import AddAnime
from .models import Anime_All

# Create your views here.s


def get_res(url):
    requestHeaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }
    return requests.get(url, headers=requestHeaders, allow_redirects=True)


def get_anime_meta_data(ani_url):
    base_url = os.getenv("gogoanime_base_url")
    url = f"{base_url}/category/{ani_url}"
    response = get_res(url)
    html_res = html.fromstring(response.text)
    anime_name = html_res.xpath('//div[@class="anime_info_body_bg"]/h1/text()')[0].strip()
    anime_id = html_res.xpath('//input[@id="movie_id"]/@value')[0].strip()
    try:
        summary = re.findall(r"Plot Summary: </span>(.*?)</p>", response.text)[0]
    except:
        norma_string = response.text.replace("\n", "")
        summary = re.findall(r"Plot Summary: </span>(.*?)</p>", norma_string)[0]
    return anime_name, anime_id, summary


def add_anime(request):
    if request.POST:
        updated_request = request.POST.copy()
        # print(updated_request)
        anime_name, anime_id, summary = get_anime_meta_data(
            updated_request["gogoanime_url"]
        )
        # updated_request.update({"summary": str(summary)})
        updated_request.update(
            {
                "anime_name": anime_name,
                "gogoanime_id": anime_id,
                "summary": str(summary),
            }
        )
        form = AddAnime(updated_request)
        if form.is_valid():
            form.save()
            messages.success(request, "success.")
        else:
            messages.error(request, form.errors)
    context = {"form": AddAnime}
    template_name = "add_anime.html"
    return render(request, template_name, context)


def all_anime(request):
    all_anime = Anime_All.objects.all()
    context = {"all_anime": all_anime}
    template_name = "all_anime.html"
    return render(request, template_name, context)


def anime_info(request, gogoanime_url):
    anime_info = Anime_All.objects.get(gogoanime_url=gogoanime_url)
    context = {"anime_info": anime_info}
    template_name = "anime_info.html"
    return render(request, template_name, context)
    pass


def download_all_eps(request):
    if request.method == "POST":
        email = request.POST.get("AnimeUrl")
        print(email)
        return HttpResponse(
            "Download Added!\nhttp://192.168.1.10:8600/"
        )  # Sending an success response
    else:
        return HttpResponse("Some Error!!")
    # return redirect(AllAnimeInfo)
