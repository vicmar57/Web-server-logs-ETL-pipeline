# Project Name

Web-server-logs-ETL-pipeline

## Installation

faker is needed to generate fake log data (pip install faker)

## Usage

run log_generator to generate a stream of logs that will get into log_a.txt and log_b.txt 
run store_logs to parse and store the log data in a PostgreSQL db
run count_visitors and count_browsers to generate analytics

## Credits

credit to Vik Paruchuri for his tutorial on data pipelines with python!!
(https://www.dataquest.io/blog/data-pipelines-tutorial/)
