# -*- coding: utf-8 -*-
import os
import sys

''' 
	Author : chenyy
	Copyright(c): chenyy@unionpaysmart.com
	2015-08

	Input:
		cardNo, flag, age
		cardNo, flag, year, gain
	
	Output:
		age,year \t sum(gain), sum(counts), sum(cardNum)
'''


if __name__ == '__main__':
	old_cardNo = "AAAAAA"
	cardNo_1 = "BBBBBB"
	cardNo_2 = ""
	old_age = ""
	age = ""
	dAge = {} 	# age 为 key
	lYear = []	# Year 为 key

	for line in sys.stdin:
		items = line.strip('\n').split('\t')
		if len(items) == 3:
			cardNo_1 = items[0]
			age = items[2]
		if len(items) == 4:
			cardNo_2 = items[0]
			year = items[2]
			gain = float(items[3])	
			# 卡号未出现在逻辑08中
			if cardNo_1 != cardNo_2:
				age = "other"
			# 统计，卡号不一样，卡数 +1
			if cardNo_2 != old_cardNo and old_cardNo != "AAAAAA":
				for key in lYear:
					dAge[old_age][key][2] += 1
				lYear = []
			
			if dAge.get(age,0) == 0:
				dAge[age] = {}
			if year not in dAge[age].keys():
				dAge[age][year] = [0.0, 0, 0]	# {gender:{year:[金额，笔数，卡数]}}
			dAge[age][year][0] +=  gain  # 金额累加
			dAge[age][year][1] += 1	# 次数 +1
			old_cardNo = cardNo_2
			old_age = age
			if year not in lYear:
				lYear.append(year)

	# 善后
	if old_cardNo == cardNo_2:
		for key in lYear:
			dAge[old_age][key][2] += 1 # 卡数 +1
	# 输出 dAge[age][year] = [金额，笔数，卡数]
	age = ""
	year = ""
	for age in dAge.keys():
		for year in dAge[age].keys():
			sumGain = '%.2f'%dAge[age][year][0]
			print age + ',' + year + '\t' + sumGain + ',' + str(dAge[age][year][1]) + ',' + str(dAge[age][year][2])

