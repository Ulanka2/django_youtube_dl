from youtube_dl import YoutubeDL
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import View, TemplateView


class MainPageView(TemplateView):
    template_name = 'home.html'

class DownloadView(View):
    def post(self, request):
        if request.method == 'POST':
            video_url = request.POST['url']
            if video_url:
                download_option = {
                    'outtmp1': '/Users/a1/Desktop',
                }
                with YoutubeDL(download_option ) as ydl:
                    ydl.download([video_url])
                    messages.success(request, 'vashe video dowlad')
                    return redirect('home')
            else:
                messages.warning(request, "vedite url")
                redirect('home')
        return redirect('home')

