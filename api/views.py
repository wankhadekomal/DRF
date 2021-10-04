from rest_framework import views,response , status
from . import serializers

class BlogAPIView(views.APIView):
    serializer_class=serializers.BlogAPIView
    def get(self,request):
        getList=[
            'this is HTTP GET method',
            'this is APIView'
        ]
        return response.Response({'data':getList})

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            title =serializer.validated_data.get('title')
            postList=[
                'this is HTTP POST method',
                'this is APIView',
                title
            ]
            return response.Response({'data':postList})    
        else:
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            title =serializer.validated_data.get('title')
            putList=[
                'this is HTTP PUT method',
                'this is APIView',
                title
            ]
            return response.Response({'data':putList})    
        else:
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    def patch(self,request):
        patchList=[
            'this is HTTP PATCH method',
            'this is APIView'
        ]
        return response.Response({'data':patchList})  

    def delete(self,request):
        test=False
        if test:
            deleteList=[
            'this is HTTP DELETE method',
            'this is APIView'
            ]
            return response.Response({'data':deleteList})
        else:
            return response.Response({'message':'Something went wrong !'} , status=status.HTTP_400_BAD_REQUEST)           
