from django.db import models

# Create your models here.


class Study(models.Model):
    STATUS_CHOICE = (
        ('h', 'Hide'),
        ('o', 'Open'),
    )
    title = models.CharField(max_length=200, verbose_name='제목', help_text='제목을 입력하세요')
    writer = models.CharField(max_length=100, verbose_name='글쓴이')
    book = models.CharField(max_length=50)
    tags = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)
    tag_set = models.ManyToManyField('Tag', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    study = models.ForeignKey(Study)
    writer = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


