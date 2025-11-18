from django.contrib import admin
from .models import Empleado, Cliente, VentaProducto, Proveedor, Producto, PedidoProveedor

# ===============================
# ADMIN: EMPLEADO
# ===============================
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'puesto',
        'telefono',
        'email',
        'activo'
    )
    search_fields = ('nombre', 'apellido', 'puesto', 'email')
    list_filter = ('activo', 'puesto')
    ordering = ('id',)


# ===============================
# ADMIN: CLIENTE
# ===============================
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'telefono',
        'email',
        'direccion',
        'fecha_registro',
        'activo'
    )
    search_fields = ('nombre', 'apellido', 'email', 'telefono')
    list_filter = ('activo', 'fecha_registro')
    ordering = ('id',)


# ===============================
# ADMIN: VENTA_PRODUCTO
# ===============================
@admin.register(VentaProducto)
class VentaProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_producto',
        'descripcion',
        'mostrar_empleados',  # método para mostrar ManyToMany
        'cliente',
        'cantidad',
        'precio_unitario',
        'total',
        'fecha_venta',
    )
    search_fields = ('nombre_producto', 'cliente__nombre', 'empleados__nombre')
    list_filter = ('fecha_venta',)
    ordering = ('-fecha_venta',)

    # Método para mostrar empleados en admin
    def mostrar_empleados(self, obj):
        return ", ".join([str(e) for e in obj.empleados.all()])
    mostrar_empleados.short_description = "Empleados"

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'empresa', 'telefono', 'email', 'pagina_web', 'activo')
    search_fields = ('nombre', 'empresa', 'email', 'telefono')
    list_filter = ('activo',)
    ordering = ('id',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'proveedor', 'precio', 'stock', 'activo')
    search_fields = ('nombre', 'marca', 'proveedor__nombre')
    list_filter = ('activo', 'marca')
    ordering = ('id',)

@admin.register(PedidoProveedor)
class PedidoProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'producto', 'cantidad', 'estado', 'fecha_pedido', 'fecha_entrega', 'empleado')
    search_fields = ('proveedor__nombre', 'producto__nombre', 'empleado__nombre')
    list_filter = ('estado', 'fecha_pedido')
    ordering = ('-fecha_pedido',)