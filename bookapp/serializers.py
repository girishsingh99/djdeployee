from rest_framework.serializers import ModelSerializer
from .models import Book

class BookSerialization(ModelSerializer):

    class Meta:
        model = Book
        fields = '_all_'