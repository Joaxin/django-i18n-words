from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_('amor/'), views.index,name='index'),
]