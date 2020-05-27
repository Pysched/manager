import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-46ezx.mongodb.net/task_manager?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in already' + sesion['username']

    return render_template('index.html')



@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find(),
    profiles=mongo.db.profiles.find())


@app.route('/add_task')
def add_task():
    return render_template("addtask.html", tasks=mongo.db.tasks.find(),
    profiles=mongo.db.profiles.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get("PORT")), debug=True)