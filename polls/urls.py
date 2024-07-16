from django.urls import include, path

from .apiviews import ChoiceList, CreateVote, PollDetail, PollList, UserCreate

# from .views import polls_list, polls_detail

# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail")
# ]



urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    # path("vote/", CreateVote.as_view(), name="create_vote"),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),

]
