import pandas as pd

# Load dataset
df = pd.read_excel("Decode_labs_dataset.xlsx")

print("Original Dataset:")
print(df)

print("-------------------------------------------------------------------") 
# 1. Check Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
print("-------------------------------------------------------------------") 

# -----------------------------
# 2. Remove Duplicates
# -----------------------------
df = df.drop_duplicates()
print("-------------------------------------------------------------------") 

# -----------------------------
# 3. Correct Date Formats
# -----------------------------
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

# Convert date format(dates numbers text)
df["Date"] = df["Date"].dt.strftime('%Y-%m-%d')
print("-------------------------------------------------------------------") 

# -----------------------------
# 4. Standardize Text Columns
# -----------------------------
text_columns = [
    "Product",
    "PaymentMethod",
    "OrderStatus",
    "ReferralSource"
]

for col in text_columns:
    df[col] = df[col].str.title()
print("-------------------------------------------------------------------") 

# -----------------------------
# 5. Check Duplicate Order IDs
# -----------------------------
duplicate_ids = df["OrderID"].duplicated().sum()

print("\nDuplicate Order IDs:", duplicate_ids)
print("-------------------------------------------------------------------") 

# -----------------------------
# 6. Save Cleaned Dataset
# -----------------------------
df.to_excel("cleaned_dataset.xlsx", index=False)

print("\nCleaned Dataset:")
print(df)

print("\nData Cleaning Completed Successfully!")