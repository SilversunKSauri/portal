from django.conf.urls import include, url, patterns

from designsafe.apps.api.notifications.views.api import ManageNotificationsView
from designsafe.apps.api.notifications.views.webhooks import JobsWebhookView, FilesWebhookView

urlpatterns = patterns('designsafe.apps.notifications.views.api',
    url(r'^$', ManageNotificationsView.as_view(), name='index'),
    url(r'^(?P<event_type>\w+)/?$', ManageNotificationsView.as_view(), 
                                        name='event_type_notifications'),
)

urlpatterns += patterns('designsafe.apps.notifications.views.webhooks',
    url(r'^wh/jobs/$', JobsWebhookView.as_view(), name='jobs_wh_handler'),
    url(r'^wh/files/$', FilesWebhookView.as_view(), name='files_wh_handler'),
)