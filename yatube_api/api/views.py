from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """
    Получение списка всех публикаций.
    При указании параметров limit и offset выдача работает с пагинацией.
    Добавление новой публикации в коллекцию публикаций.
    Получение публикации по id.
    Обновление/частичное обновление/удаление публикации по id.
    Обновить/удалить публикацию может только автор публикации.
    Анонимные запросы, кроме запросов на получение публикаций, запрещены.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Получение всех комментариев к публикации.
    Добавление нового комментария к публикации.
    Получение комментария к публикации по id.
    Обновление/частичное обновление/удаление комментария к публикации по id.
    Обновить/удалить комментарий может только автор комментария.
    Анонимные запросы, кроме запросов на получение комментариев, запрещены.
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comment.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Получение списка доступных сообществ или информации о сообществе по id.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """
    Получение всех подписок пользователя, сделавшего запрос.
    Подписка пользователя, сделавшего запрос,
    на пользователя, переданного в теле запроса.
    Анонимные запросы запрещены.
    """
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.following.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
