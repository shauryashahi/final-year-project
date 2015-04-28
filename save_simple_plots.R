save_simple_plots = function(data, fname1, fname2, fname3) {
  p = ggplot(data)
  p = p + geom_line(aes(x = prob_click_b, y = num_click_naive), color="red")
  p = p + geom_line(aes(x = prob_click_b, y = num_click_bayesian), color="green")
  p = p + geom_line(aes(x = prob_click_b, y = num_click_multiarm), color="blue")
  p = p + theme_bw(base_size=14) + xlab("Probability of click on version B") + ylab("Number of clicks")
  ggsave(plot = p,filename = fname1)
  
  p = ggplot(data)
  p = p + geom_line(aes(x = prob_click_b, y = num_click_bayesian / num_click_naive), color="green")
  p = p + geom_line(aes(x = prob_click_b, y = num_click_multiarm / num_click_naive), color="blue")
  p = p + theme_bw(base_size=14) + xlab("Probability of click on version B") + ylab("Ratio of clicks")
  ggsave(plot = p,filename = fname2)
  
  p = ggplot(data)
  p = p + geom_line(aes(x = prob_click_b, y = prob_correct_naive * 100), color="red")
  p = p + geom_line(aes(x = prob_click_b, y = prob_correct_bayesian * 100), color="green")
  p = p + geom_line(aes(x = prob_click_b, y = prob_correct_multiarm * 100), color="blue")
  p = p + theme_bw(base_size=14) + xlab("Probability of click on version B") + ylab("% correct")
  ggsave(plot = p,filename = fname3)
}
