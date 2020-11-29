# Please complete the TODO items below

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pathlib


def run_spark_streaming():
    """
    In this lesson, we're going to import a static json file first to explore the data
    Then load that static data as streaming data
    and show in our terminal
    :return:
    """
    spark = SparkSession.builder \
            .master("local") \
            .appName("spark streaming example") \
            .getOrCreate()


    # read the data file
    file_path = './resources/lesson1/json/data.txt'
    df = spark.read.json(file_path)

    df.show(10, False)

    # TODO based on the df.show, build schema
    jsonSchema =

    # TODO create streamning input dataframe that reads the same dataset, with jsonSchema you created
    streamingInputDF = (

    )

    # This will be given
    streamingCountsDF = (
        streamingInputDF
            .groupBy(
            streamingInputDF.status,
            window(streamingInputDF.timestamp, "1 hour"))
            .count()
    )

    streamingCountsDF.isStreaming

    # TODO Write query output to console
    query = (

    )

if __name__ == "__main__":
    run_spark_streaming()