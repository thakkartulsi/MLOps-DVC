import pandas as pd
import os

# sample dataset
data = {
    'Product_id':['P01', 'P02', 'P03'],
    'Product_Name':['Laptop', 'Smartphone', 'Tablet'],
    'Price': [80000, 12000, 25000]
}

# converting the data to pandas dataframe
df = pd.DataFrame(data)

# defining the directory to store data
data_dir = 'data'

# creating the directory if it doesn't exist
os.makedirs(data_dir,exist_ok=True)

# defining the file path for the CSV file
file_path = os.path.join(data_dir,'sample_data.csv')

# saving DataFrame to a CSV file
df.to_csv(file_path,index=False)

print(f'File saved successfully at {file_path}')