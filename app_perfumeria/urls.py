from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_perfumeria, name='inicio_perfumeria'),

    # Cliente
    path('cliente/', views.ver_cliente, name='ver_cliente'),
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),

    # Empleado
    path('empleado/', views.ver_empleado, name='ver_empleado'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    # Venta Producto
    path('venta_producto/', views.ver_venta_producto, name='ver_venta_producto'),
    path('venta_producto/agregar/', views.agregar_venta_producto, name='agregar_venta_producto'),
    path('venta_producto/actualizar/<int:venta_id>/', views.actualizar_venta_producto, name='actualizar_venta_producto'),
    path('venta_producto/borrar/<int:venta_id>/', views.borrar_venta_producto, name='borrar_venta_producto'),

        # Proveedor
    path('proveedor/', views.ver_proveedor, name='ver_proveedor'),
    path('proveedor/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedor/actualizar/<int:proveedor_id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedor/borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),

    # Producto
    path('producto/', views.ver_producto, name='ver_producto'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),

    # Pedido Proveedor
    path('pedido_proveedor/', views.ver_pedido_proveedor, name='ver_pedido_proveedor'),
    path('pedido_proveedor/agregar/', views.agregar_pedido_proveedor, name='agregar_pedido_proveedor'),
    path('pedido_proveedor/actualizar/<int:pedido_id>/', views.actualizar_pedido_proveedor, name='actualizar_pedido_proveedor'),
    path('pedido_proveedor/borrar/<int:pedido_id>/', views.borrar_pedido_proveedor, name='borrar_pedido_proveedor'),

]

