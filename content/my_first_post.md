Title: How to learn SQL from scratch by yourself?
Date: 2026-04-24
Category: Data Science
Tags: SQL
Summary: In this post, I will give the step to learn and understand SQL.

Coming from non-tech background, SQL was like a foreign-language to me. I didn't understand the needs of the SQL. Isn't Python / Code will do all the heavylifting? (My thinking back then). But then I realize, SQL is mandatory for some certain reasons that Python is not capable of. Once knowing the purpose of it, then I know and understand how to use it properly.

# Why SQL?
SQL is a Structured Query Language (yes, it's an abbreviation). Basically, SQL is a language that you use to communicate with the database and return the data that you need. The reason why SQL is powerful because of how easy it is to interpret the language as well as the data retrieval process is already masked behind the SQL syntax. You may think SQL as the translator in daily life analogy.

# SQL Structure
SQL syntax formed into several parts, they are:
- `FROM` statement: Define where to get the data from
- `WHERE` statement: Define the filter that we want to apply for the data we want to retrieve
- `SELECT` statement: Define the field / columns we want to retrieve
- `ORDER BY` statement: Define how you want to order the results
Actually, there are more syntaxes, but these are the basic foundations of the SQL structure. You may take a look at the data below:
```sql
SELECT
    date,
    store_id,
    city_id,
    item_id,
    item_name,
    num_orders
FROM coffee_orders
WHERE
    date >= "2026-01-01"
    AND date <= "2026-01-31"
ORDER BY date, store_id, city_id, item_id -- Can be change to column numbers (1,2,3)
```
The SQL syntax above tells the machine like follows:
> _"Hey machine, please help me to retrieve the information **FROM** `coffee_orders`, please filter the data **WHERE** the date is between `"2026-01-01"` and `"2026-01-31"`. From the data, please help me to retrieve and **SELECT** these informations: `date`, `store_id`, `city_id`, `item_id`, `item_name`, and `num_orders`. Please also do sort the data with **ORDER BY** `date`, `store_id`, `city_id`, and its `item_id`."_

Behind the scene, there are bunch of processes happening, but worry not, you don't have to understand what the machine is doing, you just focus to construct your needs. Basically, from the above information you tell to the machine, I put the syntax in certain orders. This is actually _how the SQL is processed_ in every SQL syntax and understanding this order of operation will be important for you!

# I don't know where to start, where should I learn?
This is exactly the questions I had 3 years ago, but you have blessed with the opportunity to learn from many sources. Some of the source that can be the best places for you to grind are:
- datalemur.com
- hackerrank.com

If you have any questions, feel free to have a discussion!

Have a nice day!