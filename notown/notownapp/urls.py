from django.conf.urls import url

from . import views
from notownapp.views import *

urlpatterns = [ url(r'^$' , views.index, name='index'),
                url(r'^musicians/$',MusiciansList.as_view(),name='musicians_list'),
                url(r'^musiciansnew/$',MusiciansCreate.as_view(),name='musicians_new'),
                url(r'^musiciansedit/(?P<pk>\d+)$',MusiciansUpdate.as_view(),name='musicians_edit'),
                url(r'^musiciansdelete/(?P<pk>\d+)$',MusiciansDelete.as_view(),name='musicians_delete'),
                url(r'^plays/$',PlaysList.as_view(),name='plays_list'),
                url(r'^playsnew/$',PlaysCreate.as_view(),name='plays_new'),
                url(r'^playsedit/(?P<pk>\d+P\d+)$',PlaysUpdate.as_view(),name='plays_edit'),
                url(r'^plays/(?P<pk>\d+P\d+)$',PlaysDelete.as_view(),name='plays_delete'),
                url(r'^albumproducerslist/$',Album_ProducerList.as_view(),name="album_producers_list"),
                url(r'^albumproducersnew/$',Album_ProducerCreate.as_view(),name='album_producers_new'),
                url(r'^albumproducersedit/(?P<pk>\d+)$',Album_ProducerUpdate.as_view(),name='album_producers_edit'),
                url(r'^albumproducersdelete/(?P<pk>\d+)$',Album_ProducerDelete.as_view(),name='album_producers_delete'),
                url(r'^instruments/$',InstrumentsList.as_view(),name='instruments_list'),
                url(r'^instrumentsnew/$',InstrumentsCreate.as_view(),name='instruments_new'),
                url(r'^instrumentsedit/(?P<pk>\d+)$',InstrumentsUpdate.as_view(),name='instruments_edit'),
                url(r'^instrumentsdelete/(?P<pk>\d+)$',InstrumentsDelete.as_view(),name='instruments_delete'),
                url(r'^songappears/$',SongAppearsList.as_view(),name='songappears_list'),
                url(r'^songappearsnew/$',SongAppearsCreate.as_view(),name='songappears_new'),
                url(r'^songappearsedit/(?P<pk>\d+)$',SongAppearsUpdate.as_view(),name='songappears_edit'),
                url(r'^songappearsdelete/(?P<pk>\d+)$',SongAppearsDelete.as_view(),name='songappears_delete'),

               ]

#url(r'^form_test/$', views.form_test,name='form_test')
