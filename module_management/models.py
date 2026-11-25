from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify

from course_management.models import Course

class Module(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="modules"
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    description = models.TextField(blank=True)

    order = models.PositiveIntegerField(
       
        help_text="Module sequence within the course",
        null= True
    )

   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):

# we take the module of whichever course is passed and take its last order and updates it by 1 to get the corct order        
        module_instance = Module.objects.filter(course=self.course).last()

        if module_instance:

            self.order = module_instance.order + 1
        else:
            self.order = 1

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        ordering = ["order"]

# unique together is used to make the course and order be in an order like c1 o1 and not c2 o3 it should be same
        unique_together = ["course", "order"]