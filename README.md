News Aggregator CLI
This project is a Python-based News Fetcher that automates the process of gathering the latest headlines from around the world. By interfacing with the NewsAPI, it eliminates the need for manual browsing by programmatically retrieving and filtering news based on specific interests.

🚀 Features
Multi-Topic Support: Fetches news for Technology, Sports, and Health by default.

Real-time Updates: Connects to the NewsAPI "everything" endpoint for the latest global data.

Automated Filtering: Sorts articles by publication date to ensure the most recent news appears first.

Clean Output: Parses complex JSON responses into a readable list of the top 5 headlines and their direct source URLs.

🛠️ Technical Overview
The script uses the requests library to handle HTTP GET requests. It follows a structured workflow:

Authentication: Uses a secure API Key to communicate with the NewsAPI server.

Payload Configuration: Passes parameters such as q (query), sortBy, and language to refine results.

Data Parsing: Extracts specific keys from the JSON response to display only the most relevant information to the console.

📋 Prerequisites
Python 3.x

requests library (pip install requests)

A valid API Key from newsapi.org

👤 Author Details
Name: Sakshi

Registration No: 25BAI11058

Institution: VIT Bhopal University
