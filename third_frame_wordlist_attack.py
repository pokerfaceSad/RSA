#By now,we have found that the structure of plaintext frame.
#In this program,we give the prefix of the third plaintext frame.And we already have get the second plaintext frame which ends with 'f',we just construct a wordlist of the words start with 'f',padding the rest letters with exhaustive attack and we can finally decode the plaintext frame.   
import os
import os.path
import sys
import copy
import binascii
import math
import timeit

plain_pre="9876543210abcdef000000020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
#The third plaintext frame starts with the string,plain_pre.


def gcd(a,b):
	while(a!=0):
		a,b=b%a,a
	return b
def findModInverse(a,m):
	if(gcd(a,m)!=1):
		return None
	u1,u2,u3=1,0,a
	v1,v2,v3=0,1,m
	while(v3!=0):
		q=u3//v3
		v1,v2,v3,u1,u2,u3=(u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
	#print v1,v2,v3,u1,u2,u3
	return u1%m


def classify(class_list):
	#store_list=copy.deepcopy(class_list)
	#result_list=[]
	result_dict={}
	for item in class_list:
		if item[0] not in result_dict.keys():
			#result_list.append(item[0])
			result_dict[item[0]]={}
		#index_num=result.index(item[0])
		if item[1] not in result_dict[item[0]].keys():
			result_dict[item[0]][item[1]]=set()
		result_dict[item[0]][item[1]]=result_dict[item[0]][item[1]]|{item[2]}
	return result_dict








os.chdir("./fujian2")
list_dir=os.listdir('.')
#print list_dir
frame_list=[]
E_attemp=3

len_8_list=[]
len_7_list=[]
len_6_list=[]
len_5_list=[]
len_4_list=[]
len_3_list=[]
len_2_list=[]
len_1_list=[]

with open('../dictionary.txt') as dic_fd:      #From attemping,we have found that this attack takes a lot of time,and with the length of the word decrease,the time the exhaustive attack takes rates exponentially  
	for line in dic_fd.readlines():
		tmp=line.strip().lower()
		if(len(tmp)>=9):
			len_8_list.append(tmp[1:9])
		elif(len(tmp)==8):
			len_7_list.append(tmp[1:])
		elif(len(tmp)==7):
			len_6_list.append(tmp[1:])
		elif(len(tmp)==6):
			len_5_list.append(tmp[1:])
		elif(len(tmp)==5):
			len_4_list.append(tmp[1:])
		elif(len(tmp)==4):
			len_3_list.append(tmp[1:])
		elif(len(tmp)==3):
			len_2_list.append(tmp[1:])
		elif(len(tmp)==2):
			len_1_list.append(tmp[1:])

for frame_file in list_dir:                    #frame_list is the list whose element is the tuples of (e,N,c,frame_name)
	with open(frame_file) as fd:
		code_str=fd.readline()
		N=int(code_str[0:256],16)              #extract N in the frame
		e=int(code_str[256:512],16)            #extract e in the frame
		c=code_str[512:768].lower()            #extract c in the frame
		if(e==E_attemp):
			frame_list.append((frame_file,e,N,c))
#print len_8_list[:10]
#print frame_list
def len_8_attemp():                                                                    #Words in this wordlist all have 8 letters,so we do not need to apply exhaustive attack
	for item in len_8_list:
		plain_attemp=plain_pre+binascii.b2a_hex(item)
		#print plain_attemp
		plain_attemp_num=int(plain_attemp,16)
		for item_0 in frame_list:
			#print hex(pow(plain_attemp_num,E_attemp,item_0[2]))
			if(item_0[3].lstrip('0') in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
				print item_0[0]
				print plain_attemp
	print "length 8 attemped."

def len_7_attemp():                                                                    #Words in this wordlist all have 7 letters,so we need to apply one-letter exhaustive attack
	for item in len_7_list:
		for item_1 in ' ,.:(!\'\"':
			plain_attemp=plain_pre+binascii.b2a_hex(item+item_1)
			plain_attemp_num=int(plain_attemp,16)
			for item_0 in frame_list:
				if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
					print item_0[0]
					print plain_attemp
	print "length 7 attemped."

def len_6_attemp():                                                                    #Words in this wordlist all have 6 letters,so we need to apply two-letter exhaustive attack
	for item in len_6_list:
		for item_1 in ' ,:(\'\"':
			for item_2 in 'abcdefghijklmnopqrstuvwxyzI':
				plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2)
				plain_attemp_num=int(plain_attemp,16)
				for item_0 in frame_list:
					if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
						print item_0[0]
						print plain_attemp
		for item_1 in '.!':
			for item_2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2)
				plain_attemp_num=int(plain_attemp,16)
				for item_0 in frame_list:
					if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
						print item_0[0]
						print plain_attemp
	print "length 6 attemped."


def len_5_attemp():                                                                    #Words in this wordlist all have 5 letters,so we need to apply three-letter exhaustive attack
	for item in len_5_list:
		for item_1 in ' ,:(\'\"':
			for item_2 in 'abcdefghijklmnopqrstuvwxyzI':
				for item_3 in ' abcdefghijklmnopqrstuvwxyzI':
					plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2+item_3)
					plain_attemp_num=int(plain_attemp,16)
					for item_0 in frame_list:
						if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
							print item_0[0]+" is decoded"
							print "The plaintext frame is: \n "+plain_attemp
							print "The plaintext message is :\n"+item+item_1+item_2+item_3
		for item_1 in '.!':
			for item_2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				for item_3 in ' abcdefghijklmnopqrstuvwxyzI':
					plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2+item_3)
					plain_attemp_num=int(plain_attemp,16)
					for item_0 in frame_list:
						if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
							print item_0[0]+" is decoded"
							print "The plaintext frame is: \n "+plain_attemp
							print "The plaintext message is :\n"+item+item_1+item_2+item_3
	print "length 5 attemped."

def len_4_attemp():                                                                    #Words in this wordlist all have 4 letters,so we need to apply four-letter exhaustive attack
	for item in len_4_list:
		for item_1 in ' ,:(\'\"':
			for item_2 in 'abcdefghijklmnopqrstuvwxyzI':
				for item_3 in ' abcdefghijklmnopqrstuvwxyzI':
					for item_4 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2+item_3+item_4)
						plain_attemp_num=int(plain_attemp,16)
						for item_0 in frame_list:
							if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
								print item_0[0]
								print plain_attemp
		for item_1 in '.!':
			for item_2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				for item_3 in ' abcdefghijklmnopqrstuvwxyzI':
					for item_4 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2+item_3+item_4)
						plain_attemp_num=int(plain_attemp,16)
						for item_0 in frame_list:
							if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
								print item_0[0]
								print plain_attemp
	print "length 4 attemped."

def len_3_attemp():                                                                    #Words in this wordlist all have 3 letters,so we need to apply five-letter exhaustive attack
	for item in len_3_list:
		for item_1 in ' ,:(\'\"':
			for item_2 in 'abcdefghijklmnopqrstuvwxyzI':
				for item_3 in ' abcdefghijklmnopqrstuvwxyzI':
					for item_4 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						for item_5 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
							plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2+item_3+item_4+item_5)
							plain_attemp_num=int(plain_attemp,16)
							for item_0 in frame_list:
								if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
									print item_0[0]
									print plain_attemp
		for item_1 in '.!':
			for item_2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				for item_3 in ' abcdefghijklmnopqrstuvwxyzI':
					for item_4 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						for item_5 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
							plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2+item_3+item_4+item_5)
							plain_attemp_num=int(plain_attemp,16)
							for item_0 in frame_list:
								if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
									print item_0[0]
									print plain_attemp
	print "length 3 attemped."


def len_2_attemp():                                                                    #Words in this wordlist all have 2 letters,so we need to apply six-letter exhaustive attack
	for item in len_2_list:
		for item_1 in ' ,:(\'\"':
			for item_2 in 'abcdefghijklmnopqrstuvwxyzI':
				for item_3 in ' abcdefghijklmnopqrstuvwxyzI':
					for item_4 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						for item_5 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
							for item_6 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
								plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2+item_3+item_4+item_5+item_6)
								plain_attemp_num=int(plain_attemp,16)
								for item_0 in frame_list:
									if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
										print item_0[0]
										print plain_attemp
		for item_1 in '.!':
			for item_2 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
				for item_3 in ' abcdefghijklmnopqrstuvwxyzI':
					for item_4 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
						for item_5 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
							for item_6 in ' abcdefghijklmnopqrstuvwxyz ,.:(!\'\"ABCDEFGHIJKLMNOPQRSTUVWXYZ':
								plain_attemp=plain_pre+binascii.b2a_hex(item+item_1+item_2+item_3+item_4+item_5+item_6)
								plain_attemp_num=int(plain_attemp,16)
								for item_0 in frame_list:
									if(item_0[3] in hex(pow(plain_attemp_num,E_attemp,item_0[2]))):
										print item_0[0]
										print plain_attemp
	print "length 2 attemped."


if __name__=="__main__":                                                               #We try to decode the third frame.Meanwhile,we output the time each wordlist take.
	print "Taking time "+repr(timeit.timeit("len_8_attemp()",setup="from __main__ import len_8_attemp",number=1))+"seconds.\n"
	print "Taking time "+repr(timeit.timeit("len_7_attemp()",setup="from __main__ import len_7_attemp",number=1))+"seconds.\n"
	print "Taking time "+repr(timeit.timeit("len_6_attemp()",setup="from __main__ import len_6_attemp",number=1))+"seconds.\n"
	print "Taking time "+repr(timeit.timeit("len_5_attemp()",setup="from __main__ import len_5_attemp",number=1))+"seconds.\n"
	#print "Taking time "+repr(timeit.timeit("len_4_attemp()",setup="from __main__ import len_4_attemp",number=1))+"seconds."
	#print "Taking time "+repr(timeit.timeit("len_3_attemp()",setup="from __main__ import len_3_attemp",number=1))+"seconds."
	#print "Taking time "+repr(timeit.timeit("len_2_attemp()",setup="from __main__ import len_2_attemp",number=1))+"seconds."



