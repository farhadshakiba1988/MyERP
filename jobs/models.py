from django.db import models

STATUS = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
)

JOB_TITLE = (
    ('1', 'اپراتور'),
    ('2', 'انتظامات'),
    ('3', 'برنامه نویس'),
    ('4', 'تحلیلگر کسب و کار'),
    ('5', 'توسعه دهنده نرم افزار'),
    ('6', 'توسعه دهنده وب'),
    ('7', 'تکنسین شبکه'),
    ('8', 'تکنسین فنی'),
    ('9', 'خیاط'),
    ('10', 'دستیار اجرائی مدیر عامل'),
    ('11', 'رئیس امور فروشگاهها'),
    ('12', 'رئیس تولید'),
    ('13', 'سرپرست آزمایشگاه'),
    ('14', 'طراح لباس'),
    ('15', 'فروشنده'),

)

DEPART_TITLE = (
    ('1', 'کارخانه'),
    ('2', 'دفتر مرکزی'),
    ('3', 'فروشگاه'),

)
LEVEL_TITLE = (
    ('1', 'کارشناس'),
    ('2', 'کارمند'),
    ('3', 'مدیر'),
    ('4', 'سرپرست'),

)


# فرصت های شعلی موجود در سیستم
class JobOffers(models.Model):
    department = models.CharField(choices=DEPART_TITLE, max_length=20, default='')
    job_title = models.CharField(choices=JOB_TITLE, max_length=20, default='')
    organization_level = models.CharField(choices=LEVEL_TITLE, max_length=20, default='')
    workplace = models.CharField(max_length=120)
    descriptions = models.TextField()
    skills_required = models.CharField(max_length=120)
    experience = models.CharField(max_length=20)
    education = models.CharField(max_length=120)
    salary = models.CharField(max_length=100)
    release_time = models.CharField(max_length=120)
    show_salary = models.BooleanField(default=False)
    creation_date = models.DateTimeField()
    operation = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS, max_length=10, default='InActive')

    def __str__(self):
        """
            1. بازگرداندن نام بر اساس عنوان شغلی
        """
        return self.job_title