blueberry_kcal_100g= 43
cherry_kcal_100g=57
orange_kcal_100g= 47

Blueberry_g= int(input("블루베리의 g수를 입력하세요=>" ))
Cherry_g= int(input("체리의 g수를 입력하세요=>" ))
orange_g= int(input("오렌지의 g수를 입력하세요=>"))

blueberry_total_kcal = (Blueberry_g / 100)*blueberry_kcal_100g
cherry_total_kcal = (Cherry_g/100)*cherry_kcal_100g
orange_toatl_kcal = (orange_g/100)*orange_kcal_100g

total_kcal = blueberry_total_kcal + cherry_total_kcal + orange_toatl_kcal

print("블루베리가{}g일때 {}㎉이고,체리가{}g일때 {}㎉이고,오렌지가{}g일떄 {}㎉이고, 총kcal은{}입니다".\
      format(Blueberry_g,blueberry_total_kcal,Cherry_g,cherry_total_kcal,orange_g,orange_toatl_kcal,total_kcal ))