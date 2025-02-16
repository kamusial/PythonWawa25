import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import os


class CSVAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizator CSV")
        self.root.geometry("1000x800")
        self.df = None

        # Główny kontener
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Frame na opcje wczytywania
        self.options_frame = ttk.LabelFrame(self.main_frame, text="Opcje wczytywania", padding="5")
        self.options_frame.grid(row=0, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        # Separator
        ttk.Label(self.options_frame, text="Separator:").grid(row=0, column=0, padx=5, pady=2)
        self.separator_var = tk.StringVar(value=',')
        self.separator_combo = ttk.Combobox(self.options_frame, textvariable=self.separator_var, width=5)
        self.separator_combo['values'] = [',', ';', '\t', '|', ' ']
        self.separator_combo.grid(row=0, column=1, padx=5, pady=2)

        # Kodowanie
        ttk.Label(self.options_frame, text="Kodowanie:").grid(row=0, column=2, padx=5, pady=2)
        self.encoding_var = tk.StringVar(value='utf-8')
        self.encoding_combo = ttk.Combobox(self.options_frame, textvariable=self.encoding_var, width=10)
        self.encoding_combo['values'] = ['utf-8', 'ascii', 'iso-8859-1', 'cp1250', 'cp1252']
        self.encoding_combo.grid(row=0, column=3, padx=5, pady=2)

        # Symbol dziesiętny
        ttk.Label(self.options_frame, text="Symbol dziesiętny:").grid(row=0, column=4, padx=5, pady=2)
        self.decimal_var = tk.StringVar(value='.')
        self.decimal_combo = ttk.Combobox(self.options_frame, textvariable=self.decimal_var, width=5)
        self.decimal_combo['values'] = ['.', ',']
        self.decimal_combo.grid(row=0, column=5, padx=5, pady=2)

        # Wiersz nagłówka
        ttk.Label(self.options_frame, text="Wiersz nagłówka:").grid(row=1, column=0, padx=5, pady=2)
        self.header_var = tk.StringVar(value='0')
        self.header_combo = ttk.Combobox(self.options_frame, textvariable=self.header_var, width=5)
        self.header_combo['values'] = ['0', 'None', '1', '2', '3', '4', '5']
        self.header_combo.grid(row=1, column=1, padx=5, pady=2)

        # Znak komentarza
        ttk.Label(self.options_frame, text="Znak komentarza:").grid(row=1, column=2, padx=5, pady=2)
        self.comment_var = tk.StringVar(value='#')
        self.comment_combo = ttk.Combobox(self.options_frame, textvariable=self.comment_var, width=5)
        self.comment_combo['values'] = ['#', '%', '//', 'None']
        self.comment_combo.grid(row=1, column=3, padx=5, pady=2)

        # Obsługa brakujących wartości
        ttk.Label(self.options_frame, text="Brakujące wartości:").grid(row=1, column=4, padx=5, pady=2)
        self.na_values_var = tk.StringVar(value='NA')
        self.na_values_combo = ttk.Combobox(self.options_frame, textvariable=self.na_values_var, width=10)
        self.na_values_combo['values'] = ['NA', 'NaN', 'null', '', '?']
        self.na_values_combo.grid(row=1, column=5, padx=5, pady=2)

        # Przyciski
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.grid(row=1, column=0, pady=5)

        ttk.Button(self.buttons_frame, text="Wczytaj plik CSV", command=self.load_csv).grid(row=0, column=0, pady=5)
        ttk.Button(self.buttons_frame, text="Sprawdź duplikaty", command=self.check_duplicates).grid(row=1, column=0,
                                                                                                     pady=5)
        ttk.Button(self.buttons_frame, text="Sprawdź spójność danych", command=self.check_data_consistency).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 pady=5)
        ttk.Button(self.buttons_frame, text="Generuj wykres", command=self.show_plot_options).grid(row=3, column=0,
                                                                                                   pady=5)
        ttk.Button(self.buttons_frame, text="Zapisz plik", command=self.save_file).grid(row=4, column=0, pady=5)

        # Panel wyników
        self.result_text = tk.Text(self.main_frame, height=15, width=60)
        self.result_text.grid(row=1, column=1, rowspan=5, padx=10)

        # Frame na wykres
        self.plot_frame = ttk.Frame(self.main_frame)
        self.plot_frame.grid(row=6, column=0, columnspan=2, pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Przygotowanie parametrów wczytywania
                header = None if self.header_var.get() == 'None' else int(self.header_var.get())
                comment = None if self.comment_var.get() == 'None' else self.comment_var.get()
                na_values = self.na_values_var.get()

                # Wczytanie pliku z wybranymi parametrami
                self.df = pd.read_csv(
                    file_path,
                    sep=self.separator_var.get(),
                    encoding=self.encoding_var.get(),
                    decimal=self.decimal_var.get(),
                    header=header,
                    comment=comment,
                    na_values=na_values
                )

                # Wyświetlenie informacji o wczytanym pliku
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Wczytano plik: {file_path}\n")
                self.result_text.insert(tk.END, f"Liczba wierszy: {len(self.df)}\n")
                self.result_text.insert(tk.END, f"Liczba kolumn: {len(self.df.columns)}\n")
                self.result_text.insert(tk.END, "\nParametry wczytywania:\n")
                self.result_text.insert(tk.END, f"Separator: {self.separator_var.get()}\n")
                self.result_text.insert(tk.END, f"Kodowanie: {self.encoding_var.get()}\n")
                self.result_text.insert(tk.END, f"Symbol dziesiętny: {self.decimal_var.get()}\n")
                self.result_text.insert(tk.END, f"Wiersz nagłówka: {self.header_var.get()}\n")
                self.result_text.insert(tk.END, f"Znak komentarza: {self.comment_var.get()}\n")
                self.result_text.insert(tk.END, f"Brakujące wartości: {self.na_values_var.get()}\n")
                self.result_text.insert(tk.END, "\nKolumny:\n" + "\n".join(self.df.columns))

            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się wczytać pliku: {str(e)}")

    def check_duplicates(self):
        if self.df is None:
            messagebox.showwarning("Ostrzeżenie", "Najpierw wczytaj plik CSV!")
            return

        duplicates = self.df.duplicated()
        dup_count = duplicates.sum()

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Znaleziono {dup_count} duplikatów.\n\n")

        if dup_count > 0:
            self.result_text.insert(tk.END, "Duplikaty:\n")
            self.result_text.insert(tk.END, str(self.df[duplicates]))

    def check_data_consistency(self):
        if self.df is None:
            messagebox.showwarning("Ostrzeżenie", "Najpierw wczytaj plik CSV!")
            return

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Analiza spójności danych:\n\n")

        # Sprawdzenie brakujących wartości
        missing_values = self.df.isnull().sum()
        self.result_text.insert(tk.END, "Brakujące wartości:\n")
        self.result_text.insert(tk.END, str(missing_values) + "\n\n")

        # Podstawowe statystyki
        self.result_text.insert(tk.END, "Podstawowe statystyki:\n")
        self.result_text.insert(tk.END, str(self.df.describe()))

    def show_plot_options(self):
        if self.df is None:
            messagebox.showwarning("Ostrzeżenie", "Najpierw wczytaj plik CSV!")
            return

        plot_window = tk.Toplevel(self.root)
        plot_window.title("Opcje wykresu")
        plot_window.geometry("300x200")

        ttk.Label(plot_window, text="Wybierz typ wykresu:").pack(pady=5)

        plot_type = tk.StringVar()
        ttk.Radiobutton(plot_window, text="Wykres słupkowy", variable=plot_type, value="bar").pack()
        ttk.Radiobutton(plot_window, text="Wykres liniowy", variable=plot_type, value="line").pack()
        ttk.Radiobutton(plot_window, text="Wykres punktowy", variable=plot_type, value="scatter").pack()

        ttk.Button(plot_window, text="Generuj wykres",
                   command=lambda: self.generate_plot(plot_type.get())).pack(pady=10)

    def generate_plot(self, plot_type):
        if len(self.df.columns) < 2:
            messagebox.showwarning("Ostrzeżenie", "Potrzebne są co najmniej dwie kolumny do wygenerowania wykresu!")
            return

        # Czyszczenie poprzedniego wykresu
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(8, 4))

        if plot_type == "bar":
            self.df.iloc[:, 0:2].plot(kind='bar', ax=ax)
        elif plot_type == "line":
            self.df.iloc[:, 0:2].plot(kind='line', ax=ax)
        elif plot_type == "scatter":
            self.df.plot.scatter(x=self.df.columns[0], y=self.df.columns[1], ax=ax)

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def save_file(self):
        if self.df is None:
            messagebox.showwarning("Ostrzeżenie", "Najpierw wczytaj plik CSV!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
        )

        if file_path:
            try:
                if file_path.endswith('.csv'):
                    self.df.to_csv(file_path, index=False)
                else:
                    self.df.to_excel(file_path, index=False)
                messagebox.showinfo("Sukces", "Plik został zapisany pomyślnie!")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVAnalyzer(root)
    root.mainloop()