# Book-Recommendation-System
The system is built based on Collaborative filtering. Collaborative filtering is a technique that can filter out items that a user might like on the basis of reactions by similar users. The following steps have been followed in bringing up the project
1. The dataset is obtained from Kaggle which has 3 files - Books, Users, Ratings.
2. Data preprocessing - The unwanted columns are removed and duplicates are dropped from the dataframe.
3. Criterias - Users who have rated more than or equal to 200 books and books that have more than or equal to 50 ratings are considered.
4. A pivot table is formed with Book-Title as index, User as Column and values as Book-Rating.
5. Similarity scores are calculated using cosine_similairty from sklearn.
6. From the result, we can filter the most popular books and also recommend books based on the title given by the user.
7. A simple website for easy access to the user has been created using Django.

## Home Page
Home page has the top 50 books based on the user ratings.
![Screenshot 2023-10-16 105250](https://github.com/bhavanap12/Book-Recommendation-System/assets/23119773/d1098843-2f0d-469d-a8e7-7f73bca48b26)

## Recommend
Recommend page has one input column for user. User can key in the title and get the top 7 recommended books.
![Screenshot 2023-10-16 105302](https://github.com/bhavanap12/Book-Recommendation-System/assets/23119773/fb40ab19-25cf-4482-b2ed-f1bf25e41a53)

### Example 1 - 1984
1984 is a dystopian novel written by George Orwell. Similar dystopian novels like Animal Farm, The Handmaid's tale, Fahrenheit 451 have been recommended.
![Screenshot 2023-10-16 105436](https://github.com/bhavanap12/Book-Recommendation-System/assets/23119773/907403fe-bb70-40f3-80c0-442672294573)

### Example 2 - Animal Farm
Animal Farm is also a dystopian novel written by George Orwell. It has been recommended when 1984 is given as the input in the above example and here, 1984 is recommended when Animal Farm is keyed in.
![Screenshot 2023-10-16 105454](https://github.com/bhavanap12/Book-Recommendation-System/assets/23119773/c5867a2b-65b2-4b37-a3d0-1a75ab59dad6)

### Example 3 - Harry Potter and the Prisoner of Azkaban (Book 3)
The Prisoner of Azkaban is a fantasy themed novel written by JK Rowling and is part of Harry Potter series. Hence other books in the series and Lord of the Rings which is also a part of the fantasy series have been recommended.
![Screenshot 2023-10-16 105516](https://github.com/bhavanap12/Book-Recommendation-System/assets/23119773/5d084662-9138-47e7-8ce1-4238267560ac)

# Technologies and languages used:
* Python
* Django
* Pandas
* Jupyter Notebook
* Scikit-Learn
* HTML
* CSS    
 
