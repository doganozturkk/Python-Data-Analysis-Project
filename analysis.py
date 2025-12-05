
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

df = df.dropna()

avg_rating_by_genre = df.groupby("genre")["rating"].mean()
avg_rating_by_genre.plot(kind="bar")
plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.savefig("genre_ratings.png")
plt.close()

top10 = df.nlargest(10, "rating")
top10.plot(x="title", y="rating", kind="bar")
plt.title("Top 10 Movies by Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10.png")
plt.close()

print("Analysis completed! Charts saved.")
