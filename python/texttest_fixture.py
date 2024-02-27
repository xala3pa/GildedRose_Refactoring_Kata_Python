# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *
from python.aged_brie_item import AgedBrieItem
from python.backstage_item import BackstageItem
from python.common_item import CommonItem
from python.conjured_item import Conjured

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             CommonItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
             AgedBrieItem(name="Aged Brie", sell_in=2, quality=0),
             CommonItem(name="Elixir of the Mongoose", sell_in=5, quality=7),
             BackstageItem(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             BackstageItem(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             BackstageItem(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Conjured(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 30
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).process_inventory()
