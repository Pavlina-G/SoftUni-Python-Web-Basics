'''
3. Routes
        •	http://localhost:8000/ - index page
        •	http://localhost:8000/profile/create - profile create page
        •	http://localhost:8000/catalogue/ - catalogue page
        •	http://localhost:8000/car/create/ - car create page
        •	http://localhost:8000/car/<car-id>/details/ - car details page
        •	http://localhost:8000/car/<car-id>/edit/ - car edit page
        •	http://localhost:8000/car/<car-id>/delete/ - car delete page
        •	http://localhost:8000/profile/details/ - profile details page
        •	http://localhost:8000/profile/edit/ - profile edit page
        •	http://localhost:8000/profile/delete/ - profile delete page

'''
from django.urls import path, include

from car_collection_app.car_collection.views import index, catalogue, \
    create_profile, details_profile, edit_profile, delete_profile, \
    create_car, details_car, edit_car, delete_car

urlpatterns = (
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('car-<int:pk>/', include([
            path('details/', details_car, name='details car'),
            path('edit/', edit_car, name='edit car'),
            path('delete/', delete_car, name='delete car'),
        ])),
    ])),
)
