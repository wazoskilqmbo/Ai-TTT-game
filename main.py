import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI Game")
        self.dark_mode = True
        self.set_theme()
        self.main_menu()

    def set_theme(self):
        if self.dark_mode:
            self.bg_color = "#1e1e1e"
            self.fg_color = "#ffffff"
            self.btn_color = "#3c3f41"
            self.highlight_color = "#61afef"
        else:
            self.bg_color = "#f0f0f0"
            self.fg_color = "#000000"
            self.btn_color = "#ffffff"
            self.highlight_color = "#007acc"
        self.root.configure(bg=self.bg_color)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.set_theme()
        self.main_menu()

    def main_menu(self):
        self.clear_window()

        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(expand=True)

        tk.Label(frame, text="Tic-Tac-Toe AI", font=("Helvetica", 24, "bold"),
                fg=self.highlight_color, bg=self.bg_color).pack(pady=30)

        tk.Button(frame, text="Start Game", font=("Helvetica", 16),
                  command=self.start_game, bg=self.btn_color, fg=self.fg_color).pack(pady=10)

        tk.Button(frame, text="Switch Theme", font=("Helvetica", 16),
                  command=self.toggle_theme, bg=self.btn_color, fg=self.fg_color).pack(pady=10)

        tk.Button(frame, text="Exit", font=("Helvetica", 16),
                  command=self.root.quit, bg=self.btn_color, fg=self.fg_color).pack(pady=10)

    def start_game(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, bg=self.bg_color)
        frame.pack(expand=True)

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = []

        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(frame, text=" ", font=('Helvetica', 20),
                                width=6, height=3, bg=self.btn_color, fg=self.fg_color,
                                command=lambda r=i, c=j: self.make_move(r, c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        tk.Button(frame, text="Restart", font=("Helvetica", 12),
                  command=self.start_game, bg=self.btn_color, fg=self.fg_color).grid(row=3, column=0)

        tk.Button(frame, text="Main Menu", font=("Helvetica", 12),
                  command=self.main_menu, bg=self.btn_color, fg=self.fg_color).grid(row=3, column=1)

        tk.Button(frame, text="Exit", font=("Helvetica", 12),
                  command=self.root.quit, bg=self.btn_color, fg=self.fg_color).grid(row=3, column=2)

        if self.current_player == "O":
            self.root.after(100, self.ai_move)

    def make_move(self, row, col):
        if self.board[row][col] == " " and self.current_player == "X":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X")
            if self.check_game_over("X"):
                return
            self.current_player = "O"
            self.root.after(200, self.ai_move)  # Delay AI move slightly

    def ai_move(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    self.buttons[i][j].config(text="O")
                    if self.check_game_over("O"):
                        return
                    self.current_player = "X"
                    return

    def check_game_over(self, player):
        try:
            if not self.root.winfo_exists():
                return True 
            if self.check_winner(player):
                messagebox.showinfo("Game Over", f"{player} wins!")
                self.start_game()
                return True
            elif all(cell != " " for row in self.board for cell in row):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.start_game()
                return True
        except tk.TclError:
            return True
        return False

    def check_winner(self, symbol):
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)): return True
            if all(self.board[j][i] == symbol for j in range(3)): return True
        if all(self.board[i][i] == symbol for i in range(3)): return True
        if all(self.board[i][2 - i] == symbol for i in range(3)): return True
        return False

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
