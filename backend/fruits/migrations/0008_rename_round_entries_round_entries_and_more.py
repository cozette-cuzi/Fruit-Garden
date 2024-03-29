# Generated by Django 4.1.4 on 2022-12-13 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fruits", "0007_remove_order_order_entries_order_entries_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="round",
            old_name="round_entries",
            new_name="entries",
        ),
        migrations.AlterField(
            model_name="roundentry",
            name="round_id",
            field=models.ForeignKey(
                db_column="round_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="round_entries",
                to="fruits.round",
            ),
        ),
    ]
