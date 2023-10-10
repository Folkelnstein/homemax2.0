from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

class Advertisement(models.Model):

    title = models.CharField('заголовок',max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("Цена", max_length=10,decimal_places=2,max_digits=20)
    auction = models.BooleanField('Topг',help_text="Отметить если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.action(description="Дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.action(description="Дата обновления")
    def update_date(self):
        if self.update_at.date() == timezone.now().date():
            update_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: purple; font-weight: bold;">Сегодня в {}</span>', update_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    class Meta:
        db_table='advertisement'

# Create your models here.
