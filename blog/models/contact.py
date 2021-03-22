from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)


    class Meta:
        db_table = "contact"
        verbose_name = "Contact"

    def __str__(self) -> str:
        return self.email