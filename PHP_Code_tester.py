import tkinter as tk
import subprocess


class PythonExecutor:
    def __init__(self, master):
        self.master = master
        master.title("Python Executor")

        # Create text box for user to enter code
        self.code_box = tk.Text(master, height=20, width=50)
        self.code_box.pack()

        # Create button to execute the code
        self.execute_button = tk.Button(
            master, text="Execute", command=self.execute_code)
        self.execute_button.pack()

        # Create text box to display output
        self.output_box = tk.Text(master, height=10, width=50)
        self.output_box.pack()

    def execute_code(self):
        code = self.code_box.get("1.0", tk.END)
        try:
            output = subprocess.check_output(
                ["python", "-c", code], stderr=subprocess.STDOUT, timeout=5)
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, output.decode('utf-8').strip())
        except subprocess.CalledProcessError as e:
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, e.output.decode('utf-8').strip())
        except subprocess.TimeoutExpired as e:
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(
                tk.END, "Execution timed out after 5 seconds")


root = tk.Tk()
app = PythonExecutor(root)
root.mainloop()
