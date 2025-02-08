from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Child(models.Model):
    b: int = models.IntegerField()

    def __init__(self, b, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b=b


    def __str__(self):
        return f'Child(b={self.b})'

class Child2(models.Model):
    b: int = models.IntegerField()

    def __init__(self, b, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b=b


    def __str__(self):
        return f'Child2(b={self.b})'

class Parent(models.Model):
    title = models.CharField(max_length=100)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)

    def __init__(self, title, child, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.child = child

    def __str__(self):
        return f'Parent(title={self.title}, child={self.child})'