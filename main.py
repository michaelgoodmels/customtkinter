import customtkinter as ctk
from time import strftime


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Michael's Wordclock")
        self.geometry("800x200")
        self.configure(fg_color="black")

        self.label = ctk.CTkLabel(self, text="", fg_color="black", text_color="white")
        self.label.cget("font").configure(family="Consolas", size=42)
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.update_time()

    def update_time(self):
        current_time = strftime("%H:%M:%S")
        self.label.configure(text=current_time)
        self.after(1000, self.update_time)


class WordClock(App):
    def __init__(self):
        super().__init__()

    def update_time(self):
        current_time = strftime("%H:%M:%S")
        words = self.convert_to_words(current_time)
        self.label.configure(text=words)
        self.after(1000, self.update_time)

    def convert_to_words(self, time_str):
        hour, minute, _ = time_str.split(":")
        hour = int(hour)
        minute = int(minute)

        hours = [
            "zwölf",
            "eins",
            "zwei",
            "drei",
            "vier",
            "fünf",
            "sechs",
            "sieben",
            "acht",
            "neun",
            "zehn",
            "elf"
        ]

        minutes = [
            "genau",
            "fünf nach",
            "zehn nach",
            "viertel nach",
            "zwanzig nach",
            "fünf vor halb",
            "halb",
            "fünf nach halb",
            "zwanzig vor",
            "viertel vor",
            "zehn vor",
            "fünf vor"
        ]

        if minute == 0:
            return f"Es ist {hours[hour]} Uhr."
        elif minute <= 30:
            return f"Es ist {minutes[minute // 5]} {hours[hour % 12]}."
        else:
            return f"Es ist {minutes[(60 - minute) // 5]} vor {hours[(hour + 1) % 12]}."


if __name__ == "__main__":
    app = WordClock()
    app.mainloop()
