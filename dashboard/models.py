from django.db import models
from django.contrib.auth.models import User

import dashboard.model_choices as choices

# Create your models here.


class Parameter(models.Model):
    name = models.CharField(
        max_length=30,
        help_text="The name of the parameter"
    )
    parameter_type = models.CharField(
        max_length=30,
        help_text="The type of object that this is a parameter for (Content, DataSource, etc)"
    )
    value_type = models.CharField(
        max_length=500,
        choices=choices.value_types(),
        help_text="The type of value that may populate this value"
    )


class Argument(models.Model):
    parameter = models.ForeignKey(
        to=Parameter,
        on_delete=models.CASCADE,
        help_text="The parameter that this is a value for"
    )
    is_environmental = models.BooleanField(
        default=False,
        help_text="Whether or not the value is the name of an environment variable"
    )
    value = models.CharField(
        max_length=1000,
        help_text="The value for the argument"
    )


class Tab(models.Model):
    owner = models.ForeignKey(
        to=User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        help_text="The owner of the tab (blank means that it's public)"
    )
    index = models.IntegerField(
        help_text="The index of the tab"
    )
    header = models.CharField(
        max_length=50,
        blank=True,
        help_text="An optional header for the tab"
    )
    tab_text = models.CharField(
        max_length=20,
        help_text="Text to place on the tab"
    )
    tab_color = models.CharField(
        max_length=7,
        help_text="The color of the tab"
    )


class DataSource(models.Model):
    name = models.CharField(
        max_length=50
    )
    provider = models.CharField(
        max_length=500
    )
    parameters = models.ManyToManyField(
        to=Parameter,
        help_text="The parameters required for this data source to function"
    )


class Content(models.Model):
    arguments = models.ManyToManyField(
        to=Argument,
        help_text="The arguments that direct what will be displayed on the card"
    )


class Card(models.Model):
    tab = models.ForeignKey(
        to=Tab,
        on_delete=models.CASCADE,
        help_text="An item on a tab"
    )
    data_sources = models.ManyToManyField(
        to=DataSource,
        help_text="All providers of data"
    )
    row = models.IntegerField(
        help_text="The row to place the card on (zero indexed)"
    )
    column = models.IntegerField(
        help_text="The column to place the card on (zero indexed)"
    )
    title = models.CharField(
        max_length=50,
        help_text="The optional title for the card"
    )
    classes = models.CharField(
        max_length=250,
        help_text="Custom class names for pre-defined behavior"
    )


class CardStyle(models.Model):
    card = models.ForeignKey(
        to=Card,
        on_delete=models.CASCADE,
        help_text="The card that this style applies to"
    )
    style = models.CharField(
        max_length=50,
        choices=choices.css_styles(),
        help_text="The style to modify"
    )
    value = models.CharField(
        max_length=50,
        help_text="The value for the style"
    )
