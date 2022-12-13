# Generated by Django 4.1.4 on 2022-12-13 10:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fruit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("done", "done"),
                            ("collecting", "collecting"),
                            ("new", "new"),
                        ],
                        default="new",
                        max_length=16,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="OrderEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                (
                    "fruit_id",
                    models.ForeignKey(
                        db_column="fruit_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fruits.fruit",
                    ),
                ),
                (
                    "order_id",
                    models.ForeignKey(
                        db_column="order_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fruits.order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Round",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("done", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="RoundEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(50),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                (
                    "fruit_id",
                    models.ForeignKey(
                        db_column="fruit_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fruits.fruit",
                    ),
                ),
                (
                    "round_id",
                    models.ForeignKey(
                        db_column="round_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fruits.round",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="round",
            name="round_entries",
            field=models.ManyToManyField(
                related_name="round_entries",
                through="fruits.RoundEntry",
                to="fruits.fruit",
            ),
        ),
        migrations.CreateModel(
            name="OrderRound",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField()),
                (
                    "fruit_id",
                    models.ForeignKey(
                        db_column="fruit_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fruits.fruit",
                    ),
                ),
                (
                    "order_entry_id",
                    models.ForeignKey(
                        db_column="order_entry_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_round_entries",
                        to="fruits.orderentry",
                    ),
                ),
                (
                    "round_entry_id",
                    models.ForeignKey(
                        db_column="round_entry_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_round_entries",
                        to="fruits.roundentry",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="order_entries",
            field=models.ManyToManyField(
                default=None,
                related_name="order_entries",
                through="fruits.OrderEntry",
                to="fruits.fruit",
            ),
        ),
    ]
