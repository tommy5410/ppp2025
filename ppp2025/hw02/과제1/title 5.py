price = 2000
sale =  15
total = price-(price*sale/100) 
#print("{}원, {}%, {}원".format(price,sale,total))
print("할인된 가격은 {:,.0f}입니다.".format(total)