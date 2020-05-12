import requests
from bs4 import BeautifulSoup
import json
from operator import itemgetter 
  


res  = requests.get('https://www.kuk.ac.in/hpcontent.php?action=hpcontent&id=NDg=') #fetch website

soup = BeautifulSoup(res.text,'html.parser') #html parser


subjects_links =[]
for link_gen in range(60,81): # 60 to 81 range for website specific
       links = soup.select('a')[link_gen]
       links_generated = links.get('href',None)
       subjects_links.append({'Links':"https://www.kuk.ac.in"+links_generated})
    

subjects = []

for list1 in range(1,31,2): #top 20 results from the website
    
       sub_name =soup.select('table')[4]('td')[list1]
       subject_list = sub_name.getText().replace('\n',"")
       subjects.append({'subject':subject_list})
   

    #    res1 = [ sub['subject'] for sub in subjects]  # to get items from the list of dictioneries


# Getting the results un new file
f=open ("results.txt","w+")
f1= open("resultsLinks","w+")
for sub in subjects :
 f.write(json.dumps(sub, indent=4))
for links in subjects_links:
       f1.write(json.dumps(links,indent=4))
print(subjects +subjects_links)



# if (res== Enter_Subject):
#     print(res1)
# else:
#     print("subject not there")
