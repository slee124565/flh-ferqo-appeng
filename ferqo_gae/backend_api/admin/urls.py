
from django.conf.urls import url

from .views import FirebaseDBReachabilityView

urlpatterns = [

    # == backend api for admin start ==
    url(r'^views/db_reachability/$', FirebaseDBReachabilityView.as_view(), name='db_reachability_view'),

]

