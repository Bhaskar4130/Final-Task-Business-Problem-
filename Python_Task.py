import pandas as pd

# Load dataset
data_path = "c:\Users\bhask\Downloads\supply_chain_extended_data (1).csv"
df = pd.read_csv(data_path)

# Display basic information
print("Dataset Info:")
df.info()

# Display first few rows
print("\nFirst 5 rows:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
# Fill numerical columns with their mean
num_cols = df.select_dtypes(include=['number']).columns
df[num_cols] = df[num_cols].apply(lambda x: x.fillna(x.mean()))

# Fill categorical columns with the most frequent value
cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].apply(lambda x: x.fillna(x.mode()[0]))

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert date columns to datetime format if present
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'])

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Analyzing delivery delays (Example: finding warehouses with the longest shipping times)
if 'delivery_time' in df.columns:
    print("\nAverage Delivery Time by Warehouse:")
    print(df.groupby('warehouse')['delivery_time'].mean().sort_values())

# Inventory analysis (Example: checking stock imbalances)
if 'stock_level' in df.columns:
    print("\nStock Levels by Warehouse:")
    print(df.groupby('warehouse')['stock_level'].sum())

# Demand trends (Example: checking monthly demand patterns)
if 'order_date' in df.columns:
    df['month'] = df['order_date'].dt.to_period('M')
    print("\nMonthly Demand Trends:")
    print(df.groupby('month')['order_quantity'].sum())

# Save cleaned data to a new file
df.to_csv('C:/Users/tejar/Downloads/cleaned_supply_chain_data.csv', index=False)
print("\nCleaned dataset saved successfully.")


