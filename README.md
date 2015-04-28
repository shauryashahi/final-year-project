#Can multi-armed bandit and Bayesian methods save life and money?

_Shaurya Kumar Shahi             Himanshu
Rai Jain_

_BE/1413/2011                         BE/1383/2011_


*Project Guide: Dr. Sandip Dutta*


*Abstract*

The general problem of choosing the best alternative solution from several possible
ones comes up in different fields. Most real world problems involve complex
phenomenon and solution is needed under tight deadline. Statistical hypothesis
testing has emerged as the most popular method to solve such problems of
choice. Some examples include medical drug trials, social policy experiments,
and web A/B testing. Classical statistical hypothesis testing involves
enumerating the available choices (formally called hypothesis), and randomly
assigning one of the choice to a test subject. This random assignment of the
choice is repeated for all test subjects and the performance of each available
choice is tabulated and compared using standard statistical methods. In a drug
trial patients are randomly assigned different alternative drugs (often one
drug and one placebo is used) and the performance of the drugs is tested by
comparing the fraction of people who were cured with each of the drug being
tested (in case of terminal illness average lifetime after treatment may also
be compared). In a web A/B test a visitor to the website is randomly shown a
variation of the user interface (UI) and the average revenue generated using
different UI variations are compared. 

This approach to testing has worked well, but has a big flaw.
In a randomized experiment we use the sub optimal solution for several test
subjects. We ignore the possible signals from the first few test subjects when
deciding which solution to choose for a later test subject. This suboptimal
choice may result in loss of revenue in case of a web A/B test and possible
loss of lives in case of drug trials. In this project we will explore alternate
ways to conduct these randomized experiments, namely Bayesian approach, and
multi armed bandit approach, which try to use the signals from early subjects
when making a choice for later subjects. We will conduct a parametric study and
compare these methods for different practical cases. The parametric study will
involve changing both the parameter of the models, and the parameters of the
problem (e.g., cost/click, probability of click, for a web A/B test), and
compare the performance of each method for different combination of the
parameters. We expect to deepen the understanding of the similarity and
differences between common approaches used to solve very important practical
problems in the real world.
