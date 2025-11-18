from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Empleado, VentaProducto, Proveedor, Producto, PedidoProveedor

# ------------------------------
# PÁGINA DE INICIO
# ------------------------------
def inicio_perfumeria(request):
    return render(request, 'inicio.html')


# ------------------------------
# CLIENTES
# ------------------------------
def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})


def agregar_cliente(request):
    empleados = Empleado.objects.all()  # Para el select en el formulario
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado')
        empleado = Empleado.objects.get(id=empleado_id) if empleado_id else None

        fecha_registro = request.POST.get('fecha_registro')  # Tomamos la fecha del formulario

        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            direccion=request.POST.get('direccion'),
            fecha_registro=fecha_registro,
            activo=True if request.POST.get('activo') == 'on' else False,
            empleado=empleado
        )
        return redirect('ver_cliente')

    return render(request, 'cliente/agregar_cliente.html', {'empleados': empleados})


def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado')
        cliente.empleado = Empleado.objects.get(id=empleado_id) if empleado_id else None

        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direccion = request.POST.get('direccion')
        cliente.fecha_registro = request.POST.get('fecha_registro')
        cliente.activo = True if request.POST.get('activo') == 'on' else False
        cliente.save()
        return redirect('ver_cliente')

    return render(request, 'cliente/actualizar_cliente.html', {
        'cliente': cliente,
        'empleados': empleados
    })


def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    
    # Si no es POST, mostrar la página de confirmación
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ------------------------------
# EMPLEADOS
# ------------------------------
def ver_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})


def agregar_empleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            puesto=request.POST.get('puesto'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            fecha_contratacion=request.POST.get('fecha_contratacion'),
            activo=('activo' in request.POST)
        )
        return redirect('ver_empleado')
    return render(request, 'empleado/agregar_empleado.html')


def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.puesto = request.POST.get('puesto')
        empleado.telefono = request.POST.get('telefono')
        empleado.email = request.POST.get('email')
        empleado.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion')
        empleado.activo = 'activo' in request.POST
        empleado.save()
        return redirect('ver_empleado')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})


def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# ------------------------------
# VENTAS PRODUCTOS
# ------------------------------
def ver_venta_producto(request):
    ventas = VentaProducto.objects.all()
    return render(request, 'venta/ver_venta.html', {'ventas': ventas})


def agregar_venta_producto(request):
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        cliente = Cliente.objects.get(id=cliente_id) if cliente_id else None

        venta = VentaProducto.objects.create(
            nombre_producto=request.POST.get('nombre_producto'),
            descripcion=request.POST.get('descripcion'),
            precio_unitario=request.POST.get('precio_unitario'),
            cantidad=request.POST.get('cantidad'),
            cliente=cliente
        )

        empleados_ids = request.POST.getlist('empleados')
        venta.empleados.set(empleados_ids)
        venta.save()
        return redirect('ver_venta_producto')

    return render(request, 'venta/agregar_venta.html', {
        'empleados': empleados,
        'clientes': clientes
    })


def actualizar_venta_producto(request, venta_id):
    venta = get_object_or_404(VentaProducto, id=venta_id)
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        venta.nombre_producto = request.POST.get('nombre_producto')
        venta.descripcion = request.POST.get('descripcion')
        venta.precio_unitario = request.POST.get('precio_unitario')
        venta.cantidad = request.POST.get('cantidad')

        cliente_id = request.POST.get('cliente')
        venta.cliente = Cliente.objects.get(id=cliente_id) if cliente_id else None

        empleados_ids = request.POST.getlist('empleados')
        venta.empleados.set(empleados_ids)

        venta.save()
        return redirect('ver_venta_producto')

    return render(request, 'venta/editar_venta.html', {
        'venta': venta,
        'empleados': empleados,
        'clientes': clientes
    })


def borrar_venta_producto(request, venta_id):
    venta = get_object_or_404(VentaProducto, id=venta_id)
    
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_venta_producto')
    
    return render(request, 'venta/borrar_venta.html', {'venta': venta})

# ------------------------------
# PROVEEDORES
# ------------------------------
def ver_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/ver_proveedor.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        Proveedor.objects.create(
            nombre=request.POST.get('nombre'),
            empresa=request.POST.get('empresa'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            direccion=request.POST.get('direccion'),
            pagina_web=request.POST.get('pagina_web'),
            activo=('activo' in request.POST)
        )
        return redirect('ver_proveedor')
    return render(request, 'proveedor/agregar_proveedor.html')

def actualizar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.nombre = request.POST.get('nombre')
        proveedor.empresa = request.POST.get('empresa')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.pagina_web = request.POST.get('pagina_web')
        proveedor.activo = 'activo' in request.POST
        proveedor.save()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedor')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})


# ------------------------------
# PRODUCTOS
# ------------------------------
def ver_producto(request):
    productos = Producto.objects.select_related('proveedor').all()
    return render(request, 'producto/ver_producto.html', {'productos': productos})

def agregar_producto(request):
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        Producto.objects.create(
            nombre=request.POST.get('nombre'),
            marca=request.POST.get('marca'),
            proveedor=Proveedor.objects.get(id=request.POST.get('proveedor')) if request.POST.get('proveedor') else None,
            precio=request.POST.get('precio') or 0,
            stock=request.POST.get('stock') or 0,
            descripcion=request.POST.get('descripcion'),
            activo=('activo' in request.POST)
        )
        return redirect('ver_producto')
    return render(request, 'producto/agregar_producto.html', {'proveedores': proveedores})

def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        proveedor_id = request.POST.get('proveedor')
        producto.proveedor = Proveedor.objects.get(id=proveedor_id) if proveedor_id else None
        producto.precio = request.POST.get('precio') or 0
        producto.stock = request.POST.get('stock') or 0
        producto.descripcion = request.POST.get('descripcion')
        producto.activo = 'activo' in request.POST
        producto.save()
        return redirect('ver_producto')
    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'proveedores': proveedores})

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})


# ------------------------------
# PEDIDOS PROVEEDOR
# ------------------------------
def ver_pedido_proveedor(request):
    pedidos = PedidoProveedor.objects.select_related('proveedor', 'producto', 'empleado').all()
    return render(request, 'pedido/ver_pedido_proveedor.html', {'pedidos': pedidos})

def agregar_pedido_proveedor(request):
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        proveedor = Proveedor.objects.get(id=request.POST.get('proveedor')) if request.POST.get('proveedor') else None
        producto = Producto.objects.get(id=request.POST.get('producto')) if request.POST.get('producto') else None
        PedidoProveedor.objects.create(
            proveedor=proveedor,
            producto=producto,
            cantidad=request.POST.get('cantidad') or 1,
            fecha_entrega=request.POST.get('fecha_entrega') or None,
            estado=request.POST.get('estado') or 'PENDIENTE',
            empleado=Empleado.objects.get(id=request.POST.get('empleado')) if request.POST.get('empleado') else None
        )
        return redirect('ver_pedido_proveedor')
    return render(request, 'pedido/agregar_pedido_proveedor.html', {
        'proveedores': proveedores,
        'productos': productos,
        'empleados': empleados
    })

def actualizar_pedido_proveedor(request, pedido_id):
    pedido = get_object_or_404(PedidoProveedor, id=pedido_id)
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        pedido.proveedor = Proveedor.objects.get(id=request.POST.get('proveedor')) if request.POST.get('proveedor') else None
        pedido.producto = Producto.objects.get(id=request.POST.get('producto')) if request.POST.get('producto') else None
        pedido.cantidad = request.POST.get('cantidad') or 1
        pedido.fecha_entrega = request.POST.get('fecha_entrega') or None
        pedido.estado = request.POST.get('estado') or 'PENDIENTE'
        pedido.empleado = Empleado.objects.get(id=request.POST.get('empleado')) if request.POST.get('empleado') else None
        pedido.save()
        return redirect('ver_pedido_proveedor')
    return render(request, 'pedido/actualizar_pedido_proveedor.html', {
        'pedido': pedido,
        'proveedores': proveedores,
        'productos': productos,
        'empleados': empleados
    })

def borrar_pedido_proveedor(request, pedido_id):
    pedido = get_object_or_404(PedidoProveedor, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedido_proveedor')
    return render(request, 'pedido/borrar_pedido_proveedor.html', {'pedido': pedido})