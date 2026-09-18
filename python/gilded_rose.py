# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1


# ASSUMPTION: For items, whose quality increase over time (Except Backstage passes), the rate at which quality increases remains same.
    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            elif item.name == "Aged Brie":
                self._update_aged_brie(item)

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self._update_backstage_passes(item)

            elif item.name == "Conjured Mana Cake":
                self._update_conjured_item(item)

            else:
                self._update_normal_item(item)

    def _update_item_quality(self,item, amount):
        if item.quality + amount < 0:
            item.quality = 0
        elif item.quality + amount > 50:
            item.quality = 50
        else:
            item.quality += amount

    def _update_aged_brie(self,item):
        self._update_item_quality(item,1)
        item.sell_in -= 1

    def _update_backstage_passes(self,item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in <= 5:
            self._update_item_quality(item,3)
        elif item.sell_in <= 10:
            self._update_item_quality(item,2)
        else:
            self._update_item_quality(item,1)
        item.sell_in -= 1

    def _update_conjured_item(self,item):
        if item.sell_in >= 0:
            self._update_item_quality(item,-2)
        else:
            self._update_item_quality(item,-4)
        item.sell_in -= 1

    def _update_normal_item(self,item):
        if item.sell_in >= 0:
            self._update_item_quality(item,-1)
        else:
            self._update_item_quality(item,-2)
        item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
