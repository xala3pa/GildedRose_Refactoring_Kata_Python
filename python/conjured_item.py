from python.gilded_rose_item import GildedRoseItem


class Conjured(GildedRoseItem):
    def update_quality(self):
        self.decrease_quality(2)
        if self.is_expired():
            self.decrease_quality(2)
