from __future__ import division
from scipy.special import beta


class BayesianSelector(object):
    def __init__(self):
        self.versions_served = []
        self.clicks = 0
        self.missed = 0

        self.success_count = {
            "A": 0,
            "B": 0
        }
        self.failure_count = {
            "A": 0,
            "B": 0
        }

    def handle_response_from_new_user(self, user_data):
        selection, not_selected = self._get_selection()
        self.versions_served.append(selection)
        self._update_success_and_failure_count(selection, user_data)
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
        prob_b_better_than_a = self._get_bayesian_prob()
        if prob_b_better_than_a > 0.5:
            return 1
        else:
            return 0

    def _update_success_and_failure_count(self, selection, user_data):
        if user_data[selection]:
            self.success_count[selection] += 1
        else:
            self.failure_count[selection] += 1

    def _get_selection(self):
        prob_b_better_than_a = self._get_bayesian_prob()
        if prob_b_better_than_a > 0.5:
            return "B", "A"
        else:
            return "A", "B"

    def _get_bayesian_prob(self):
        alpha_a = 1 + self.success_count["A"]
        beta_a = 1 + self.failure_count["A"]
        alpha_b = 1 + self.success_count["B"]
        beta_b = 1 + self.failure_count["B"]

        return sum(
            beta(alpha_a + i, beta_b + beta_a) * 1.0 /
            ((beta_b + i) * beta(1 + i, beta_b) * beta(alpha_a, beta_a))
            for i in range(alpha_b)
        )
