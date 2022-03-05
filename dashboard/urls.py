#!/bin/env python
"""
Put module documentation here
"""

from django.urls import path

import dashboard.views.DataSource as DataSourceViews

urlpatterns = [
    path("datasource/create", DataSourceViews.CreateDataSource.as_view(), name="create_datasource"),
]
