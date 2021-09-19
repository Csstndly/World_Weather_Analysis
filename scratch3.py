import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

counties = []
county_votes = {}
voter_turnout = 0
largest_county = ""
largest_county_winning = 0
county_winning_percentage = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
    voter_turnout = voter_turnout + 1

    # For each row in the CSV file.
    for row in reader:
        voter_turnout = voter_turnout + 1
        county = row[1]

        if county not in counties:
            counties.append(county)
            county_votes[county] = 0

        county_votes[county] += 1

        if county not in counties:
            counties.append(county)
            county_votes[county] = 0
        county_votes[county] += 1

with open(file_to_save, "w") as txt_file:

    for county in county_votes.keys():
        county_count = county_votes.get(county)
        county_percentage = float(county_count) / float(voter_turnout) * 100
        county_results = (
            f"{county}: {county_percentage:.1f}% ({county_count:,})\n")
        print(county_results)

        txt_file.write(county_results)

        if (county_count > largest_county_winning ) and (county_percentage > county_winning_percentage):
            largest_county_winning = county_count
            county_winning_percentage = county_percentage
            largest_county = county
    turnout_results = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}")
    print(turnout_results)