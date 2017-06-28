import requests
import bs4

class ParseSite(object):
    def __init__(self,mail,passw):
       self.url = "http://14.139.233.57/mmmut/StudentLogin.aspx"
       self.mail = mail
       self.passw = passw
    def extract_headings(self):
        response = requests.session()
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTTARGET\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTARGUMENT\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__VIEWSTATE\"\r\n\r\n/wEPDwULLTE0OTQ2MTUzMzZkZAc4SbtTSHLUbg0ViOvVOr4HkFr1w6l+FiUUfNXadonr\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTVALIDATION\"\r\n\r\n/wEdAAbO3LImvAZ6n/EuT78+opQuY3plgk0YBAefRz3MyBlTcHY2+Mc6SrnAqio3oCKbxYainihG6d/Xh3PZm3b5AoMQRFGbj2vrNrQTo53xeYkuF9lIETJhURQdME90gSeMN4R7Xe2ZfLJNil7n6yzSP73lQGo4ohzA1gzSJQHXagjQcA==\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"txtUserName\"\r\n\r\n"+self.mail+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"txtPassword\"\r\n\r\n"+self.passw+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"btnLogin\"\r\n\r\nSubmit\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "cb28a4c7-8e41-0728-8a93-f881f47a7146"
        }

        c = response.request("POST", self.url, data=payload, headers=headers)
        b = bs4.BeautifulSoup(c.content , "html.parser")
        table = b.find("table", attrs={"id":"ContentPlaceHolder1_grdattendance"})
        w = table.find_all("tr")
        headings = [[th.get_text() for th in x.find_all("td")] for x in w]
        headings = headings[1:]
        for i in range(len(headings)):
                headings[i] = headings[i][:-1]
        return headings