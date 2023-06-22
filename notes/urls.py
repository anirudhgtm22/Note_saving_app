from django.urls import path
from . import views
from .views import UserRegistrationAPIView, UserLoginAPIView ,NoteListCreateAPIView, NoteDetailAPIView, SharedNoteListCreateAPIView

urlpatterns = [
    path('', views.home, name='homepage'),
    path('create-note/', views.create_note, name='create_note'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search_notes'),
    path('notes/', views.notes, name='notes'),
    path('api/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('api/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('api/notes/', NoteListCreateAPIView.as_view(), name='note-list'),
    path('api/notes/<int:pk>/', NoteDetailAPIView.as_view(), name='note-detail'),
    path('api/shared-notes/', SharedNoteListCreateAPIView.as_view(), name='shared-note-list'),
]
