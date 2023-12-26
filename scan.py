import socket,os,time,sys
#ip查询
def ip_check(url):
  ip=socket.gethostbyname(url)
  print(ip)
  print('------------------------------------++++++-------------------------------------------')
#whois查询
# def whois_check(url):
#   data = whois.whois(url)
#   print(data)
#   print('------------------------------------++++++-------------------------------------------')

#CDN判断-利用返回IP条数进行判断
def cdn_check(url):
  ns="nslookup "+url
  #data=os.system(ns)
  #print(data) #结果无法读取操作
  data=os.popen(ns,"r").read()
  if data.count(".")>8:
      print("存在CDN")
  else:
      print("不存在CDN")
  print('------------------------------------++++++-------------------------------------------')
#子域名查询-
#1.利用字典记载爆破进行查询
#2.利用第三方接口进行查询
def zym_list_check(url):
  url=url.replace("www.","")
  for zym_list in open("./Subdomains_En.txt"):
      zym_list=zym_list.replace("\n","")
      zym_list_url=zym_list+"."+url
      try:
          ip=socket.gethostbyname(zym_list_url)
          print(zym_list_url+"->"+ip)
          time.sleep(0.1)
      except Exception as e:
          time.sleep(0.1)
  print('------------------------------------++++++-------------------------------------------')

def zym_api_check(url):
  url=url.replace("www.", "")


#端口扫描
def port_check(url):
  ip = socket.gethostbyname(url)
  #ip="192.168.76.155"
  #ports={'21','22','135','443','445','80','1433','3306',"3389",'1521','8000','7002','7001','8080',"9090",'8089',"4848}
  server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  #for port in ports:
  try:
      data=server.connect_ex((ip, 80))
      if data==0:
          print(ip+":"+str(80)+"|open")
      else:
          print(ip+":"+str(80)+"|close")
          pass
  except Exception as err:
          print("error")
  print('------------------------------------++++++-------------------------------------------')

#系统判断-
#1.基于TTL值进行判断
#2.基于第三方脚本进行判断
def os_check(url):
  data = os.popen("nmap\\nmap -O "+url, "r").read()
  print(data)
  print('------------------------------------++++++-------------------------------------------')

if __name__ == '__main__':
  print("Test：python test.py www.dudu.com all")
  url = sys.argv[1]
  check = sys.argv[2]
  #print(url +"\n"+ check)
  if check=="all":
      ip_check(url)
      # whois_check(url)
      port_check(url)
      cdn_check(url)
      os_check(url)
      zym_list_check(url)