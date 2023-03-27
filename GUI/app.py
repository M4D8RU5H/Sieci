import tkinter

import customtkinter as ct
import os
from PIL import Image
from tkinter import font
from algorithms.ialgorithm import IAlgorithm


class App(ct.CTk):
    _nav_buttons = []
    _frames = []

    def __init__(self, algorithms: IAlgorithm):
        super().__init__()

        ct.set_appearance_mode("Dark")
        ct.set_default_color_theme("dark-blue")

        self.title("Sieci")
        self.geometry("1280x730")
        self.resizable(False, False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load logo image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = ct.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(55, 55))

        # create navigation frame
        self.navigation_frame = ct.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        self.navigation_frame_label = ct.CTkLabel(master=self.navigation_frame,
                                                             text="   Algorytmy\n   kryptograficzne",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=ct.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # create algorithm frames and navigation buttons
        i = 1
        for algorithm in algorithms:
            # create algorithm frames
            self.algorithm_frame = ct.CTkFrame(self, corner_radius=0, fg_color="transparent")
            self.algorithm_frame.grid_columnconfigure(index=0, weight=1)
            self.algorithm_frame.grid_columnconfigure(index=1, weight=15)

            self.algorithm_name_label = ct.CTkLabel(master=self.algorithm_frame,
                                                    text=algorithm.get_name(),
                                                    font=(font.nametofont("TkDefaultFont"), 25))
            self.algorithm_name_label.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

            self.selected_option = tkinter.StringVar()

            self.encrypt_radio_button = ct.CTkRadioButton(master=self.algorithm_frame, text="Szyfrowanie",
                                                          variable=self.selected_option, value="encrypt")
            self.encrypt_radio_button.grid(row=2, column=0, padx=(20, 0), pady=10, sticky="w")
            self.encrypt_radio_button.select()

            self.decrypt_radio_button = ct.CTkRadioButton(master=self.algorithm_frame, text="Deszyfrowanie",
                                                          variable=self.selected_option, value="decrypt")
            self.decrypt_radio_button.grid(row=2, column=1, padx=0, pady=10, sticky="w")

            self.key_prompt_label = ct.CTkLabel(master=self.algorithm_frame, text="Podaj klucz:")
            self.key_prompt_label.grid(row=3, column=0, padx=(20, 0), pady=(15, 0), sticky="w")

            self.key_entry = ct.CTkEntry(master=self.algorithm_frame)
            self.key_entry.grid(row=3, column=1, padx=0, pady=10, sticky="w")

            self.input_prompt_label = ct.CTkLabel(master=self.algorithm_frame, text="Wpisz tekst:")
            self.input_prompt_label.grid(row=4, column=0, padx=20, pady=(15, 0), sticky="w")

            self.input_textbox = ct.CTkTextbox(master=self.algorithm_frame)
            self.input_textbox.grid(row=5, column=0, padx=20, pady=10, sticky="we", columnspan=2)

            self.output_label = ct.CTkLabel(master=self.algorithm_frame, text="Wynik:")
            self.output_label.grid(row=6, column=0, padx=20, pady=(15, 0), sticky="w")

            self.output_textbox = ct.CTkTextbox(master=self.algorithm_frame)
            self.output_textbox.grid(row=7, column=0, padx=20, pady=10, sticky="we", columnspan=2)
            self.output_textbox.bind("<Key>", lambda e: "break")

            self.calculate_button = ct.CTkButton(master=self.algorithm_frame, text="Zaszyfruj",
                                                 command=lambda i=self.input_textbox, k=self.key_entry, o=self.output_textbox,
                                                                a=algorithm, s=self.selected_option: self.calculate(i, k, o, a, s))
            self.calculate_button.grid(row=8, column=1, padx=20, pady=(15, 10), sticky="e")

            self.encrypt_radio_button.configure(
                command=lambda s=self.selected_option, b=self.calculate_button: self.handle_user_selection(s, b))
            self.decrypt_radio_button.configure(
                command=lambda s=self.selected_option, b=self.calculate_button: self.handle_user_selection(s, b))

            self._frames.append(self.algorithm_frame)

            # create navigation buttons
            self.nav_button = ct.CTkButton(master=self.navigation_frame,
                                           corner_radius=0,
                                           height=40,
                                           border_spacing=10,
                                           text=algorithm.get_name(),
                                           fg_color="transparent",
                                           text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           anchor="w")
            self.nav_button.configure(command=lambda f=self.algorithm_frame, b=self.nav_button: self.select_frame(f, b))
            self.nav_button.grid(row=i, column=0, sticky="ew")

            self._nav_buttons.append(self.nav_button)

            if (i == 1):
                self.select_frame(self.algorithm_frame, self.nav_button)

            i += 1

    @staticmethod
    def handle_user_selection(selected_option: tkinter.StringVar, calculate_button: ct.CTkButton):
        if selected_option.get() == "encrypt":
            calculate_button.configure(text="Zaszyfruj")
        elif selected_option.get() == "decrypt":
            calculate_button.configure(text="Odszyfruj")
        pass

    @staticmethod
    def calculate(input_textbox: ct.CTkTextbox, key_entry: ct.CTkEntry, output_textbox: ct.CTkTextbox, algorithm: IAlgorithm,
                  selected_option: tkinter.StringVar):
        output_textbox.delete("0.0", "end")

        input = input_textbox.get("0.0", "end")
        key = key_entry.get()

        if selected_option.get() == "encrypt":
            output_textbox.insert("end", algorithm.encrypt(input, key))
        elif selected_option.get() == "decrypt":
            output_textbox.insert("end", algorithm.decrypt(input, key))
        pass

    def select_frame(self, frame: ct.CTkFrame, button: ct.CTkButton):
        for f in self._frames:
            f.grid_forget()

        frame.grid(row=0, column=1, sticky="nsew")

        for nb in self._nav_buttons:
            nb.configure(fg_color="transparent")

        button.configure(fg_color=("gray75", "gray25"))
        pass


