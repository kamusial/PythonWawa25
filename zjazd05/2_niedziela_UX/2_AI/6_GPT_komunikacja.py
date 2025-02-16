import openai

# Ustaw swój klucz API
openai.api_key = "TWÓJ_KLUCZ_API"

# System prompt – możesz go zmodyfikować, aby określić kontekst, styl i zachowanie modelu.
# Przykład: "Jesteś ekspertem ds. finansów, udzielającym szczegółowych i precyzyjnych odpowiedzi na pytania dotyczące inwestycji."
system_prompt = {
    "role": "system",
    "content": "Jesteś pomocnym asystentem, który udziela jasnych i zwięzłych odpowiedzi na pytania użytkownika."
}

# Inicjujemy historię konwersacji z systemowym promptem
conversation = [system_prompt]

print("Wpisz 'exit' lub 'quit', aby zakończyć rozmowę.\n")

while True:
    # Miejsce, gdzie użytkownik wprowadza swój prompt (pytanie)
    user_input = input("Wprowadź prompt (Twoje pytanie): ").strip()
    if user_input.lower() in {"exit", "quit"}:
        break

    # Dodajemy wiadomość użytkownika do historii konwersacji
    conversation.append({"role": "user", "content": user_input+'odpowiedz krótko, bardzo formalnie, z uzyciem trudnych i wyszukanyc słów. Odpowiedź podizel na 3 akapity, ostatni akapit to podsumowanie'})

    try:
        # Wywołanie API OpenAI z pełną historią wiadomości
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation,
            temperature=0.7
        )
        # Pobieramy odpowiedź modelu
        answer = response.choices[0].message.content.strip()
        # Dodajemy odpowiedź asystenta do historii
        conversation.append({"role": "assistant", "content": answer})
        print("GPT:", answer)
    except Exception as e:
        print("Błąd podczas komunikacji z API:", e)
