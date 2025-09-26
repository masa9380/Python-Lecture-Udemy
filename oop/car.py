class Car(object):

    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print(f'{self.manufacturer}の{self.model_name}(燃費：{self.mileage})アクセル全開')

    def brakes(self):
        print('{0.manufacturer}の{0.model_name}(燃費：{0.mileage})ブレーキ全開'.format(self))


if __name__ == "__main__":
    prius = Car("Prius", 20, "TOYOTA")
    conti_gt = Car('Bentley Continental',4 ,'Bentley')
    print(prius.manufacturer)
    prius.gas()
    prius.brakes()

    print(conti_gt.manufacturer)
    conti_gt.gas()
    conti_gt.brakes()