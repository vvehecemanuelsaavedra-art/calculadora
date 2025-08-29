def generar_recibo(cliente, articulos, iva=0.13):
    """
    Genera e imprime un recibo de compra.

    Args:
        cliente (str): El nombre del cliente.
        articulos (dict): Un diccionario donde las llaves son los nombres
                          de los artículos y los valores son tuplas
                          (precio_unitario, cantidad).
        iva (float): La tasa de impuesto sobre las ventas (IVA). Por defecto es 0.13 (13%).
    """
    total_bruto = 0
    ancho_recibo = 50

    print("=" * ancho_recibo)
    print(" " * ((ancho_recibo - len("RECIBO DE COMPRA")) // 2) + "RECIBO DE COMPRA")
    print("=" * ancho_recibo)
    print(f"Cliente: {cliente}")
    print("-" * ancho_recibo)
    print(f"{'Artículo':<30}{'Precio':>10}{'Cant.':>8}")
    print("-" * ancho_recibo)

    for articulo, (precio, cantidad) in articulos.items():
        subtotal = precio * cantidad
        print(f"{articulo:<30}${precio:7.2f}{cantidad:8d}")
        total_bruto += subtotal

    print("-" * ancho_recibo)
    print(f"{'Subtotal:':<30}${total_bruto:>10.2f}")
    
    monto_iva = total_bruto * iva
    print(f"{f'IVA ({iva*100:.0f}%):':<30}${monto_iva:>10.2f}")

    total_neto = total_bruto + monto_iva
    print(f"{'TOTAL:':<30}${total_neto:>10.2f}")
    print("=" * ancho_recibo)
    print(" " * ((ancho_recibo - len("¡Gracias por su compra!")) // 2) + "¡Gracias por su compra!")
    print("=" * ancho_recibo)

# Ejemplo de uso:
if __name__ == "__main__":
    compras = {
        "Manzanas": (0.75, 5),
        "Pan de molde": (2.50, 1),
        "Leche (1L)": (1.20, 2),
        "Huevos (docena)": (3.00, 1)
    }

    generar_recibo("Juan Pérez", compras)
