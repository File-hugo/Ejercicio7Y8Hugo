"""
7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se
puede modificar directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.

"""
import colorama
from colorama import Fore

class Cuenta:
    def __init__(self,retirar=0):#Va vacio el constructor
        self.__resultadoTitulo=[]
        salidaTituloOpcional=True
        contadorTitulo=0
        self.__retirar=retirar
        #-
        while contadorTitulo<2:
            self.__titularOpcional = input('ingresa titular opcional :')
            if self.__titularOpcional in "01233456789":
                print("Debe tener solo letras")
                salidaTituloOpcional=False           
            elif self.__titularOpcional not in "0123456789":
                contadorTitulo+=1
                salidaTituloOpcional==True
                self.__resultadoTitulo.append(self.__titularOpcional)
            if contadorTitulo==2:
                salidaTituloOpcional==True
    
    def ingresar(self):
        self.__resultadoCantidad=[]
        self.__cantidad = ""  
        self.__sumasumaCantidad=0
        print("ingresa cantidad en numeros o salga con *")
        
        while  self.__cantidad!="*":
            self.__cantidad = input("ingresa cantidad o salir con *:")
            if self.__cantidad  in"0123456789" and self.__cantidad!="" and self.__cantidad>str(0):
                self.__resultadoCantidad.append(float(self.__cantidad))
            print(self.__resultadoCantidad)
            
        for i in self.__resultadoCantidad:
            self.__sumasumaCantidad=self.__sumasumaCantidad+int(i)
            
        print("La suma es", self.__sumasumaCantidad)
    
    def retirar(self,retirar):
        retirar = input("ingresa cuanto dinero retiraras:")
        #self.__retirar=retirar
        while retirar.isalpha():
            print("Solo numeros")
            retirar = input("ingresa cuanto dinero retiraras:")
            pass
        else:
            self.__retirar=retirar
            print( f'{self.__retirar} ahora vale {retirar}"')

            retirar=int(self.__retirar)
            self.__cantidad=int(self.__sumasumaCantidad)
            #print(type(sumasuma))
            retirar=self.__sumasumaCantidad-retirar
            print(Fore.RED,retirar,"Es el precio que te quedo")
            #return retirar
   
    def __str__(self,titularOpcional):
        return self.titularOpcional
    
    def get_titularOpcional(self):
        return self.__titularOpcional
    
    def get_cantidad(self):
        return self.__cantidad

    def get_retirar(self):
        return retirar
    
    #def set_retirar(self,retirar):
         #return self.__retirar
        #print( f'{self.__retirar} ahora vale {retirar}"')
        #self.__retirar=retirar
       
    def set_titularOpcional(self,__titularOpcional):
        return self.__titularOpcional
    
    def set_cantidad(self,cantidad):
        return self.__cantidad

    def set_cantidad(self,cantidad):
        return self.__sumasumaCantidad
    
    def mostrar(self):
        #result=f'{cantidad:.2f}'               
        return self.__cantidad
        return self.__titularOpcional
        return self.__sumaCantidad
        return self.__sumasumaCantidad
        return retirar

#Instanciamos
cuenta1=Cuenta()
cuenta1.ingresar()
cuenta1.retirar(1)
#cuenta1.retirar()
print(cuenta1.retirar)
cuenta1.mostrar()
    
#cuenta1=Cuenta(22.2,"Dorival")#No importa que ponga 1 o mas de 1 argumento
#Setters permite cambiar el valor de las propiedades encapsuladas/actualizar
#print(cuenta1.get_cantidad(),cuenta1.get_titularOpcional())
#cuenta1.set_cantidad(30)#Actualizo valor


