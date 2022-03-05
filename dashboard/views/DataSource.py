#!/bin/env python
"""
Put module documentation here
"""

from django.views import generic

import dashboard.models as models
import dashboard.forms.DataSource as forms


class CreateDataSource(generic.CreateView):
    template_name_suffix = "_create_form"
    model = models.DataSource
    form_class = forms.CreateDataSourceForm
