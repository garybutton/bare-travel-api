from rest_framework.pagination import PageNumberPagination


class StoryPageNumberPagination(PageNumberPagination):
    page_size = 20
