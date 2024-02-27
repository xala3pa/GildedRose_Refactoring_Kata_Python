from python.gilded_rose_item import GildedRoseItem


class CommonItem(GildedRoseItem):
    def update_quality(self):
        self.decrease_quality()
        if self.is_expired():
            self.decrease_quality()
