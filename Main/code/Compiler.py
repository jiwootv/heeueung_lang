# 헤으응 언어 메인 파일

DEBUG = False
class Main():
	def __init__(self, __value : str, mode = False):
		self.l_value = __value
		self.l_values = self.l_value.split("\n")
		self.now_data = {}

		if DEBUG:
			print(self.l_values)


	def data_append(self, ind, v):

		if ind == 1:
			if "." in v:
				print(v.count("."), end="")
			else: print(v, end="")
		else:
			self.now_data[ind] = v

	def compile_main(self):
		for syntax in self.l_values:
			if syntax.count("♡")%2 == 1: raise Exception("하트 열이 닫히지 않았습니다")
			n_syntax = syntax
			temp = syntax.split("♡")
			if DEBUG: print(temp)
			result = 0


			for i in range(1, len(temp), 2):  # 하트 열 index 계산
				t = temp[i].split()
				if DEBUG: print(t, i)
				for k in range(len(t)):
					if DEBUG: print(10 ** (len(t)-k-1) * t[k].count("."))
					result += 10 ** (len(t)-k-1) * t[k].count(".")

			n_syntax = temp[0] + " " + "." * result
			if DEBUG:
				print(result)
				print(n_syntax)

			temp = n_syntax.split()
			temp4, temp3 = 0, 0
			if DEBUG: print(temp)
			if "응기잇" in temp:
				temp4 = temp.index("응기잇")+1
				if DEBUG: print(self.now_data[temp[temp4].count(".")-1])
				temp[temp4] = self.now_data[temp[temp4].count(".")-1]
				del temp[temp4 - 1]


			if "가버렷" in temp:
				temp3 = temp.index("가버렷")+1
				if DEBUG: print(chr(temp[temp3].count(".")))
				temp[temp3] = chr(temp[temp3].count("."))
				del temp[temp3-1]
			if DEBUG: print(temp)
			for i in range(1, len(temp)):
				if temp[i-1] == "헤으응":
					self.data_append(temp[i].count("."), temp[i+1])


text = """헤으응 . 가버렷♡........ ...♡\n헤으응 . ♡. ......... ....... ..♡"""
M = Main(text)
M.compile_main()
