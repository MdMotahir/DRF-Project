from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.

class File(models.Model):
    TYPES=[('Documents','Documents'), ('Video','Video'), ('Image','Image'), ('Song','Song'), ('Others', 'Others')]
    name=models.CharField(max_length=100)
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    type=models.CharField(choices=TYPES, max_length=15,default='Others')
    file=models.FileField(upload_to='storage/',blank=True)
    slug=models.SlugField(unique=True,blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural='Files'