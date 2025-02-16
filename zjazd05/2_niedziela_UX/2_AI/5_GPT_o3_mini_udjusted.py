import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Aby matplotlib poprawnie działał z tkinter
matplotlib.use("TkAgg")


class CSVAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analiza pliku CSV")
        self.geometry("900x700")

        # Obiekt DataFrame, do którego wczytamy dane
        self.df = None

        # Tworzymy elementy interfejsu
        self.create_widgets()

    def create_widgets(self):
        # Ramka z parametrami wczytywania pliku CSV
        param_frame = tk.Frame(self)
        param_frame.pack(side="top", fill="x", pady=5)

        # Kodowanie
        tk.Label(param_frame, text="Encoding:").pack(side="left", padx=5)
        self.encoding_var = tk.StringVar(value="utf-8")
        encoding_options = ["utf-8", "latin1", "cp1252"]
        encoding_menu = tk.OptionMenu(param_frame, self.encoding_var, *encoding_options)
        encoding_menu.pack(side="left", padx=5)

        # Separator
        tk.Label(param_frame, text="Separator:").pack(side="left", padx=5)
        self.sep_var = tk.StringVar(value="Comma")
        sep_options = ["Comma", "Semicolon", "Tab"]
        sep_menu = tk.OptionMenu(param_frame, self.sep_var, *sep_options)
        sep_menu.pack(side="left", padx=5)

        # Komentarz
        tk.Label(param_frame, text="Comment:").pack(side="left", padx=5)
        self.comment_var = tk.StringVar(value="None")
        comment_options = ["None", "#"]
        comment_menu = tk.OptionMenu(param_frame, self.comment_var, *comment_options)
        comment_menu.pack(side="left", padx=5)

        # Ramka na przyciski
        button_frame = tk.Frame(self)
        button_frame.pack(side="top", fill="x", pady=10)

        btn_load = tk.Button(button_frame, text="Wczytaj CSV", command=self.load_csv)
        btn_load.pack(side="left", padx=5)

        btn_duplicates = tk.Button(button_frame, text="Sprawdź duplikaty", command=self.check_duplicates)
        btn_duplicates.pack(side="left", padx=5)

        btn_consistency = tk.Button(button_frame, text="Sprawdź spójność", command=self.check_consistency)
        btn_consistency.pack(side="left", padx=5)

        btn_errors = tk.Button(button_frame, text="Wykryj błędy", command=self.detect_errors)
        btn_errors.pack(side="left", padx=5)

        btn_plot = tk.Button(button_frame, text="Generuj wykres", command=self.generate_plot)
        btn_plot.pack(side="left", padx=5)

        btn_save = tk.Button(button_frame, text="Zapisz plik CSV", command=self.save_csv)
        btn_save.pack(side="left", padx=5)

        # Pole tekstowe do wyświetlania wyników analiz
        self.output_text = tk.Text(self, wrap="word", height=15)
        self.output_text.pack(fill="both", expand=True, padx=10, pady=10)

    def load_csv(self):
        """Wczytanie pliku CSV z wykorzystaniem wybranych parametrów."""
        file_path = filedialog.askopenfilename(
            title="Wybierz plik CSV",
            filetypes=[("Pliki CSV", "*.csv"), ("Wszystkie pliki", "*.*")]
        )
        if file_path:
            # Pobieramy wybrane parametry
            encoding = self.encoding_var.get()
            sep_choice = self.sep_var.get()
            if sep_choice == "Comma":
                sep = ","
            elif sep_choice == "Semicolon":
                sep = ";"
            elif sep_choice == "Tab":
                sep = "\t"
            else:
                sep = ","
            comment_choice = self.comment_var.get()
            comment = None if comment_choice == "None" else comment_choice

            try:
                self.df = pd.read_csv(file_path, encoding=encoding, sep=sep, comment=comment)
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
        - Wyszukuje brakujące wartości (NaN).
        """
        if self.df is None:
            messagebox.showwarning("Brak danych", "Najpierw wczytaj plik CSV.")
            return

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
        Przykładowe wykrywanie błędów:
        Wyszukuje kolumny numeryczne, w których występują wartości ujemne.
        """
        if self.df is None:
            messagebox.showwarning("Brak danych", "Najpierw wczytaj plik CSV.")
            return

        self.output_text.insert("end", "Wykrywanie błędów...\n")
        numeric_cols = self.df.select_dtypes(include=["int", "float"]).columns
        negative_values = {}

        for col in numeric_cols:
            negatives = (self.df[col] < 0).sum()
            if negatives > 0:
                negative_values[col] = negatives

        if not negative_values:
            self.output_text.insert("end", "Nie wykryto wartości ujemnych.\n")
        else:
            self.output_text.insert("end", "Wykryto wartości ujemne w kolumnach:\n")
            for col, count in negative_values.items():
                self.output_text.insert("end", f" - {col}: {count} wartości ujemnych\n")

        self.output_text.insert("end", "-" * 40 + "\n")

    def generate_plot(self):
        """
        Generowanie przykładowego wykresu – histogramu dla pierwszej kolumny numerycznej.
        """
        if self.df is None:
            messagebox.showwarning("Brak danych", "Najpierw wczytaj plik CSV.")
            return

        numeric_cols = self.df.select_dtypes(include=["int", "float"]).columns
        if len(numeric_cols) == 0:
            messagebox.showwarning("Brak kolumn liczbowych",
                                   "W tym pliku nie ma kolumn liczbowych do wyświetlenia wykresu.")
            return

        first_numeric_col = numeric_cols[0]
        fig = plt.Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.set_title(f"Histogram kolumny: {first_numeric_col}")
        self.df[first_numeric_col].plot(kind="hist", ax=ax, bins=10)

        plot_window = tk.Toplevel(self)
        plot_window.title("Wykres")
        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def save_csv(self):
        """
        Zapis pliku CSV przy użyciu biblioteki pandas.
        Plik jest zapisywany z parametrami:
         - separatorem ';'
         - bez indeksu
        """
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
                self.df.to_csv(file_path, sep=";", index=False)
                messagebox.showinfo("Sukces", f"Plik zapisany jako: {file_path}")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")


if __name__ == "__main__":
    app = CSVAnalyzer()
    app.mainloop()
