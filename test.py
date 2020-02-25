import requests
import json

def func():
	# url = "http://192.168.217.100:8888/v1/restserver/ting?method=baidu.ting.ugcdiy.getLabelSongList&cuid=33ac183037c32c8a980b20c0b2b718496c4c7d93&from=ios&version=8.1.1&qa=1&label_id=74,49"
	# ret = requests.get(url)
	# ret = ret.json()
	# ret_songlist = ret["song_list"]

	# ret_set = set()
	# ret_list = []
	# for v in ret_songlist:
	# 	ret_set.add(v["song_id"])
	# 	ret_list.append(v["song_id"])
	# print(len(ret_set))
	# print(len(ret_list))
	# print(ret_set)
	# 
	url = "http://192.168.217.103:7698/diybase/diylist/getDJDiyList?dj_id=554324223&start=0&num=20&diy_type=1"
	#获取返回的json数据
	ret = requests.get(url)
	print (type(ret))   #requests.models.Response
	ret = ret.text
	print(type(ret))   #str
	# print(ret)
	ret = requests.get(url).json()
	print(type(ret))   #dict
	# print(ret)


	# ret = ret["result"]
	# # ret_set = ()
	# ret_list = []
	# for  i in ret:
	# 	# print(i['id'])
	# 	ret_list.append(i['id'])

	# print(sorted(ret_list))
	# for i in sorted(ret_list):
	# 	print(i)
    	

if __name__ == '__main__':
	func()
