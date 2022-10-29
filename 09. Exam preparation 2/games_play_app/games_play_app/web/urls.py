from django.urls import path, include

from games_play_app.web.views import index, dashboard, \
    edit_game, create_game, delete_game, details_game, \
    delete_profile, details_profile, edit_profile, create_profile

'''

•	http://localhost:8000/profile/create - create profile page

•	http://localhost:8000/game/create/ - create game page
•	http://localhost:8000/game/details/<id>/ - details game page
•	http://localhost:8000/game/edit/<id>/ - edit game page
•	http://localhost:8000/game/delete/<id>/ - delete game page
•	http://localhost:8000/profile/details/ - details profile page
•	http://localhost:8000/profile/edit/ - edit profile page
•	http://localhost:8000/profile/delete/ - delete profile page
'''

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard page'),
    path('game/', include([
        path('create/', create_game, name='create game'),
        path('details/<int:pk>/', details_game, name='details game'),
        path('edit/<int:pk>/', edit_game, name='edit game'),
        path('delete/<int:pk>/', delete_game, name='delete game'),
    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)