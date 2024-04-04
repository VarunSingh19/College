from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text
text = "Python is a high-level programming language that is widely used for various purposes such as web development, data analysis, machine learning, and artificial intelligence."

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
