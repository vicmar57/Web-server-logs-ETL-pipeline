# Web server logs ETL pipeline

ETL streaming pipeline using python. generating a constant stream of fake web server logs and analyzing it, and storing in a PostgreSQL DB

![Alt text](log_stream_pipeline.png?raw=true "Pipeline illustration")

## Installation

faker is needed to generate fake log data (pip install faker)

## Usage

1. run log_generator to generate a stream of logs that will get into log_a.txt and log_b.txt 
2. run store_logs to parse and store the log data in a PostgreSQL db
3. run count_visitors and count_browsers to generate analytics

## Credits

credit to Vik Paruchuri for his tutorial on data pipelines with python!!
(https://www.dataquest.io/blog/data-pipelines-tutorial/)
