from django.db import models

# Create your models here.


class User(models.Model):
    """User table"""

    user_name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        unique=True,
        verbose_name="User display name",
    )

    class Meta:
        ordering = ["user_name"]

    def __repr__(self):
        return f"<User(user_name={self.user_name!r})>"

    def __str__(self):
        return self.user_name
