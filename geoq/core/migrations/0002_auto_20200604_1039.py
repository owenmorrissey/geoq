# Generated by Django 3.0.5 on 2020-06-04 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aoi',
            name='assignee_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='aoi',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aois', to='core.Job'),
        ),
        migrations.AlterField(
            model_name='aoitimer',
            name='aoi',
            field=models.ForeignKey(help_text='Workcell that was changed', on_delete=django.db.models.deletion.CASCADE, to='core.AOI'),
        ),
        migrations.AlterField(
            model_name='aoitimer',
            name='user',
            field=models.ForeignKey(help_text='User who worked on workcell', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='aoi',
            field=models.ForeignKey(help_text='Associated AOI for comment', on_delete=django.db.models.deletion.CASCADE, to='core.AOI'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, help_text='User who made comment', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='assignee_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
