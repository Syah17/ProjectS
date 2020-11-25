from flask import Flask, request, render_template
import Twitter_Sentiment_Analysis


app = Flask(__name__)



@app.route('/')
def home(): 
    return render_template('Twitter.html')


@app.route('/keyword',methods=['POST','GET'])
def keyword():
    #val = request.form.get("val")
    val=request.form["keyword"]
    word=Twitter_Sentiment_Analysis.keyword.key(val)
    polarity=Twitter_Sentiment_Analysis.plotting.PolarityAndSubjectivity(word)
        
    word_cld=Twitter_Sentiment_Analysis.plotting.show_wordcloud(word['tweets'])
    negative_positive_plot=Twitter_Sentiment_Analysis.plotting.sentiment(word)
    pie_chart=Twitter_Sentiment_Analysis.plotting.pie(word) 
    return render_template('Twitter.html',prediction=word['tweets'].head(),Top_Five_Tweets="Raw Tweets:",plot=word_cld,Word_cloud="Common words used",plot_polarity=polarity,polatiry_plot="Subjectivity against Polarity",plot_sentiment=negative_positive_plot,Sentiment="Tweets Sentiment")
    


if __name__ == "__main__":
    app.run()
    
