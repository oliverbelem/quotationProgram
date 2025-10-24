from customtkinter import CTk, CTkFrame, CTkLabel


class visual:
    def __init__(self):
        self._root = CTk()
        self._information_box:CTkFrame = None

        self.layout()

    def layout(self):
        self._root.minsize(800, 600)
        self._root.title("CTk example")

        self._information_box = CTkFrame(master= self._root)
        self._information_box.grid(row=0, column=0, pady=10, padx=10)

        self._label_info_box = CTkLabel(master= self._information_box, text="Infobox")
        self._label_info_box.pack()

    def run(self):
       self._root.mainloop()

def main():
    app = visual()
    app.run()

if __name__ == "__main__":
    main()