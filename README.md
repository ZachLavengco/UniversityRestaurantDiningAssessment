### Description
For this project have used data science techniques to determine the quality of restaurant food around college campuses.

### Problem
To understand the current restaurant experience ratings across the top 100 college campuses. These ratings were also used to compare to specific campuses (for our report we used UIC). There were many questions to answer to solve this problem, including:
-Enjoyment of restaurants?
-Divesity of restaurants?
-Availability of restaurants?
-How do specific campuses like UIC compare?

### APIs / Data Collection
The tools we used for this project include:
College Scorecard API:
    -Used to gather data the data for the top 100 populated colleges
Google Maps API:
    - For college addresses
Yelp API:
    - Gather all restaurant information per college address

With these three API we collected the following data:
Each restaurant within a 1 mile radius of each college campus:
    - Restaurant name
    - Restaurant rating
    - Food prices
    - Distance

As you can imaging aggregating this data took a substantial amount of time (100s of Yelp API calls representing all the restaurants for each college campus) and thus would be difficult to send as a file.

In addtion to restaurant data, the data from each of the top 100 schools (based on population) included:
    - Student population
    - College address

### Visualizations
Working with the average ratings for UIC and the top 100 colleges based on population, we pulled data from the yelp API and retrieved the reviews of the nearest restaurants that are within a half a mile radius from the school. After cleaning and processing the data we can see that when we calculate the average ratings for UIC yelp reviews. UIC stands at a 3.71/5.0, meaning, UIC is above average which is good but not the best. In comparison to the top 100 colleges which scored a 3.48/5.0. There are many possible factors that can attribute to this such as proximity from school, price, and of course the quality of the food.

If we take a look at the availability score visualization, we can see that it is based on average price and average distance, this is how we defined availability. In our findings, we noticed that most restaurants average one to two dollar sign ratings according to yelp. This means, restaurants nearby colleges are fairly inexpensive. When we take UIC into account (red dot), we can see UIC price average is roughly 1.5 dollar signs and is less than 5,000 distance away from restaurants which puts UIC in the top percentile of schools with the highest availability

Our last visualization is the income/price visualization. This visualization shows the income to price metric of UIC vs the top 100 universities. We used income to price as a metric for the affordability of the restaurants for the university demographic. Income being the average family income of the students and price being the average price of the restaurants. It is important to note that the price is given as a score from 1 - 4, where 1 is least expensive and 4 is the most expensive. So with the income to price metric the higher the score the better the restaurants affordability for the students at the university and as you can see UIC falls below the average of the top 100 universities meaning our restaurants are not as affordable for our students.

### ML/Statisics Models
The first model we made for our ML analysis was an attempt to correlate population and average ratings for each college campus by using linear regression. With the top 100 colleges, we already have obtained a training set to work with. The test set we used for this analysis was UIC. Our hypothesis was that smaller colleges would have a smaller ranger of options but because of this the quality of each of these restaurants would be higher. However, the actual data pulled for UIC does not fit the prediciton line: despite having a smaller population, the ratings for all of the restaurants was average.

The next model was made to find a correlation between the population of schools and the number of restaurant categories available. Our hypothesis was that schools with a lower population will have a lower number of categories. We assumed that, in general, bigger schools will have more fast food and chain restaurants that are similar to one another to account for their big population. We did linear regression to rest the data of the top 100 schools and found that UIC stands well above average and does not fall within the prediciton curve; UIC has a great amount of diversity despite having a lower population.

### UIC Compared to Top 100

In our restaurant dining assessment of UIC, we determined that UIC's dining experience was above average compared to the top 100 college campuses by population. These were the final results based on our visualizations and anaylsis:
    - Ratings: Above Average
    - Availability: Above Average
    - Income to Price: Below Average
    - Pop/Avg Rating: Below Average
    - Diversity: Above Average

UIC is above average in comparison to the top universities yet lacks in affordability for our demographic, and due to our lower population we’re supposed to have higher average restaurant ratings when taking into account our schools relatively smaller population.
