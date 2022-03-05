# Generated by Django 3.2.9 on 2021-11-29 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_environmental', models.BooleanField(default=False, help_text='Whether or not the value is the name of an environment variable')),
                ('value', models.CharField(help_text='The value for the argument', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(help_text='The row to place the card on (zero indexed)')),
                ('column', models.IntegerField(help_text='The column to place the card on (zero indexed)')),
                ('title', models.CharField(help_text='The optional title for the card', max_length=50)),
                ('classes', models.CharField(help_text='Custom class names for pre-defined behavior', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the parameter', max_length=30)),
                ('parameter_type', models.CharField(help_text='The type of object that this is a parameter for (Content, DataSource, etc)', max_length=30)),
                ('value_type', models.CharField(choices=[('integer', 'Integer'), ('float', 'Float'), ('string', 'String'), ('boolean', 'Boolean')], help_text='The type of value that may populate this value', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(help_text='The index of the tab')),
                ('header', models.CharField(blank=True, help_text='An optional header for the tab', max_length=50)),
                ('tab_text', models.CharField(help_text='Text to place on the tab', max_length=20)),
                ('tab_color', models.CharField(help_text='The color of the tab', max_length=7)),
                ('owner', models.ForeignKey(blank=True, help_text="The owner of the tab (blank means that it's public)", null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('provider', models.CharField(max_length=500)),
                ('parameters', models.ManyToManyField(help_text='The parameters required for this data source to function', to='dashboard.Parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arguments', models.ManyToManyField(help_text='The arguments that direct what will be displayed on the card', to='dashboard.Argument')),
            ],
        ),
        migrations.CreateModel(
            name='CardStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('color', 'Text Color'), ('padding', 'Padding'), ('margin', 'Margin'), ('background', 'Background'), ('cursor', 'Cursor')], help_text='The style to modify', max_length=50)),
                ('value', models.CharField(help_text='The value for the style', max_length=50)),
                ('card', models.ForeignKey(help_text='The card that this style applies to', on_delete=django.db.models.deletion.CASCADE, to='dashboard.card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='data_sources',
            field=models.ManyToManyField(help_text='All providers of data', to='dashboard.DataSource'),
        ),
        migrations.AddField(
            model_name='card',
            name='tab',
            field=models.ForeignKey(help_text='An item on a tab', on_delete=django.db.models.deletion.CASCADE, to='dashboard.tab'),
        ),
        migrations.AddField(
            model_name='argument',
            name='parameter',
            field=models.ForeignKey(help_text='The parameter that this is a value for', on_delete=django.db.models.deletion.CASCADE, to='dashboard.parameter'),
        ),
    ]
