import json
from urllib.request import urlopen,quote
import requests,csv



# def getlnglat(adress):
#     url = 'http://api.map.baidu.com/geocoder/v2/?address='
#     url3 = 'http://api.map.baidu.com/geocoding/v3/?address=北京市海淀区上地十街10号&output=json&ak=您的ak&callback=showLocation'
#     output = 'json'
#     ak = 'Czisx4SsRGajk4mTuAHRyjxDk2p7SGRr'
#     add = quote(adress)#使用quote进行编码 为了防止中文乱码
#     url2 = url + add + '&output=' + output + '&ak=' + ak + '&callback=showLocation'
#     req = urlopen(url3)
#     res = req.read().decode()
#     temp = json.loads(res)
#     return temp
#
# print(getlnglat("浙江杭州"))

# testurl = 'http://api.map.baidu.com/geocoding/v3/?address=北京市海淀区上地十街10号&output=json&ak=Czisx4SsRGajk4mTuAHRyjxDk2p7SGRr&callback=showLocation'
# res = requests.get(testurl)
# print(res.text)


def get(loc):
	yourAkcode = ''#get your akcode in baidu API website
    url = 'http://api.map.baidu.com/geocoding/v3/?address=' + loc + '&output=json&ak='+yourAkcode+'&callback=showLocation'
    res = requests.get(url)
    result = res.text
    lng = result[67:73]
    # print("lng:"+lng)
    lat = result[92:98]
    # print("lat:"+lat)
    # print(result)
    return lng, lat

# print(get("安徽省安庆市"))

 file = open('ra.csv', encoding="gbk").read()
 writefile = open('newdata.csv','w')
 arr = file.splitlines()
 for i in range(1, len(arr)):
     location = arr[i].split(',')
     loc0x, loc0y = get(location[0])
     loc1x, loc1y = get(location[1])
     # print(loc0)
     # print(loc1)
     writefile.write(location[0]+","+location[1]+","+str(loc0x)+"，"+str(loc0y)+","+str(loc1x)+"，"+str(loc1y)+"\n")
 print("succeess")

# print()

#file = open('data.csv',encoding='gbk').read()
#writefile = open('modifydata.csv','w')
#arr = file.splitlines()
#for i in range(len(arr)):
#    data = arr[i].split(',')
#    # print(data)
#    writefile.write(data[0]+","+data[1]+","+data[2]+"，"+data[3]+","+data[4]+"，"+data[5]+"\n")
#print("success")
