import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import time as t
from colorama import init,Fore
# def load_data(path='imdb_top_1000.csv'):
#     try:
#         file=pd.read_csv(path)
#         file['combined_features'] = file['Genre'].fillna('') + ' ' + file['Overview'].fillna('')
#         return file
#     except FileNotFoundError as e:
#         print('File Not Found')
#         exit()
# moviedata=load_data()
# tfidf=TfidfVectorizer(stop_words='english')
# tfidf_matrix = tfidf.fit_transform(moviedata['combined_features'])
# cosine_sim=cosine_similarity(tfidf_matrix,tfidf_matrix)

# def list_genre(df):
#     return sorted(set(genre.strip() for i in df['Genre'].dropna().str.split(',') for genre in i))
# genres=list_genre(moviedata)

# def recommend_movies(genre=None, mood=None, rating=None, top_n=5):

#     filtered_df = moviedata

#     if genre:

#         filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]

#     if rating:

#         filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]

#         filtered_df = filtered_df.sample(frac=1).reset_index(drop=True) # Randomize the order

#         recommendations = []

#     for idx, row in filtered_df.iterrows():

#         overview = row['Overview']

#         if pd.isna(overview):

#             continue

#         polarity = TextBlob(overview).sentiment.polarity

#         if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or   polarity >= 0)) or not mood:

#             recommendations.append((row['Series_Title'], polarity))

#         if len(recommendations) == top_n:

#             break

#     return recommendations if recommendations else "No suitable movie recommendations found."


# while True:

#     rating_input = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()

#     if rating_input.lower() == 'skip':

#         rating = None

#         break

#     try:

#         rating = float(rating_input)

#         if 7.6 <= rating <= 9.3:

#             break

#         print(Fore.RED + "Rating out of range. Try again.\n")

#     except ValueError:

#         print(Fore.RED + "Invalid input. Try again.\n")

#     # Processing animation while finding movies

#         print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True)

#         processing_animation() # Small processing animation while finding movies

#         recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)

#         if isinstance(recs, str):

#             print(Fore.RED + recs + "\n")

#         else:

#             display_recommendations(recs, name)

#         while True:

#             action = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()

#             if action == 'no':

#                 print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🎬🍿\n")

#                 break

#             elif action == 'yes':

#                 recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)

#                 if isinstance(recs, str):

#                     print(Fore.RED + recs + "\n")

#                 else:

#                     display_recommendations(recs, name)

#             else:

#                 print(Fore.RED + "Invalid choice. Try again.\n")

#             # Main program

#             def main():

#                 print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")

#                 name = input(Fore.YELLOW + "What's your name? ").strip()

#                 print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")

#                 handle_ai(name)

#             if __name__ == "__main__":

#                 main()



df = pd.read_csv("imdb_top_1000.csv", sep=",", quotechar='"', engine="python")
df.columns = df.columns.str.strip()   # remove extra spaces

print(df.head(1))        # show first row
print("\nOne column (Genre):")
print(df['Genre'].head(1))