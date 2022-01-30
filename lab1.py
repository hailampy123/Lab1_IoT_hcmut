
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import time

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome("D:\HK212\IoT\chromedriver.exe")
driver.get('https://www.google.com')

string = '''
   function getLocation(callback) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var myjson = {"latitude":position.coords.latitude, "longitude":position.coords.longitude};
                console.log(position);
                console.log(position.coords.latitude);
                console.log(position.coords.longitude); 
                var stringJson = JSON.stringify(myjson);
                callback(stringJson);
            });
        } else {
            console.log("Geolocation is not supported by this browser.");
        }
    }
    
    getLocation(function(callback) {
        console.log(callback);
        const para = document.createElement("p");
        para.innerHTML = callback;
        para.id = "location";
        document.body.appendChild(para);
    });'''.replace('\n', '').replace('\t', '')


# repeat this code
driver.execute_script(string)
time.sleep(2)
res = driver.find_element(By.ID, "location")
loc = res.text
locDict = json.loads(loc)
print("latitude: %f, longitude: %f" % (locDict["latitude"], locDict["longitude"]))