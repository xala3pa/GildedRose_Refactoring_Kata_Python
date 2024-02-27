from python.gilded_rose_item import GildedRoseItem


class BackstageItem(GildedRoseItem):
    def update_quality(self):
        self.increase_quality()
        if self.sell_in < 11:
            self.increase_quality()
        if self.sell_in < 6:
            self.increase_quality()
        if self.is_expired():
            self.quality = 0
