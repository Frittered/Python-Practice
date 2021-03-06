--python3
import pandas as pd

class DDM:
    """This Data Description and Meta-analysis (DDM) module aims to automate descriptive analysis of data to prepare the 
    user for cleaning tasks.
    
    Arguments: 
        csv: string of location for the analysis csv
        safety: string 'safe' or 'unsafe' to control row/column limiters
    
    Use: Script can first be dragged and dropped into project directory, then imported into other scripts if needed.
    Individual functions can be called, or full() which calls all description functions
    """
    def __init__(self, csv, safety):
        self.safety_input = safety
        self.csv = pd.read_csv(csv)
        self.set_safety()
    def set_safety(self):
        if self.safety_input == 'unsafe':
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_colwidth', -1)

    def full(self):
        self.info()
        self.column_value_counts()
        self.column_type_errors()
        
    def info(self):
        self.csv.info()
        print(self.csv.isna().sum())
        print(self.csv.describe())

    def column_type_errors(self):
        column_errors = []
        for column in self.csv.columns:
            column_type_count = len(list(set([type(i) for i in self.csv[column]])))
            column_types = list(set([type(i) for i in self.csv[column]]))
            if column_type_count > 1:
                column_errors.append(f'Column:{column} with types: {column_types}')
        print('\n'.join(column_errors))

    def column_value_counts(self):
        for column in self.csv.columns:
            if self.csv[column].dtype in ['object']:
                print(f'{column} \n{self.csv[column].value_counts()}\n')
            else:
                print(column, f'Unique values: {len(pd.unique(self.csv[column]))}')
