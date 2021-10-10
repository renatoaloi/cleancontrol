from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView

@login_required
def x(request):
    # if request.user.is_autenticated:
    if request.method == 'GET':
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False, "msg": "Metodo não permitido"})
    #return JsonResponse({"ok": False, "msg": "Usuário não autenticado"})


class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, format=None):
        if request.user.is_staff:
            return Response({'ok':True})
        return Response({'ok':False, 'error': 'Unauthorized'})
