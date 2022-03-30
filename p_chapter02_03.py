# Chapter02-03
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리가능

class car():
    """
    Car class
    Author : Lee
    Date : 2022.03.18
    Description : Class, Static, Instance Method
    """

    # 클래스 변수(모든 인스턴스가 공유)
    price_per_raise = 1.0


    def __init__(self, company, details):
        self._company = company
        # self.car_count = 10
        self._details = details
        

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before car price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    # Instance Method
    def get_price_calc(self):
        return 'After car price -> company : {}, price : {}'.format(self._company, self._details.get('price') * car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        print('Succeed price increased.')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return  'OK! This car is {}'.format(inst._company)
        return 'Sorry. This is not a BMW car'

# Self 의미
car1 = car('Ferrari', {'color': 'white', 'horsepower': 400, 'price': 8000})
car2 = car('BMW', {'color': 'black', 'horsepower': 270, 'price': 5000})

# 전체 정보
car1.detail_info()
car2.detail_info()

# 가격 정보(직접 접근)
print(car1._details.get('price'))
print(car2._details.get('price'))

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격 인상(클래스 메소드 미사용)
car.price_per_raise = 1.4

# 가격 정보(인상 후)
print(car1.get_price_calc())
print(car2.get_price_calc())

# 가격 인상(클래스 메소드 사용)
car.raise_price(2)

print(car1.get_price_calc())
print(car2.get_price_calc())

# Static
# 인스턴스로 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
# 클래스로 호출
print(car.is_bmw(car1))
print(car.is_bmw(car2))














