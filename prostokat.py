class Prostokat:
    def __init__(self,szerokosc,wysokosc):
        self.szer = szerokosc
        self.wys  = wysokosc
    def pobierz_obwod(self):
        
        return  2 * (self.szer + self.wys)
    def pobierz_pole(self):
       
        return (self.szer * self.wys)