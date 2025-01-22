from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from todo_list.models import *
from todo_list.views import *

urlpatterns = patterns(
    'todo_list.views',
    (r'^set_done/(\d+)$', 'set_done'),
    (r'^set_open/(\d+)$', 'set_open'),
    (r'^drop/(\d+)$', 'drop'),
    (r'^create_task', 'create_task'),
    (r'^create_project', 'create_project'),
    (r'^login', 'login'),
    (r'^logout', 'logout'),
    (r'', 'main'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
