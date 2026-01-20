# Day 1: CHALLENGES - Now It's YOUR Turn!
# Complete these challenges to practice what you learned

"""
🎯 INSTRUCTIONS:
1. Read each challenge
2. Write your code where it says # YOUR CODE HERE
3. Run the file to check your work
4. If you get stuck, hints are provided below each challenge

💡 TIP: Comment out challenges you're not working on yet
    Just add # at the start of the line
"""

import pandas as pd

# Load the data (you know how to do this now!)
df = pd.read_csv("job_applications.csv")

print("=" * 60)
print("DAY 1 CHALLENGES - TEST YOUR SKILLS")
print("=" * 60)

# ============================================
# CHALLENGE 1: BASIC FILTERING
# ============================================
print("\n🎯 CHALLENGE 1: Filter for Rejected Applications")
print("-" * 60)
print("Task: Show only applications with status = 'Rejected'")
print("Expected: Should show all rows where status is Rejected")

# YOUR CODE HERE

rejected_apps = df[df['status'] == 'Rejected']
print("-" * 60)
print("Task: Show only applications with status = 'Rejected'")
print("Expected: Should show all rows where status is Rejected")
print(rejected_apps)

"""
💡 HINT: Remember the syntax is df[df['column'] == 'value']
Review lesson.py line 110-120 if you need help!
"""

# ============================================
# CHALLENGE 2: COUNTING
# ============================================
print("\n🎯 CHALLENGE 2: Count Onsite Applications")
print("-" * 60)
print("Task: How many applications are for Onsite positions?")
print("Expected: A single number")


onsite_count = len(df[df['location'] == 'Onsite'])
print("-" * 60)
print("Task: How many applications are for Onsite positions?")
print("Expected: A single number")
# Uncomment this line when you're ready to test:
print(f"Onsite applications: {onsite_count}")

"""
💡 HINT: 
1. First filter: df[df['location'] == 'Onsite']
2. Then count: len(filtered_df)
You can do it in one line or two!
"""

# ============================================
# CHALLENGE 3: MULTIPLE CONDITIONS
# ============================================
print("\n🎯 CHALLENGE 3: Remote Applications Still Pending")
print("-" * 60)
print("Task: Show applications that are BOTH Remote AND Applied status")
print("Expected: Rows that match both conditions")

# YOUR CODE HERE
remote_pending = df[(df['location'] == 'Remote') & (df['status'] == 'Applied')]
remote_applied = df[(df['location'] == 'Remote') & (df['status'] == 'Applied')]
print("\nRemote  still waiting for response:")
print(remote_applied)
print(remote_pending)
print("\nRemote jobs still waiting for response:")
"""
💡 HINT: Use & for AND logic
df[(df['column1'] == 'value1') & (df['column2'] == 'value2')]
Don't forget the parentheses around each condition!
"""

# ============================================
# CHALLENGE 4: GROUPING
# ============================================
print("\n🎯 CHALLENGE 4: Count Applications Per Company")
print("-" * 60)
print("Task: Show how many times you applied to each company")
print("Expected: Company names with counts")

# YOUR CODE HERE
company_counts = df.groupby('company').size()
print("\nApplications per company:")
print(company_counts)
# Uncomment this line when you're ready to test:
print(company_counts)

"""
💡 HINT: Use .groupby('column').size()
Review lesson.py line 175-185 if needed
"""

# ============================================
# CHALLENGE 5: CALCULATING PERCENTAGES
# ============================================
print("\n🎯 CHALLENGE 5: What % of Applications are Remote?")
print("-" * 60)
print("Task: Calculate the percentage of remote vs total applications")
print("Expected: A percentage like 66.7%")

# YOUR CODE HERE
total = len(df)
remote = len(df[df['location'] == 'Remote'])
percentage = (remote / total) * 100

# Uncomment this line when you're ready to test:
print(f"Remote applications: {percentage:.1f}%")

"""
💡 HINT: 
    1. total = len(df)
    2. remote = len(df[df['location'] == 'Remote'])
    3. percentage = (remote / total) * 100
"""
    The formula is always: (part / whole) * 100
"""

# ============================================
# CHALLENGE 6: SORTING
# ============================================
print("\n CHALLENGE 6: Sort by Date, Newest First")
print("-" * 60)
print("Task: Show applications sorted by date_applied, newest at the top")
print("Expected: Rows sorted with most recent dates first")

# YOUR CODE HERE
sorted_df = df.sort_values('date_applied', ascending=False)
print("Applications sorted by date:")
# Uncomment this line when you're ready to test:
print(sorted_df)

#HINT : .sort_values('column', ascending=False)
#ascending=False means largest/newest first
"""

# ============================================
# CHALLENGE 7: FINDING SPECIFIC VALUES
# ============================================
print("\n🎯 CHALLENGE 7: Which Companies Led to Interviews?")
print("-" * 60)
print("Task: Show the company names where status is 'Interview'")
print("Expected: Just the company names (a list or Series)")
"""
# YOUR CODE HERE
interview_companies = df[df['status'] == 'Interview']['company']

# Uncomment this line when you're ready to test:
print(f"Interviewing with: {interview_companies.tolist()}")

"""
#💡 HINT:
#1. Filter for interviews: df[df['status'] == 'Interview']
#2. Get just the company column: filtered_df['company']
#Or combine in one line: df[df['status'] == 'Interview']['company']
"""

# ============================================
# CHALLENGE 8: BRINGING IT ALL TOGETHER
# ============================================
print("\n🎯 CHALLENGE 8: Create a Status Report")
print("-" * 60)
print("Task: For each status, show the count AND percentage")
print("Expected output example:")
print("   Applied: 3 (50.0%)")
print("   Interview: 2 (33.3%)")
print("   Rejected: 1 (16.7%)")

# YOUR CODE HERE
total = len(df)
for status in df['status'].unique():
count = len(df[df['status'] == status])
percentage = (count / total) * 100 
print(f"   {status}: {count} ({percentage:.1f}%)")

"""
    #💡 HINT:
    #This combines filtering, counting, and percentage calculation
#1. Get total: len(df)
#2. Loop through each unique status
#3. For each status, filter and count: len(df[df['status'] == status])
#4. Calculate percentage: (count / total) * 100
"""

# ============================================
# BONUS CHALLENGE (OPTIONAL)
# ============================================
print("\n🏆 BONUS CHALLENGE: Find Your Response Rate")
print("-" * 60)
print("Task: What % of applications got ANY response (Interview OR Rejected)?")
print("This is harder! You need to filter for EITHER status.")

# YOUR CODE HERE
# (Try this only after completing the other challenges)

"""
#💡 HINT:
#Use | for OR logic
#responded = df[(df['status'] == 'Interview') | (df['status'] == 'Rejected')]
#Then calculate percentage
"""

print("\n" + "=" * 60)
print("🎓 ONCE YOU COMPLETE THESE:")
print("=" * 60)
print("1. Move to portfolio_project.py")
print("2. Build your own job tracker analyzer")
print("3. Add it to your GitHub")
print("")
print("Remember: Struggling is LEARNING. Don't give up!")
print("Check lesson.py if you need to review concepts.")
print("=" * 60)
"""