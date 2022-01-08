from django.contrib import admin
from .models import Contact
from .models import Destination
from .models import Newuser
from .models import Upload_book
# Register your models here.
admin.site.register(Contact)

admin.site.register(Destination)
admin.site.register(Newuser)
admin.site.register(Upload_book)