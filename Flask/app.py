from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/Stocks")


# Route to render index.html template using data from Mongo
@app.route("/")
def stock():
        print("Insert ticker symbol")
        name = input()
        name = str(name)
        # Find one record of data from the mongo database
        
        transformed_data = mongo.db.Transformed.find_one({"name" : name},sort=[("date", -1)])
        print(transformed_data)
        # Return template and data
        return render_template("stock.html", transformed=transformed_data)


if __name__ == "__main__":
    app.run(debug=True)
