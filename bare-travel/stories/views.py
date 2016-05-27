from django.db.models import Q

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Story
from .pagination import StoryPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import StoryCreateUpdateSerializer, StoryDetailSerializer, StoryListSerializer


class StoryCreateView(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StoryDetailView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]


class StoryUpdateView(RetrieveUpdateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class StoryDeleteView(DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]


class StoryListView(ListAPIView):
    serializer_class = StoryListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title', 'content', 'user__first_name']
    pagination_class = StoryPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Story.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list
