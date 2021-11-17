import requests
from random import choice

username="mino159" #your nick on BGG

def main():
	titles=giveList() 		#take a list of all games
	# titles=[stripBetween(title,"(",")") for title in titles]
	chosen=choice(titles) 	#choose one
	print(chosen) 			#print it

def stripBetween(string,str_start,str_end):
	"Strip string of all characters between 2 strings"
	index_start=string.find(str_start)
	index_end  =string.find(str_end)
	if index_start!=-1:
		string=string[:index_start]+string[index_end+1:]
	return string

def find_all(a_str, sub_start,sub_end):
	"find all the titles of games"
	names=[]
	start = 0;
	while True:
		name_starts = a_str.find(sub_start, start)
		# print(finding)
		if name_starts == -1: 
			break
		start = name_starts + len(sub_start)
		name_ends= a_str.find(sub_end,start)
		name=a_str[start:name_ends]
		# print(name)

		names.append(name)
		
	return names


def giveList():
	url=f"https://boardgamegeek.com/collection/user/{username}?own=1&subtype=boardgame&ff=1"
	response = requests.get(url)
	soup= response.text
	all_titles=find_all(soup,"class='primary' >","<")

	return all_titles

main()