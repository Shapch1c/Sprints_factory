from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
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
    def submit_data(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(status='new')
            return Response({
                'status': status.HTTP_200_OK,
                'message': None,
                'id': serializer.data['id'],
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Bad Request',
            'id': None,
        }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='submitData')
    def get_one_pereval(self, request, pk=None):
        pereval = self.get_object()
        serializer = PerevalSerializer(pereval)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='submitData')
    def update_pereval(self, request, pk=None):
        instance = self.get_object()

        if instance.status != 'new':
            return Response(
                {'state': 0, 'message': 'Запись нельзя редактировать, так как она не в статусе new'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Проверка на попытку изменить запрещенные поля
        user_data = request.data.get('user', {})
        forbidden_fields = ['email', 'phone', 'fam', 'name', 'otc']
        if any(field in user_data for field in forbidden_fields):
            return Response(
                {'state': 0, 'message': 'Редактирование ФИО, почты и телефона запрещено'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response({'state': 1, 'message': 'Запись успешно обновлена'})

    @action(detail=False, methods=['get'], url_path='submitData')
    def filter_by_email(self, request):
        email = request.query_params.get('user__email')
        if not email:
            return Response(
                {'message': 'Необходимо указать email'},
                status=status.HTTP_400_BAD_REQUEST
            )

        perevals = self.queryset.filter(user__email=email)
        serializer = PerevalSerializer(perevals, many=True)
        return Response(serializer.data)