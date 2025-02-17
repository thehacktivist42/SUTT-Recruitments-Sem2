import pandas as pd
import json
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"] # Days of the Week
a = pd.read_excel("Mess Menu Sample.xlsx", skiprows = 1) # Skips the day row as it is not needed
a = a.fillna(0) # Replaces NaN values with 0; easier to handle
data = {str(i)[:10] : {} for i in a} # Creates an empty dictionary using comprehension.
for i in data:
    k = list(a[i])
    # Explanation of the three lines below
    # For every entry whose index is between 0 and 11 (that is, between the words BREAKFAST AND LUNCH), it is added to a 
    # list under the dictionary key "BREAKFAST".
    # For every entry whose index is between 11 and 21 (that is, between the words LUNCH AND DINNER), it is added to a 
    # list under the dictionary key "LUNCH".
    # For every entry whose index is more than 21 (that is, after the word DINNER), it is added to a 
    # list under the dictionary key "DINNER".
    # 0 entries and ******* entries are handled using conditionals.
    # String processing functions like strip, upper and replace are used for grammatical corrections and consistency.

    data[i]["BREAKFAST"] = [' '.join((j.strip().upper().replace("/ ", " / ").replace("+ ", " + ").replace(" +", " + ").replace(" /", " / ").replace("( ", "(").replace(" (", "(").replace(" )", ")").replace(") ", ")")).split()) for j in k if j and 0 < k.index(j) < 11 and j not in days and j[0] != "*"]
    data[i]["LUNCH"] = [' '.join((j.strip().upper().replace("/ ", " / ").replace("+ ", " + ").replace(" +", " + ").replace(" /", " / ").replace("( ", "(").replace(" (", "(").replace(" )", ")").replace(") ", ")")).split()) for j in k if j and 11 < k.index(j) < 21 and j not in days and j[0] != "*"]
    data[i]["DINNER"] = [' '.join((j.strip().upper().replace("/ ", " / ").replace("+ ", " + ").replace(" +", " + ").replace(" /", " / ").replace("( ", "(").replace(" (", "(").replace(" )", ")").replace(") ", ")")).split()) for j in k if j and k.index(j) > 21 and j not in days and j[0] != "*"]
print(json.dumps(data, indent = 4))
with open("data.json", "w") as f:
    f.write(json.dumps(data, indent = 4)) # Writes the json object to data.json
