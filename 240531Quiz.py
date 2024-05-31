class Beverage:
    def __init__(self):
        self.manu = {"커피": 3000, "녹차": 2500, "아이스티": 3000}
    def calculate(self,name,num):
        if name in self.manu:
            all_price = self.manu[name]*num
            print(f"{Beverage_name} {Beverage_num}잔의 가격은 {all_price} 입니다")
            return all_price
        else:
            print("존재하지 않는 음료입니다.")
            return None
음료 = Beverage()


# class 외부에 존재
Beverage_name = input("주문할 음료를 입력하세요")
Beverage_num = int(input("주문할 수량을 입력하세요"))

all_price = 음료.calculate(Beverage_name,Beverage_num)



# total = menu[drink] *num
# print("고객이 주문한 음료는"+ drink)
# print("고객이 주문한 수량은"+ num)
# pirnt("총 구입 가격은" + total)
