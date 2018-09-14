import sys

def get_substr_2(input, sub_len):
	sub_str = []
	if sub_len == 1:
		for x in input:
			sub_str.append(x)
		#print sub_str
		return sub_str
		
	if (sub_len):
		nw_input = input[1:]
		for i in range(0, len(nw_input)):
			x = input[i: i + 1]
			sub_str1 = get_substr_2(input[i + 1:], sub_len - 1)
			'''for sub in sub_str1:
				sub_str.append(sub)'''
			for sub in sub_str1:
				sub_str.append(x + sub)
	#print sub_str
	return sub_str
		
def get_substr_3(input):
	sub_str = []
	for i in range (0, len(input)):
		tmp_substr = get_substr_2(input, i + 1)
		for sub in tmp_substr:
			sub_str.append(sub)
		
	return sub_str

def get_substr_1(prx, input):
	print (prx, input)
	sub_str = []

	for x in input:
		n_prx = prx + x 
		sub_str.append(prx + x)
		n_sub_str = get_substr_1(n_prx, input[1:])
		sub_str = sub_str + n_sub_str

	print sub_str

	return sub_str
		

def get_substr(input):
	sub_str = []

	if len(input) == 0:
		return sub_str

	for i in range(0, len(input)):
		sub_str.append(input[i : i + 1])
		print ("start::::")
		sub_str = sub_str + get_substr_1(input[i : i + 1], input[i + 1:])
	return sub_str

def revers_str(input):
	new_str = ""
	for i in input:
		new_str = i + new_str 
	return new_str

def remove_non_poly(sub_str):
	poly_str = []
	for tmp_str in sub_str:
		tmp_rsv = revers_str(tmp_str)
		if (tmp_rsv == tmp_str):
			poly_str.append(tmp_str)
	
	return poly_str

def remove_dup(sub_str):
	nw_sub_str = []
	for sub in sub_str:
		if sub not in nw_sub_str:
			nw_sub_str.append(sub)
	return nw_sub_str

def get_poly(input):
	sub_str = get_substr_3(input)
	print (sub_str)
	poly_str = remove_non_poly(sub_str)
	print len(poly_str)
	return poly_str

def get_common_substr(sub_str1, sub_str2):
	common_list = []
	for str1 in sub_str1:
		if str1 in sub_str2:
			common_list.append(str1)

	return common_list
		

def get_common_poly(input1, input2):
	poly1 = get_poly(input1)
	poly2 = get_poly(input2)
	common_poly = get_common_substr(poly1, poly2)
	nw_sub = remove_dup(common_poly)	
	#return common_poly
	return nw_sub



def main():
	if (len(sys.argv) < 3):
		print("usage error: file <str> <str>")
		return 1

	sub_str = get_common_poly(sys.argv[1], sys.argv[2])
	#sub_str = get_substr_2(sys.argv[1], sys.argv[1], int(sys.argv[2]))
	print len(sub_str)
	print sub_str

if __name__ == "__main__":
	main()
