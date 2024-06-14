import tkinter as tk
import math
from ply.lex import lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'POWER',
    'SIN',
    'COS',
    'TAN',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_POWER = r'\^'
t_SIN = r'sin'
t_COS = r'cos'
t_TAN = r'tan'


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex()

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

      
        self.entry = tk.Entry(master, width=20, font=('Arial', 16), bg='#ECECEC', fg='black', bd=5)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

      
        self.output_text = tk.Text(master, height=10, width=40, wrap=tk.WORD, font=('Arial', 12), padx=5, pady=5, bg='#ECECEC', fg='black', bd=5)
        self.output_text.grid(row=1, column=0, columnspan=4, pady=10)

     
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '(', ')', 'sin', 'cos',
            'tan', 'AC', '^'
        ]

        row_val = 2
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, command=lambda b=button: self.on_button_click(b), font=('Arial', 12), bg='black', fg='white', bd=5).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        current_text = self.entry.get()

        if button == '=':
            try:
                result = eval(current_text, {'sin': lambda x: math.sin(math.radians(x)), 'cos': lambda x: math.cos(math.radians(x)), 'tan': lambda x: math.tan(math.radians(x)), '^': '**'})
                self.output_text.insert(tk.END, f"{current_text} = {result}\n")
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))

                
                tokens = self.get_tokens(current_text)
                self.display_tokens(tokens)

            except SyntaxError as e:
                self.output_text.insert(tk.END, f"Syntax Error: {str(e)}\n")
            except Exception as e:
                self.output_text.insert(tk.END, f"Error: {str(e)}\n")
        elif button == 'C':
            self.entry.delete(0, tk.END)
            self.output_text.delete('1.0', tk.END)
        elif button == 'AC':
            self.clear_all()
        else:
            self.entry.insert(tk.END, button)

    def get_tokens(self, expression):
        lexer.input(expression)
        tokens = []

        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens.append((tok.type, tok.value))

        return tokens

    def display_tokens(self, tokens):
        self.output_text.delete('1.0', tk.END)
        for token in tokens:
            if token[0] == 'TIMES':
                token_type = 'TIMES'
                token_value = '/'
            else:
                token_type = token[0]
                token_value = repr(token[1])

            self.output_text.insert(tk.END, f"{token_type}: {token_value}\n")

    def clear_all(self):
        self.entry.delete(0, tk.END)
        self.output_text.delete('1.0', tk.END)


root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
