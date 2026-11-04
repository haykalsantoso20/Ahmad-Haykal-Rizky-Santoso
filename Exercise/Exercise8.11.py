def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)


isi = [
    'Halo, apa kabar?',
    'Jangan lupa tugas hari ini.',
    'Nanti malam jadi kumpul?',
]
sent_messages = []

send_messages(isi[:], sent_messages)

print("\nList isi:", isi)
print("List sent_messages:", sent_messages)