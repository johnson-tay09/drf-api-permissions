from rest_framework import generics

from .models import Entry
from .permissions import IsAuthorOrReadOnly
from .serializer import EntrySerializer


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer