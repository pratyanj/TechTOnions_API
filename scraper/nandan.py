from bs4 import BeautifulSoup
import requests

all_data={
        "Delivery_Information":{
        "Delivery Center":"",
        "Phone Number":"",
        "Regional Office":"",
        "Area Name":"",
        "Delivery Date":"",
        "Delivery Status":"",
        },

        "Booking_Information":{
        "Booking Center":"",
        "Phone Number":"",
        "Consignment Number":"",
        "Consignment Type":"",
        "Booking Date":"",
        "Consignee":"",
        "Destination":"",
        },

        "tracking_info":{}
        }

# Delivery_Information={
        
#         }
# tracking_id={} 


track_id = 3695200023186

class scraper_1():
    
    def scrapedata(self,id):
        
        url="http://www.shreenandancourier.com/TrackingInfo.aspx?cn="+str(id)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
        r = requests.get(url,headers=headers).text.strip()
        soup = BeautifulSoup(r, "html.parser")
        
        all_data["Booking_Information"]["Booking Center"] = soup.find('span', {"id": "content_BookingCenterNameLabel"})
        # print(Delivery_Information["Booking Center"])
        if all_data["Booking_Information"]["Booking Center"] is not None:
            all_data["Booking_Information"]["Booking Center"] = all_data["Booking_Information"]["Booking Center"].text.strip()
        else:
            all_data["Booking_Information"]["Booking Center"] = ""

        all_data["Booking_Information"]["Phone Number"] = soup.find('span', {"id": "content_BookingCenterPhoneNumberLabel"})
        if all_data["Booking_Information"]["Phone Number"] is not None:
            all_data["Booking_Information"]["Phone Number"] = all_data["Booking_Information"]["Phone Number"].text.strip()
        else:
            all_data["Booking_Information"]["Phone Number"] = ""

        all_data["Booking_Information"]["Consignment Number"] = soup.find('span', {"id": "content_ConsignmentNumberLabel"})
        if all_data["Booking_Information"]["Consignment Number"] is not None:
            all_data["Booking_Information"]["Consignment Number"] = all_data["Booking_Information"]["Consignment Number"].text.strip()
        else:
            all_data["Booking_Information"]["Consignment Number"] = ""

        all_data["Booking_Information"]["Consignment Type"] = soup.find('span', {"id": "content_ConsignmentTypeLabel"})
        if all_data["Booking_Information"]["Consignment Type"] is not None:
            all_data["Booking_Information"]["Consignment Type"] = all_data["Booking_Information"]["Consignment Type"].text.strip()
        else:
            all_data["Booking_Information"]["Consignment Type"] = ""

        all_data["Booking_Information"]["Booking Date"] = soup.find('span', {"id": "content_BookingDateLabel"})
        if all_data["Booking_Information"]["Booking Date"] is not None:
            all_data["Booking_Information"]["Booking Date"] = all_data["Booking_Information"]["Booking Date"].text.strip()
        else:
            all_data["Booking_Information"]["Booking Date"] = ""

        all_data["Booking_Information"]["Consignee"] = soup.find('span', {"id": "content_ReceiverLabel"})
        if all_data["Booking_Information"]["Consignee"] is not None:
            all_data["Booking_Information"]["Consignee"] = all_data["Booking_Information"]["Consignee"].text.strip()
        else:
            all_data["Booking_Information"]["Consignee"] = ""

        all_data["Booking_Information"]["Destination"] = soup.find('span', {"id": "content_DestinationCenterLabel"})
        if all_data["Booking_Information"]["Destination"] is not None:
            all_data["Booking_Information"]["Destination"] = all_data["Booking_Information"]["Destination"].text.strip()
        else:
            all_data["Booking_Information"]["Destination"] = ""

        # Delivery_Information
        all_data["Delivery_Information"]["Delivery Center"] = soup.find('span', {"id": "content_DeliveryCenterNameLabel"})
        if all_data["Delivery_Information"]["Delivery Center"] is not None:
            all_data["Delivery_Information"]["Delivery Center"] = all_data["Delivery_Information"]["Delivery Center"].text.strip()
        else:
            all_data["Delivery_Information"]["Delivery Center"] = ""

        all_data["Delivery_Information"]["Phone Number"] = soup.find('span', {"id": "content_DeliveryCenterPhoneNumberLabel"})
        if all_data["Delivery_Information"]["Phone Number"] is not None:
            all_data["Delivery_Information"]["Phone Number"] = all_data["Delivery_Information"]["Phone Number"].text.strip()
        else:
            all_data["Delivery_Information"]["Phone Number"] = ""

        all_data["Delivery_Information"]["Regional Office"] = soup.find('span', {"id": "content_RegionalOfficeLabel"})
        if all_data["Delivery_Information"]["Regional Office"] is not None:
            all_data["Delivery_Information"]["Regional Office"] = all_data["Delivery_Information"]["Regional Office"].text.strip()
        else:
            all_data["Delivery_Information"]["Regional Office"] = ""

        all_data["Delivery_Information"]["Area Name"] = soup.find('span', {"id": "content_DeliveryAreaLabel"})
        if all_data["Delivery_Information"]["Area Name"] is not None:
            all_data["Delivery_Information"]["Area Name"] = all_data["Delivery_Information"]["Area Name"].text.strip()
        else:
            all_data["Delivery_Information"]["Area Name"] = ""

        all_data["Delivery_Information"]["Delivery Date"] = soup.find('span', {"id": "content_DeliveryDateLabel"})
        if all_data["Delivery_Information"]["Delivery Date"] is not None:
            all_data["Delivery_Information"]["Delivery Date"] = all_data["Delivery_Information"]["Delivery Date"].text.strip()
        else:
            all_data["Delivery_Information"]["Delivery Date"] = ""

        all_data["Delivery_Information"]["Delivery Status"] = soup.find('span', {"id": "content_DeliveryStatusLabel"})
        # Delivery_Information["Delivery Status"] = soup.find('span', {"id": "content_DeliveryStatusLabel")
        if all_data["Delivery_Information"]["Delivery Status"] is not None:
            all_data["Delivery_Information"]["Delivery Status"] = all_data["Delivery_Information"]["Delivery Status"].text.strip()
        else:
            all_data["Delivery_Information"]["Delivery Status"] = ""
        # print(Delivery_Information["Delivery Status"])
        
        num_rows = len(soup.select('#content_TravelInfoGridView tr'))
        for i in range(1, num_rows):
            ti_u_0={f"ti_u_{i-1}":{"date": "","Time": "","Details": "","From_Location": "","To Location": ""}}
           
            ti_u_0[f"ti_u_{i-1}"]["date"]=(soup.select('#content_TravelInfoGridView tr')[i].select('td') [0].text.strip().replace("-", " "))
            ti_u_0[f"ti_u_{i-1}"]["Time"]=(soup.select('#content_TravelInfoGridView tr')[i].select('td')[1].text.strip().replace(".", ":"))
            ti_u_0[f"ti_u_{i-1}"]["Details"]=(soup.select('#content_TravelInfoGridView tr')[i].select('td') [2].text.strip())
            ti_u_0[f"ti_u_{i-1}"]["From_Location"]=(soup.select('#content_TravelInfoGridView tr')[i].select('td')[3].text.strip())
            ti_u_0[f"ti_u_{i-1}"]["To Location"]=(soup.select('#content_TravelInfoGridView tr')[i].select('td')[4].text.strip())
            # print(ti_u_0["ti_u_0"])
            all_data["tracking_info"].update(ti_u_0)
       
        return all_data
        
# track = scraper()
# track.scrapedata(3695200023187)
 