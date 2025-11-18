from django.db import models
from decimal import Decimal

# ===============================
# MODELO: EMPLEADO
# ===============================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)        # Campo editable
    fecha_contratacion = models.DateField(blank=True, null=True)      # Campo editable
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ===============================
# MODELO: CLIENTE
# ===============================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, blank=True, null=True, related_name='clientes_atendidos'
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
# ===============================
# MODELO: VENTA PRODUCTO
# ===============================
class VentaProducto(models.Model):
    nombre_producto = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_venta = models.DateField(auto_now_add=True)

    # Relaciones
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    empleados = models.ManyToManyField(Empleado, related_name='ventas_asociadas')

    def save(self, *args, **kwargs):
        # Convierte cantidad y precio a tipos correctos antes de multiplicar
        cantidad_int = int(self.cantidad)
        precio_decimal = Decimal(self.precio_unitario)
        self.total = cantidad_int * precio_decimal
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_producto} - {self.cliente}"

# ------------------------------
# MODELO: PROVEEDOR
# ------------------------------
class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    pagina_web = models.URLField(blank=True, null=True)  # NUEVO CAMPO
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.empresa})" if self.empresa else self.nombre
# ------------------------------
# MODELO: PRODUCTO
# ------------------------------
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=150, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, blank=True, null=True, related_name='productos')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    stock = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}" if self.marca else self.nombre

# ------------------------------
# MODELO: PEDIDO PROVEEDOR
# (para simplicidad cada pedido referencia un producto + cantidad)
# ------------------------------
class PedidoProveedor(models.Model):
    ESTADO_CHOICES = (
        ('PENDIENTE', 'Pendiente'),
        ('EN_CAMINO', 'En camino'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    )

    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='pedidos')
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True, related_name='pedidos')
    cantidad = models.PositiveIntegerField(default=1)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='PENDIENTE')
    empleado = models.ForeignKey('Empleado', on_delete=models.SET_NULL, blank=True, null=True, related_name='pedidos_realizados')

    def __str__(self):
        return f"Pedido #{self.id} - {self.proveedor} - {self.producto} x{self.cantidad}"