# Generated by Django 2.2.3 on 2019-07-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CancellationPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'cancellation_policy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Commissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'commissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('short_code', models.CharField(blank=True, max_length=25, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'countries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'currencies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('code', models.CharField(blank=True, max_length=10, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'languages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=25, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'notification_content',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'notification_methods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'payment_methods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'personal_services',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaceImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
                ('local_path', models.CharField(blank=True, max_length=1000, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'place_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'places',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TermsConditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('creation_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'terms_conditions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VoyagerServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('creation_date', models.DateTimeField(db_column='creation_Date')),
            ],
            options={
                'db_table': 'voyager_services',
                'managed': False,
            },
        ),
    ]
