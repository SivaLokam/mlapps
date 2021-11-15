import requests
from bs4 import BeautifulSoup
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def process():

    try: 
        url = 'https://www.ndtv.com/'
        response = requests.get(url)
        response_text = response.text
        soup = BeautifulSoup(response_text,'html.parser')
        
        #fetch the headlines
        lhs_div = soup.find('div',['hmpage_lhs'])#.find_all('a',['item_title'])   
        headlines = lhs_div.find_all('a',class_='item-title')
            
        content = [headline.text for headline in headlines]
        data = " ".join(content)
        to_be_removed = set(stopwords.words('english'))
        tokens = word_tokenize(data)
        
        data = pd.DataFrame(content,columns=['headline'])
        data.to_excel("content.xlsx")
        
    except Exception as e:
        print("Exceptin Occured")
        print(e)

if __name__=='__main__':
    process()