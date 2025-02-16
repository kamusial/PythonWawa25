import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib

matplotlib.use("TkAgg")  # Użycie backendu TkAgg do wykresów
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CSVAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Analiza danych CSV")
        self.geometry("800x600")

        # DataFrame, w którym będziemy przechowywać wczytane dane
        self.df = None

        # Tworzymy menu
        self.create_menu()

        # Ramka główna z przyciskami i polami
        self.create_main_frame()

        # Ramka do wyświetlania komunikatów i logów
        self.log_text = tk.Text(self, height=10, wrap="word")
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)

        # Ramka na wykres (na razie pusta)
        self.plot_frame = ttk.Frame(self)
        self.plot_frame.pack(fill="both", expand=True, padx=5, pady=5)

    def create_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Otwórz CSV", command=self.open_csv)
        file_menu.add_command(label="Zapisz jako...", command=self.save_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Wyjście", command=self.quit)

        menubar.add_cascade(label="Plik", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="O aplikacji", command=self.show_about)

        menubar.add_cascade(label="Pomoc", menu=help_menu)

        self.config(menu=menubar)

    def create_main_frame(self):
        frame = ttk.Frame(self)
        frame.pack(fill="x", padx=5, pady=5)

        # Przycisk do otwierania pliku CSV
        open_button = ttk.Button(frame, text="Otwórz CSV", command=self.open_csv)
        open_button.grid(row=0, column=0, padx=5, pady=5)

        # Przycisk do sprawdzania duplikatów
        duplicates_button = ttk.Button(frame, text="Sprawdź duplikaty", command=self.check_duplicates)
        duplicates_button.grid(row=0, column=1, padx=5, pady=5)

        # Przycisk do sprawdzania spójności
        consistency_button = ttk.Button(frame, text="Sprawdź spójność", command=self.check_consistency)
        consistency_button.grid(row=0, column=2, padx=5, pady=5)

        # Przycisk do wykrywania błędów
        errors_button = ttk.Button(frame, text="Wykryj błędy", command=self.detect_errors)
        errors_button.grid(row=0, column=3, padx=5, pady=5)

        # Przycisk do generowania wykresu
        plot_button = ttk.Button(frame, text="Generuj wykres", command=self.generate_plot)
        plot_button.grid(row=0, column=4, padx=5, pady=5)

        # Przycisk do zapisu CSV
        save_button = ttk.Button(frame, text="Zapisz jako...", command=self.save_csv)
        save_button.grid(row=0, column=5, padx=5, pady=5)

        # Ustawienia kolumn w grid
        for col in range(6):
            frame.columnconfigure(col, weight=1)

    def open_csv(self):
        """
        Otwiera okno dialogowe do wyboru pliku CSV i wczytuje go do DataFrame.
        """
        file_path = filedialog.askopenfilename(
            title="Wybierz plik CSV",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.log_message(f"Wczytano plik: {file_path}\n")
                self.log_message(f"Liczba wierszy: {len(self.df)} | Liczba kolumn: {len(self.df.columns)}\n")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się wczytać pliku.\n{e}")

    def save_csv(self):
        """
        Zapisuje DataFrame do nowej lokalizacji z określonymi parametrami (np. index=False).
        """
        if self.df is None:
            messagebox.showinfo("Informacja", "Najpierw wczytaj plik CSV.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Zapisz jako...",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if file_path:
            try:
                # Przykładowe parametry: separator, brak indeksu
                self.df.to_csv(file_path, index=False, sep=",")
                self.log_message(f"Zapisano plik CSV jako: {file_path}\n")
            except Exception as e:
                messagebox.showerror("Błąd zapisu", f"Nie udało się zapisać pliku.\n{e}")

    def check_duplicates(self):
        """
        Sprawdza powtarzające się wartości w DataFrame i wyświetla informację w logu.
        """
        if self.df is None:
            messagebox.showinfo("Informacja", "Najpierw wczytaj plik CSV.")
            return

        # Przykład: liczymy duplikaty w całym DataFrame
        duplicates = self.df.duplicated().sum()
        self.log_message(f"Liczba zduplikowanych wierszy: {duplicates}\n")

    def check_consistency(self):
        """
        Przykładowa metoda sprawdzania spójności danych (np. brakujące wartości).
        """
        if self.df is None:
            messagebox.showinfo("Informacja", "Najpierw wczytaj plik CSV.")
            return

        # Liczymy brakujące wartości w każdej kolumnie
        missing_counts = self.df.isnull().sum()
        self.log_message("Brakujące wartości w kolumnach:\n")
        for col, val in missing_counts.items():
            self.log_message(f"  {col}: {val}\n")

    def detect_errors(self):
        """
        Przykładowa metoda wykrywania błędów w kolumnach numerycznych (np. nieprawidłowe typy).
        """
        if self.df is None:
            messagebox.showinfo("Informacja", "Najpierw wczytaj plik CSV.")
            return

        # Dla każdej kolumny numerycznej próbujemy zrzutować na float i sprawdzić, czy pojawią się błędy
        numeric_columns = self.df.select_dtypes(include=["int", "float"]).columns
        self.log_message("Sprawdzanie kolumn numerycznych:\n")
        for col in numeric_columns:
            # W prosty sposób sprawdzimy, czy kolumna nie ma dziwnych wartości
            # (np. wartości mniejszych niż 0, jeśli tak zakładamy)
            negatives = (self.df[col] < 0).sum()
            if negatives > 0:
                self.log_message(f"  Ostrzeżenie: w kolumnie {col} występuje {negatives} wartości < 0.\n")

    def generate_plot(self):
        """
        Generuje przykładowy wykres na podstawie wybranych kolumn.
        Dla prostoty – jeśli DataFrame ma kolumnę 'x' i 'y', rysujemy wykres.
        """
        if self.df is None:
            messagebox.showinfo("Informacja", "Najpierw wczytaj plik CSV.")
            return

        # Czy mamy kolumny "x" i "y"? (Możesz tu dodać własną logikę wyboru kolumn)
        if "x" not in self.df.columns or "y" not in self.df.columns:
            messagebox.showinfo("Informacja",
                                "Brak kolumn 'x' i 'y' w danych. Wybierz inne kolumny lub zmodyfikuj kod.")
            return

        # Usuwamy poprzedni wykres (jeśli istnieje)
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(self.df["x"], self.df["y"], marker="o", linestyle="-", color="blue")
        ax.set_title("Wykres x vs y")
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def log_message(self, message):
        """
        Funkcja pomocnicza do wypisywania komunikatów w polu tekstowym (logu).
        """
        self.log_text.insert("end", message)
        self.log_text.see("end")

    def show_about(self):
        messagebox.showinfo("O aplikacji", "Prosty program do analizy danych z plików CSV.\nAutor: Twoje Imię.")


if __name__ == "__main__":
    app = CSVAnalyzerApp()
    app.mainloop()
