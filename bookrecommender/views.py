from django.shortcuts import render
import pickle
import os
from django.conf import settings
import numpy as np

def open_model(file_name):
    models_folder = settings.BASE_DIR / 'bookrecommender'
    file_path = os.path.join(models_folder, os.path.basename(file_name))
    popular_df = pickle.load(open(file_path, 'rb')
                         )
    return popular_df

popular_books = open_model('./popular_books.pkl')
books = open_model('./books.pkl')
similarity_scores = open_model('./similarity_scores.pkl')
ratings = open_model('./ratings.pkl')

# Create your views here.
def home(request):
    title = "Welcome to Book Recommendation System"
    context = {
        "title": title,
        "book_name": list(popular_books['Book-Title'].values),
        "author": list(popular_books['Book-Author'].values),
        "image": list(popular_books['Image-URL-M'].values),
        "votes": list(popular_books['num_ratings'].values),
        "rating": list(popular_books['avg_rating'].values),
        "loop_times": range(len(list(popular_books['Book-Title'].values)))
    }
    return render(request, "home.html", context)

def recommend_book(book_name):
    index = np.where(ratings.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:7]
    result = []
    for idx in similar_items:
        item = []
        results_df = books[books['Book-Title'] == ratings.index[idx[0]]]
        results_df = results_df.drop_duplicates('Book-Title')
        item.extend(list(results_df['Book-Title'].values))
        item.extend(list(results_df['Book-Author'].values))
        item.extend(list(results_df['Image-URL-M'].values))
        result.append(item)
    return result

def recommend(request):
    title = "Recommend Books"
    context = {
        "title": title
    }
    # try:
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        result = recommend_book(book_name)
        context = {
            "title": title,
            "result": result
        }
    # except:
        # pass
    return render(request, "recommend.html", context)