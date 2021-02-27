import time

class TrafficLight:
    __color = ''

    def __init__(self):
        pass

    def running(self):
        i = 1
        max = 4
        while True:
            self.__color = 'Red'
            print(self.__color)
            time.sleep(7)

            self.__color = 'Yellow'
            print(self.__color)
            time.sleep(2)

            self.__color = 'Green'
            print(self.__color)
            time.sleep(4)
            i += 1
            if i > max:
                break

traffic_light_1 = TrafficLight()

traffic_light_1.running()
