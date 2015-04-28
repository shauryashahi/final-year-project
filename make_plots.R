rm(list = ls())
library("ggplot2")
source("./save_simple_plots.R")
data = read.csv("./simulation_results.csv")

data_low_prob = subset(data, prob_click_a == 0.1)
save_simple_plots(
  data_low_prob,
  "./fig/low_click_prob/clicks.png",
  "./fig/low_click_prob/ratio.png",
  "./fig/low_click_prob/correct.png"
)

data_mid_prob = subset(data, prob_click_a == 0.3)
save_simple_plots(
  data_mid_prob,
  "./fig/mid_click_prob/clicks.png",
  "./fig/mid_click_prob/ratio.png",
  "./fig/mid_click_prob/correct.png"
)

data_high_prob = subset(data, prob_click_a == 0.6)
save_simple_plots(
  data_high_prob,
  "./fig/high_click_prob/clicks.png",
  "./fig/high_click_prob/ratio.png",
  "./fig/high_click_prob/correct.png"
)



