import pandas as pd
import string #package for string manipulation. Here it's used to manipulate the base url to produce the full list of urls

def compile_url_list(root = "https://public.wiwdata.com/engineering-challenge/data/",
                    url_name = list(string.ascii_lowercase), filetype = "csv"):
    list_of_urls = [f'{root}{url}.{filetype}' for url in url_name]
    return list_of_urls
 """
    This function compiles the list of urls using a root url (root), a list of url (file) names (url_name), and the file types (file_type).
 """

    
def compile_files(list_of_urls):
    file_list = []
    for url in list_of_urls:
        file = pd.read_csv(url)
        file_list.append(file)
        compiled_csv = pd.concat(file_list, axis = 0, ignore_index = True)
    return compiled_csv
"""
    This function takes the list of urls compiled above and combines them into a single df.
"""


def save_to_csv(compiled_csv):
    data = compiled_csv.pivot_table(index = "user_id", columns = "path",
                                   values = "length", aggfunc = "sum")
    data.to_csv("transformed_data.csv")
"""This function transforms the dataframe combined above into a pivot table, by setting the index to user_id, 
   transforming the values of the path column (i.e. webpages visited) into separate columns, and calculating the total time spent 
   on each page (length) by calling the aggfunc (aggregation function) and setting it to sum.
"""
   
#Running the program
files = compile_url_list()
csvs = compile_files(files)
files_to_csv = save_to_csv(csvs)