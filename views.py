from django.shortcuts import render
from gpm.http.response import Response

def info(request):
    """
        @description:
    """
    res = Response(request=request)
    return res.success()