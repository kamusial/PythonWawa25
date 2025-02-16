import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Aby matplotlib poprawnie działał w tkinter (bez wywoływania "mainloop" w dziwnych momentach)
matplotlib.use("TkAgg")


class CSVAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analiza pliku CSV")
        self.geometry("800x600")

        # Obiekt DataFrame, do którego wczytamy dane z CSV
        self.df = None

        # Tworzymy elementy interfejsu
        self.create_widgets()

    def create_widgets(self):
        # Ramka na przyciski
        button_frame = tk.Frame(self)
        button_frame.pack(side="top", fill="x", pady=10)

        # Przycisk: Wczytaj CSV
        btn_load = tk.Button(button_frame, text="Wczytaj CSV", command=self.load_csv)
        btn_load.pack(side="left", padx=5)

        # Przycisk: Sprawdź duplikaty
        btn_duplicates = tk.Button(button_frame, text="Sprawdź duplikaty", command=self.check_duplicates)
        btn_duplicates.pack(side="left", padx=5)

        # Przycisk: Sprawdź spójność
        btn_consistency = tk.Button(button_frame, text="Sprawdź spójność", command=self.check_consistency)
        btn_consistency.pack(side="left", padx=5)

        # Przycisk: Wykryj błędy
        btn_errors = tk.Button(button_frame, text="Wykryj błędy", command=self.detect_errors)
        btn_errors.pack(side="left", padx=5)

        # Przycisk: Generuj wykres
        btn_plot = tk.Button(button_frame, text="Generuj wykres", command=self.generate_plot)
        btn_plot.pack(side="left", padx=5)

        # Przycisk: Zapisz jako...
        btn_save = tk.Button(button_frame, text="Zapisz plik CSV", command=self.save_csv)
        btn_save.pack(side="left", padx=5)

        # Pole tekstowe do wyświetlania wyników analiz
        self.output_text = tk.Text(self, wrap="word", height=10)
        self.output_text.pack(fill="both", expand=True, padx=10, pady=10)

    def load_csv(self):
        """Wczytanie pliku CSV z użyciem pandas.read_csv()."""
        file_path = filedialog.askopenfilename(
            title="Wybierz plik CSV",
            filetypes=[("Pliki CSV", "*.csv"), ("Wszystkie pliki", "*.*")]
        )
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.output_text.insert("end", f"Wczytano plik: {file_path}\n")
                self.output_text.insert("end", f"Liczba wierszy: {len(self.df)}\n")
                self.output_text.insert("end", f"Kolumny: {list(self.df.columns)}\n\n")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się wczytać pliku CSV:\n{e}")

    def check_duplicates(self):
        """Sprawdzenie, czy w danych występują zduplikowane wiersze."""
        if self.df is None:
            messagebox.showwarning("Brak danych", "Najpierw wczytaj plik CSV.")
            return

        # Sprawdzamy duplikaty
        duplicated_rows = self.df.duplicated()
        num_duplicates = duplicated_rows.sum()

        if num_duplicates > 0:
            self.output_text.insert("end", f"Znaleziono {num_duplicates} zduplikowanych wierszy.\n")
        else:
            self.output_text.insert("end", "Brak zduplikowanych wierszy.\n")
        self.output_text.insert("end", "-" * 40 + "\n")

    def check_consistency(self):
        """
        Przykładowe sprawdzenie spójności danych:
        - Sprawdzenie wartości pustych (NaN).
        - Możesz dodać inne kryteria, np. zakresy liczb, format dat itp.
        """
        if self.df is None:
            messagebox.showwarning("Brak danych", "Najpierw wczytaj plik CSV.")
            return

        # Sprawdzamy brakujące wartości
        null_count = self.df.isnull().sum()
        total_null = null_count.sum()

        self.output_text.insert("end", "Sprawdzanie spójności danych...\n")
        if total_null == 0:
            self.output_text.insert("end", "Brak brakujących wartości (NaN) w danych.\n")
        else:
            self.output_text.insert("end", f"Liczba brakujących wartości: {total_null}\n")
            self.output_text.insert("end", f"{null_count}\n")
        self.output_text.insert("end", "-" * 40 + "\n")

    def detect_errors(self):
        """
        Przykładowa funkcja do 'wykrywania błędów'.
        Możesz zdefiniować własne reguły walidacji – np. wartości ujemne w kolumnie,
        niepoprawne formaty dat, itp. Tutaj jako przykład wykrywamy wartości ujemne.
        """
        if self.df is None:
            messagebox.showwarning("Brak danych", "Najpierw wczytaj plik CSV.")
            return

        self.output_text.insert("end", "Wykrywanie błędów...\n")

        # Przykład: sprawdzamy, czy w dataframe są kolumny liczbowe z wartościami ujemnymi
        numeric_cols = self.df.select_dtypes(include=["int", "float"]).columns
        negative_values = {}

        for col in numeric_cols:
            negatives = (self.df[col] < 0).sum()
            if negatives > 0:
                negative_values[col] = negatives

        if len(negative_values) == 0:
            self.output_text.insert("end", "Nie wykryto wartości ujemnych.\n")
        else:
            self.output_text.insert("end", "Wykryto wartości ujemne w kolumnach:\n")
            for col, count in negative_values.items():
                self.output_text.insert("end", f" - {col}: {count} wartości ujemnych\n")

        self.output_text.insert("end", "-" * 40 + "\n")

    def generate_plot(self):
        """
        Generowanie przykładowego wykresu (np. histogram pierwszej kolumny numerycznej).
        Jeśli chcesz, możesz zapytać użytkownika o wybór kolumny i rodzaj wykresu.
        """
        if self.df is None:
            messagebox.showwarning("Brak danych", "Najpierw wczytaj plik CSV.")
            return

        # Szukamy pierwszej kolumny liczb owej
        numeric_cols = self.df.select_dtypes(include=["int", "float"]).columns
        if len(numeric_cols) == 0:
            messagebox.showwarning("Brak kolumn liczbowych",
                                   "W tym pliku nie ma kolumn liczbowych do wyświetlenia wykresu.")
            return

        first_numeric_col = numeric_cols[0]

        # Tworzymy okno z matplotlib Figure
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_title(f"Histogram kolumny: {first_numeric_col}")

        # Rysujemy histogram
        self.df[first_numeric_col].plot(kind="hist", ax=ax, bins=10)

        # Tworzymy nowe okno tkinter, w którym wyświetlamy wykres
        plot_window = tk.Toplevel(self)
        plot_window.title("Wykres")

        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def save_csv(self):
        """Zapis pliku CSV z określonymi parametrami (np. bez indeksu, zmiana separatora itp.)."""
        if self.df is None:
            messagebox.showwarning("Brak danych", "Najpierw wczytaj plik CSV.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Zapisz plik CSV",
            defaultextension=".csv",
            filetypes=[("Pliki CSV", "*.csv"), ("Wszystkie pliki", "*.*")]
        )
        if file_path:
            try:
                # Przykład: zapiszmy plik z separatorem ';', bez indeksu
                self.df.to_csv(file_path, sep=";", index=False)
                messagebox.showinfo("Sukces", f"Plik zapisany jako: {file_path}")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")


if __name__ == "__main__":
    app = CSVAnalyzer()
    app.mainloop()
