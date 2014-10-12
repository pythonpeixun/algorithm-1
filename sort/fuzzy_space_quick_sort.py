#!/usr/bin/env python 
#-*- coding:utf-8 -*-
from math import *
"""
模糊空间排序唯一需要考虑的问题就是空间的合并。
其实也比较简单，因为排序之后的数组中：可以合并的元素都在附近，因此可以一次合并。
复杂度是O(n),因此不影响总体的复杂度。
"""
class Range(object):
	"""docstring for Range"""
	def __init__(self, start,end):
		super(Range, self).__init__()
		self.__start=start
		self.__end=end

	def __cmp__(self,other):
		if self.__end<other.__start:
			return -1
		elif self.__start>other.__end:
			return 1
		else:
			return 0

	def merge(self,other):
		if self!=other:
			raise ValueError("the two range can not be marge")
		return Range(min(self.__start,other.__start),max(self.__end,other.__end))

	def __str__(self):
		return "Range(%s->%s)" % (self.__start,self.__end)

	def __unicode__(self):
		return self.__str__()



def partition(li,start,end):
	li_len=end-start+1
	if li_len<2:
		raise ValueError("list which lenght is less then 2 do not need to partition")
	#使用最后一个元素作为分割点
	print "end %s" % end
	key=li[end]
	middle_index=start
	for x in xrange(start,end):
		if li[x]<key:
			li[middle_index],li[x]=li[x],li[middle_index]
			middle_index+=1
	li[end],li[middle_index]=li[middle_index],li[end]
	return middle_index

def sort(li,start,end):
	li_len=end-start+1
	if li_len<2:
		return li
	middle_index=partition(li,start,end)
	sort(li,start,middle_index-1)
	sort(li,middle_index+1,end)
	print li
	result=[]
	for x in li:
		if result and result[-1]==x:
			result[-1].merge(x)
		else:
			result.append(x)
	li[:]=result[:]
	return li

def main():
	li=[Range(10,20),Range(20,30),Range(30,40),Range(40,50)]
	sort(li,0,3)
	for x in li:
		print x

if __name__ == '__main__':
	main()