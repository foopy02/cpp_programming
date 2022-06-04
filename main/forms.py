from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings 
from .models import Lesson
NUMBER_OF_LESSONS = 26
topics = {
    1:"Негіздер",
    2:'Бірінші C++ бағдарламасы',
    3:'Айнымалылар және калькулятор құру',
    4:'Шарттар және логикалық операциялар',
    5:'Сандардың генераторы және жолды манипуляциялау',
    6:'For, While, Do while циклдері',
    7:'Ерекшеліктер және анықтау қателері',
    8:'Деректер массивтері. Бір өлшемді және көп өлшемді',
    9:'Көрсеткіштер мен сілтемелер',
    10:'Динамикалық массив',
    11:'Таңбалар мен жолдар',
    12:'Деректер құрылымдары',
    13:'Сандар',
    14:'Файлдармен жұмыс',
    15:'C++ тіліндегі функциялар',
    16:'Функцияның шамадан тыс жүктелуі',
    17:'Математикалық амалдар',
    18:'(OOP-ке кіріспе) Кластар мен нысандар',
    19:'Конструкторлар мен деструкторлар',
    20:'Достық мүмкіндіктері',
    21:'Достық сабақтар',
    22:'Көрсеткіш this',
    23:'Класс мұрасы (OOP)',
    24:'Функция үлгілері (template)',
    25:'C++ тіліндегі класс үлгілері',
    26:'Қорытынды сабақ',
}

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-class'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        for i in range(1, NUMBER_OF_LESSONS + 1):
            lesson = Lesson(user=user,number=i,topic=topics[i])
            lesson.save()
        return user