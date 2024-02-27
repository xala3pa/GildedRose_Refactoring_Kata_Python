# -*- coding: utf-8 -*-
import unittest

from python.gilded_rose import GildedRose
from python.conjured_item import Conjured
from python.sulfuras_item import SulfurasItem
from python.common_item import CommonItem
from python.backstage_item import BackstageItem
from python.aged_brie_item import AgedBrieItem

BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
FOO = "foo_item"
AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [CommonItem(FOO, 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(FOO, items[0].name)

    def test_at_the_end_of_the_day_common_product_sellIn_decrease(self):
        items = [CommonItem(FOO, 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(14, items[0].sell_in)

    def test_at_the_end_of_the_day_common_product_quality_decrease(self):
        items = [CommonItem(FOO, 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(9, items[0].quality)

    def test_quality_decrease_x2_after_sellIn_date(self):
        items = [CommonItem(FOO, -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(8, items[0].quality)

    def test_item_quality_is_never_minus_one(self):
        items = [CommonItem(FOO, 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(0, items[0].quality)

    def test_brie_item_increase_quality_the_older_it_gets(self):
        items = [AgedBrieItem(AGED_BRIE, 20, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(11, items[0].quality)

    def test_brie_item_increase_quality_x2_when_sellIn_less_than_0(self):
        items = [AgedBrieItem(AGED_BRIE, -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(12, items[0].quality)

    def test_brie_item_increase_quality_when_sellIn_decrease(self):
        items = [AgedBrieItem(AGED_BRIE, 20, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(11, items[0].quality)

    def test_item_never_increase_quality_more_than_50(self):
        items = [AgedBrieItem(AGED_BRIE, 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(50, items[0].quality)

    def test_lengendary_items_change_quality_or_sellIn(self):
        items = [SulfurasItem(SULFURAS, 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(20, items[0].sell_in)

    def test_Backstage_items_change_quality_with_sellIn_more_than_10_days(self):
        items = [BackstageItem(BACKSTAGE, 20, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(21, items[0].quality)

    def test_Backstage_items_change_quality_with_sellIn_between_10_and_5_days(self):
        items = [BackstageItem(BACKSTAGE, 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(22, items[0].quality)

    def test_Backstage_items_change_quality_with_sellIn_5_or_less_days(self):
        items = [BackstageItem(BACKSTAGE, 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(23, items[0].quality)

    def test_Backstage_items_quality_equals_zero_with_sellIn_less_than_zero(self):
        items = [BackstageItem(BACKSTAGE, -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(0, items[0].quality)

    def test_Conjured_items_quality_degrade_twice_as_fast_as_normal_items(self):
        items = [Conjured(CONJURED, 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(18, items[0].quality)

    def test_Conjured_sellIn_items_quality_degrade_twice_as_fast_as_normal_items(self):
        items = [Conjured(CONJURED, -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.process_inventory()
        self.assertEqual(16, items[0].quality)


if __name__ == '__main__':
    unittest.main()
