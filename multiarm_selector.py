from __future__ import division
import random


class MultiarmSelector(object):
    def __init__(self):
        self.versions_served = []
        self.clicks = 0
        self.missed = 0

        self.success_count = {
            "A": 0,
            "B": 0
        }
        self.total_count = {
            "A": 0,
            "B": 0
        }

    def handle_response_from_new_user(self, user_data):
        selection, not_selected = self._get_selection()
        self.versions_served.append(selection)
        self._update_success_and_total(selection, user_data)
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

    def did_give_correct_answer(self):
        "We are assuming for test that B is always better than A"
        expected_reward_A = self.success_count["A"] / self.total_count["A"]
        expected_reward_B = self.success_count["B"] / self.total_count["B"]
        if expected_reward_B > expected_reward_A:
            return 1
        else:
            return 0

    def _update_success_and_total(self, selection, user_data):
        self.total_count[selection] += 1
        if user_data[selection]:
            self.success_count[selection] += 1

    def _get_selection(self):
        if random.random() < 0.1:
            return self._get_random_selection()

        if self.total_count["A"] == 0 or self.total_count["B"] == 0:
            return self._get_random_selection()

        expected_reward_A = self.success_count["A"] / self.total_count["A"]
        expected_reward_B = self.success_count["B"] / self.total_count["B"]

        if expected_reward_B > expected_reward_A:
            return "B", "A"
        else:
            return "A", "B"

    def _get_random_selection(self):
        if random.random() < 0.5:
            return "A", "B"
        else:
            return "B", "A"
