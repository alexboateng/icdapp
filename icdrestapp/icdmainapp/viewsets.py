# from rest_framework import viewsets
# from . import models
# from . import serializers
# from .common.ResponseModelViewSet import ResponseModelViewSet

# class  ICDVersionViewset(ResponseModelViewSet):
#     queryset = models.ICDVersion.objects.all()
#     serializer_class = serializers.ICDVersionSerializer

    #list() retrive() create() update() destroy()

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import ICDVersion
from .models import ICDCode
from .serializers import ICDVersionSerializer
from .serializers import ICDCodeSerializer

@api_view(['GET', 'POST'])
def icdverion_list(request):
    response_format = {}
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = ICDVersion.objects.all()
        serializer = ICDVersionSerializer(snippets, many=True)
        response_format["status"] = 'success'
        response_format["data"] = serializer.data
        if not serializer.data:
            response_format["message"] = "List empty"
        return Response(response_format)

    elif request.method == 'POST':
        if ("version" in request.data):
            serializer = ICDVersionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_format["status"] = 'success'
                response_format["data"] = serializer.data
                return Response(response_format, status=status.HTTP_201_CREATED)
            response_format["status"] = 'error'
            response_format["errors"] = serializer.errors
            return Response(response_format, status=status.HTTP_400_BAD_REQUEST)
        else:
            response_format["status"] = 'error'
            response_format["message"] = 'Version is required'
            return Response(response_format, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def icdverion_detail(request, pk):
    response_format = {}
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = ICDVersion.objects.get(pk=pk)
    except ICDVersion.DoesNotExist:
        response_format["status"] = 'error'
        response_format["errors"] = 'Data Not found'
        return Response(response_format, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ICDVersionSerializer(snippet)
        response_format["status"] = 'success'
        response_format["data"] = serializer.data
        return Response(response_format)

    elif request.method == 'DELETE':
        snippet.delete()
        response_format["status"] = 'success'
        response_format["message"] = 'Deleted Succesfully'
        return Response(response_format)



# FOR ICD CODE
@api_view(['GET', 'POST'])
def icdcode_list(request, av):
    response_format = {}

    try:
        snippet = ICDVersion.objects.get(version=av)
    except ICDVersion.DoesNotExist:
        response_format["status"] = 'error'
        response_format["errors"] = 'ICD Code Version Not found'
        return Response(response_format, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # snippets = ICDCode.objects.filter(appVersion=av)

        snippets = ICDCode.objects.filter(appVersion=av).values().order_by('id') 

        page = request.GET.get('page')
        paginator = Paginator(snippets, 20)

        try:
            icdCodes = paginator.page(page)
        except PageNotAnInteger:
            icdCodes = paginator.page(1)
        except EmptyPage:
            icdCodes = paginator.page(paginator.num_pages)

        # serializer = ICDCodeSerializer(snippets, many=True)
        response_format["status"] = 'success'
        response_format["page"] = page or 1
        response_format["number_of_pages"] = paginator.num_pages
        response_format["data"] = list(icdCodes)
        if not icdCodes:
            response_format["message"] = "List empty"
        return Response(response_format)

    elif request.method == 'POST':
        if ("diagnosisCode" in request.data):
            diagnosisCode = request.data['diagnosisCode']
            try:
                snippet = ICDCode.objects.get(diagnosisCode=diagnosisCode, appVersion=av)
                response_format["status"] = 'error'
                response_format["errors"] = 'ICD Diagnoses code {dcode} available for ICD Version {appV}'.format(appV = av, dcode=diagnosisCode)
                return Response(response_format, status=status.HTTP_404_NOT_FOUND)
            except ICDCode.DoesNotExist:
                request.data["appVersion"] = av
                serializer = ICDCodeSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    response_format["status"] = 'success'
                    response_format["message"] = "Successfully added ICDCode"
                    response_format["data"] = serializer.data
                    return Response(response_format)
                response_format["status"] = 'error'
                response_format["errors"] = serializer.errors
                return Response(response_format, status=status.HTTP_400_BAD_REQUEST)
        else:
            response_format["status"] = 'error'
            response_format["message"] = 'Diagnoses code is required'
            return Response(response_format, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def icdcode_detail(request, av, pk):
    response_format = {}
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        snippet = ICDVersion.objects.get(version=av)
    except ICDVersion.DoesNotExist:
        response_format["status"] = 'error'
        response_format["errors"] = 'ICD Code Version Not found'
        return Response(response_format, status=status.HTTP_404_NOT_FOUND)

    try:
        snippet = ICDCode.objects.get(pk=pk, appVersion=av)
    except ICDCode.DoesNotExist:
        response_format["status"] = 'error'
        response_format["errors"] = 'ICD Data Not found fro ICD Version {appV}'.format(appV = av)
        return Response(response_format, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ICDCodeSerializer(snippet)
        response_format["status"] = 'success'
        response_format["data"] = serializer.data
        return Response(response_format)

    elif request.method == 'PUT':
        if ("diagnosisCode" in request.data):
            serializer = ICDCodeSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                response_format["status"] = 'success'
                response_format["message"] = "Successfully updated ICDCode"
                response_format["data"] = serializer.data
                return Response(response_format)
            response_format["status"] = 'error'
            response_format["errors"] = serializer.errors
            return Response(response_format, status=status.HTTP_400_BAD_REQUEST)
        else:
            response_format["status"] = 'error'
            response_format["message"] = 'Diagnoses code is required'
            return Response(response_format, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        response_format["status"] = 'success'
        response_format["message"] = 'Deleted ICD Code Succesfully'
        return Response(response_format)


# class ApiICDListView(ListAPIView):
#     queryset = ICDCode.objects.all()
#     # model = ICDCode
#     serializer_class = ICDCodeSerializer
#     pagination_class = PageNumberPagination

#     # def get_queryset(self, queryset):
#     #     appVersion = self.kwargs.get('av', None)
#     #     print("appVersionCode", appVersion)
#     #     if appVersion is not None:
#     #         queryset = queryset.filter(appVersion=appVersion)
#     #     return queryset

#     def filter_queryset(self, queryset, *args, **kwargs):
#         #  pk, *args, **kwargs):
#         appVersion = kwargs.get('appversion', None)
#         print("kwargs", kwargs)
#         print("args", args)

#         if appVersion is not None:
#             queryset = queryset.filter(appVersion=appVersion)
#         return queryset
