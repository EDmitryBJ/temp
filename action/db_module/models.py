# todo установить оптимальные max_digits и decimal_places для decimal полей
from ntpath import realpath
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

TYPE_OPTIONS = {
    ('ALL', 'ALL'),
    ('MUSIC', 'MUSIC'),
    ('MEETING', 'MEETING'),
    ('PERFORMANCE', 'PERFORMANCE'),
    ('OTHER', 'OTHER'),
    ('FESTIVAL', 'FESTIVAL'),
    ('EXHIBITION', 'EXHIBITION'),
}


# Create your models here.
class Contacts(models.Model):
    # Контакты пользователя/контакты события
    vk = models.CharField(null=True, max_length=250)
    telegram = models.CharField(null=True, max_length=250)
    instagram = models.CharField(null=True, max_length=250)
    web_site = models.URLField(null=True)
    email = models.EmailField(null=True)


class FilterSettings(models.Model):
    # user_profile = models.OneToOneField(UserProfile, on_delete=CASCADE)
    type = models.CharField(choices=TYPE_OPTIONS, max_length=15, default='ALL')
    date = models.DateField(auto_now_add=True)
    subscription = models.BooleanField(default=False)
    latitude = models.DecimalField(default=0.0, decimal_places=6, max_digits=12)
    longitude = models.DecimalField(default=0.0, decimal_places=6, max_digits=12)


def upload_to_by_id(instance, filename):
    return '/'.join(['users', instance.user.id, filename])


# todo добавить обработчики при создании и удалении для всех ссылочных полей со свойством null = True
# todo использовать User как объект привязки
# todo отмечать как удалённые все связанные с автоом события при удалении автора
# todo добавлять UserInfo при создании автора
# todo создавать сложные связанные объекты при создании UserInfo
class UserProfile(models.Model):
    # Надстройка над моделью User, содержит дополнительную информацию
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    about = models.TextField(default='')
    contacts = models.OneToOneField(Contacts, on_delete=models.DO_NOTHING, related_name='userprofile_contacts')
    filter_settings = models.OneToOneField(FilterSettings, on_delete=models.DO_NOTHING, related_name='userprofile_filters')
    black_list = models.ManyToManyField(User, symmetrical=False, related_name='blacklist', blank=True)
    subscriptions = models.ManyToManyField(User, symmetrical=False, related_name='subscriptions', blank=True)
    subscribers_num = models.IntegerField(default=0)
    image = models.ImageField(default='/default_icon.png', upload_to=upload_to_by_id)

    def delete(self, *args, **kwargs):
        self.filter_settings.delete()
        self.contacts.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    def user_id(self):
        # получает id соответствующей модели User, нужен только для сокращения кода. Использовать не обязательно.
        return self.user.id

    def get_user_name(self):
        return self.user.username

    def __str__(self) -> str:
        return self.get_user_name()

    def get_info_by_user_id(target_id):
        '''Возвращает экземпляр UserInfo по id User из Auth'''
        try:
            user_info = UserProfile.objects.get(user_id=target_id)
        except (UserProfile.DoesNotExist, User.DoesNotExist):
            return None
        return user_info


# todo выбирать изображение по умолчанию в зависимости от категории места
class Event(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=250)
    image = models.ImageField(default='/test_default_place.png', upload_to=upload_to_by_id)
    about = models.TextField(default='')
    contacts = models.OneToOneField(Contacts, on_delete=models.DO_NOTHING, related_name='event_contacts')
    # latitude = models.DecimalField(default=0.0, decimal_places=6, max_digits=12)
    # longitude = models.DecimalField(default=0.0, decimal_places=6, max_digits=12)
    # date = models.DateField(null=False)
    # timetable = models.TextField(default='')
    # is_private = models.BooleanField(default=False)
    # invited_users = models.ManyToManyField(User, symmetrical=True, blank=True)
    # is_deleted = models.BooleanField(default=False)
    # type = models.CharField(choices=TYPE_OPTIONS, max_length=15, default='OTHER')

    def delete(self, *args, **kwargs):
        self.contacts.delete()
        return super(self.__class__, self).delete(*args, **kwargs)


class EventPlan(models.Model):
    events = models.ManyToManyField(Event)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=50)
    is_shareable = models.BooleanField(default=False)


class ShareableEventPlan(models.Model):
    parent_plan = models.OneToOneField(EventPlan, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    redactors = models.ManyToManyField(User, related_name='redactors')


class EventPositionInPlan(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    plan = models.ForeignKey(EventPlan, on_delete=models.CASCADE)
    position = models.IntegerField()


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_name = models.CharField(max_length=50, default='')
    users = models.ManyToManyField(User, related_name='users')
    admins = models.ManyToManyField(User, related_name='admins')


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message_type = models.CharField(max_length=30, default='')
    text = models.TextField(null=False)
