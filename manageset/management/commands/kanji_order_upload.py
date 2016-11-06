# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from manageset.models import Kanji
import csv
import sys
import os
print os.path.dirname(os.path.abspath(__file__))
class Command(BaseCommand):
    help = 'Uploading master kanji order'

    def _upload_kanji_order(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "kanji_order_NOV6.csv"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, 'rU') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            row_count = 0
            for row in reader:
                row_count += 1
                if row_count == 1:
                    pass
                else:
                    kanji = row[2].decode("utf-8")
                    try:
                        kanji = Kanji.objects.get(kanji_name=kanji)
                        kanji.master_order = row[0]
                        kanji.save()
                    except:
                      duplicate = Kanji.objects.filter(kanji_name=kanji)
                      print duplicate
                      duplicate[1].delete()
            print "complete!"

    def handle(self, *args, **options):
        self._upload_kanji_order()       
    
