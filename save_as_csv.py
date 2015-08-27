# -*- coding: utf-8 -*-
import os
import sys
import csv
import string
import codecs

''' 
	Author : chenyy
	Copyright(c): chenyy@unionpaysmart.com
	2015-08

	Input:
		core,year \t gain, counts, cardNum
		coreName
	
	save as .csv file 

	执行：
	cat res_09 | sort | cat | python save_as_csv.py gender
	
'''
if __name__ == '__main__':
	ecName = sys.argv[1]
	if ecName == 'age':
		coreName = '年龄'	# 指标名称
	elif ecName == 'gender':
		coreName = '性别'
	else:
		coreName = '未知'
	
	filename = 'oversea' + '_' + ecName + '_' + 'core' + '.csv'
	fh = [coreName, '年', '金额', '笔数', '卡数']
	
	# csv file
	csvfile = file(filename, 'wb')
	csvfile.write(codecs.BOM_UTF8)
	writer = csv.writer(csvfile)
	writer.writerow(fh)	# writer table head

	old_coreYear = 'AAAAAA'
	coreYear = ''
	row = ['AAA', 'AAA', 0.0, 0, 0]	# 单行值: 指标，年，金额，笔数，卡数
	
	for line in sys.stdin:
		items = line.strip('\n').split('\t')
		if len(items) != 2:
			continue
		coreYear = items[0]
		key = items[0].split(',') # 指标，年
		value = items[1].split(',')
		if coreYear != old_coreYear and old_coreYear != 'AAAAAA':
			row[2] = '%.2f'%row[2]	# 金额保留2位小数
			writer.writerow(row)	# writer table by row
			row = ['AAA', 'AAA', 0.0, 0, 0]

		row[0] = key[0]
		row[1] = key[1]
		row[2] += float(value[0])
		row[3] += int(value[1])
		row[4] += int(value[2])
		old_coreYear = coreYear
		
	# 善后
	if coreYear == old_coreYear:
		row[2] = '%.2f'%row[2]	# 金额保留2位小数
		writer.writerow(row)	# writer table by row

	# end file
	csvfile.close()	
