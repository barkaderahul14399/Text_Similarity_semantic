# this file contains fuction for calculating similarity yscore between two sentences
from thefuzz import fuzz
import re

def sim_score(s1,s2):
     score=fuzz.ratio(s1,s2)
     print(score)
     pr=fuzz.partial_ratio(s1,s2)
     tsr=fuzz.token_sort_ratio(s1,s2)
     ptsr=fuzz.partial_token_set_ratio(s1,s2)
     sum=score+pr+tsr+ptsr
     avg=(sum/4)*0.01
     avg=round(avg,2)
     return(avg)


def text_preprocessing(txt):
    # Define the regular expression pattern to match text and digits to remove any unusual characters from text
    pattern = re.compile(r'[a-zA-Z0-9]+')
    # Find all matches in the text
    matches = pattern.findall(txt)
    # Join the matches into a single string
    cleaned_text = ' '.join(matches)
    # Print or further process the cleaned text
    print(cleaned_text)
    return(cleaned_text)


#sim_score("bye, we wiil meet tomarrow","hii how are u")