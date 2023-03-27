"""
8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
"""

class CuentaJoven:
    def __init__(self,valorCuenta=0,sumaBonificacion=0):#Constructor
        self.__listaDeEdad=[]
        self.__edad=""
        boolCorroboroNumeros=True
        self.__sumaBonificacion=0
        self.__contadorEdad=0
        self.__x=0
        #-
        self.__retirarUno=""
        self.__retirarDos=""
        #-
        self.__resultadoTitulo=[]
        self.__salidaTituloOpcional=True
        self.__contadorTitulo=0
        self.__bonificacion=0.5#5% de
        self.__valorCuenta=0        
        #----
        self.__resultadoCantidadUno=[]
        self.__engloboTodo={}
        self.__resultadoCantidadDos=[]
        self.__cantidadTitularUno = ""
        self.__cantidadTitularDos = ""
        self.__sumaCantidadUno=0
        self.__sumaCantidadDos=0
        self.__agrupoListaUno=[]
        self.__agrupoListaDos=[]

        self.__boolMayorMenorEdad=""
####Otra funcion#########

    def proceso(self):
        while self.__contadorEdad<2:
            self.__edad = input('ingresa edad :')
            if self.__edad=="*":
                break
            #if self.__edad.isalpha() or any(self.__edad!="0123456789"):
#and c<=0 and c>150 or c in "0123456789" and c<=0 and c>150
            resultado=(any(map(str.isalpha, self.__edad)))
            resultadoDigito=(any(map(str.isdigit, self.__edad)))
            if resultado:
                print("Error")
                    #if self.__edad.isdigit():
                boolCorroboroNumeros=False
            #elif int(self.__edad)>=10 or int(self.__edad)<150 :
            elif resultadoDigito:
                boolCorroboroNumeros=True
                self.__contadorEdad+=1
                    
            if boolCorroboroNumeros==True:
            #if boolCorroboroNumeros==True and int(self.__edad)>=0 and int(self.__edad)<150:
                #print(self.__edad)
                self.__listaDeEdad.append(self.__edad)
                print(self.__listaDeEdad)
            else:
                print("Edad debe ser entre 1 y 149")
        
        #-----  
        while self.__contadorTitulo<2:
            self.__titularOpcional = input('ingresa titular opcional:')
            if self.__titularOpcional in "01233456789":
                print("Debe tener solo letras")
                self.__salidaTituloOpcional=False           
            elif self.__titularOpcional not in "0123456789":
                self.__contadorTitulo+=1
                self.__salidaTituloOpcional==True
                #self.__resultadoTitulo.update({self.__titularOpcional:self.__edad})
                self.__resultadoTitulo.append(self.__titularOpcional)

        self.__agrupoListaUno.append("Titular 1: "+self.__resultadoTitulo[0]+ " , " + self.__listaDeEdad[0] + " años")
        print(self.__agrupoListaUno)
        
        self.__agrupoListaDos.append("Titular 2: "+self.__resultadoTitulo[1]+ " , " + self.__listaDeEdad[1] + " años")
        print(self.__agrupoListaDos)
    

        ###Titular uno###
        while self.__cantidadTitularUno!="*":
            self.__cantidadTitularUno = input("ingresa cantidad o salir con *:")
            if self.__cantidadTitularUno.isdigit() and self.__cantidadTitularUno!="":
                if self.__cantidadTitularUno>=str(0):
                    self.__resultadoCantidadUno.append(float(self.__cantidadTitularUno))
                self.__agrupoListaUno.append("Titular 1 " +self.__resultadoTitulo[0]+ " , " + self.__listaDeEdad[0] + " años" +str(self.__resultadoCantidadUno[0]) +" es la cantidad")
                print(self.__resultadoCantidadUno)
            
        for i in self.__resultadoCantidadUno:
            self.__sumaCantidadUno=self.__sumaCantidadUno+int(i)            
        print("La suma es", self.__sumaCantidadUno)
        
        self.__resultadoTitulo.append(self.__sumaCantidadUno)
        print(self.__resultadoTitulo)
        
    ###Titular Dos###
        print(" ")
        print("Cantidad titular dos")
        print(" ")
        while self.__cantidadTitularDos!="*":
            self.__cantidadTitularDos = input("ingresa cantidad o salir con *:")
            if self.__cantidadTitularDos.isdigit() and self.__cantidadTitularDos!="":
                if self.__cantidadTitularDos>=str(0):
                    self.__resultadoCantidadDos.append(float(self.__cantidadTitularDos))
                self.__agrupoListaDos.append("Titular 2 " +self.__resultadoTitulo[1]+ " , " + self.__listaDeEdad[1] + " años" +str(self.__resultadoCantidadDos[0]) +" es la cantidad")
                print(self.__resultadoCantidadDos)
            
        for x in self.__resultadoCantidadDos:
            self.__sumaCantidadDos=self.__sumaCantidadDos+int(x)            
        print("La suma es", self.__sumaCantidadDos)
        
        self.__resultadoTitulo.append(self.__sumaCantidadDos)
        print(self.__resultadoTitulo)
    
    #Otra funcion#
    def titular_valido(self):
        global x
        
        for x in (self.__listaDeEdad):
            if int(x)<18:
                self.__boolMayorMenorEdad=False#Porque es menor de edad
                #print( "Error "+x+" años es = a menor de edad. No puede retirar $")

            elif int(x)>=18:
                self.__boolMayorMenorEdad=True              
                        ######Retiro dinero titular 1###
                self.__retirarUno=input("Cuanto deseas retirar el titular uno:?")
                self.__retirarDos=input("Cuanto deseas retirar el titular dos:?")
                
                if self.__retirarUno.isdigit() <0 or self.__retirarDos.isdigit()<0:
                    print("Error, no puede ser cero")      
                else:
                    if self.__retirarUno.isdigit() and self.__retirarUno!="":
                        self.__cantidadNuevaTitularUno=self.__sumaCantidadUno-float(self.__retirarUno)
                        self.__cantidadNuevaTitularUno=self.__bonificacion*self.__cantidadNuevaTitularUno
                        #print("Tienes ahora", self.__cantidadNuevaTitularUno, "$", "porque retiraste", self.__retirarUno)
                    
                    if self.__retirarDos.isdigit() and self.__retirarDos!="" :
                        self.__cantidadNuevaTitularDos=self.__sumaCantidadDos-float(self.__retirarDos)    
                        self.__cantidadNuevaTitularDos=self.__bonificacion*self.__cantidadNuevaTitularDos
                        self.__sumaBonificacion=int(self.__sumaBonificacion)  
                        #print("Tienes ahora", self.__cantidadNuevaTitularDos, "$", "porque retiraste", self.__retirarDos)              
        return self.__boolMayorMenorEdad     
    def get_edad(self):
        return get_edad
    
    def set_edad(self):
        return self.__edad
    
    def mostrar(self):
            #return self.__listaDeEdad
            #return self.__titularOpcional
            #return self.__valorCuenta
        if self.__boolMayorMenorEdad==True:            
            print("Tienes ahora", self.__cantidadNuevaTitularUno, "$", "porque retiraste", self.__retirarUno)              
            print("Tienes ahora", self.__cantidadNuevaTitularDos, "$", "porque retiraste", self.__retirarDos)              
        elif self.__boolMayorMenorEdad==False:
            print( "Error "+x+" años es = a menor de edad. No puede retirar $")

instancioUno=CuentaJoven()
instancioUno.proceso()
instancioUno.titular_valido()
instancioUno.mostrar()
#print()
        #self.__engloboTodo.update({self.__titularOpcional:self.__edad})
        #self.__resultadoTitulo.append(self.__titularOpcional)
#         if contadorTitulo==2:
#             salidaTituloOpcional==True
#             #print(self.__engloboTodo)
#             primeraKeyValue = list(self.__engloboTodo.items())[0]
#             segundaKeyValue = list(self.__engloboTodo.items())[1]           
#             print("Primer titular:",primeraKeyValue)
#             print("Segundo titular:",segundaKeyValue)
#             #print("Titulares:",self.__resultadoTitulo[0])
#             #print("Titulares:",self.__resultadoTitulo[1])