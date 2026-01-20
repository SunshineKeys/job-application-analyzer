# Day 1: PORTFOLIO PROJECT - Job Application Analyzer
# Build something you can show employers!

"""
🎯 PROJECT GOAL:
Create a complete job application analyzer that answers key questions:
1. How many applications have you sent?
2. What's your interview success rate?
3. Which companies are most promising?
4. Should you focus on remote or onsite?
5. What's your weekly application rate?

"""

import pandas as pd

# ============================================
# LOAD YOUR DATA
# ============================================
# TODO: Load job_applications.csv into a DataFrame
df = pd.read_csv("job_applications.csv")

print("=" * 70)
print("JOB APPLICATION ANALYZER - PORTFOLIO PROJECT")
print("=" * 70)

# ============================================
# SECTION 1: OVERVIEW STATISTICS
# ============================================
print("\n📊 APPLICATION OVERVIEW")
print("-" * 70)

# TODO: Calculate and print:
# - Total applications
# - Number of unique companies
# - Number of unique job titles
# - Date range (earliest to latest application)

# HINT: Use len(df), .nunique(), .min(), .max()

# Example output format:
# Total applications: 5
# Companies applied to: 4
# Job titles: 3
# Date range: 2025-01-01 to 2025-01-10

# YOUR CODE HERE
total_applications = len(df)
print(f"Total applications: {total_applications}")
unique_companies = df['company'].nunique()
print(f"Companies applied to: {unique_companies}")
unique_titles = df['title'].nunique()
print(f"Job titles: {unique_titles}")
earliest_date = df['date_applied'].min()
latest_date = df['date_applied'].max()
print(f"Date range: {earliest_date} to {latest_date}")


# ============================================
# SECTION 2: SUCCESS METRICS
# ============================================
print("\n🎯 SUCCESS METRICS")
print("-" * 70)

# TODO: Calculate and print:
# - Interview count and percentage
# - Rejection count and percentage
# - Still pending count and percentage

# HINT: Filter by status, count with len(), calculate percentage

# Example output:
# Interviews: 2 (40.0%)
# Rejections: 1 (20.0%)
# Pending: 2 (40.0%)

# YOUR CODE HERE
total= len(df)
interview_count = len(df[df['status'] == 'Interview'])
interview_percentage = (interview_count / total) * 100
print(f"Interviews: {interview_count} ({interview_percentage:.1f}%)")
rejected_count = len(df[df['status'] == 'Rejected'])
rejected_percentage = (rejected_count / total) * 100
print(f"Rejections: {rejected_count} ({rejected_percentage:.1f}%)")
applied_count = len(df[df['status'] == 'Applied'])
applied_percentage = (applied_count / total) * 100
print(f"Pending: {applied_count} ({applied_percentage:.1f}%)")
# ============================================
# SECTION 3: LOCATION ANALYSIS
# ============================================
print("\n🌍 LOCATION BREAKDOWN")
print("-" * 70)

# TODO: Compare Remote vs Onsite
# Show counts and success rates for each

# HINT: 
# 1. Group by location, count with .size()
# 2. For each location, calculate interview rate
#    Example: Remote interviews / Total remote applications

# Example output:
# Remote: 3 applications, 2 interviews (66.7% success rate)
# Onsite: 2 applications, 0 interviews (0.0% success rate)

# YOUR CODE HERE
total = len(df)
remote_count = len(df[df['location'] == 'Remote'])
remote_percentage = (remote_count / total) * 100
print(f"Remote: {remote_count} applications ({remote_percentage:.1f}%)")
remote_interviews = len(df[(df['location'] == 'Remote') & (df['status'] == 'Interview')])
remote_success_rate = (remote_interviews / remote_count) * 100 if remote_count > 0 else 0
print(f"  → Interview success rate: {remote_success_rate:.1f}%")
onsite_count = len(df[df['location'] == 'Onsite'])
onsite_percentage = (onsite_count / total) * 100
print(f"Onsite: {onsite_count} applications ({onsite_percentage:.1f}%)")
onsite_interviews = len(df[(df['location'] == 'Onsite') & (df['status'] == 'Interview')])
onsite_success_rate = (onsite_interviews / onsite_count) * 100 if onsite_count > 0 else 0
print(f"  → Interview success rate: {onsite_success_rate:.1f}%")
# ============================================
# SECTION 4: COMPANY ANALYSIS
# ============================================
print("\n🏢 COMPANY INSIGHTS")
print("-" * 70)

# TODO: 
# - Show application count per company
# - Identify which companies led to interviews
# - Flag companies you applied to multiple times

# HINT: Use .groupby('company').size() and filtering

# Example output:
# Applications per company:
#   Alpha Co: 2
#   Beta LLC: 1
#   Gamma Inc: 1
# 
# Interview opportunities:
#   Beta LLC: Interview stage
# 
# Multiple applications sent to: Alpha Co

# YOUR CODE HERE
total=len(df)
print("Applications per company:")
company_counts = df.groupby('company').size()
for company, count in company_counts.items():
    print(f"  {company}: {count}")
print("\nInterview opportunities:")
interview_companies = df[df['status'] == 'Interview']['company']
if len(interview_companies) > 0:
    for company in interview_companies:
        print(f"  {company}: Interview stage")
else:
    print("  None yet")
print("\nMultiple applications sent to:")
multiple_apps = company_counts[company_counts > 1]
if len(multiple_apps) > 0:
    for company in multiple_apps.index:
        print(f"  {company}")
else:
    print("  None")
# ============================================
# SECTION 5: TIMELINE ANALYSIS
# ============================================
from datetime import datetime

print("\n📅 TIMELINE INSIGHTS")
print("-" * 70)

# TODO: 
# - Show applications sorted by date
# - Calculate days since each application
# - Identify oldest pending application

# HINT: 
# - Use .sort_values('date_applied')
# - Calculate days: convert date_applied to datetime, subtract from today

# ADVANCED (optional):
# - Group by week and show application volume
# - Calculate average applications per week

# YOUR CODE HERE
df['date_applied'] = pd.to_datetime(df['date_applied'])
df_sorted = df.sort_values('date_applied')
today = pd.Timestamp(datetime.today().date())
df_sorted['days_since_applied'] = (today - df_sorted['date_applied']).dt.days
print("\nApplications timeline:")
for _, row in df_sorted.iterrows():
    print(
        f"{row['date_applied'].date()} | "
        f"{row['company']} | "
        f"{row['title']} | "
        f"{row['status']} | "
        f"{row['days_since_applied']} days ago"
    )
pending_apps = df_sorted[df_sorted['status'] == 'Applied']
print("\nOldest pending application:")
if not pending_apps.empty:
    oldest = pending_apps.iloc[0]
    print(
        f"{oldest['company']} | "
        f"{oldest['title']} | "
        f"Applied on {oldest['date_applied'].date()} "
        f"({oldest['days_since_applied']} days ago)"
    )
else:
    print("No pending applications 🎉")
df_sorted['week'] = df_sorted['date_applied'].dt.to_period('W')
weekly_counts = df_sorted.groupby('week').size()
print("\nApplications per week:")
for week, count in weekly_counts.items():
    print(f"{week}: {count} applications")
avg_per_week = weekly_counts.mean()
print(f"\nAverage applications per week: {avg_per_week:.2f}")


# ============================================
# SECTION 6: ACTION ITEMS
# ============================================
print("\n✅ ACTION ITEMS")
print("-" * 70)

# TODO: Generate actionable recommendations
# - Which applications need follow-up? (Applied > 7 days ago)
# - Which companies have highest success rate?
# - Should you focus more on remote or onsite?

# Example output:
# 📌 Follow up with these companies (no response in 7+ days):
#    - Gamma Inc (applied 13 days ago)
# 
# 📌 Remote positions have 67% higher success rate - apply to more!
# 
# 📌 You have 2 pending applications - great! Keep momentum going.

# YOUR CODE HERE
follow_up_threshold = 7

follow_ups = df_sorted[
    (df_sorted['status'] == 'Applied') &
    (df_sorted['days_since_applied'] > follow_up_threshold)
]

print(f"\n📌 Follow up with these companies (no response in {follow_up_threshold}+ days):")
if not follow_ups.empty:
    for _, row in follow_ups.iterrows():
        print(
            f"  - {row['company']} "
            f"(applied {row['days_since_applied']} days ago)"
        )
else:
    print("  None — you're all caught up! 🎉")

# ----------------------------
# 2. Company success rates
# ----------------------------
print("\n📌 Companies with interview success:")

company_stats = df.groupby('company').agg(
    total_apps=('company', 'count'),
    interviews=('status', lambda x: (x == 'Interview').sum())
)

company_stats['success_rate'] = (
    company_stats['interviews'] / company_stats['total_apps'] * 100
)

successful_companies = company_stats[company_stats['interviews'] > 0]

if not successful_companies.empty:
    for company, row in successful_companies.sort_values(
        'success_rate', ascending=False
    ).iterrows():
        print(
            f"  - {company}: "
            f"{row['success_rate']:.1f}% success rate "
            f"({int(row['interviews'])}/{int(row['total_apps'])} interviews)"
        )
else:
    print("  No interviews yet — keep applying and iterating!")

# ----------------------------
# 3. Remote vs Onsite strategy
# ----------------------------
print("\n📌 Application strategy recommendation:")

location_stats = df.groupby('location').agg(
    total_apps=('location', 'count'),
    interviews=('status', lambda x: (x == 'Interview').sum())
)

location_stats['success_rate'] = (
    location_stats['interviews'] / location_stats['total_apps'] * 100
)

if len(location_stats) > 1:
    best_location = location_stats['success_rate'].idxmax()
    best_rate = location_stats.loc[best_location, 'success_rate']

    print(
        f"  {best_location} positions have the highest success rate "
        f"({best_rate:.1f}%). Consider focusing more applications there."
    )
else:
    print("  Not enough data to compare remote vs onsite yet.")

# ----------------------------
# 4. Momentum check
# ----------------------------
pending_count = len(df[df['status'] == 'Applied'])

print("\n📌 Momentum check:")
print(f"  You have {pending_count} active applications — keep the momentum going!")


# ============================================
# EXPORT RESULTS (BONUS)
# ============================================
print("\n💾 SAVE RESULTS")
print("-" * 70)

# TODO (optional): Save your analysis to a file
# - Export summary statistics to a CSV
# - Save status report to a text file

# HINT: 
# df.to_csv('application_summary.csv', index=False)
# with open('report.txt', 'w') as f:
#     f.write("Your report content")

# YOUR CODE HERE
# ----------------------------
# 1. Export summary statistics to CSV
# ----------------------------
summary_data = {
    'total_applications': [len(df)],
    'unique_companies': [df['company'].nunique()],
    'unique_job_titles': [df['title'].nunique()],
    'interviews': [(df['status'] == 'Interview').sum()],
    'rejections': [(df['status'] == 'Rejected').sum()],
    'pending': [(df['status'] == 'Applied').sum()]
}

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv('application_summary.csv', index=False)

print("✅ application_summary.csv saved")

# ----------------------------
# 2. Save status report to text file
# ----------------------------
with open('application_report.txt', 'w') as f:
    f.write("JOB APPLICATION ANALYSIS REPORT\n")
    f.write("=" * 40 + "\n\n")

    f.write("OVERVIEW\n")
    f.write(f"Total applications: {len(df)}\n")
    f.write(f"Companies applied to: {df['company'].nunique()}\n")
    f.write(f"Job titles: {df['title'].nunique()}\n\n")

    f.write("STATUS BREAKDOWN\n")
    f.write(f"Interviews: {(df['status'] == 'Interview').sum()}\n")
    f.write(f"Rejections: {(df['status'] == 'Rejected').sum()}\n")
    f.write(f"Pending: {(df['status'] == 'Applied').sum()}\n\n")

    f.write("FOLLOW-UP REQUIRED (7+ DAYS)\n")
    follow_ups = df_sorted[
        (df_sorted['status'] == 'Applied') &
        (df_sorted['days_since_applied'] > 7)
    ]

    if not follow_ups.empty:
        for _, row in follow_ups.iterrows():
            f.write(
                f"- {row['company']} | "
                f"{row['title']} | "
                f"{row['days_since_applied']} days ago\n"
            )
    else:
        f.write("None\n")

    f.write("\nEND OF REPORT\n")

print("✅ application_report.txt saved")


print("\n" + "=" * 70)
print("✅ ANALYSIS COMPLETE!")
print("=" * 70)

"""
🎓 PROJECT COMPLETE CHECKLIST:
□ All sections print meaningful output
□ Calculations are accurate (check your math!)
□ Output is formatted and easy to read
□ Code is commented (explain your logic)
□ You understand every line of code

