# When I Work Web Traffic Transformation Challenge

This program was created for the When I Work Web Traffic Transformation challenge.

The data was sourced from the root url found [here](https://public.wiwdata.com/engineering-challenge/data/) and the url is manipulated so that the lowercase ascii letters (a-z) are appended, followed by the file type (here it is `.csv`) The data is downloaded directly within the program and is re-downloaded each time it is ran. 

The final outputted `.csv` file is a transformation of the dataframe created into a pivot table, with the user_id set as the index, each webpage visited set into an its own individual column, and the total time spent on each page (length) aggregated for per webpage, per user.

The root url can be changed within the `compile_url_list()` function in the `data_transformation.py` file.

Below, you'll find instructions on how to set up and run the program.

## Environment Setup & Package Installation
1- Clone this repository down to your system using the `git clone` command in your terminal.

2- Navigate to the repository folder.

3- Create the project's environment `wiwenv` by using the `python -m venv wiwenv` command.

4- Activate the environment by using `"wiwenv/Scripts/Activate"` for Windows and `source wiwenv/bin/activate` for OS.

5- Install the required packages by running `pip install -r requirements.txt`

## Running the Program
1- In your terminal, run the following command: 

`python data_transformation.py` 

The data will be saved as `transformed_data.csv` in your repository's folder.
