from django.db import models

from django.utils.text import slugify

from accounts.models import User


class Course(models.Model):
    
    COURSE_CATEGORIES = [
        ("development", "Web Development"),
        ("data_science", "Data Science"),
        ("data_analytics", "Data Analytics"),
        ("ai_ml", "AI & Machine Learning"),
        ("programming", "Programming"),
        ("design", "UI/UX Design"),
        ("other", "Other"),
    ]

    COURSE_LEVELS = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]


    title = models.CharField(max_length=200)

# used to get a unique text instead of the id in urls so it'll be unpredictable
    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=COURSE_CATEGORIES
    )

    thumbnail = models.ImageField(
        upload_to="courses/thumbnails/",
        blank=True,
        null=True
    )

    trainer = models.ForeignKey(
       User,
        on_delete=models.CASCADE,
        related_name="created_courses"
    )

    level = models.CharField(
        max_length=20,
        choices=COURSE_LEVELS,
        default="beginner"
    )

    duration = models.PositiveIntegerField(
        help_text="Course duration in hours"
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]