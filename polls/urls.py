from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .apiviews import (ChoiceList, CreateVote, LoginView, PollDetail, PollList,
                       PollViewSet, UserCreate)

# from .views import polls_list, polls_detail

# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail")
# ]


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')



urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    # path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]

urlpatterns += router.urls
