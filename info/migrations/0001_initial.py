# Generated by Django 3.0.3 on 2020-04-09 08:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed.')])),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=20)),
                ('pesel', models.BigIntegerField(unique=True)),
                ('blood_group', models.CharField(choices=[('0 Rh+', '0 Rh+'), ('A Rh+', 'A Rh+'), ('B Rh+', 'B Rh+'), ('AB Rh+', 'AB Rh+'), ('0 Rh-', '0 Rh-'), ('A Rh-', 'A Rh-'), ('B Rh-', 'B Rh-'), ('AB Rh-', 'AB Rh-')], max_length=10)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+48', max_length=128, region=None, unique=True)),
                ('date_of_register', models.DateField(default=django.utils.timezone.now)),
                ('medical_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_donation', models.DateField(default=django.utils.timezone.now)),
                ('accept_donate', models.BooleanField()),
                ('refuse_information', models.TextField(blank=True, null=True)),
                ('medical_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.Patient')),
            ],
        ),
    ]
