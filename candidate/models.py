import os
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


def determine_upload_location(instance, filename):
    """
        تعیین میکنیم که پرونده ها در کجا بارگزاری شوند
        به عنوان مثال : کاربر مورد نظر
        نام پرونده: رزومه در حال بارگزاری
        و در نهایت مسیر بارگزاری رزومه
    """
    _, extension = os.path.splitext(filename)
    return os.path.join("resumes", instance.user.username + extension)


# کلاس افراد منتخب برای ارسال رزومه که مشخصات خود را وارد مینمایند
class Candidate(models.Model):
    LEVEL_CHOICES = (
        ("IN", "Intern"),
        ("NG", "New grad"),
        ("CL", "Career level"),
        ("SR", "Senior"),
        ("PR", "Principal"),
    )
    STATUS_CHOICES = (
        ("1", "دیپلم"),
        ("2", "فوق دیپلم"),
        ("3", "لیسانس"),
        ("4", "کارشناسی ارشد"),
        ("5", "دکترا"),
    )

    CHOICES_SEX = (
        ("1", "آقا"),
        ("2", "خانم"),
    )

    CHOICES_SKILLS = (
        ("JA", "Python"),
        ("PY", "Java"),
        ("HA", "Haskell"),
        ("C", "C"),
        ("JS", "Javascript (Node)"),
        ("PE", "Perl"),
        ("PH", "PHP"),
        ("CP", "C++"),
        ("RA", "Racket"),
        ("RU", "Ruby"),
        ("SC", "Scala"),
    )

    # از کلاس user پیشفرض  جنگو برای احراز هویت استفاده میکنیم
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES, blank=True, null=True)
    education = models.CharField(max_length=3, choices=STATUS_CHOICES, default="NEW")
    phone = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150)
    sex = models.CharField(max_length=2, choices=CHOICES_SEX, default="")
    email = models.CharField(max_length=150)
    skills = models.CharField(max_length=20, choices=CHOICES_SKILLS, default="")
    skills_offers = models.CharField(max_length=100)
    referrer = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField()
    resume = models.FileField(blank=True,
                              null=True,
                              upload_to=determine_upload_location,
                              validators=[FileExtensionValidator(['pdf', 'txt', 'doc', 'docx'])])
    resume_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name()

    def name(self):
        n = []
        if self.user.first_name: n.append(self.user.first_name)
        if self.user.last_name: n.append(self.user.last_name)
        return " ".join(n) if n else str(self.user)
