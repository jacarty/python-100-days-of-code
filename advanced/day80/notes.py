"""
Day 80 Goals: what you will make by the end of the day

Your Story

Today you will become a doctor, but not just any doctor. You will become Dr Ignaz Semmelweis, a Hungarian physician born in 1818 who worked in the Vienna General Hospital.

In the past, people didn't know about bacteria, germs, or viruses. People illness was caused by "bad air" or evil spirits. But in the 1800s Doctors started looking more at anatomy, doing autopsies and making arguments based on data. Dr Semmelweis suspected that something was going wrong with the procedures at Vienna General Hospital. Dr Semmelweis wanted to figure out why so many women in maternity wards were dying from childbed fever (i.e., puerperal fever).


Today you'll learn:

    How to make a compelling argument using data

    How to superimpose histograms to show differences in distributions

    How to use a Kernel Density Estimate (KDE) to show a graphic estimate of a distribution.

    How to use scipy and test for statistical significance by looking at p-values.

    How to highlight different parts of a time series chart in Matplotib.

    How to add and configure a Legend in Matplotlib.

    Use NumPy's .where() function to process elements depending on a condition.
    """


"""

Today you've learned

    How to use histograms to visualise distributions

    How to superimpose histograms on top of each other even when the data series have different lengths

    How to use a to smooth out kinks in a histogram and visualise a distribution with a Kernel Density Estimate (KDE)

    How to improve a KDE by specifying boundaries on the estimates

    How to use scipy and test for statistical significance by looking at p-values.

    How to highlight different parts of a time series chart in Matplotib.

    How to add and configure a Legend in Matplotlib.

    Use NumPy's .where() function to process elements depending on a condition.

The Tragic Story of Dr Semmelweis

Gather round, gather round. Now I'll tell you how our story ends. Despite the incredible evidence in favour of Dr Semmelweis' theory - that childbed fever was caused by some "substance" (which today we know as bacteria) from autopsy room corpses - was rejected by the medical community at the time. But why?! 

Part of the reason is that Semmelweis was not very tactful. He made it look like doctors were giving childbed fever to women (which they in fact were). This is not something people wanted to hear.

However, he also published his data in the form of long tables without any data visualisations:

The long tables made it very hard to see what's actually going on! Also, at the time statistics and statistical arguments were quite uncommon in the field of medicine.

Eventually, Dr Semmelweis belligerent campaigning made him some powerful and influential enemies. He lost his job at the Vienna hospital, and doctors gave up washing their hands with chlorine. As Dr Semmelweis grew older he got even angrier and eventually quite "strange". This was either the immense frustration or possibly a result of another disease like Alzheimer's or syphilis. In 1965, at the age of 47, Dr Semmelweis was committed to a mental asylum. And at the asylum, he was probably beaten since he eventually died of sepsis, a complication of an infection in the bloodstream. The tragic irony is that sepsis is a similar kind of disease that he fought so hard to prevent in women who died from childbed fever. It wasn't until 20 years later with Louis Pasteur's work on germ theory that Dr Semmelweis' work gained acceptance. RIP Dr Semmelweis. 

"""