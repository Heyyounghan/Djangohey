from django.db import models
from django.conf import settings
from django.utils import timezone
#다른 파일에 있는 것을 추가하라는 의미.

class Post(models.Model): #모델을 정의하는 코드 Model = object 객체!
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #다른 모델에 대한 링크
    title= models.CharField(max_length=200) #글자수가 제한된 텍스트를 정의할때 사용
    text= models.TextField() #글자 수 제한 없는 긴 텍스트를 위한 속성
    created_date= models.DateTimeField( #날짜
            default=timezone.now)
    published_date= models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
