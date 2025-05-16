import pandas as pd

# Load merged telecom dataset
df = pd.read_csv("telecom_model_dataset.csv")

# Create segmentation labels
def segment(row):
    if row['ARPU'] > 20 and row['Churned'] == False:
        return "High Value"
    elif row['ARPU'] <= 20 and row['Churned'] == False:
        return "Standard"
    elif row['Churned']:
        return "At Risk"
    else:
        return "Other"

df['CustomerSegment'] = df.apply(segment, axis=1)

# Save results
df.to_csv("telecom_segmented_customers.csv", index=False)
