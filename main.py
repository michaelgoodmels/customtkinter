import customtkinter as ctk
from time import strftime


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Wordclock")
        self.geometry("800x200")
        self.configure(fg_color="black")
        self.configure(hover_color="black")

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
        hour, minute, second = time_str.split(":")
        hour = int(hour)
        minute = int(minute)
        second = int(second)

        hours = [
            "zwölfi",
            "eis",
            "zwei",
            "dü",
            "vieri",
            "fünfi",
            "sechsi",
            "siebni",
            "achti",
            "nüni",
            "zehni",
            "ölfi"
        ]

        minutes = [
            "gnau",
            "füf ab",
            "zeh ab",
            "viertel ab",
            "zwinzg ab",
            "füf vor halbi",
            "halbi",
            "füf ab halbi",
            "zwinzg vor",
            "viertel vor",
            "zeh vor",
            "füf vor"
        ]

        if minute == 0:
            return f"Es isch jetz {hours[hour]} \n\n und {self.format_second(second)}"
        elif minute <= 30:
            return f"Es isch jetz {minutes[minute // 5]} {hours[hour % 12]} \n\n und {self.format_second(second)}"
        else:
            return f"Es isch jetz {minutes[(60 - minute) // 5]} {hours[(hour + 1) % 12]} \n\n und {self.format_second(second)}"

    def format_second(self, second):
        if second == 1:
            return "ei Sekundä"
        else:
            return f"{second} Sekundä"


if __name__ == "__main__":
    app = WordClock()
    app.mainloop()
