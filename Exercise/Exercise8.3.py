def make_shirt(size, message):
    """Menampilkan ringkasan ukuran dan tulisan pada kaos."""
    print(f"Kaos ini berukuran {size} dengan tulisan '{message}'.")


# Argumen posisional
make_shirt('M', 'Saya suka ayam')

# Argumen kata kunci
make_shirt(message='Halo', size='L')