from django.urls import path
from .views import (
    index,
    addUser,
    authUser,
    addWebsitePassword,
    showStoredPasswords,
    # detail,
    # results,
)

urlpatterns=[
    path('', index, name='index'),
    path('user/',addUser,name='user'),
    path('user/auth/',authUser,name='authUser'),
    path('sites',addWebsitePassword,name='addWebsitePassword'),
    path('sites/list/',showStoredPasswords,name='showStoredPasswords'),
    # ex: /polls/5/
    # path('<int:question_id>/', detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', vote, name='vote'),
]