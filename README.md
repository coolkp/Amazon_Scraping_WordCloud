# ENGR113
Wordcloud from a scraping amazon reviews
## Dependencies
  ` pip install scrapy wordcloud requests matplotlib  pandas`
## Run Scraping
`scrapy runspider amazon_reviews_scraping/amazon_reviews_scraping/spiders/amazon_review.py -o reviews.csv`
## Generate Word Cloud
` python3 word_cloud.py `
## Product Link
(https://www.amazon.com/LifeStraw-Personal-Camping-Emergency-Preparedness/dp/B006QF3TW4/ref=sr_1_1_sspa?ie=UTF8&qid=1547522373&sr=8-1-spons&keywords=water+filter+outdoor&psc=1)
