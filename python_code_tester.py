import subprocess
import tkinter as tk


class PythonCodeTester(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create text area for user to enter code
        self.code_text = tk.Text(self)
        self.code_text.pack()

        # Create button to run the code
        self.run_button = tk.Button(self, text="Run", command=self.run_code)
        self.run_button.pack()

        # Create text area for output
        self.output_text = tk.Text(self)
        self.output_text.pack()

    def run_code(self):
        # Get user's code from the text area
        user_code = self.code_text.get("1.0", tk.END)

        # Run the user's code and get the result
        result = self.execute_python_code(user_code)

        # Display the result in the output text area
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

    def execute_python_code(self, code):
        try:
            result = subprocess.check_output(
                ["python", "-c", code], stderr=subprocess.STDOUT, timeout=5)
            return result.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
        except subprocess.TimeoutExpired:
            return "Error: Execution timed out"


root = tk.Tk()
app = PythonCodeTester(master=root)
app.mainloop()
