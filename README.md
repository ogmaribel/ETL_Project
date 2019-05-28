# ETL_Project

For this project a stock market recommendation system was created using the Extract, Transform and Load method. It consists of two tools a Dashboard to check the last updates of an specific company and a chatbot using slack as the interface to ask some questions in order to figure out if the company is a good investment:

![Slack-Chatbot](Images/chatbot.png)

![Dashboard](Images/dashboard.png)


## Extract
For the extract phase two APIs were used the yahoo finance and Apha Vantage. 1 year of data was collected for more than 30 companies. (located in the  jupyter notebook file)

# Transform
A trading strategy was defined to transform the raw data to recommendation parameters. (Located in the jupyter notebook file)

# Load
The new data was stored in a new table in MongoDB and was used to feed the dashboard developed in Flask.

# Dashboard
The dashboard was developed using Flask, MongoDB and HTML. (Located in the Flask folder)

# Chatbot
The chatterbot librarie was used to train the bot, then it was connected to Slack using the Slackbot Tool and Slack Client.



