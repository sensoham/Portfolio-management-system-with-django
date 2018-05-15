from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
# we use the inbuilt generic view because it saves us a lot of trouble
from investshow.models import Post

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date"), template_name="investshow/investshow.html")),
				url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="investshow/post.html"))] 


