
'''

Reference URLs: 

https://sqlite.org/cli.html
'''
import sqlite3
import argparse
from os.path import exists, join
from os import makedirs
import pandas as pd

def showSQLite3TblToCSV(inputDFPath, outputDirPath): 

    # connect database file
    conn = sqlite3.connect(inputDFPath)
    # set SQL connection and cursor
    cursor = conn.cursor()
    print(cursor)
    # get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # fechall table
    tables = cursor.fetchall()
    # loop through all tables 
    for table_name in tables:
        table_name = table_name[0]
        print(table_name)
        # set table 
        table = pd.read_sql_query("SELECT * from %s" % table_name, conn)

        # set output file path 
        outputFilePath = join(outputDirPath, table_name + '.csv')
        # output database tables in csv file format
        table.to_csv(outputFilePath, index_label='index')

    cursor.close()
    conn.close()

def main(args):

    if not exists(args.input_db_path): 
        print("Please enter database file path")
        exit(0)

    if not exists(args.output_dir_path): 
        makedirs(args.output_dir_path)
        
    showSQLite3TblToCSV( args.input_db_path, 
                         args.output_dir_path)

if __name__ == '__main__': 

    parser = argparse.ArgumentParser(description='readSQLite.py -- read slite3 data file and show tables.')

    parser.add_argument('--input_db_path', type=str, 
                        default='.\db.sqlite3',
                        help='db.splite3 file path')

    parser.add_argument('--output_dir_path', type=str,
                        default='C:\\Users\\toruh\\Downloads\\outputs',
                        help='Output directory path.')

    args = parser.parse_args()
    main(args)

