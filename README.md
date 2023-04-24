# sqlite-query-tool-vuejs-flask
VueJS and Flask-powered tool for database analysis. Allows users to select tables from SQLite database, execute queries, and display results in a table format. Includes pre-written queries and displays all available tables. Uses custom delimiters and asynchronous method for fast retrieval of table names.

## Project Description: 
A web-based SQLite query tool created using Vue.js and Flask that allows users to select tables from a database, execute SQL queries, and display the results in a table format. It includes helpful pre-written queries and displays all available tables in the selected database. The tool uses custom delimiters and an asynchronous method to retrieve table/view names from the SQLite database.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

A brief introduction to the project and its purpose.

## DOCUMENTATION
The database structure is documentated using drawSQL.app
https://drawsql.app/teams/testteam-28/diagrams/veastagendringer

## Features

- List of features and functionalities of the project.

## Getting Started

- Prerequisites
- Installation
- Configuration
- How to run the project locally

## Usage

- How to use the tool
- Examples of queries
- How to interpret the results

Upon visiting the homepage, the user will be prompted to select a database file. Once a file has been selected, the available tables/views will be displayed on the left side of the page. Users can then select a table/view and execute a SQL query. The results of the query will be displayed in a table format on the right side of the page.

The tool also includes several pre-written queries that can be executed with the click of a button. To execute a pre-written query, simply select the query from the drop-down menu and click the "Run Query" button.

## Installation
To run this project locally, you will need to have the following software installed on your machine:

-Python 3.x
-Flask
-Vue.js
-SQLite

Once you have installed these dependencies, follow the steps below:

1.Clone the repository to your local machine.
1.Navigate to the project directory in your terminal.
1.Run pip install -r requirements.txt to install the necessary Python packages.
1.Navigate to the frontend directory and run npm install to install the necessary Vue.js packages.
1.Run npm run build to build the Vue.js application.
1.Navigate back to the project directory and run python app.py to start the Flask server.
1.Open your web browser and navigate to http://localhost:5000.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

- Guidelines for contributing to the project
- Code of conduct

## License
This project is licensed under the MIT License. See the LICENSE file for more information.
- Information about the project's license
- How to obtain a copy of the license
