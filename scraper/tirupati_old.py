from bs4 import BeautifulSoup
import requests
 

# user_input=106501173232
class scraper_2( ):
    
    def scrapedata(self,id):
        url="http://www.shreetirupaticourier.net/frm_doctrackweb.aspx?docno="+str(id)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        main_page = requests.get(url,headers=headers).text.strip()
        # print(main_page)
        soup = BeautifulSoup(main_page,'html.parser')

        all_data={"Booking_Detail"
        : {
            "DocNo": "",
            "From_Center": "",
            "To_Center": "",
            "Date": "",
            "Time": "",
            "Consignee": ""
        },
        "STATUS":"",
        "tracking_info":{}}

        all_data["Booking_Detail"]["DocNo"]=soup.find(id="lblDocNumber").text
        all_data["Booking_Detail"]["From_Center"]=soup.find(id="txtFromCenter").text
        all_data["Booking_Detail"]["To_Center"]=soup.find(id="txtToCenter").text
        Datetime=soup.find(id="txtDate").text
        all_data["Booking_Detail"]["Date"]=Datetime[0:8]
        all_data["Booking_Detail"]["Time"]=Datetime[11:]
        all_data["Booking_Detail"]["Consignee"]=soup.find(id="txtReceiver").text
        all_data["Booking_Detail"]["STATUS"]=soup.find(id="lblStatus").text
        print(all_data["Booking_Detail"])
        num_rows = len(soup.select('#tblTrack tr'))
        # print(num_rows)
        for i in range(1, num_rows):
            ti_u_0={f"ti_u_{i-1}":{"JOB": "","DATE": "","From_Location": "","To_Location": ""}}
                
            ti_u_0[f"ti_u_{i-1}"]["JOB"]=(soup.select('#tblTrack tr')[i].select('td') [0].text)
            ti_u_0[f"ti_u_{i-1}"]["DATE"]=(soup.select('#tblTrack tr')[i].select('td')[1].text)
            ti_u_0[f"ti_u_{i-1}"]["From_Location"]=(soup.select('#tblTrack tr')[i].select('td')[2].select("a")[0].text)
            ti_u_0[f"ti_u_{i-1}"]["To_Location"]=(soup.select('#tblTrack tr')[i].select('td')[2].select("a")[1].text)
            # print( ti_u_0[f"ti_u_{i-1}"]["To_Location"])
            all_data["tracking_info"].update(ti_u_0)

        return all_data
# print(all_data)
