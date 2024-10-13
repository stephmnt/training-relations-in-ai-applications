import pandas as pd

# Load the CSV file to inspect the content and find unnecessary line breaks
file_path = 'applis-ia.csv'
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure and see where line breaks might exist
df.head()

# Let's check the entire dataframe for line breaks in all columns
# We will use a function to remove any line breaks found within the cells

# Function to remove line breaks from the dataframe
def remove_line_breaks(df):
    return df.replace(r'[\r\n]+', ' ', regex=True)

# Apply the function to the entire dataframe
df_cleaned = remove_line_breaks(df)

# Save the cleaned dataframe to a new CSV file
output_path = 'applis-ia.csv'
df_cleaned.to_csv(output_path, index=False)
