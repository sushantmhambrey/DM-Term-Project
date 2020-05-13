from flask import Flask, render_template,url_for, request, redirect
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib


#load model
classifier=joblib.load('model/ridge_classifier.sav')
tfidf=joblib.load('model/tfidf_model.sav')

#initiliase vectorizer
tfidf_vect= TfidfVectorizer(stop_words='english', max_df=0.7)
#print("hello world")
app=Flask(__name__)

@app.route('/', methods=['POST','GET'])

def index():
    if request.method== 'POST':
        x=request.form['review']
        tfidf_review=tfidf.transform([x,])
        #sent=vect.transform(sentence)
        y_pred=classifier.predict(tfidf_review)
        res=int(y_pred)
        return render_template('index.html',result=res)
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
