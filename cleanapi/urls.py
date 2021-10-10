from django.urls import path
from cleanapi.views import x, MyView

urlpatterns=[
    path('', x),
    path('x', MyView.as_view())
]