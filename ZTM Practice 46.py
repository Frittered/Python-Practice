class American:
    @staticmethod
    def print_nationality():
        print('American')
class NewYorker(American):
    @staticmethod
    def whereyafrom():
        print('New Yoahk')
aNY = NewYorker()
aNY.print_nationality()
aNY.whereyafrom()
