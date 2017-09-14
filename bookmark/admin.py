from django.contrib import admin
from .models import Bookmark    # . <= 현재 폴더에서 models 를 가져오겠다
# Register your models here.

admin.site.register(Bookmark)