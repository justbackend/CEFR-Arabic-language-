from django.db import transaction
from django.http import FileResponse
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from pathlib import Path
import zipfile
from django.core.files.storage import default_storage
from django.views import View
from django.http import JsonResponse


class Part1Api(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Part1Serializer

    def get(self, request):
        part1 = Part1.objects.filter().order_by("?")[:5]
        serializer = Part1Serializer(part1, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Part2Api(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Part2Serializer

    def get(self, request):
        part2 = Part2.objects.filter().order_by("?").first()
        serializer = Part2Serializer(part2)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Part3Api(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Part3Serializer

    def get(self, request):
        part3 = Part3.objects.filter().order_by('?').first()
        serializer = Part3Serializer(part3)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Settings(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TimeSettingsSerializer

    def get(self, request):
        model = Time_Settings.objects.filter(is_active=True).last()
        serializer = TimeSettingsSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckSubscription(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = Subscription.objects.get(user=request.user)
            if user.is_active():
                return Response({"status": "True"}, status=status.HTTP_200_OK)
            return Response({"status": "False"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "False"}, status=status.HTTP_200_OK)


class AudioApi(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AudioSerializer

    @transaction.atomic()
    def post(self, request):
        serializer = AudioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data['status'] == "False":
                return Response({"message": "Created successfully"}, status=status.HTTP_201_CREATED)
            current_user = request.data['id_code']
            audios = DoNotEnter.objects.filter(id_code=current_user)
            user = TestTaker.objects.get(id_code=current_user)
            zip_file_name = f"{user.name}_{user.surname}_{user.id_code}.zip"
            zip_file_path = Path(settings.MEDIA_ROOT / "exam") / zip_file_name
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                for file in audios:
                    zipf.write(file.audio.path, arcname=file.audio.name)
            DoNotEnter.objects.filter(id_code=current_user).delete()
            return Response({"message": "All audios are ready for download"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestTakerApi(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TestTakerSerializer

    def post(self, request):
        serializer = TestTakerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDownloadView(View):
    permission_classes = [IsAuthenticated]

    @transaction.atomic()
    def get(self, request, pk):
        user = TestTaker.objects.get(id_code=pk)
        file_name = f"{user.name}_{user.surname}_{user.id_code}.zip"
        download_name = f"{user.name}_{user.surname}_{user.middle_name}.zip"
        file_path = Path(settings.MEDIA_ROOT / "exam") / file_name
        try:
            response = FileResponse(open(file_path, 'rb'))
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(download_name)
            return response
        except FileNotFoundError:
            return JsonResponse({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'error': f"An error occurred: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CleanTrash(View):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = TestTaker.objects.get(id_code=pk)
        file_name = f"{user.name}_{user.surname}_{user.id_code}.zip"
        file_path = Path(settings.MEDIA_ROOT / "exam") / file_name
        default_storage.delete(file_path)
        return JsonResponse({"message": "Deleted Successfullly"})


class ShartAudio(AudioApi):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        model = JuzAudio.objects.all().first()
        serializer = JuzAudioSerializer(model)
        return Response(serializer.data, status=status.HTTP_200_OK)
