Assignment 9: Web Scraping Project
Sarah Nguyen


THE GOAL


        The goal of the scraper was to open www.usa.gov/federal-agencies and scrape the link to each agency’s page and the the name of the agency, their address, and phone number. 


HOW
The U.S. Federal Agency index page sorts all the agencies into alphabetical categories. I needed to get the partial url of each alphabet page, e.g. /federal-agencies/a, /federal-agencies/b, /federal-agencies/c, and so on.To do this, I made the get_letter_page function that would fetch the partial url of the next letter after the current letter. The original www.usa.gov/federal-agencies/ url opens up the page that shows all the “A” agencies. So I would need to scrape all the agencies on the “A” page and then get the partial url for the next letter (/federal-agencies/b).


Next, on the current letter page, I needed to scrape all of the agency links that correspond to that letter. I used the get_agencies function for this. By using a couple nested for loops, I was able to first find the ul tag that contained all the links, then the li tags that contained the hrefs. The partial urls obtained through these for loops were then appended into a list called agency_list.


Agency_list was then used in the third function, agency_deets, to run each partial url for each agency and grab the information I wanted from each link. Name, address, and phone were variables that became labels in the CSV. phone_p was used to narrow down the variables and to help phone variable along.




ISSUES


        The first problem was with the get_letter_page function. I had trouble grabbing the specific li for the letter that came directly after the letter the page currently was on. I tried try/except and if/else to see if I could skip over the current letter and grab the partial url for the next letter. In the end, I played with next_sibling until I was able to grab the subsequent letter.
        
        Another problem I had was with the function get_agencies getting the for loops to properly run and appending them onto the list. Actually, there were many problems within other problems. The easiest one was getting the list to work. I had to play a lot with global/local values in order to get the list to validate. Another problem was that I initially wrote “for li in ul.find('li'):” instead of “for li in ul.find_all('li'):”. Which meant that I didn’t grab all the partial links that I wanted.
        
        A really quick issue I had with the last function, agency_deets, was that the variable address would scrape the right p tag but with a lot of weird /n’s and awkward looking spaces when I ran it because of a few <br> within the p tag. I first tried strip() and found out that that only took away some of the spaces but not all of them. So I tried .get_text(strip=True) and that did the job!


        Honestly, it wasn’t much of a problem than a roadblock, but sitting down and figuring out the logistics and pathways that I would have to take to scrape what I wanted to scrape. A lot of this process was testing these functions separately in their own .py files and making sure they worked perfectly on their own. After that, I would piece them together in the final.py file and slowly troubleshoot the code by running it over and over and seeing where it broke.