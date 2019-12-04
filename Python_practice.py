print("Hello World")
help("keywords")
5+2*3
8//5-3
8+22*2-4
16-3/2+7-1
3**3%5
5+9*3/2-4
type(2019)
5+(9*3/2-4)
5+(9*3/(2-4))
counties=["Arapahoe","Denver","Jefferson"]
type(counties)
counties[1]
counties[0:3]
counties.append("El Paso")
counties.pop(3)
counties[1] ="El Paso"
counties.pop(0)
counties.append("Denver")
counties.append("Arapahoe")
counties_tuple=("Arapahoe","Denver","Jefferson")
len(counties_tuple)
counties_tuple[1]
counties_dict={'Arapahoe':422829,'Denver':463353,'Jefferson':432438}
counties_dict.values()
counties_dict['Arapahoe']
voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data[1]= {"county":"El Paso", "registered_voters": 461149}
voting_data.pop(0)

voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

counties=["Arapshoe",'Denver','Jefferson']
if counties[1]=='Denver':
    print(counties[1])

temperature=int(input("What is the temperature outside?"))

def temperature(temp):
    if temp>80:
        print('Turn on the AC.')
    else:
        print('Open the windows.')

def grade(score):
    if score>=90:
        print('Your grade is an A.')
    elif score>=80:
        print('Your grade is a B.')
    elif score>=70:
        print('Your grade is a C.')
    elif score>=60:
        print('Your grade is a D.')
    else:
        print('Your score is a F.')

counties = ["Arapahoe","Denver","Jefferson"]

if "El Paso" in counties:
    print("El Pasi is in the list of counties.")
else:
    print("El Paso is not in the list of counites.")

if "Arapahoe" and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not the list of counties.")

if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

x=0
while x<=5:
    print(x)
    x= x+1

for county in counties:
    print(county)

numbers=[0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county,voters in counties_dict.items():
    print(county,'county has',voters,'registered voters.')

voting_data =[{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(counties_dict)

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['registered_voters'])

my_votes=int(input("How many votes did you get in the election?"))
total_votes=int(input("What is the total votes in the election?"))
percentage_votes=(my_votes/total_votes)*100
print("I recieved "+ str(percentage_votes)+"% of the total votes.")

my_votes=int(input("How many votes did you get in the election?"))
total_votes=int(input("What is the total votes in the election?"))
print(f"I received {my_votes/total_votes *100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")
print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]
for counties_dict in voting_data:
    print(f'{counties_dict["county"]} county has {counties_dict["registered_voters"]:,} registered voters.')


import random
dir(int)
dir(float)
dir(bool)
import datetime

now= datetime.datetime.now()
print('The time right now is,',now)

dir(list)
dir(tuple)
dir(dict)
dir(datetime)
dir(random)
import numpy
dir(numpy)