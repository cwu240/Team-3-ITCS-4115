# Generated by Django 4.1.7 on 2023-04-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact_us", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
