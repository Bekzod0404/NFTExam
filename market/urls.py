from django.urls import path

from market.views import HomeView, AuthorDetailView, ProductListView, AuthorListView, ProductCreateView, \
    ProfileView, SignUpView, SignInView, ProductDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('author/', AuthorDetailView.as_view(), name='author-detail'),
    path('product_list/', ProductListView.as_view(), name='product-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('product_create/', ProductCreateView.as_view(), name='product-create'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('detail/', ProductDetailView.as_view(), name='detail'),
]
