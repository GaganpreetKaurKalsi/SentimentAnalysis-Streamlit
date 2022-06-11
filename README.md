![GaganpreetKaurKalsi (1600 × 840 px) (3)](https://user-images.githubusercontent.com/54144759/173081855-4057d6b4-2e57-475b-961e-5cdb91604bda.png)

<br>

# Sentiment Analysis App 😊😐😔😡

<br>

## About
**A sentiment analysis application built using Streamlit( An open source framework to build web applications in python )**

Sentiment Analysis is one of the most famous applications of Natural Language Processing. Wherever data is present, we can apply it. It applies to all types of data, from text to audio to video to image. Data in any form can be processed to get sentiments out of it. The objective of the project is to create a web application which will harbor all sorts of applications in the field of sentiment analysis from applying it on text to analyzing images.

<br>

## Live Link
**Hosted on streamlit**

### 🔗 https://share.streamlit.io/gaganpreetkaurkalsi/sentimentanalysis-streamlit/main/app.py
<br>

## Project Specifications

**Below are the libraries and frameworks used to create the project**
- **Web Framework** :- Streamlit
- **Graphs and Images** :- PIL, plotly, cv2
- **Libraries for sentiment analysis** :- textblob, nltk(vader), flair, text2emotion, fer
- **Libraries for API requests** :- requests, json

<br>

## Project Components

**The project currently contains 3 applications :-**
1. **Text** - Applying sentiment analysis on text given by the user.
2. **IMDb movie reviews** - We get review data based on movie entered by user from the IMDb API and process the same to obtain emotions of people regarding the movie.
3. **Image** - Here we analyze sentiments out of image uploaded by the user. We detect faces and then analyze sentiments for each.  We also calculate the sentiment of image as a whole.

<br>

## Video Demonstration

**Application 1 - User Input**          

https://user-images.githubusercontent.com/54144759/173093720-5b753229-3ea8-428d-a4cb-1384c738382e.mp4

<br>

**Application 2 - IMDb reviews**   

https://user-images.githubusercontent.com/54144759/173201517-909e9bc8-19cc-4667-8a8f-bd19fba75a0d.mp4

<br>

**Application 3 - Image analysis** 

https://user-images.githubusercontent.com/54144759/173202138-a7b0648a-ba13-471d-88d2-c91432958aab.mp4


<br>

# Important information

## **IMDb API**

API documentation link - https://imdb-api.com/api/#Reviews-header

<br>

To work with the API, you need to first **create an API key**.
To create an API key, **register** on the site mentioned above and a unique key will be generated for you. We will use this key to make successful requests.


***Note : API call limit per day is 100***

<br>

### **API specifications**
To get reviews, we will need to make 2 API calls. 
1. Get movies based on user input. Each movie received will have a unique id.
2. Get reviews for a movie by passing the unique id associated with it received from the above API call.


**Movie API** - https://imdb-api.com/en/API/SearchMovie/{apiKey}/{movieName}    
    
**Review API** - https://imdb-api.com/en/API/Reviews/{apiKey}/{id}

<br>

## Models used
There are multiple libraries available in python for sentiment analysis. Let's see them below 👇

- **TextBlob** - TextBlob is a Python library for processing textual data. It provides a simple API for diving into common (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.
- **Flair** - A very simple framework for state-of-the-art NLP. It is a powerful NLP library which allows you to apply state-of-the-art natural language processing (NLP) models to your text, such as named entity recognition (NER), part-of-speech tagging (PoS), etc.
- **Vader** - VADER (Valence Aware Dictionary and Sentiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. 
- **text2emotion** - text2emotion is the python package which will help you to extract the emotions from the content. It processes any textual message and recognize the emotions embedded in it. It is compatible with 5 different emotion categories as Happy, Angry, Sad, Surprise and Fear.

<br>

*__Note :-__* 
1. textblob, flair and vader provide polarity score where text is declared in either of 3 states (POSITIVE🙂, NEGATIVE☹️, NEUTRAL😐)
2. text2emotion is the only library among the others mentioned above which can classify text in 5 emotion categories (HAPPY😊, ANGRY😡, SAD😔, SURPRISE😲, FEAR😨)

<br>

## Project development ideas

**Below mentioned applications can be implemented as a future scope -**
- Tweets analysis using Twitter API
- Sentiment analysis on Live video streaming
- Sentiment analysis of Audio data
- Sentiment analysis of data received from site given by user using web scraping in python.

<br>

## Thank You!
Thank you. **I hope you liked the project**. 

If you really did then don't forget to **give a star**⭐ to this repo. It would mean a lot.
