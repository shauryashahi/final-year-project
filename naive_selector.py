import random


class NaiveSelector(object):
    def __init__(self):
        self.versions_served = []
        self.clicks = 0
        self.missed = 0

    def handle_response_from_new_user(self, user_data):
        selection, not_selected = self._get_selection()
        self.versions_served.append(selection)
        if user_data[selection]:
            self.clicks += 1
            return
        if user_data[not_selected]:
            self.missed += 1
            return

    def prepare_report(self):
        return self.clicks, self.missed

    def versions_served(self):
        return self.versions_served

    def _get_selection(self):
        r = random.random()
        if r < 0.5:
            return "A", "B"
        else:
            return "B", "A"
