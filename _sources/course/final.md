# Final Project

## Overview

For the final project, your job will be to use the **skills** you've acquired in this class to *ask questions* of a real-world dataset (or datasets).

You'll work independently, but we highly encourage you to come to office hours and lab to get feedback on your ideas.

## Grading and Deliverables

Your final deliverable (what you turn in) will be a Jupyter notebook with the following sections (See the table below); each section is worth a certain number of points, adding up to 17; the **final project proposal** is also worth 1 point.


| Section | Points | Description | Example 1| Example 2 |
| --------------- | ---- | ---------- | -------- | ------- |
| Introduction |  2 | What dataset are you looking at? Where/how was it created? What question(s) will you be asking? | Dataset about which construction people use in the [dative alternation](http://www.glottopedia.org/index.php/Dative_alternation): do they use NP ("She gave the man the box") or PP ("She gave the box to the man"). I will ask which features predict the use of one construction vs. the other. | |
| Data |  3 |  Descriptive statistics about the dataset: number of rows/columns, central tendency (mean/median/mode), variability, any missing values, etc. Should also include details of **cleaning** or **merging** datasets, should you need to do that. | The [dativeSimplified](https://rdrr.io/cran/languageR/man/dativeSimplified.html) dataset contains 903 observations with 5 variables; it was created by examining transcriptions of conversational data from Switchboard. No cleaning was required. | |
| Visualizations | 4 |2-3 graphs showing specific patterns or features you'd like to highlight. Each visualization should be accompanied by a short (1-2 sentences) description of what you think it shows. | Boxplot showing **length** of the *theme* argument when recipient is realized as a noun phrase vs. prepositional phrase. Barplot showing proportion of **NP** realizations depending on animacy of recipient. | | 
| Analyses |  4| 2-3 analyses discussed in class (e.g., linear regression, etc.) to address your question. Each analysis should be accompanied by a short (1-3 sentences) *interpretation*. Should also include **evaluation** of your model somehow, e.g., $R^2$, AIC, etc. | Logistic regression predicting **realization** (NP vs. PP) from Animacy and Length. Compare AIC of this model to a model omitting each variable in turn. | |
| Limitations and Ethical Issues| 3 | Discuss any limitations to your approach, as well as potential ethical issues (if relevant). | Variables could be inter-related; also only 4 predictor variables total. |  |
| Conclusion |  1 | Drawing a conclusion about the dataset and the questions you posed. | An NP realization is more likely for *longer themes*.| |


### Suitable datasets

There are two critical requirements for your dataset:

1. First, it should be about **Social science data**. If you're unsure whether a given dataset qualifies, feel free to ask us.  
2. Second, it should at least **3 variables** (but preferably more). We don't want you to just analyze a single variable, nor how a single variable relates to one other variable. Ideally, you would consider how multiple variables relate (e.g., in **multiple regression**). 

With that in mind, here are some ideas for **suitable datasets**. You can use one of these (and ask questions that you find interesting), but you can also feel free to find one of your own; that said, these datasets have been **vetted** a little more.

| Dataset | Social Science Domain | Description | Accessing |
| ------ | ---- | ---------- | ------- |
| World Bank Open Data | Economics / Global Development | Contains time series data for **many domains**, such as agricultural development, rural poverty, carbon emissions, and much, much more. | [Link to Data Bank](https://data.worldbank.org/); can browse by "indicator"; may require merging datasets for more information. |
| [World Happiness Report](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021) | Economics / Global Development | Dataset about global happiness scores; might need to be merged with other datasets to ask useful questions. | [Kaggle](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2021)|
| World Energy Consumption | Contains time series data about consumption of **energy** and **electricity**. | [Link on Kaggle](https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption) |
| SCARFS (Spontaneous, controlled, acts of reference between friends and strangers) | Linguistics/Communication | Data about friends and strangers playing the game **Taboo**, which clues they gave, and whether a trial was wason. | [GitHub Link](https://github.com/seantrott/scarfs) |
| [California Housing Prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices) | Economics | Information about the median house value for different districts in California. | [Link on Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices). |
| [Student alcohol consumption](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption?select=student-por.csv) | Public Health | Information about student behavior, including alcohol consumption and more. |  [Link on Kaggle](https://www.kaggle.com/datasets/uciml/student-alcohol-consumption?select=student-por.csv). |
| [Dative Alternation](https://rdrr.io/cran/languageR/man/dative.html) | Linguistics | Dataset about which construction people use in the dative alternation: do they use NP ("She gave the man the box") or PP ("She gave the box to the man"). | Online, or ask Professor Trott for `.csv` file |




### Project difficulty
Note that we will also take into consideration the **difficulty** involved in your project, especially in the **Data** stage (e.g., cleaning data, merging multiple datasets). 

Finding and merging multiple datasets is not *necessary*––i.e., you can get full points without it––but if you successfully clean and merge multiple datasets, it could "offset" lower performance on another section (e.g., **Visualization**); that is, you can think of it as a kind of unofficial extra credit.

Here are some examples of some things that, while not necessary, would make your project more difficult and thus more impressive:

- **Merging** multiple datasets that you've found to leverage data linkage.  
- **Comparing** multiple statistical models using *model selection* methods we've discussed in class. 

