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
    user_img = models.ImageField(default="avatar_3.png", blank=True)
    # user_img = models.ImageField(upload_to="users/", default="users/avatar_1.png")

    class Meta:
        ordering = ["user_name"]

    def __repr__(self):
        return f"<User(user_name={self.user_name!r})>"

    def __str__(self):
        return self.user_name
