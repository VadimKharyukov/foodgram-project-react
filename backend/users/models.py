from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(verbose_name='Имя пользователя',
                                unique=True,
                                max_length=150)
    email = models.EmailField(verbose_name='Почтовый ящик',
                              unique=True,
                              max_length=254)
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        ordering = ('-id', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    user = models.ForeignKey(CustomUser,
                             related_name='follower',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser,
                               related_name='following',
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(fields=('user', 'author'),
                                    name='unique_list'),
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')), name='author'
            )
        ]
