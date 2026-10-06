import requests
from bs4 import BeautifulSoup

###Problem 2###
def get_courses(school):
    try:
        surfing = requests.get(school, timeout=30)
        surfing.raise_for_status()
        dish = BeautifulSoup(surfing.text, "html.parser")
        headings = ["h2","h3", "h4", "h5"]
        prior = ""


        for course in dish.select(".Schedule-Item"):
            main = course.find_previous(headings[0:3]).get_text(" ", strip=True)
            
            if main != prior:
                print("\n" + main)
                prior = main
            info = course.find("ul").find_all("li")

            wutangclan = info[0].get_text(" ", strip=True)
            aintnothing =info[1].get_text(" ", strip=True)
            tofw = ""     

            if "Online" in aintnothing or "Sync" in aintnothing:
                tofw = "💻"
            else:
                tofw = "🏫"



            print(f"   " + wutangclan + " @ " + aintnothing, tofw, "\n", end="")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error} + try again later, idk.")
        
    print(info)
get_courses("https://my.cdm.depaul.edu/v2/Public/Schedule?Department=CSEC&CourseNumber=&Quarter=1&Year=2027")

