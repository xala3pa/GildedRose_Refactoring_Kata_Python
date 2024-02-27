from python.gilded_rose_item import GildedRoseItem


class AgedBrieItem(GildedRoseItem):
    def update_quality(self):
        self.increase_quality()
        if self.is_expired():
            self.increase_quality()
