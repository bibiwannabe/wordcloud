from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from searchserver.service import search


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        post = request.POST
        keyword = post.get('keyword', '')
        print(keyword)
        image = search(keyword)
        return HttpResponse(image, content_type="image/png")

