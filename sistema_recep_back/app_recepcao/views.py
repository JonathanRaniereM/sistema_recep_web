from django.shortcuts import render

from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class LoginAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Login bem-sucedido!', 'token': token, 'username': user.username})
        else:
            return JsonResponse({'status': 'error', 'message': 'Erro: Usuário ou senha incorretos!'}, status=401)


class LogoutAPI(APIView):
    
    def post(self, request, *args, **kwargs):
        # Aqui, podemos invalidar o token de alguma forma ou apenas 
        # retornar uma resposta de sucesso. Porque, na prática, a 
        # invalidação do token será feita no lado do cliente removendo 
        # o token do armazenamento.

        # Por simplicidade, apenas retornaremos uma resposta de sucesso
        return Response({'status': 'success', 'message': 'Logout bem-sucedido!'}, status=status.HTTP_200_OK)