from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class Part1(models.Model):
    question = models.CharField(max_length=500, verbose_name='savol')
    audio = models.FileField(upload_to='part1')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Juz_1'
        verbose_name_plural = "Juz_1"


class Part2(models.Model):
    topic = models.CharField(max_length=150, verbose_name="Mavzu")
    question1 = models.CharField(max_length=500, verbose_name='savol_1')
    question2 = models.CharField(max_length=500, verbose_name='savol_2')
    question3 = models.CharField(max_length=500, verbose_name='savol_3')
    question4 = models.CharField(max_length=500, verbose_name='savol_4')
    question5 = models.CharField(max_length=500, verbose_name='savol_5')
    audio = models.FileField(upload_to='part2')


    class Meta:
        verbose_name = 'Juz_2'
        verbose_name_plural = "Juz_2"

    def __str__(self):
        return str(self.id)


class Part3(models.Model):
    topic = models.CharField(max_length=150, verbose_name="Mavzu")
    question1 = models.CharField(max_length=500, verbose_name='savol_1')
    audio1 = models.FileField(upload_to='part3')
    question2 = models.CharField(max_length=500, verbose_name='savol_2')
    audio2 = models.FileField(upload_to='part3')
    question3 = models.CharField(max_length=500, verbose_name='savol_3')
    audio3 = models.FileField(upload_to='part3')
    question4 = models.CharField(max_length=500, verbose_name='savol_4')
    audio4 = models.FileField(upload_to='part3')
    question5 = models.CharField(max_length=500, verbose_name='savol_5')
    audio5 = models.FileField(upload_to='part3')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Juz_3'
        verbose_name_plural = "Juz_3"


tomorrow = timezone.now().date() + timedelta(days=1)


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(default=tomorrow, verbose_name="Saytdan foydalanish so'ngi muddati")

    def __str__(self):
        return self.user.username

    def is_active(self):
        return self.end_date >= timezone.now().date()


class Time_Settings(models.Model):
    part1_question_time = models.PositiveIntegerField(default=30,
                                                      verbose_name="1 juz savollariga javob berish davomiyligi")
    part1_waiting_time = models.PositiveIntegerField(default=5,
                                                     verbose_name="Savollar yozib olinishi boshlangunigacha bo'lgan vaqt")
    part2_question_time = models.PositiveIntegerField(default=120,
                                                      verbose_name="2 juz savollariga javob berish davomiyligi")
    part2_waiting_time = models.PositiveIntegerField(default=60, verbose_name="1 va 2 juzlar oralig'i")
    part3_question_time = models.PositiveIntegerField(default=30,
                                                      verbose_name="3 juz savollariga javob berish davomiyligi")
    part3_waiting_time = models.PositiveIntegerField(default=5, verbose_name="2 va 3 juzlar orasidagi kutish vaqti")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{str(self.id)}: Vaqt sozlamalari"

    class Meta:
        verbose_name = 'Vaqt sozlamalari'
        verbose_name_plural = "Vaqt sozlamalari"


class JuzAudio(models.Model):
    audio1 = models.FileField(upload_to='juz_sharti', verbose_name="1-juz sharti")
    audio2 = models.FileField(upload_to='juz_sharti', verbose_name="2-juz sharti")
    audio3 = models.FileField(upload_to='juz_sharti', verbose_name="3-juz sharti")

    def __str__(self):
        return f"{self.id}: Shartlar audiolari"


class DoNotEnter(models.Model):
    id_code = models.CharField(max_length=100)
    audio = models.FileField(upload_to="zip_files")


    def __str__(self):
        return f"{self.audio.name}:{self.id_code}"


class TestTaker(models.Model):
    id_code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"





