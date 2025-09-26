from car import Car

class Truck(Car):

    def __init__(self, model_name, mileage, manufacturer, load_cap):
        super().__init__(model_name=model_name, mileage=mileage, manufacturer=manufacturer)
        self._load_cap = load_cap
        self._current_load = 0


    def gas(self):
        if self._current_load > self._load_cap:
            print('重量オーバーなので走れません。')
            print(f'{self._current_load-self._load_cap}の荷物をおろしてください')
        else:
            super().gas()

    def load(self, weight):
        if self._current_load + weight >= 0:
            self._current_load += weight
            self.show_load()
        else:
            self._current_load = 0
            print(f'荷物を全て下ろしました。現在の積載量：{self._current_load}')

        if self._current_load > self._load_cap:
            print(f'現在の積載量が最大積載量を超えているので注意。最大積載量は{self._load_cap}です')


    def show_load(self):
        print(f'loadしました。現在の積載量は{self._current_load}です')

if __name__ == "__main__":
    isuzu = Truck('model', 7, 'isuzu', 5000)
    print(isuzu.model_name)
    isuzu.gas()
    isuzu.load(1000)
    isuzu.load(5000)
    isuzu.gas()
    isuzu.load(-7000)
