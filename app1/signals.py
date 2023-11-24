from pathlib import Path
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from .models import Subscription, Part1, Part3, Part2, JuzAudio, TestTaker, DoNotEnter
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from datetime import timedelta


@receiver(post_save, sender=User)
def subscription_add(sender, instance, created, **kwargs):
    if created:
        Subscription.objects.create(user=instance)


@receiver(pre_save, sender=Part1)
def delete_old_file(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Part1.objects.get(pk=instance.pk)
        if old_instance.audio != instance.audio:
            if bool(old_instance.audio):
                default_storage.delete(old_instance.audio.path)


@receiver(pre_delete, sender=Part1)
def delete_music_file(sender, instance, **kwargs):
    if instance.audio:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio.storage
        file_path = instance.audio.name
        print(file_path)
        storage.delete(file_path)


@receiver(pre_save, sender=Part2)
def delete_old_file(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Part2.objects.get(pk=instance.pk)
        if old_instance.audio != instance.audio:
            if bool(old_instance.audio):
                default_storage.delete(old_instance.audio.path)


@receiver(pre_delete, sender=Part2)
def delete_music_file(sender, instance, **kwargs):
    if instance.audio:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio.storage
        file_path = instance.audio.name
        storage.delete(file_path)


@receiver(pre_save, sender=Part3)
def delete_old_file(sender, instance, **kwargs):
    if instance.pk:
        old_instance = Part3.objects.get(pk=instance.pk)
        if old_instance.audio1 != instance.audio1:
            if bool(old_instance.audio1):
                default_storage.delete(old_instance.audio1.path)

    if instance.pk:
        old_instance = Part3.objects.get(pk=instance.pk)
        if old_instance.audio2 != instance.audio2:
            if bool(old_instance.audio2):
                default_storage.delete(old_instance.audio2.path)

    if instance.pk:
        old_instance = Part3.objects.get(pk=instance.pk)
        if old_instance.audio3 != instance.audio3:
            if bool(old_instance.audio3):
                default_storage.delete(old_instance.audio3.path)

    if instance.pk:
        old_instance = Part3.objects.get(pk=instance.pk)
        if old_instance.audio4 != instance.audio4:
            if bool(old_instance.audio4):
                default_storage.delete(old_instance.audio4.path)

    if instance.pk:
        old_instance = Part3.objects.get(pk=instance.pk)
        if old_instance.audio5 != instance.audio5:
            if bool(old_instance.audio5):
                default_storage.delete(old_instance.audio5.path)


@receiver(pre_delete, sender=Part3)
def delete_music_file(sender, instance, **kwargs):
    if instance.audio1:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio1.storage
        file_path = instance.audio1.name
        storage.delete(file_path)

    if instance.audio2:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio2.storage
        file_path = instance.audio2.name
        storage.delete(file_path)

    if instance.audio3:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio3.storage
        file_path = instance.audio3.name
        storage.delete(file_path)

    if instance.audio4:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio4.storage
        file_path = instance.audio4.name
        storage.delete(file_path)

    if instance.audio5:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio5.storage
        file_path = instance.audio5.name
        storage.delete(file_path)


@receiver(pre_save, sender=JuzAudio)
def delete_old_file(sender, instance, **kwargs):
    if instance.pk:
        old_instance = JuzAudio.objects.get(pk=instance.pk)
        if old_instance.audio1 != instance.audio1:
            if bool(old_instance.audio1):
                default_storage.delete(old_instance.audio1.path)
    if instance.pk:
        old_instance = JuzAudio.objects.get(pk=instance.pk)
        if old_instance.audio2 != instance.audio2:
            if bool(old_instance.audio2):
                default_storage.delete(old_instance.audio2.path)
    if instance.pk:
        old_instance = JuzAudio.objects.get(pk=instance.pk)
        if old_instance.audio1 != instance.audio3:
            if bool(old_instance.audio3):
                default_storage.delete(old_instance.audio3.path)


@receiver(pre_delete, sender=JuzAudio)
def delete_music_file(sender, instance, **kwargs):
    if instance.audio1:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio1.storage
        file_path = instance.audio1.name
        storage.delete(file_path)
    if instance.audio2:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio2.storage
        file_path = instance.audio2.name
        storage.delete(file_path)
    if instance.audio3:
        storage = default_storage if isinstance(default_storage, FileSystemStorage) else instance.audio3.storage
        file_path = instance.audio3.name
        storage.delete(file_path)


@receiver(pre_delete, sender=TestTaker)
def delete_test(sender, instance, **kwargs):
    id_code = instance.id_code
    audios = DoNotEnter.objects.filter(id_code=id_code)
    if len(audios) > 0:
        for instancee in audios:
            storage = default_storage if isinstance(default_storage, FileSystemStorage) else instancee.audio.storage
            file_path = instancee.audio.name
            storage.delete(file_path)
        audios.delete()
    file_name = f"{instance.name}_{instance.surname}_{instance.id_code}.zip"
    file_path = Path(settings.MEDIA_ROOT / "exam") / file_name
    default_storage.delete(file_path)



@receiver(pre_delete, sender=DoNotEnter)
def trash_audio_answer(sender, instance, **kwargs):
    storage = default_storage if isinstance(default_storage, FileSystemStorage) else instancee.audio.storage
    file_path = instance.audio.name
    storage.delete(file_path)


@receiver(post_save, sender=TestTaker)
def clean_storage(sender, instance, created, **kwargs):
    if created:
        now_time = timezone.now() - timedelta(minutes=30)
        TestTaker.objects.filter(created_time__lte=now_time).delete()
        # for user in users:
        #     print(user)
        #     id_code = user.id_code
        #     audios = DoNotEnter.objects.filter(id_code=id_code)
        #     if len(audios) > 0:
        #         for instancee in audios:
        #             storage = default_storage if isinstance(default_storage,
        #                                                     FileSystemStorage) else instancee.audio.storage
        #             file_path = instancee.audio.name
        #             storage.delete(file_path)
        #         audios.delete()
        #     file_name = f"{user.name}_{user.surname}_{user.id_code}.zip"
        #     file_path = Path(settings.MEDIA_ROOT / "exam") / file_name
        #     default_storage.delete(file_path)