from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import MyUser, Coord, Level, Images, Pereval
from .serializers import CoordSerializer, UserSerializer, LevelSerializer, ImagesSerializer, PerevalSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    @action(detail=False, methods=['post'], url_path='submitData')
    def submitData(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(status='new')
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data,
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Bad Request',
            'id': None,
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != 'new':
            return Response({'state': '0', 'message': 'Можно редактировать только записи со статусом "new"'})

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'state': '1', 'message': 'Успешно удалось отредактировать запись в базе данных'})

    def get_queryset(self):
        queryset = Pereval.objects.all()
        user = self.request.query_params.get('user__email', None)
        if user is not None:
            queryset = queryset.filter(user__email=user)
        return queryset
