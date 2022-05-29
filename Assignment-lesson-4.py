import requests , names
from selenium import webdriver
def check_repos(repos_list,amount):
    repos_list = repos_list.json()
    repo_amount = 0
    for repo in repos_list:
        if(bool(repo["name"]) ):
            repo_amount += 1
    if(repo_amount > amount): return True
def check_age():
    for i in range(1,3):
        response = requests.get(f'https://api.agify.io/?name={names.get_first_name()}').json()
        if(0 > response["age"] < 120):
            return False
def check_israel(univer):
    return univer["country"] == "israel"

def check_title(url,webtitle):
    my_driver = webdriver.Chrome()
    my_driver.get(url)
    return my_driver.title == webtitle
#Exercise 1
response = requests.get("https://api.github.com/users/avielb/repos")
if(check_repos(response,5)):
    print("repos is above 5 repositorys")

#Exercise 2
if(check_age()):
    print("it worked")

#Exercise 3
universite = requests.get("http://universities.hipolabs.com/search?country=Israel")
amount = 0
for i in universite.json():
    if(check_israel(i)):
        amount += 1
if(amount > 5): print("More then 5 israelis Universites has been found")

#Exercise 4
assert check_title("https://www.ycombinator.com/","Y Combinator")
#Exercise 5
assert check_title("https://hub.docker.com", "Docker Hub Container Image Library | App Containerization")


