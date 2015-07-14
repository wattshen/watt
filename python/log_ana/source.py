
'''
Content = {
	"0":{"SESSION_ID":""},
	"1":{"F_DATE":""},
	"2":{"F_TIME":""},
	"3":{"F_MOBILE":""},
	"4":{"F_CITY":""},
	"5":{"F_BRAND":""},
	"6":{"F_KEYWORD":""},
	"7":{"SYSTEM_ID":""},
	"8":{"CATEGORY_ID":""},
	"9":{"F_ID":""},
	"10":{"F_USER_AGENT":""},
	"11":{"F_TOTAL":""},
	"12":{"F_OFFSET":""},
	"13":{"F_URL":""},
	"14":{"F_TITLE":""},
	"15":{"F_DESC":""},
	"16":{"F_BACK_KEYWORD":""}
}
'''


Content_k = range(17)
Content_v = {}.fromkeys(["SESSION_ID","F_DATE","F_TIME","F_MOBILE","F_CITY","F_BRAND","F_KEYWORD","SYSTEM_ID","CATEGORY_ID","F_ID","F_USER_AGENT","F_TOTAL","F_OFFSET","F_URL","F_TITLE","F_DESC","F_BACK_KEYWORD"])
i = 0
while i < 17:
	Content = {Content_k[i]:Content_v}
	i += 1