from django.urls import path

from departments_app.departments.views import show_departments, show_department_details, show_not_found, \
    redirect_to_first_department

urlpatterns = (
    # /departments/
    path('', show_departments, name='show_departments'),

    # /departments/{department_id}/
    # path('<department_id>/', show_department_details, name='show department details with string'), # path: /departments/7/

    # /departments/int/{department_id}/
    path('by-id/<int:department_id>/', show_department_details, name='show department by id'), # path: /departments/by-id/8/, id: 8

    path('not-found/', show_not_found, name='not found'),

    path('redirect/', redirect_to_first_department, name='redirect demo'),
)

# paths = (
#     '',
#     '<department_id>/',
#     'int/<int:department_id>/',
# )
#
# urlpatterns = [path(url, sample_view) for url in paths]
#
# urlpatterns = ()
# urlpatterns += (path('', sample_view),)
# urlpatterns += (path('<department_id>/', sample_view),)
# urlpatterns += (path('int/<int:department_id>/', sample_view),)