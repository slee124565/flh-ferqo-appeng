
from django.conf.urls import url

from .apis import DemoMessagesAPI

urlpatterns = [

    # == backend api for admin start ==
    url(r'^notes$', DemoMessagesAPI.as_view()),

]

