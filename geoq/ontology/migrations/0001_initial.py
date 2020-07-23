# Generated by Django 3.0.5 on 2020-07-22 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ontology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Ontology Name', max_length=200)),
                ('url', models.URLField(help_text='Location of ontology')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(help_text='Value of term', max_length=100)),
                ('identifier', models.URLField(help_text='Term Identifier')),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Vocabulary', max_length=200)),
                ('terms', models.ManyToManyField(to='ontology.Term')),
            ],
        ),
    ]