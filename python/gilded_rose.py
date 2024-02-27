# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def process_inventory(self):
        for item in self.items:
            item.update()
