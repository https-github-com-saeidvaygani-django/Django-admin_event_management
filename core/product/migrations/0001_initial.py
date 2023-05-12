# Generated by Django 4.2 on 2023-05-12 14:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EventTable",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="EventTable Id"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        validators=[product.models.EventTable.validate_character_only],
                        verbose_name="Event Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(max_length=250, verbose_name="Describe Event"),
                ),
                ("date", models.DateField(auto_now=True, null=True)),
                (
                    "location",
                    models.TextField(max_length=100, verbose_name="Event Location"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="media/events/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png"]
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PaymentTable",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="PaymentTable Id",
                    ),
                ),
                (
                    "payment_type",
                    models.CharField(max_length=50, verbose_name="Payment Type"),
                ),
                (
                    "amount",
                    models.IntegerField(
                        choices=[
                            ("Active (Early Bird)", "Active (Early Bird)"),
                            ("Active (Standart)", "Active (Standart)"),
                            ("Active (on site)", "Active (on site)"),
                            ("Student (Early Bird)", "Student (Early Bird)"),
                            ("Student (Standart)", "Student (Standart)"),
                            ("Student (on site)", "Student (on site)"),
                        ],
                        verbose_name="Amount",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SpeakersTable",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="SpeakersTable Id",
                    ),
                ),
                ("fname", models.CharField(max_length=50, verbose_name="First Name")),
                ("lname", models.CharField(max_length=50, verbose_name="Last Name")),
                (
                    "biography",
                    models.CharField(max_length=200, verbose_name="Biography"),
                ),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("Associate's Degree", "Associate's Degree"),
                            ("Bachelor's Degree", "Bachelor's Degree"),
                            ("Master's Degree", "Master's Degree"),
                            ("Doctorate Degree", "Doctorate Degree"),
                        ],
                        max_length=50,
                        verbose_name="Degree",
                    ),
                ),
                (
                    "event_id",
                    models.ManyToManyField(
                        limit_choices_to={"name__isnull": False},
                        to="product.eventtable",
                        verbose_name="Event id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SessionTable",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="SessionTable Id",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="Title")),
                (
                    "description",
                    models.TextField(max_length=200, verbose_name="Descripton"),
                ),
                (
                    "start_time",
                    models.DateField(
                        auto_now=True, null=True, verbose_name="Start Time"
                    ),
                ),
                (
                    "end_time",
                    models.DateField(auto_now=True, null=True, verbose_name="End Time"),
                ),
                (
                    "event_id",
                    models.ManyToManyField(
                        limit_choices_to={"name__isnull": False},
                        to="product.eventtable",
                        verbose_name="Event Id",
                    ),
                ),
                (
                    "speaker_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.speakerstable",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AttendeeTable",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="AttendeeTable Id",
                    ),
                ),
                ("fname", models.CharField(max_length=50, verbose_name="First Name")),
                ("lname", models.CharField(max_length=50, verbose_name="Last Name")),
                ("company", models.CharField(max_length=50, verbose_name="Company")),
                ("country", models.CharField(max_length=50, verbose_name="Country")),
                ("phone", models.CharField(max_length=50, verbose_name="Phone")),
                ("email", models.EmailField(max_length=50, verbose_name="Email")),
                (
                    "website",
                    models.CharField(max_length=50, verbose_name="Website Address"),
                ),
                (
                    "biography",
                    models.TextField(max_length=200, verbose_name="Biography"),
                ),
                ("degree", models.CharField(max_length=50, verbose_name="Degree")),
                (
                    "industries_type",
                    models.CharField(
                        choices=[
                            ("Association", "Association"),
                            ("Refiners", "Refiners"),
                            ("Crushers", "Crushers"),
                            ("Others", "Others"),
                        ],
                        max_length=30,
                        verbose_name="Industy Type",
                    ),
                ),
                (
                    "event_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.eventtable",
                        to_field="name",
                    ),
                ),
                (
                    "payment_is",
                    models.ManyToManyField(
                        limit_choices_to={"payment_type__isnull": False},
                        to="product.paymenttable",
                        verbose_name="Payment Option",
                    ),
                ),
            ],
        ),
    ]
