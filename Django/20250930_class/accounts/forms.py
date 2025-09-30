from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# UserCreationForm
# --> model = 장고의 기본 auth model
# --> 우리는 그걸 accounts.User 로 바꿔주어야 함
class SignupForm(UserCreationForm):
    class Meta:
        # 현재 프로젝트에 설정된 기본 유저 모델을 가져온다
        model = get_user_model()
        fields = ('username', 
                  'password1', 
                  'password2',
                  'nickname',
                  )

