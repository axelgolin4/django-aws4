from django.db import models


class Sample(models.Model):
    attachment = models.FileField()

class Empleados(models.Model):
    id=models.AutoField(primary_key = True)
    nombre = models.CharField('Nombres',max_length = 200, blank = False, null = False)
    apellidos = models.CharField('Apellidos',max_length = 200, blank = False, null = False)
    puesto = models.CharField('Puesto',max_length = 200, blank = False, null = False)
    telefono = models.CharField('Telefono',max_length = 200, blank = False, null = False)
    direccion = models.CharField('Direccion',max_length = 200, blank = False, null = False)
    usuario = models.CharField('Usuario',max_length = 200, blank = False, null = False)
    contraseña = models.CharField('Contraseña',max_length = 200, blank = False, null = False)


    class Meta:
         verbose_name = 'Empleado'
         verbose_name_plural = 'Empleados'
         ordering = ['nombre']

    def __str__(self):
        return self.nombre
class Productos(models.Model):
        id=models.AutoField(primary_key = True)
        producto = models.CharField('Producto',max_length = 250, blank = False, null = False)
        descripcion = models.CharField('Descripcion',max_length = 250, blank = False, null = False)
        preciocompra = models.FloatField('Precio de compra', blank = False, null= False)
        precioventa = models.FloatField('Precio de venta', blank = False, null= False)
        existencia = models.IntegerField('Existencia', blank = False, null= False)
        fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)

        class Meta:
             verbose_name = 'Producto'
             verbose_name_plural = 'Productos'
             ordering = ['producto']

        def __str__(self):
            return self.producto


class Ventas(models.Model):
        id=models.AutoField(primary_key = True)
        total = models.IntegerField('Total', blank = False, null= False)
        fecha = models.DateField('Fecha', blank = False, null= False)
        nit = models.CharField('Nit',max_length = 250, blank = False, null = False)
        nombre = models.CharField('Nombre',max_length = 250, blank = False, null = False)
        direccion = models.CharField('Direccion',max_length = 250, blank = False, null = False)

        empleados_id = models.ForeignKey(Empleados, on_delete = models.CASCADE,null = True)

        fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)

        class Meta:
             verbose_name = 'Venta'
             verbose_name_plural = 'Ventas'
             ordering = ['nombre']

        def _str_(self):
            return self.id


class Infoventas(models.Model):
    id=models.AutoField(primary_key = True)
    cantidad = models.IntegerField('Cantidad', blank = False, null= False)
    subtotal = models.IntegerField('Subtotal', blank = False, null= False)


    productos_id = models.ForeignKey(Productos, on_delete = models.CASCADE, null = True)
    ventas_id = models.ForeignKey(Ventas, on_delete = models.CASCADE, null = True)



    fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)


    class Meta:
         verbose_name = 'Infoventa'
         verbose_name_plural = 'Infoventas'
         ordering = ['id']

    def _str_(self):
        return self.id






class Compras(models.Model):
    id=models.AutoField(primary_key = True)
    cantidad = models.IntegerField('Cantidad', blank = False, null= False)
    subtotal = models.IntegerField('Subtotal')
    descripcion = models.CharField('Descripcion',max_length = 250,blank = False,  null = False)
    productos_id = models.ForeignKey(Productos, on_delete = models.CASCADE,null = True)

    fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)





    class Meta:
         verbose_name = 'Compra'
         verbose_name_plural = 'Compras'
         ordering = ['id']


    def _str_(self):
        return self.id
