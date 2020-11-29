# Please complete the TODO items below

from pyspark.sql import SparkSession


def explore_data():

    # TODO build a spark session (SparkSession is already imported for you!)
    spark =

    # couple ways of setting config
    #spark.conf.set("spark.executor.memory", '8g')
    #spark.conf.set('spark.executor.cores', '3')
    #spark.conf.set('spark.cores.max', '3')
    #spark.conf.set("spark.driver.memory", '8g')

    # TODO set correct path for file_path using Pathlib
    # TODO use a correct operator to load a csv file (cities.csv in your resources folder)

    file_path =
    df =

    # view schema
    df.printSchema()

    # TODO create another dataframe, drop null columns for start_year
    # TODO select start_year and country only and get distinct values
    # TODO sort by start_year ascending

    distinct_df =

    # show distinct values
    distinct_df.show()

    # which country had the metro system the earliest?

if __name__ == "__main__":
    explore_data()