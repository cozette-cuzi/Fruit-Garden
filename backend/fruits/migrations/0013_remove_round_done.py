# Generated by Django 4.1.4 on 2022-12-16 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fruits", "0012_order_entries"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="round",
            name="done",
        ),
    ]