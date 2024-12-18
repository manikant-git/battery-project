import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/reddy/Downloads/battery_analysis/cleaned_dataset/metadata.csv')  # Replace 'data.csv' with the correct path

# Remove any leading or trailing spaces in the column names
df.columns = df.columns.str.strip()

# Check the column names to ensure they are correct
print(df.columns)

# Check the first few rows to confirm the data structure
print(df.head())

# Clean the data by selecting the relevant columns
# Adjust the column names based on your inspection
df_clean = df[['Cycle_count', 'Battery_impedance', 'Re', 'Rct']]  # Adjust column names as needed

# Check for missing values
print(df_clean.isnull().sum())

# Create the plots using Plotly (after cleaning the data)
import plotly.express as px

# Plot Battery Impedance over Cycles
fig1 = px.line(df_clean, x='Cycle_count', y='Battery_impedance', title='Battery Impedance over Cycles')
fig1.update_layout(xaxis_title='Cycle Count', yaxis_title='Battery Impedance (Ohms)')
fig1.show()

# Plot Electrolyte Resistance (Re) over Cycles
fig2 = px.line(df_clean, x='Cycle_count', y='Re', title='Electrolyte Resistance (Re) over Cycles')
fig2.update_layout(xaxis_title='Cycle Count', yaxis_title='Electrolyte Resistance (Ohms)')
fig2.show()

# Plot Charge Transfer Resistance (Rct) over Cycles
fig3 = px.line(df_clean, x='Cycle_count', y='Rct', title='Charge Transfer Resistance (Rct) over Cycles')
fig3.update_layout(xaxis_title='Cycle Count', yaxis_title='Charge Transfer Resistance (Ohms)')
fig3.show()

