import streamlit as st
import streamlit.components.v1 as components
from textblob import TextBlob
from PIL import Image
import text2emotion as te
import plotly.graph_objects as go
import requests
import json
import modals
import pandas as pd


baseURL = 'https://imdb-api.com/en/API'
apiKey = 'k_9usdv193'

def plotPie(labels, values):
    fig = go.Figure(
        go.Pie(
        labels = labels,
        values = [value*100 for value in values],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    st.plotly_chart(fig, use_container_width=True)

globalData = {
    "userSearch": "Harry Potter",
    "result": [
        {
            "title": "Harry Potter and the Sorcerer's Stone",
            "image": "https://imdb-api.com/images/original/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_Ratio0.7273_AL_.jpg",
            "reviews": [
                "Great fun!",
                "Gem of a children's film and a fine adaptation of the Rowling novel",
                "Good Start to the Series",
                "Great chemistry set up for the rest of the series",
                "Charming and Endearing!",
                "Year 1 at Hogwarts",
                "Hogwarts or hogwash?",
                "Good but too long and with few strong characters",
                "Part 1",
                "\"There won't be a child in our world who doesn't know his name.\"",
                "Where it all began.",
                "Off to a Successful Start",
                "Harry Potter and the Philosopher's Stone",
                "A Surprise",
                "First Harrry Potter entry in which he makes friends and battles mysterious evil forces",
                "DVD owners please read.",
                "Yes, I believe it deserves all the 8, 9, and 10 votes it has gotten.",
                "Overrated but entertaining",
                "We're Off to See the Wizard",
                "The magic begins",
                "Hermione's Mouth",
                "Ahh, the magic begins.",
                "Bloody Brilliant ? Bloody Crap More Like",
                "Nice",
                "Harry Potter is a bore!"
            ]
        },
        {
            "title": "Harry Potter and the Goblet of Fire",
            "image": "https://imdb-api.com/images/original/MV5BMTI1NDMyMjExOF5BMl5BanBnXkFtZTcwOTc4MjQzMQ@@._V1_Ratio0.7273_AL_.jpg",
            "reviews": [
                "Good though rushed",
                "Harry Potter and the TriWizard Cup.",
                "See the movie for action, read the book for story",
                "Dark and engrossing!",
                "what the hell?!",
                "A huge, HUGE disappointment...",
                "Dark, and funny.",
                "HP4",
                "Fourth episode with Harry Potter and friends fighting dark forces in this amazing adventure",
                "The worst Potter film yet.",
                "A movie standing alone",
                "Best Potter Yet",
                "Shortest 2.5 hour movie",
                "Pretty darn good",
                "horrible idea to make it one movie and not two",
                "It's a movie, NOT the book",
                "They got Dumbledore all WRONG!! and lots of other stuff too",
                "Rowling's Roller-coaster Gathers Pace",
                "The PR Machine Fails the Product... Again.",
                "Darker, funnier, reveling in spectacular CGI, teenage angst and Brit-humor",
                "The Best Of The Harry Potter Movies By Far!!!!!",
                "Harry Potter and the Goblet of Fire Review",
                "Very Good",
                "Hello... plot? Are you under the invisible blanket?",
                "Entertaining but too short and too many omissions"
            ]
        },
        {
            "title": "Harry Potter and the Deathly Hallows: Part 2",
            "image": "https://imdb-api.com/images/original/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_Ratio0.7273_AL_.jpg",
            "reviews": [
                "The series ends on a very strong note.",
                "End of an era... End of our childhoods... End of Harry Potter",
                "My childhood..",
                "Harry Potter and the Deathly Hallows: Part II gets everything right to send off Harry on a cinematic high",
                "Gives meaning to the phrase, save the best until last",
                "Good Movie, But a Disappointing & Unsatisfying End to the series...",
                "An Exhilarating and Beautiful Conclusion to a Magnificent Saga.",
                "An exhilarating action-packed spectacle that delivers a magnificent finish to the beloved fantasy franchise",
                "In the future AVOID any movie with Mr. Yates as director",
                "A breathtaking finale to an amazing series",
                "Satisfying end to the series",
                "Better Ending",
                "Jarndyce and Jarndyce",
                "LIGHTNING HAS STRUCK",
                "Emotional Conncetion",
                "\"It all ends\" well",
                "Action packed, genuine heart and emotional drama made this movie, a very engrossing magical epic spectacle. It has everything, a finale should have.",
                "Am I the only one to be disappointed??? ***spoilerrific***",
                "Too Bad It Ended Like This",
                "Epic End",
                "2 Films for 1 Book, yet misses 1/4 of the story....",
                "A middling series ends on a low-point.",
                "They finally got it right!",
                "The Movie Of The Year",
                "I can't believe this is the last Harry Potter review I'll ever get to write!"
            ]
        },
        {
            "title": "Harry Potter and the Prisoner of Azkaban",
            "image": "https://imdb-api.com/images/original/MV5BMTY4NTIwODg0N15BMl5BanBnXkFtZTcwOTc0MjEzMw@@._V1_Ratio0.7273_AL_.jpg",
            "reviews": [
                "My Favorite Of The Harry Potter Films",
                "Darkest and best one yet",
                "Finally, a movie that captures the books' magic",
                "Best of the Harry Potter film series",
                "Best Film of the Series; One of the Best Films of All Time",
                "last of the really sweet episodes..",
                "Abstract and dark themes abound; still the most mature HP entry",
                "A Dark and Impressive Film",
                "A visual feast with bite",
                "So dark, I love it",
                "The best of the Harry Potter films so far",
                "Creepy, quirky and utterly gorgeous - Spoilers",
                "A new director who proves equal to the task.",
                "Best of the three",
                "\"A child's voice, however honest and true, is meaningless to those who've forgotten how to listen.\"",
                "Writing in character again --- on Prisoner of Azkaban",
                "Beautifully dark, but with holes",
                "Charming and Extraordinary",
                "A valiant effort bringing a truly complex book to screen!",
                "Mischief managed!",
                "Care for tea?",
                "The best of the Harry Potter movies!",
                "More than just the best \"Potter\" film (to date). It can also hold it's own against the best of fantasy entertainment.",
                "The First Potter Film to Feel Like a Film",
                "Following to Harry Potter films as exciting and amusing as the former and subsequent entries"
            ]
        },
        {
            "title": "Harry Potter and the Deathly Hallows: Part 1",
            "image": "https://imdb-api.com/images/original/MV5BMTQ2OTE1Mjk0N15BMl5BanBnXkFtZTcwODE3MDAwNA@@._V1_Ratio0.7273_AL_.jpg",
            "reviews": [
                "Dark and thrilling, this prelude packs genuine suspense, heart and the occasional exhilarating action to deliver an engrossing magical spectacle",
                "totalitarianism takes over in the wizarding world",
                "A strong beginning to a grand finale. The best film of the franchise so far.",
                "My personal favourite of the Harry Potter movies so far",
                "no longer just for kids; a dark adult-fantasy movie with a couple of lulls",
                "A Nutshell Review: Harry Potter and the Deathly Hallows: Part 1",
                "It's like everyone forgot this series was supposed to be fun",
                "The-Film-That-Should-Not-Have-Been-Made",
                "This gets better and better. Let's get ready for the final one!!",
                "Period Drama Slow",
                "A grown-up movie that fits a grown-up Potter",
                "Deathly Hollow",
                "Overly melodramatic at times, a roller coaster ride with highs, and lows, but very little middle ground.",
                "Wickedly awesome - One of the best",
                "Just Part 1, Yet Excellent Enough on its Own Merits",
                "These are getting worse",
                "Well, the fans asked for it, and they got it",
                "Long and Drug Out",
                "A big improvement in the series!",
                "I love this movie!",
                "The Best and Most Underrated Harry Potter Movie",
                "The best Harry Potter ever...are you kidding?",
                "A Dark, Amazing and Wicked Beginning of the End",
                "No emotion, disappointing film",
                "Harry Potter & the Movie of Beautiful Scenery and Not Much Else (also knows as Harry Potter goes Camping!)"
            ]
        },
        {
            "title": "Harry Potter and the Chamber of Secrets",
            "image": "https://imdb-api.com/images/original/MV5BMTcxODgwMDkxNV5BMl5BanBnXkFtZTYwMDk2MDg3._V1_Ratio0.7273_AL_.jpg",
            "reviews": [
                "Darker fantasy than the first Potter film...brisk despite its length...",
                "A wonderful journey into a world where magic is, indeed, real.",
                "Back to school, Mr. Potter: a superior second installment",
                "Entertaining, And Ranks Somewhere In The Middle Of The HP Films",
                "That bit of magic returns",
                "I want more!!!",
                "OK, but I think for fans only",
                "Somehow manages to be funnier than the first!",
                "The best Harry Potter film?",
                "The Chamber of Secrets has been opened at long last!!!!",
                "I absolutely LOVED this movie",
                "The first milestone. Sinister mystery of Hogwarts.",
                "A very good film...stop hating...",
                "The story starts here!",
                "A good follow up to Potters first outing",
                "A great sequel!",
                "Not the target of this movie...but still enjoyable.",
                "You're bland, Harry...",
                "Character palette and story drives me to read the books",
                "Zooms Along",
                "Very good but exhausting",
                "More Uninspired Magic from Chris Columbus",
                "better than the first",
                "Quite boring!",
                "Shakespearian Architecture"
            ]
        },
        {
            "title": "Harry Potter and the Half-Blood Prince",
            "image": "https://imdb-api.com/images/original/MV5BNzU3NDg4NTAyNV5BMl5BanBnXkFtZTcwOTg2ODg1Mg@@._V1_Ratio0.7273_AL_.jpg",
            "reviews": [
                "Darker and Better",
                "Love and other wars",
                "All The Least Important Parts of the Book in Movie Form.",
                "The Best Book...The Worst Movie!",
                "So far, the best of the Harry Potter films!",
                "Reaches neither the depth nor the complexity of the book but still pretty damn impressive",
                "The binding is really fragile Harry Potter and the Half-Blood Prince",
                "Harry Potter and the Half-Blood Prince, or Ron Weasley and the Half-A**ed Romance?",
                "Dark, funny, and not weighed down by too much exposition.",
                "Horribly Awful Garbage",
                "Powerful and stunning! One of the best fantasy films ever made",
                "It's Love Potions That Are Most In Demand",
                "To say I was disappointed is an understatement, Half Blood Prince is among the weakest in the series.",
                "The weakest film in the series",
                "Are you freaking kidding me!!?",
                "Far and away the best in the series",
                "A major disappointment",
                "Abrupt decline in quality",
                "Worst Interpretation EVER",
                "How to enjoy this movie if you're a fan of the HP Books",
                "An engaging set-up for the final episodes",
                "My least favourite hp movie",
                "\"Half-Blood Prince\" Is a Half-Assed Movie",
                "Mixed thoughts",
                "Hormones over excitement as part six is merely an appetiser to the double billed closure to come."
            ]
        },
        {
            "title": "Harry Potter and the Order of the Phoenix",
            "image": "https://imdb-api.com/images/original/MV5BMTM0NTczMTUzOV5BMl5BanBnXkFtZTYwMzIxNTg3._V1_Ratio0.7273_AL_.jpg",
            "reviews": [
                "My Least Favorite Up To This Point, Maybe Overall",
                "Playtimes over",
                "Slow First Half Picks Up in Finale",
                "Separate the film from the book, and you will be impressed",
                "Nothing Up My Sleeve",
                "Order of the Plot-Holes",
                "Best out of the five, but if you are only going to focus on the plot problems, don't bother because your whining will only give the rest of us headaches...",
                "A great movie, yet completely surpassed by the book",
                "Simply Put...Phenomenal (A Book-Reader's Review)",
                "Order of the Phoenix is about the Real World",
                "Who ruined Harry Potter?",
                "JK's biggest book to the screen, mission impossible? Mission accomplished!!!",
                "Riddikulus",
                "Trashing J K Rowling --- Warner's $242 million Rip-Off!",
                "Tries hard, but lacks the charm of the other Potters",
                "We were so disappointed!",
                "Snivellus Snape gets what he deserves!",
                "Humorous, But Hard To Follow If You Haven't Read The Book",
                "Everything is going downhill",
                "Too Short, Too Little, TOO LATE!",
                "Slow Down!",
                "Never been so disappointed in my life",
                "Excellent, the magic is still alive",
                "Loved it",
                "The Magic is Gone"
            ]
        }
    ]
}

lastSearched = ""
cacheData = {}
        

def getMovies(movieName):
    response = requests.get('{baseURL}/SearchMovie/{apiKey}/{movieName}'.format(baseURL=baseURL, apiKey=apiKey, movieName=movieName))
    response = response.json()
    if(isinstance(response["results"], list)):
        movies = [{"id": result['id'], "title": result['title'], "image": result["image"], "description": result["description"]} for result in response["results"]]
        return movies
    else:
        st.error(response["errorMessage"])
        return []
def getFirst200Words(string):
    if len(string)>200:
        return string[:200]
    return string

def getReviews(id):
    res = requests.get('{baseURL}/Reviews/{apiKey}/{id}'.format(baseURL=baseURL, apiKey=apiKey, id=id))
    res = res.json()
    if (res["errorMessage"] != ""):
        st.error(res["errorMessage"])
        return []
    items = res["items"]
    if len(items)>20:
        items = items[0:20]
    reviews = [getFirst200Words(item["title"]+" "+item["content"]) for item in items]
    return reviews
    
    
    
def getData(movieName):
    print("Sending request to get movies!!!!!!")
    movies = getMovies(movieName)
    data = []
    for movie in movies:
        reviews = getReviews(movie["id"])
        data.append({"title": movie["title"], "image": movie["image"], "description": movie["description"], "reviews": reviews})
    return json.dumps({"userSearch": movieName, "result": data})


def displayMovieContent(movie):
    col1, col2 = st.columns([2,3])
    with col1:
        st.image(movie["image"], width=200)
    with col2:
        st.components.v1.html("""
                                <h3 style="color: #1e293b; font-family: Source Sans Pro, sans-serif; font-size: 20px; margin-bottom: 10px; margin-top: 60px;">{}</h3>
                                <p style="color: #64748b; font-family: Source Sans Pro, sans-serif; font-size: 14px;">{}</p>
                                """.format(movie["title"], movie["description"]), height=150)

def process(movieName, packageName):
    global lastSearched, cacheData
    if(lastSearched != movieName):
        data = getData(movieName)
        st.text(data)
        lastSearched = movieName
        cacheData = data

    else:
        data = cacheData
    st.text("")
    st.components.v1.html("""
                              <h3 style="color: #ef4444; font-family: Source Sans Pro, sans-serif; font-size: 22px; margin-bottom: 0px; margin-top: 40px;">API Response</h3>
                              <p style="color: #57534e; font-family: Source Sans Pro, sans-serif; font-size: 14px;">Expand below to see the API response received for the search</p>
                              """, height=100)
    with st.expander("See JSON Response"):
        with st.container():
            st.json(data)
            
    
    # Showcasing result
    st.components.v1.html("""
                              <h3 style="color: #0ea5e9; font-family: Source Sans Pro, sans-serif; font-size: 26px; margin-bottom: 10px; margin-top: 60px;">Result</h3>
                              <p style="color: #57534e; font-family: Source Sans Pro, sans-serif; font-size: 16px;">Below are the movies we received related to your search. We have analyzed each and every one for you. Enjoy!</p>
                              """, height=150)
    
    for movie in list(json.loads(data)["result"]):
        with st.expander(movie["title"]):
            with st.container():
                result = applyModal(movie, packageName)
                keys = list(result.keys())
                values = list(result.values())
                st.write("")
                st.write("")
                displayMovieContent(movie)
                for i in range(0, len(keys), 4):
                    if((i+3)<len(keys)):
                        
                        cols = st.columns(4)
                        cols[0].metric(keys[i], round(values[i], 2), None)
                        cols[1].metric(keys[i+1], round(values[i+1], 2), None)
                        cols[2].metric(keys[i+2], round(values[i+2], 2), None)
                        cols[3].metric(keys[i+3], round(values[i+3], 2), None)
                    else:
                        cols = st.columns(4)
                        for j in range(len(keys)-i):
                            print("Range Values : ", j, len(keys))
                            cols[j].metric(keys[i+j], round(values[i+j], 2), None)
                
                col1, col2 = st.columns([3, 1])
                st.write("")
                st.write("")
                with col1:
                    st.subheader("Visual Representation")
                    plotPie(list(result.keys()), [value/len(movie["reviews"]) for value in list(result.values())])
                
                

def applyModal(movie, packageName):
    if(packageName == "Flair"):
        predictionList = [modals.flair(review) for review in movie["reviews"]]
        valueCounts = dict(pd.Series(predictionList).value_counts())
        print(valueCounts)
        return valueCounts
    elif(packageName == "TextBlob"):
        predictionList = [modals.textBlob(review) for review in movie["reviews"]]
        valueCounts = dict(pd.Series(predictionList).value_counts())
        print(valueCounts)
        return valueCounts
    elif(packageName == "Vader"):
        predictionList = [modals.vader(review) for review in movie["reviews"]]
        valueCounts = dict(pd.Series(predictionList).value_counts())
        print(valueCounts)
        return valueCounts
    elif(packageName == "Text2emotion"):
        predictionList = [modals.text2emotion(review) for review in movie["reviews"]]
        valueCounts = dict(pd.Series(predictionList).value_counts())
        print(valueCounts)
        return valueCounts
    else:
        return ""
    

def renderPage():
    st.title("Sentiment Analysis 😊😐😕😡")
    components.html("""<hr style="height:3px;border:none;color:#333;background-color:#333; margin-bottom: 10px" /> """)
    # st.markdown("### User Input Text Analysis")
    st.subheader("IMDb movie review analysis")
    st.text("Analyze movie reviews from IMDb API for sentiments.")
    st.text("")
    movieName = st.text_input('Movie Name', placeholder='Input name HERE')
    packageName = st.selectbox(
     'Select Package',
     ('Flair', 'Vader', 'TextBlob', 'Text2emotion'))
    if st.button('Search'):
        if movieName:
            process(movieName, packageName)
        else:
            st.warning("Please enter a movie name")