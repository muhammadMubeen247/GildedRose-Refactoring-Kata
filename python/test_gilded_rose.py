# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    # Test cases for normal items
    def test_normal_items_degrade_by_one_before_sell_by_date(self):
        item = Item("foo", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 9)

    def test_normal_items_degrade_by_two_after_sell_by_date(self):
        item = Item("foo", -1, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 8)

    def test_normal_items_quality_degrades_one_on_sell_by_date(self):
        item = Item("foo", 0, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 9)

    def test_quality_never_negative(self):
        item = Item("foo", 5, 0)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 0)
    
    # Test cases for Aged Brie
    def test_aged_brie_increases_quality(self):
        item = Item("Aged Brie", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 11)

    def test_aged_brie_quality_never_exceeds_50(self):
        item = Item("Aged Brie", 5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 50)

    # Test cases for Sulfuras, Hand of Ragnaros
    def test_sulfuras_never_changes(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 80)  

    # Test cases for Backstage passes
    def test_backstage_passes_increase_quality(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 21) 

    def test_backstage_passes_increase_quality_by_2_when_10_days_or_less(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 22)

    def test_backstage_passes_increase_quality_by_3_when_5_days_or_less(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 23)

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 0)

    def test_backstage_passes_quality_never_exceeds_50(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 50)

    # Test cases for Conjured items
    def test_conjured_items_degrade_by_two_before_sell_by_date(self):
        item = Item("Conjured Mana Cake", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 8)

    def test_conjured_items_degrade_by_four_after_sell_by_date(self):
        item = Item("Conjured Mana Cake", -1, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 6)

    # Test cases for all items
    def test_all_items_update_quality(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 19)

        self.assertEqual(items[1].sell_in, 1)
        self.assertEqual(items[1].quality, 1)

        self.assertEqual(items[2].sell_in, 4)
        self.assertEqual(items[2].quality, 6)

        self.assertEqual(items[3].sell_in, 0)
        self.assertEqual(items[3].quality, 80)

        self.assertEqual(items[4].sell_in, -1)
        self.assertEqual(items[4].quality, 80)

        self.assertEqual(items[5].sell_in, 14)
        self.assertEqual(items[5].quality, 21)

        self.assertEqual(items[6].sell_in, 9)
        self.assertEqual(items[6].quality, 50)

        self.assertEqual(items[7].sell_in, 4)
        self.assertEqual(items[7].quality, 50)

        self.assertEqual(items[8].sell_in, 2)
        self.assertEqual(items[8].quality, 4)

if __name__ == '__main__':
    unittest.main()
