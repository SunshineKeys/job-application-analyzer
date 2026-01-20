# Day 1: Pandas Foundations - LEARN BY DOING
# This is NOT just code that runs. This is a TUTORIAL that TEACHES.

"""
🎯 LEARNING OBJECTIVES FOR DAY 1:
By the end of this lesson, you will understand:
1. What pandas is and why it's the #1 data analysis library
2. How to load and inspect data (like opening a patient chart)
3. How to filter data (like pulling specific prescriptions)
4. How to group and count (like inventory tracking)
5. How to calculate percentages and success rates

💊 CPHT CONNECTION:
Think of pandas as your pharmacy software, but for ANY data.
You used systems to look up patients, filter by insurance, count prescriptions.
Pandas does the same thing, but you write the commands instead of clicking buttons.
"""

import pandas as pd

# ============================================
# LESSON 1: WHAT IS PANDAS?
# ============================================
"""
pandas = Python library for working with tabular data (rows and columns)

Think of it like Excel, but:
- You write code instead of clicking
- You can handle millions of rows (Excel crashes at ~1 million)
- You can automate repetitive tasks
- Every step is documented in code

Key concept: DATAFRAME
A DataFrame is like a spreadsheet - rows and columns of data.
"""

# ============================================
# LESSON 2: LOADING DATA
# ============================================
print("=" * 60)
print("DAY 1: JOB APPLICATION TRACKER - LEARN BY DOING")
print("=" * 60)

# Load CSV file into a DataFrame
# CSV = Comma Separated Values (like an Excel file saved as .csv)
df = pd.read_csv("job_applications.csv")

"""
🧠 WHAT JUST HAPPENED?
- pd.read_csv() reads a CSV file
- df = our DataFrame (common convention: use 'df' as the variable name)
- Now 'df' contains all our job application data

💡 TIP: Always use meaningful variable names in real projects.
Instead of 'df', you might use 'job_apps' or 'applications_data'
"""

# ============================================
# LESSON 3: INSPECTING DATA (ALWAYS DO THIS FIRST!)
# ============================================
print("\n📊 STEP 1: UNDERSTAND YOUR DATA")
print("-" * 60)

# How many rows (applications) do we have?
total_rows = len(df)
print(f"Total applications: {total_rows}")

"""
🧠 WHY THIS MATTERS:
Before analyzing, you need to know what you're working with.
In pharmacy: you wouldn't count pills without knowing the bottle size.
In data: you don't analyze without knowing your row count.
"""

# See the first few rows (like previewing a file)
print("\n📋 First 5 rows of data:")
print(df.head())

"""
🧠 WHAT IS .head()?
- Shows the first 5 rows by default
- Use .head(10) to see 10 rows
- Helps you understand the structure

💊 CPHT CONNECTION:
Like glancing at the top prescriptions in the queue to see what you're dealing with.
"""

# See column names and data types
print("\n🔍 Data structure:")
print(df.info())

"""
🧠 WHAT IS .info()?
Shows you:
- Column names (company, title, location, status, date_applied)
- Data types (object = text, int64 = numbers)
- Non-null count (are there missing values?)

This is like checking if all required fields in a prescription are filled.
"""

# Get basic statistics (for numeric columns)
print("\n📈 Basic statistics:")
print(df.describe())

"""
If we had numeric columns (like salary), this would show:
- count, mean, standard deviation, min, max
- Useful for spotting outliers

We don't have numeric columns here, so it's empty. That's okay!
"""

# ============================================
# LESSON 4: ACCESSING COLUMNS
# ============================================
print("\n\n📂 STEP 2: WORKING WITH COLUMNS")
print("-" * 60)

# Get a single column (returns a Series - like a single spreadsheet column)
companies = df['company']
print("All companies we applied to:")
print(companies)

"""
🧠 TWO WAYS TO ACCESS COLUMNS:
1. df['column_name']  ← Use this (more reliable)
2. df.column_name     ← Only works if name has no spaces

💡 BEST PRACTICE: Always use df['column_name']
"""

# Get unique values (no duplicates)
unique_companies = df['company'].unique()
print(f"\nUnique companies: {unique_companies}")

# Count unique values
num_unique_companies = df['company'].nunique()
print(f"Number of unique companies: {num_unique_companies}")

"""
💊 CPHT CONNECTION:
unique() = "Show me each insurance type, no repeats"
nunique() = "How many different insurance types do we accept?"
"""

# ============================================
# LESSON 5: FILTERING DATA (THE MOST IMPORTANT SKILL!)
# ============================================
print("\n\n🔎 STEP 3: FILTERING DATA")
print("-" * 60)

"""
This is THE CORE SKILL of data analysis.
You'll use filtering in every single project.

SYNTAX: df[df['column'] == 'value']

Think of it like asking questions:
- "Show me only Remote jobs"
- "Show me only applications with status = Interview"
- "Show me only prescriptions for Medicare patients"
"""

# Example 1: Filter for Remote jobs only
remote_jobs = df[df['location'] == 'Remote']
print("Remote jobs only:")
print(remote_jobs)

"""
🧠 WHAT JUST HAPPENED?
1. df['location'] == 'Remote' creates a True/False list
   - True for rows where location is Remote
   - False for rows where location is not Remote
2. df[True/False list] shows only the True rows

This is called BOOLEAN INDEXING (fancy term for filtering with True/False)
"""

# Example 2: Filter for Interview status
interviews = df[df['status'] == 'Interview']
print("\nApplications that reached interview stage:")
print(interviews)

# How many interviews?
interview_count = len(interviews)
print(f"\nTotal interviews: {interview_count}")

"""
💊 CPHT CONNECTION:
This is EXACTLY like filtering prescriptions:
- "Show me only ready-to-fill prescriptions"
- "Show me only Controlled Substance prescriptions"
- "Show me only prescriptions for this patient"

You've done this logic thousands of times. Now you're writing the code!
"""

# Example 3: Multiple conditions (AND logic)
# Find Remote jobs that are still Applied (not rejected or interview)
remote_applied = df[(df['location'] == 'Remote') & (df['status'] == 'Applied')]
print("\nRemote jobs still waiting for response:")
print(remote_applied)

"""
🧠 COMBINING CONDITIONS:
& = AND (both conditions must be True)
| = OR (at least one condition must be True)

IMPORTANT: Use parentheses around each condition!
✅ df[(df['col1'] == 'value') & (df['col2'] == 'value')]
❌ df[df['col1'] == 'value' & df['col2'] == 'value']  # This breaks!
"""

# ============================================
# LESSON 6: GROUPING AND COUNTING
# ============================================
print("\n\n📊 STEP 4: GROUP BY - COUNTING CATEGORIES")
print("-" * 60)

"""
.groupby() is how you answer questions like:
- "How many applications per company?"
- "How many of each status (Applied, Interview, Rejected)?"
- "How many prescriptions per insurance type?"

SYNTAX: df.groupby('column').size()
"""

# Count applications by status
status_counts = df.groupby('status').size()
print("Applications by status:")
print(status_counts)

"""
🧠 WHAT IS .size()?
Counts the number of rows in each group.

If we had numeric columns, we could use:
- .sum()   = add up all values
- .mean()  = calculate average
- .count() = count non-null values
"""

# Count applications by location
location_counts = df.groupby('location').size()
print("\nApplications by location:")
print(location_counts)

# Count applications by company
company_counts = df.groupby('company').size()
print("\nApplications per company:")
print(company_counts)

"""
💊 CPHT CONNECTION:
.groupby() is like your pharmacy reports:
- "How many prescriptions per doctor?"
- "How many fills per insurance type?"
- "How many controls vs non-controls?"

You've read these reports. Now you can create them!
"""

# ============================================
# LESSON 7: CALCULATING PERCENTAGES
# ============================================
print("\n\n💯 STEP 5: CALCULATING SUCCESS RATES")
print("-" * 60)

# Total applications
total_applications = len(df)

# Count interviews
interview_count = len(df[df['status'] == 'Interview'])

# Calculate percentage
success_rate = (interview_count / total_applications) * 100

print(f"Total applications: {total_applications}")
print(f"Reached interview: {interview_count}")
print(f"Success rate: {success_rate:.1f}%")

"""
🧠 PERCENTAGE FORMULA:
(part / whole) * 100

:.1f means "format as decimal with 1 digit after the point"
- 33.333333 becomes 33.3
- 50.0 stays 50.0

💊 CPHT CONNECTION:
Like calculating "What % of prescriptions are ready on time?"
- Filled on time / Total prescriptions * 100
"""

# ============================================
# LESSON 8: SORTING DATA
# ============================================
print("\n\n📈 STEP 6: SORTING DATA")
print("-" * 60)

# Sort by date (oldest to newest)
df_sorted = df.sort_values('date_applied')
print("Applications sorted by date:")
print(df_sorted)

"""
🧠 WHAT IS .sort_values()?
- Orders rows by a column
- ascending=True (default) = smallest to largest, A to Z, oldest to newest
- ascending=False = largest to smallest, Z to A, newest to oldest

💡 TIP: This doesn't change the original df, it creates a sorted copy
To save the sorted version: df = df.sort_values('column')
"""

# Sort newest to oldest
df_sorted_desc = df.sort_values('date_applied', ascending=False)
print("\nApplications sorted by date (newest first):")
print(df_sorted_desc)

# ============================================
# PUTTING IT ALL TOGETHER
# ============================================
print("\n\n" + "=" * 60)
print("🎯 KEY INSIGHTS FROM OUR DATA")
print("=" * 60)

# 1. Total applications
print(f"\n📊 Applied to {len(df)} positions")

# 2. Company diversity
print(f"📊 Applied to {df['company'].nunique()} different companies")

# 3. Location preference
remote_count = len(df[df['location'] == 'Remote'])
remote_percentage = (remote_count / len(df)) * 100
print(f"📊 {remote_percentage:.0f}% of applications are for remote positions")

# 4. Success rate
interview_count = len(df[df['status'] == 'Interview'])
success_rate = (interview_count / len(df)) * 100
print(f"📊 Interview rate: {success_rate:.1f}%")

# 5. Status breakdown
print("\n📊 Status breakdown:")
for status, count in df.groupby('status').size().items():
    percentage = (count / len(df)) * 100
    print(f"   {status}: {count} ({percentage:.0f}%)")

print("\n" + "=" * 60)
print("✅ DAY 1 COMPLETE!")
print("=" * 60)

"""
🎓 WHAT YOU LEARNED TODAY:
✅ Load data with pd.read_csv()
✅ Inspect data with .head(), .info(), .describe()
✅ Access columns with df['column']
✅ Filter data with df[df['column'] == 'value']
✅ Group and count with .groupby().size()
✅ Calculate percentages (part/whole * 100)
✅ Sort data with .sort_values()

🚀 NEXT STEPS:
1. Go to challenges.py and solve the practice problems
2. Build your own analyzer in portfolio_project.py
3. Add this to your GitHub

💡 REMEMBER:
Every data analyst job starts with these fundamentals.
Master filtering, grouping, and calculating percentages.
These are your bread and butter skills!
"""
