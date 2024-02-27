from python.item import Item

MIN_QUALITY = 0
MAX_QUALITY = 50


class GildedRoseItem(Item):
    def update(self):
        self.update_sellIn()
        self.update_quality()

    def update_sellIn(self):
        self.sell_in -= 1

    def update_quality(self):
        pass

    def is_expired(self):
        return self.sell_in < 0

    def increase_quality(self, upgrade_level=1) -> None:
        self.quality = min(MAX_QUALITY, self.quality + upgrade_level)

    def decrease_quality(self, degrade_level=1) -> None:
        self.quality = max(MIN_QUALITY, self.quality - degrade_level)
