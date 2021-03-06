from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

dept_patterns= patterns('',
    url(r'^$','web.views.dept',name='departments'),
    url(r'^aeie/$','web.views.aeie',name='aeie'),
    url(r'^bme/$','web.views.bme',name='bme'),
    url(r'^ce/$','web.views.ce',name='ce'),
    url(r'^cse/$','web.views.cse',name='cse'),
    url(r'^ee/$','web.views.ee',name='ee'),
    url(r'^ece/$','web.views.ece',name='ece'),
    url(r'^it/$','web.views.it',name='it'),
    url(r'^me/$','web.views.me',name='me'),
    url(r'^bba/$','web.views.bba',name='bba'),
    url(r'^mba/$','web.views.mba',name='mba'),
     )

'''user_patterns= patterns('',
    url(r'^(\d+)/','web.views.home',name='home'),
    url(r'^(\d+)/files/','web.views.fileupload',name='files'),
    url(r'^(\d+)/search/','web.views.search',name='search'),
   )'''



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nsecedu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','web.views.index',name='index'),
    url(r'^dirdesk/$','web.views.dirdesk',name='dirdesk'),
    url(r'^dept/',include(dept_patterns)),
    url(r'^placements/$','web.views.placements',name='placements'),
    url(r'^faculty/$','web.views.facst',name='faculty'),
    url(r'^campusmap/$','web.views.campusmap',name='campusmap'),
    url(r'^map/$','web.views.map',name='map'),
    url(r'^notice/$','web.views.notice',name='notice'),
    url(r'^login/$','web.views.log',name='login'),
    url(r'^home/(\d+)/$','web.views.home',name='home'),
    url(r'^files/$','web.views.fileupload',name='files'),
    url(r'^logout/$','web.views.logout_',name='logout'),
    url(r'^avenir/$','web.views.avenir',name='avenir'),
    url(r'^avenir_images/$','web.views.avenir_images',name='avenir_images'),
    url(r'^phoenix/$','web.views.phoenix',name='phoenix'),
    url(r'^nixal/$','web.views.nixal',name='nixal'),
    url(r'^nixal_images/$','web.views.nixal_images',name='nixal_images'),
    url(r'^password_change/$','django.contrib.auth.views.password_change',{'template_name':'web/password_change.html'},name='password_change'),
    url(r'^password_change_done/$','django.contrib.auth.views.password_change_done',{'template_name':'web/password_change_done.html'},name='password_change_done'),
    url(r'^password_reset/$','django.contrib.auth.views.password_reset',{'template_name':'web/resetpass.html',},name='password_reset',),
    url(r'^password_reset_done/$','django.contrib.auth.views.password_reset_done',{'template_name':'web/resetdone.html',},name='password_reset_done',),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm',{'template_name':'web/resetpassform.html',},name='password_reset_confirm',),
    url(r'^password_reset_complete/$','django.contrib.auth.views.password_reset_complete',{'template_name':'web/passwordresetcomplete.html',},name='password_reset_complete'),
    url(r'^search/$','web.views.search',name='search'),
    url(r'^contact/$','web.views.contact',name='contact'),
    url(r'profiles/(\d+)/$','web.views.profiles',name='profiles'),
    url(r'post/$','web.views.post',name='post'),
    url(r'remove_post/(\d)+/$','web.views.remove_post',name='remove_post'),
)+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
