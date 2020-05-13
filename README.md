# <center>Data Mining Term Project</center>
Sushant Mhambrey<br>
UTA ID:1001778625 <br>
Game Review Predictor<br> <br>

Website of the term project deployed on Heroku : [click here](https://termprojectdm.herokuapp.com/)

Project Video Demo on Youtube : [click here](https://www.youtube.com/watch?v=p0x3xA96Z-8&feature=youtu.be)

Project Blog on my Homepage : [click here](https://sushantmhambrey.github.io/post/final/)

***
The website was made using Flask.Flask is provided by Python and is very easy to understand.Follow the steps to run the project on the local machine :<br>

1. We need to freeze the requirements 
>pip3 freeze > requirements.txt 
Download all the requirments in **requirement.txt**

2. Install all dependencies mentioned and Run the code using :
>python app.py

3. localhost:5000 is where the website will be opened.

***
Screenshot  and Demo :<br>
![](Images/gif.gif)


Good Rating
![Positive example](Images/2.png) 
Bad Rating
![Negative example](Images/1.png) 



## About the project
The purpose of the term project is to predict the ratings given a particular review. Throughout the implementation of the term project many models were tested and based on the various evaluation metrics a model was selected. The dataset is taken from Kaggle BGG review dataset . Due to the vast length of dataset Google Colaboratory was used as the implementation platform. The web application made in flask contains a simple text input which takes the review of the game from the user and predicts the rating based on certiac text classification techniques and machine learning models.


# Deploy
I have used Heroku to deploy the website online.Heroku is a cloud service platform and has become very popular due to its ease of use and services provided.It helps in developemnt and deployment of simple web applications such as this one.
Check whether your app.py file is running locally with all the dependencies downloaded.
To deploy the app you need a heroku account and Python 3.7(atleast) installed on your Mac, Windows or Linux machine.

To set up Heroku we need the **HerokuCLI** which requires Git.

For Heroku CLI use the following command
>sudo snap install heroku --classic

snap is available on Linux too. For windows or we can download the CLI directly from the site (https://devcenter.heroku.com/articles/heroku-cli

After installation, you need to login to Heroku through your computer's command prompt.

Use command prompt(cmd.exe) or Powershell on Windows to access the command prompt and use the Heroku login command
>heroku login

We need to create the requirement.txt file. command for that is
>pip freeze > requirements.txt

After we have prepared the app we need to create an app on Heroku using
>heroku create

Heroku needs to understand which app to run(here app.py). For that we need to create something called as the Procfile
>touch procfile

In the procfile type the following command
>web:gunicorn app:app

We are almost done now. Just commit the changes( use git add . first) and push to Heroku master:
>git commit

>git push heroku master

We can view the information of the running application using the log command(helpful to debug)
>heroku logs --tail


For more information read ::
https://devcenter.heroku.com/articles/getting-started-with-python#set-up


## Challenges:
One of the more general challenges that I faced was tackling such a huge dataset.Using the method of sampling worked but had some variations in accuracy.Thus a more scaled data in terms of ratings did the job.
Some specific challenge that I faced was to decide whether to use Word2Vec word embedding model. On further testing , it was seen that word embeddings actually created a lower accuracy.Doc2Vec word embeddings could have worked on the larger dataset if the accurate computation was present.On smaller dataset though, it made no difference. While creating ensembles,parameters of the individual models had to be tuned and dimensions had to be adjusted to properly fit our input to the model.Applying smoothing was one more contribution which helped to increase the accuracy.Had to relax certain terms of the model for that.
Even though the database is large , it is more lobsided toward the ratings of 6 7 8 and scaling down the data does the trick.Overall, working on the dataset helped to understand key concepts from simple terms like creating charts of top 20 words or scaling down the data to more complex methodologies like smoothing and ensembles.


## References:

1. https://towardsdatascience.com/review-rating-prediction-a-combined-approach-538c617c495c

2. https://towardsdatascience.com/ensemble-methods-in-machine-learning-what-are-they-and-why-use-them-68ec3f9fef5f

3. https://www.kaggle.com/josh24990/nlp-ml-which-words-predict-a-recommendation

4. https://www.developintelligence.com/blog/2017/03/predicting-yelp-star-ratings-review-text-python/




