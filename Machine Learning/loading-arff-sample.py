import pandas as pd
from scipy.io import arff

# Load the .arff file
data, meta = arff.loadarff('sample.arff')

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Decode bytes to strings for nominal attributes (if needed)
for column in df.select_dtypes([object]):
    df[column] = df[column].str.decode('utf-8')

# Display the DataFrame
print(df.head())
