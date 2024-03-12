import requests
from bs4 import BeautifulSoup

# id=1071770321
class scraper_3():
    def scrapedata(self,id):  #use is for server 
    # def scrapedata(id):   #use this for testing
        url=f"https://shreemahabaliexpress.com/Frm_DocTrack.aspx?No={id}"

        # Disable SSL verification
        requests.packages.urllib3.disable_warnings()
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        main_page = requests.get(url,headers=headers,verify=False).text.strip()
        # print(main_page)
        soup = BeautifulSoup(main_page,'html.parser')
                
        all_data={
            "AWB_NUMBER":"",
            "STATUS":"",
            "TRACKING HISTORY":{
   
            },
            "LAST CENTER CONTACT DATA":{
                
            }
        }
        all_data["STATUS"]=soup.select("h4 span")[1].text
        all_data["AWB_NUMBER"]=soup.select("h4 span")[0].text

        all_data["LAST CENTER CONTACT DATA"]["Center"]=soup.find('table').find_all('tr')[6]("td")[0].get_text().replace("Center :","")
        all_data["LAST CENTER CONTACT DATA"]["Phone"]=soup.find('table').find_all('tr')[7]("td")[0].get_text().strip().replace("Phone :","")
        
        tr_tag = soup.find('table').find_all('tr')
        tr_list = tr_tag[2:5]
        tr_num=len(tr_list)
   
        for i in range(tr_num):
            # print("This is index ",i)
            id=soup.find('table').find_all('tr')[i+2]("td")[0].get_text().strip()
            # print(id)
            ti_u_0={f"ti_u_{i+1}":{"ManiFest/PKG.":"","Type":"","Branch":"","Date":"","Time":""}}
              
            ti_u_0[f"ti_u_{i+1}"]["ManiFest/PKG."] =soup.find('table').find_all('tr')[i+2]("td")[0].get_text().strip()
            ti_u_0[f"ti_u_{i+1}"]["Type"] =soup.find('table').find_all('tr')[i+2]("td")[1].get_text().strip()
            ti_u_0[f"ti_u_{i+1}"]["Branch"] = soup.find('table').find_all('tr')[i+2]("td")[2].get_text().strip() 
            ti_u_0[f"ti_u_{i+1}"]["Date"] =soup.find('table').find_all('tr')[i+2]("td")[3].get_text().strip()
            ti_u_0[f"ti_u_{i+1}"]["Time"] = soup.find('table').find_all('tr')[i+2]("td")[4].get_text().strip()
            
            all_data["TRACKING HISTORY"].update(ti_u_0)
            
        print(all_data)  
        return all_data 

# tracker=scraper_3
# tracker.scrapedata(1071770321)