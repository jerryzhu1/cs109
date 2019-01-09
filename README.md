# This repo is used for cs109 Data Science Course from Harvard
## Link: http://cs109.github.io/2015/pages/videos.html 

#### I translated the code from python2 to python3, errors fixed 

## HW0 (N-door Monty Hall Problem):
* Description: https://github.com/cs109/2015lab1/blob/master/hw0.ipynb
* Code: hw0.py
* Result:

![HW0](HW0.png)

<br>

## Quiz for course 02 (web-scraping and pandas):
* I skipped last 2 quizzes because the origin code not work well since the websites changed and algos not work anymore. (And I already familiar with web-scraping. Some projects I did: https://github.com/jerryzhu1/ProjectX)
* Code: ./02-DataScrapingQuizzes.ipynb
* Some tricks (for python 3):
    * Use pickle instead of cPickle
    * Use request instead of urllib2 (Can fix 404 issue)

<br>

## Lab 2 (web-scraping, lambda expressions and data cleaning):
* My code use the Wikipedia website of 'University of Toronto' instead of 'Harvard University'
* Code: ./Lab2.ipynb
* Some tricks (for python 3):
    * df.ix is deprecated, use df.loc and df.iloc instead
        * .loc for label based indexing
        * .iloc for positional indexing    

<br>

## Lab 3 (statistics and probability theory):
* Code: ./Lab3/Lab3-*.ipynb   
* Some tricks (for python 3):
    * For np.reshape(*newshape*), one shape dimension can be -1.
        * In this case, the value is inferred from the length of the array and remaining dimensions.

<br>

## Lab 4 (regression):
* Code: ./Lab4/Lab4-stats.ipynb   
* Some tricks (for python 3):
    * sklearn.cross_validation will be deprecated, use sklearn.model_selection.train_test_split instead.
    * Use result.summary2() instead of result.summary() when fit Logistic regression with statsmodels.api.logit,

<br>

## HW 1 (webs scraping and data cleaning):
* Code: ./HW1_Jerry.ipynb   
* Fixed some functions in origin material
* Some tricks (for python 3):
    * Use re (regex) instead of hnmatch
    * Use BeautifulSoup instead of web 
    * try, except is helpful since some web-sites no longer work

