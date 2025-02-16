import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Wybierz nazwę modelu Dolly v2 (3B)
model_name = "databricks/dolly-v2-3b"

# Ładujemy tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True
)

# Ładujemy model
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,     # float16 – optymalny dla GPU; na CPU można użyć float32
    device_map="auto",             # automatyczne rozmieszczenie na GPU / CPU
    offload_folder="offload",      # folder tymczasowy, jeśli zabraknie pamięci GPU
    trust_remote_code=True
)

# Inicjalny prompt nadający kontekst rozmowy
# Możesz go dostosować, by określić "charakter" Dolly (asystenta).
chat_history = (
    "Below is a conversation between a user and Dolly, a helpful AI assistant.\n"
    "Dolly is polite, honest, and concise. Dolly knows a lot about many topics.\n"
)

print("Rozpoczynamy konwersację z Dolly v2-3b! Wpisz 'exit' lub 'quit', aby zakończyć.\n")

while True:
    user_input = input("Ty: ")
    if user_input.lower() in {"exit", "quit"}:
        print("Kończę rozmowę. Do zobaczenia!")
        break

    # Dodajemy wypowiedź użytkownika do historii
    chat_history += f"\nUser: {user_input}\nDolly:"

    # Tokenizujemy cały kontekst (historię rozmowy + nowy prompt)
    inputs = tokenizer(chat_history, return_tensors="pt")
    # Przenosimy tensory na to samo urządzenie, gdzie znajduje się model
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    # Generujemy odpowiedź
    outputs = model.generate(
        **inputs,
        max_new_tokens=128,  # maksymalna liczba tokenów w odpowiedzi
        do_sample=True,
        top_k=50,
        top_p=0.9
    )

    # Dekodujemy całą sekwencję (historię + odpowiedź)
    full_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Odcinamy ostatnią część po "Dolly:" – to będzie odpowiedź modelu
    splitted = full_output.split("Dolly:")
    if len(splitted) > 1:
        dolly_response = splitted[-1].strip()
    else:
        # W razie braku podziału (co się rzadko zdarza), bierzemy całość
        dolly_response = full_output.strip()

    # Wyświetlamy odpowiedź
    print(f"Dolly: {dolly_response}")

    # Dodajemy odpowiedź do historii (kontynuacja kontekstu)
    chat_history += " " + dolly_response
