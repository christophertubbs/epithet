#!/bin/env python
"""
Put module documentation here
"""

import django.forms as forms

import dashboard.models as models


class CreateDataSourceForm(forms.ModelForm):
    class Meta:
        model = models.DataSource
        fields = ['name', 'provider', 'parameters']

