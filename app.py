import pymongo
from pymongo import MongoClient
from flask import Flask,render_template,request,url_for,redirect,flash


client = pymongo.MongoClient("mongodb+srv://ajithMongo:ajith123mongo@cluster1.3mmhuy7.mongodb.net/?retryWrites=true&w=majority")
db = client["blog"]
mycol = db["content"]

app=Flask(__name__)
app.secret_key="myblogsystem@12"


@app.route("/")
def home():
    all_post = list(mycol.find())
    return render_template("home.html",datas=all_post)

@app.route("/addpost",methods=['GET','POST'])
def addpost():
    if request.method=='POST':
        Author=request.form['author']
        Title=request.form['title']
        About=request.form['about']
        Link=request.form['url']
        mycol.insert_one({"author":Author,"title":Title,"content":About,"link":Link})
        flash('New Post Added') 
        return redirect(url_for('home'))
    return render_template("addpost.html")


@app.route("/deletepost",methods=['GET','POST'])
def deletepost():
    if request.method=='POST': 
        Title = request.form['dtitle']
        mycol.delete_one({"title":Title})
        flash('Post Deleted!',category='success')
        return redirect(url_for("home"))
    return render_template("delete.html")

if __name__=='__main__':
    app.run(debug=True)
    