from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('library/<int:id>/', views.LibraryGetPostView.as_view()),
    path('library/', views.LibraryPutView.as_view()),
    path('library/<int:library_id>/books/', views.LibraryFilterView.as_view()),
    path('book/<int:id>', views.BookGetPostView.as_view()),
    path('book/', views.BookPutView.as_view()),
    path('book/search', views.BookSearchView.as_view()),
    path('author/<int:id>', views.AuthorGetPostView.as_view()),
    path('author/', views.AuthorPutView.as_view()),
    path('leads/', views.LeadPostView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]