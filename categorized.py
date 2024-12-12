import pandas as pd

# Load the CSV file
file_path = 'data/cibc.csv'  # Replace with your file path if needed
data = pd.read_csv(file_path)


# # Display the column names
# print(data.columns)

# Function to categorize based on merchant
def categorize_merchant(merchant):
    merchant = merchant.lower()  # Convert to lowercase for case-insensitive matching
    if any(keyword in merchant for keyword in ['supermarket', 'superstore', 'mart', 'food', 'pharmacy', 'safeway', 'nofrills', 'drugs']):
        return 'MARKET'
    elif any(keyword in merchant for keyword in ['hot pot', 'noodle', 'memory', 'mcdonald', 'chicken', 'pho', 'pizza']):
        return 'RESTAURANT'
    elif any(keyword in merchant for keyword in ['tim hortons', 'starbucks', 'coffee', 'cafe', 'bakery', 'angus']):
        return 'CAFE'
    elif any(keyword in merchant for keyword in ['gym', 'fitness', 'workout', 'tennis', 'recreation']):
        return 'WORKOUT'
    elif any(keyword in merchant for keyword in ['compass', 'mobile', 'uber', 'air', 'ferry', 'bell']):
        return 'UTILITY'
    elif any(keyword in merchant for keyword in ['sephora', 'sport chek']):
        return 'BEAUTY'
    elif any(keyword in merchant for keyword in ['brainstation', 'victoria']):
        return 'EDUCATION'
    elif any(keyword in merchant for keyword in ['amazon']):
        return 'ONLINE'
    elif any(keyword in merchant for keyword in ['banff', 'kelowna', 'calgary']):
        return 'TRAVEL'
    else:
        return 'OTHER'

# Apply the categorization
data['Category'] = data['Merchant'].apply(categorize_merchant)

# Export the modified data to a new CSV
output_file_path = 'data/categorized_credit_card_data.csv'
data.to_csv(output_file_path, index=False)

print(f"Categorized data has been saved to {output_file_path}")
