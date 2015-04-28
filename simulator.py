import numpy as np
import random

from naive_selector import NaiveSelector
from bayesian_selector import BayesianSelector
from multiarm_selector import MultiarmSelector


NUM_SIM = 30
NUM_USERS = 1000


def coin_flip(prob_true):
    if random.random() < prob_true:
        return True
    else:
        return False


def simulate(prob_click_a, prob_click_b, num_users):
    naive_selector = NaiveSelector()
    bayesian_selector = BayesianSelector()
    multiarm_selector = MultiarmSelector()

    user_clicks = [
        {
            "A": coin_flip(prob_click_a),
            "B": coin_flip(prob_click_b)
        }
        for i in range(num_users)
    ]
    for user_click in user_clicks:
        naive_selector.handle_response_from_new_user(user_click)
        bayesian_selector.handle_response_from_new_user(user_click)
        multiarm_selector.handle_response_from_new_user(user_click)

    return naive_selector, bayesian_selector, multiarm_selector


def main():
    f = open("./data/simulation_results.csv", "w", 0)
    f.write(
        "prob_click_a, prob_click_b,"
        " num_click_naive, num_click_bayesian, num_click_multiarm,"
        " prob_correct_naive, prob_correct_bayesian, prob_correct_multiarm\n"
    )
    prob_click_as = [0.1, 0.3, 0.6]
    for prob_click_a in prob_click_as:
        prob_click_bs = np.arange(prob_click_a + 0.01, prob_click_a + 0.2, 0.01)
        for prob_click_b in prob_click_bs:
            print "working on", prob_click_a, prob_click_b
            num_click_naive = np.zeros(NUM_SIM)
            num_click_bayesian = np.zeros(NUM_SIM)
            num_click_multiarm = np.zeros(NUM_SIM)
            is_correct_naive = np.zeros(NUM_SIM)
            is_correct_bayesian = np.zeros(NUM_SIM)
            is_correct_multiarm = np.zeros(NUM_SIM)
            # do 1000 simulations for each run
            for i in range(NUM_SIM):
                naive_selector, bayesian_selector, multiarm_selector = simulate(
                    prob_click_a=prob_click_a,
                    prob_click_b=prob_click_b,
                    num_users=NUM_USERS
                )
                num_click_naive[i], _ = naive_selector.prepare_report()
                num_click_bayesian[i], _ = bayesian_selector.prepare_report()
                num_click_multiarm[i], _ = multiarm_selector.prepare_report()
                is_correct_naive[i] = naive_selector.did_give_correct_answer()
                is_correct_bayesian[i] = bayesian_selector.did_give_correct_answer()
                is_correct_multiarm[i] = multiarm_selector.did_give_correct_answer()

            f.write(
                "{}, {}, {}, {}, {}, {}, {}, {}\n".format(
                    prob_click_a,
                    prob_click_b,
                    np.mean(num_click_naive),
                    np.mean(num_click_bayesian),
                    np.mean(num_click_multiarm),
                    np.mean(is_correct_naive),
                    np.mean(is_correct_bayesian),
                    np.mean(is_correct_multiarm)
                )
            )
    f.close()


if __name__ == "__main__":
    main()
