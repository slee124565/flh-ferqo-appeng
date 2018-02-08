
from django.conf.urls import url

from .apis import FlhHc2SceneControlAPI
from .apis import FlhHc2EchoAPI

urlpatterns = [

    # == backend api for admin start ==
    url(r'^i/sc$', FlhHc2SceneControlAPI.as_view(), 'services.hc2.scene_ctl'),

    url(r'^echo$', FlhHc2EchoAPI.as_view(), 'services.hc2.echo'),
]

