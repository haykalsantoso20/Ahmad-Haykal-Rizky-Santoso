def print_models(unprinted_designs, completed_models):
    """
    Simulasi mencetak setiap desain, satu per satu.
    Pindahkan setiap desain ke completed_models setelah dicetak.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Menampilkan semua model yang sudah dicetak."""
    print("\nModel yang sudah dicetak:")
    for completed_model in completed_models:
        print(completed_model)