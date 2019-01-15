import csv
from wordcloud import WordCloud

your_list = ''
target = ['taste','lightweight','price','cheap','easy','fit','backpacking','bag','little','small','easy use','clean','filter']
with open('reviews.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = '\t'.join([i[1] for i in reader])
print(your_list)
word_list = your_list.split(' ')
new_list = []
for word in word_list:
    if word in target:
        new_list.append(word)
new_string = ' '.join(new_list)
print(new_string)
wordcloud = WordCloud().generate(new_string)
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(new_string)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
