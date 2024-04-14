from django.db import models
from django.contrib.auth.models import User
#장고에서 user모델을 제공해줌

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nickname = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to='profile/')
    #null=True가 안되어있을 때 오류가 나는 것이 많아서 실습을 진행하기 위해 넣어준것 뿐임
    #실제 프로젝트 때는 null을 남발하는 것은 좋지 않음 

class Meta:
    db_table = 'profile' 
    #메타 클래스는 장고가 알아서 생성해주는 db인데 이름이 지맘대로 설정됨 
    #따라서 profile이라는 이름으로 설정해줘라 라고 지정해준것


def _str_(self):
    return self.nickname
#출력시켰을 때 nickname이 return 되도록 해줌