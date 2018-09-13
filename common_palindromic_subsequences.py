import sys


def get_substr(input):
	sub_str = []
	len_str = len(input)

	for i in range (0, len_str):
		sub_str.append(input[i:i + 1])
		prfx = input[i : i + 1]
		for k in range (i + 1, len_str):
			for j in range (k, len_str):
				#if prfx + input[k : j + 1] not in sub_str:
				sub_str.append(prfx + input[k:j + 1])

		if i == 0:
			continue

		prfx = input[0 : i + 1]
		for k in range (i + 1, len_str):
			for j in range (k, len_str):
				#if prfx + input[k : j + 1] not in sub_str:
				sub_str.append(prfx + input[k:j + 1])
			

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

def get_poly(input):
	sub_str = get_substr(input)
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
	return common_poly



def main():
	if (len(sys.argv) < 3):
		print("usage error: file <str> <str>")
		return 1

	sub_str = get_common_poly(sys.argv[1], sys.argv[2])
	print len(sub_str)
	print sub_str

if __name__ == "__main__":
	main()
