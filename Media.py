class Media:
    def __init__(self, nota1, nota2, nota3):
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3
         
    def notas(self):
        return (self._nota1, self._nota2, self._nota3)
    
    def calcular_media(self):
        return (self._nota1 + self._nota2 + self._nota3) / 3

def main():
    
        nota1 = float(input("nota1: "))
        nota2 = float(input("nota2: "))
        nota3 = float(input("nota3: "))
        
        media = Media(nota1, nota2, nota3)
        
    
if __name__ == "__main__":
    main()

