class Restaurantes:
    def __init__(self):
        self.codigo = []
        self.nombre = []
        self.precio = []
        self.descuento = []
        self.descripcion = []
        self.tipo = []
        self.habilitado = []
    
    def menu(self):
        opciones = """
        1.- REGISTRAR PLATO DE COMIDA
        2.- MOSTRAR LISTADO DEL MENU
        3.- MOSTRAR MENU DEL DIA
        4.- MODIFICAR PLATO
        5.- HABILITAR PLATO
        6.- DESHABILITAR PLATO
        7.- MOSTRAR PLATOS DE DESHABILITADO
        8.- BUSCAR POR TIPO DE PLATO
        9.- SALIR
        """

        print(opciones)
        seleccionar= int(input("Seleccione una opcion: \n"))
        if (seleccionar == 1):
            print(self.agregarPlato())
            self.menu()
        elif (seleccionar == 2):
            print(self.MenuTodoPlato())
            print(self.volverMenu())
        elif (seleccionar == 3):
            print(self.verPlatoAlta())
            print(self.volverMenu())
        elif (seleccionar == 4):
            print(self.editarPlato())
            print(self.volverMenu())
        elif (seleccionar == 5):
            print(self.realizarAlta())
            print(self.volverMenu())
        elif (seleccionar == 6):
            print(self.realizarBaja())
            print(self.volverMenu())
        elif (seleccionar == 7):
            print(self.verPlatoBaja())
            print(self.volverMenu())
        elif (seleccionar == 8):
            print(self.usuarioBuscarTipoPlato())
            print(self.volverMenu())
        elif (seleccionar == 9):
            print("Transacciones realizadas exitosamente")
        else:
            print("Seleccione una opcuon del menu")
            self.menu()

    def volverMenu(self):
        eleccion = input("Desea volver al menu: y/n \n")
        if (eleccion == 'y' or eleccion == 'Y'):
            self.menu()
        return "-------Transacciones Terminadas-----------"

    def agregarPlato(self):
        codigo = input("Codigo de Plato de comida: \n")
        nombre = input("Nombre del Plato de comida: \n")
        precio = int(input("Precio del Plato de comida: \n"))
        descuento = int(input("Digite el porcentaje del Descuento para el Plato de comida: \n"))
        descripcion = input("Descripcion del Plato de comida: \n")
        tipo = input("Tipo de Plato de comida: \n")
        print(self.guardarPlato(codigo, nombre, precio, descuento, descripcion, tipo))
        agregarOtro = input("Desea agregar otro Plato de comida? y/n \n")
        if (agregarOtro == 'y' or agregarOtro == 'Y'):
            self.agregarPlato()

    def guardarPlato(self, codigo, nombre, precioPlato, descuento, descripcion, tipo):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.precio.append(precioPlato)
        self.descuento.append(precioPlato - (precioPlato * descuento / 100))
        self.descripcion.append(descripcion)
        self.tipo.append(tipo)
        self.habilitado.append('si')
        return "El Plato de comida {} fue agregado correctamente".format(nombre)

    def verPlatoAlta(self):
        return self.inventarioPlato('si')

    def verPlatoBaja(self):
        return self.inventarioPlato('no')

    def inventarioPlato(self, habilitado):
        if(self.nombre):
            for i in range(len(self.nombre)):
                self.descripcionesPlato(i, habilitado)
            return "Inventario Cargado Correctamente"
        else:
            return "TODAVIA NO SE AGREGARON PLATOS DE COMIDAS A LA BASE DE DATOS"
    
    def MenuTodoPlato(self):
        self.verPlatoAlta()
        self.verPlatoBaja()

    def descripcionesPlato(self, posicion, habilitado):
        if(self.habilitado[posicion] == habilitado):
            print("*****DESCRIPCION DEL PLATO DE COMIDA {}*****".format(self.nombre[posicion]))
            print("CODIGO DEL PLATO DE COMIDA: {}".format(self.codigo[posicion]))
            print("PRECIO DEL PLATO DE COMIDA: {} Bs".format(self.precio[posicion]))
            print("PRECIO CON DESCUENTO: {} Bs".format(self.descuento[posicion]))
            print("DESCRIPCION DEL PLATO DE COMIDA: {}".format(self.descripcion[posicion]))
            print("TIPO DEL PLATO DE COMIDA: {}".format(self.tipo[posicion]))
            print("HABILITADO: {}".format(self.habilitado[posicion]))
            print("**********************************************")
            pass

    def editarPlato(self):
        print("*********ACTUALIZAR EL PLATO DE COMIDA**********")
        self.verPlatoAlta()
        self.verPlatoBaja()
        posicion = self.buscarPlato(1)
        nuevo_precio = int(input("Digite el nuevo precio para {}: \n".format(self.nombre[posicion])))
        nuevo_descuento = int(input("Digite el nuevo porcentaje de descuento para {}: \n".format(self.nombre[posicion])))
        nuevo_descripcion = input("Digite la nueva descripcion para {}: \n".format(self.nombre[posicion]))
        nuevo_tipo = input("Digite el nuevo tipo de plato de comida entre (Desayuno, Almuerzo, Cena y Postre) para el nuevo Plato: \n")
        self.precio[posicion] = nuevo_precio
        self.descuento[posicion] = nuevo_descuento
        self.descripcion[posicion] = nuevo_descripcion
        self.tipo[posicion] = nuevo_tipo
        print(self.modificarPlato(posicion, nuevo_precio, nuevo_descuento, nuevo_descripcion, nuevo_tipo))
        # self.descripcionesPlato(posicion)
        modificarOtro = input("Desea agregar otro Plato de comida? y/n \n")
        if (modificarOtro == 'y' or modificarOtro == 'Y'):
            self.editarPlato()
        return "Modificacion del Plato en el Menu Completado"

    def modificarPlato(self, posicion, precio, descuento, descripcion, tipo):
        self.precio[posicion] = precio
        self.descuento[posicion] = precio - (precio * descuento / 100)
        self.descripcion[posicion] = descripcion
        self.tipo[posicion] = tipo
        return "El Plato de comida {} del Menu fue Modificado Correctamente".format(self.nombre[posicion])

    def buscarPlato(self, habilitado):
        print(self.inventarioPlato(habilitado))
        eleccion = input("Digite el Codigo del Plato de comida: \n")
        posicion = self.codigo.index(eleccion)
        self.inventarioPlato(posicion)
        return posicion
    
    def realizarAlta(self):
        print("*************DAR DE ALTA UN PLATO DE COMIDA*************")
        posicion = self.buscarPlato('no')
        return self.darAlta(posicion)
    
    def darAlta(self, posicion):
        self.habilitado[posicion] = 'si'
        return "El Plato de comida {} esta de Alta..!!".format(self.nombre[posicion])

    def realizarBaja(self):
        print("*************DAR DE BAJA UN PLATO DE COMIDA*************")
        posicion = self.buscarPlato('si')
        return self.darBaja(posicion)
    
    def darBaja(self, posicion):
        self.habilitado[posicion] = 'no'
        return "El Plato de comida {} esta de Baja..!!".format(self.nombre[posicion])

    def usuarioBuscarTipoPlato(self):
        tipo = input("Escriba el tipo de comida a buscar: \n")
        return self.buscarTipoPlato(tipo)

    def buscarTipoPlato(self, tipo):
        encontrado = False
        for i in range(len(self.nombre)):
            if (self.tipo[i] == tipo):
                encontrado = True
                self.descripcionesPlatobuscador(i)
        if encontrado == False:
            print("No se encontraron resultados con el tipo {}".format(tipo))
        pass

    def descripcionesPlatobuscador(self, posicion):
        print("*****DESCRIPCION DEL PLATO DE COMIDA {}*****".format(self.nombre[posicion]))
        print("CODIGO DEL PLATO DE COMIDA: {}".format(self.codigo[posicion]))
        print("PRECIO DEL PLATO DE COMIDA: {} Bs".format(self.precio[posicion]))
        print("PRECIO CON DESCUENTO: {} Bs".format(self.descuento[posicion]))
        print("DESCRIPCION DEL PLATO DE COMIDA: {}".format(self.descripcion[posicion]))
        print("TIPO DEL PLATO DE COMIDA: {}".format(self.tipo[posicion]))
        print("HABILITADO: {}".format(self.habilitado[posicion]))
        print("**********************************************")
        pass

restaurante = Restaurantes()
restaurante.guardarPlato('A1', 'Majau', 10, 20, 'Majau de Charque', 'Almuerzo')
restaurante.guardarPlato('A2', 'Pollo', 10, 15, 'Pollo Frito', 'Cena')
restaurante.guardarPlato('A3', 'Sopa de Mani', 5, 0, 'Sopa de Mani con Papas fritas', 'Almuerzo')
restaurante.guardarPlato('A4', 'Empanada', 3, 0, 'Empanada de Queso', 'desayuno')
restaurante.guardarPlato('A5', 'Helado', 8, 0, 'Helado de Frutilla', 'Postre')
restaurante.menu()