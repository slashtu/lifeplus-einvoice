from django.conf.urls import patterns, url

from einvoice import views

urlpatterns = patterns('',
    # ex: /polls/
        url(r'^$', views.index, name='index'),
        url(r'^forms/', views.forms, name='forms'),
        url(r'^tables/', views.tables, name='tables'),
        url(r'^terminal/add', views.addTerminal, name='addTerminal'),
        url(r'^group1/add', views.addGroup1, name='addGroup1'),
        url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'einvoice/login.html'}),
        url(r'^logout/', views.logout_action, name='logout'),
#        url(r'^fb/', views.fb, name='fb'),
        # ex: /polls/5/
#        url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
#        # ex: /polls/5/results/
#        url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
#        # ex: /polls/5/vote/
#        url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)