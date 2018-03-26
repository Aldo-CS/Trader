# -*- coding: utf-8 -*-
"""
Information for coin traders API's.
"""
from django.db import models
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class History(models.Model):
    history_name = models.CharField(max_length=200)
    history_data = models.FileField(upload_to='maps', storage=gd_storage)
