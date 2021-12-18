from django.contrib import admin
from .models import Test
from import_export.admin import ImportExportModelAdmin


# Register your models here.
import pandas as pd
#from __future__ import unicode_literals
from hazm import *
from persian import *
import re
import numpy
import csv


@admin.register(Test)
class AdminProject(ImportExportModelAdmin):
    #tree = ET.parse('NewXML1.xml')
    #root = tree.getroot()

    #get_range = lambda col: range(len(col))
    #l = [{r[i].tag: r[i].text for i in get_range(r)} for r in root]

    #df = pd.DataFrame.from_dict(l)
    #df.to_csv('file.csv')

    #normalizer = Normalizer()

    #df['TEXT'] = df['TEXT'].str.replace('\n', '')
    #df['TEXT'] = df['TEXT'].str.replace('.', '', regex=True)
    #df['TEXT'] = df['TEXT'].str.replace('\xa0', '', regex=True)
    #df['TEXT'] = df['TEXT'].str.replace('\d+', '', regex=True)
    #df['TEXT'] = df['TEXT'].str.replace('[^\w\s]', '', regex=True)

    #df['TITLE'] = df['TITLE'].str.replace('\n', '')
    #df['TITLE'] = df['TITLE'].str.replace('.', '', regex=True)
    #df['TITLE'] = df['TITLE'].str.replace('\xa0', '', regex=True)
    #df['TITLE'] = df['TITLE'].str.replace('\d+', '', regex=True)
    #df['TITLE'] = df['TITLE'].str.replace('[^\w\s]', '', regex=True)

    #df_persian_TEXT = persian.convert_ar_characters(df['TEXT'])
    #normalizer.normalize(df_persian_TEXT)
    #word_tokenize(df_persian_TEXT)

    #TODO create table dataframe to database and model djnago
    list_display = [
       "test"
    ]

    import_fields = [
        "id", "test"
    ]

    import_id_fields = ["id", ]


#admin.site.register(Test)