from django.conf.urls import url, include  

urlpatterns = [
    url(r'^', include('apps.book_authors.urls')),
    url(r'^', include('apps.dojo_ninjas_app.urls')),
]
