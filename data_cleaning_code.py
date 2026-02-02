import pandas as pd

# 1. Load the dataset
df = pd.read_csv('Bengaluru_Ride_Bookings_1Lac.csv')

# 2. Date and Time Formatting
# Converts the Excel float dates to standard YYYY-MM-DD
df['Date'] = pd.to_datetime(df['Date'], unit='D', origin='1899-12-30').dt.date

# 3. Handling Missing Values
# Fill ratings with median to avoid skewing
df['Driver Ratings'] = df['Driver Ratings'].fillna(df['Driver Ratings'].median())
df['Customer Rating'] = df['Customer Rating'].fillna(df['Customer Rating'].median())

# Fill cancellation reasons with 'N/A' for completed trips
df['Reason for cancelling by Customer'] = df['Reason for cancelling by Customer'].fillna('N/A')
df['Reason for cancelling by Driver'] = df['Reason for cancelling by Driver'].fillna('N/A')
df['Incomplete Rides Reason'] = df['Incomplete Rides Reason'].fillna('N/A')

# 4. Data Type Cleaning
# Ensure numeric columns are actually numbers
numeric_cols = ['Booking Value', 'Ride Distance', 'Avg VTAT', 'Avg CTAT']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# 5. Remove Duplicates
df = df.drop_duplicates()

# 6. Save as Cleaned CSV
df.to_csv('Cleaned_Bengaluru_Ride_Bookings.csv', index=False)
print("Cleaning complete! Saved as 'Cleaned_Bengaluru_Ride_Bookings.csv'")
