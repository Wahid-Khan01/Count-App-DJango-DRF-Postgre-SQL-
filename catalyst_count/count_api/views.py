import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from uploader.models import File


class FilterCountView(APIView):
    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name', None)
        industry = request.query_params.get('industry', None)
        locality = request.query_params.get('locality', None)
        country = request.query_params.get('country', None)
        year_founded = request.query_params.get('year_founded', None)

        filters = {}


        # validation k liye regex and isinstance ka use kiya gaya taakey str input pe exception handle kar sake
        def is_valid_string(value):
            if not isinstance(value, str):
                return False
            if re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
                return False
            return True
        
        # filter karne k liye orm lookup icontain ka use kiya gaya case insensitive k sath keyword contain hota hai ya nahi check karta hai
        if name:
            if not is_valid_string(name):
                return Response({'error':'Invalid Characters in name'}, status=status.HTTP_400_BAD_REQUEST)
            filters['name__icontains'] = name
        if industry:
            if not is_valid_string(industry):
                return Response({'error':'Invalid Characters in industry'}, status=status.HTTP_400_BAD_REQUEST)
            filters['industry__icontains'] = industry
        if locality:
            if not is_valid_string(locality):
                return Response({'error':'Invalid Characters in locality'}, status=status.HTTP_400_BAD_REQUEST)
            filters['locality__icontains'] = locality
        if country:
            if not is_valid_string(country):
                return Response({'error':'Invalid Characters in country'}, status=status.HTTP_400_BAD_REQUEST)
            filters['country__icontains'] = country
        if name:
            if not is_valid_string(name):
                return Response({'error':'Invalid Characters in name'}, status=status.HTTP_400_BAD_REQUEST)
            filters['name__icontains'] = name

        # int input pe exception handle karne k liye hai
        if year_founded:
            try:
                year_founded = int(year_founded)
                if year_founded < 0:
                    raise ValueError("Year cannot be negative")
                filters['year_founded'] = year_founded
            except ValueError:
                return Response({'error': 'year_founded must be a positive integer'}, status=status.HTTP_400_BAD_REQUEST)
            
        # orm aggregate ka use kiya gaya jissey count milega or usko template pe le jaa sakte hai
        try:
            filtered_count = File.objects.filter(**filters).count()
            return Response({'count': filtered_count}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)