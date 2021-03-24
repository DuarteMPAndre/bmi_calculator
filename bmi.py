try:
    import tkinter as tk

     
             
    def calculate():
    
        try:
            kg = float(entry_kg.get())
            height = float(entry_height.get())
            bmi = kg / (height ** 2)
            bmi = float("%.2f" %bmi)
            bmi_text = str(bmi)
            final_label.config(text="BMI: "+bmi_text)
            if height > 2.70:
                is_healthy_label.config(text="You are way too tall!")
            elif kg > 595:
                is_healthy_label.config(text="You are way too fat!")
            elif kg > 595 and height > 2.70:
                is_healthy_label.config(text="You are way too fat and way too tall!!!")
            elif kg < 10:
                is_healthy_label.config(text="You are way too skinny!")
            elif height < 0.30:
                is_healthy_label.config(text="You are way too short!")
            elif height < 0.30 and kg < 10:
                is_healthy_label.config(text="You are way too skinny and short!!!")
            else:    
                if (bmi <=18.4):
                    is_healthy_label.config(text="You are under weight!")
                elif (bmi >=18.5 and bmi <=24.9):
                    is_healthy_label.config(text="You have a normal weight!")
                elif (bmi >=25 and bmi <=29.9):
                    is_healthy_label.config(text="You are over weight!")
                elif (bmi >=30 and bmi <=34.9):
                    is_healthy_label.config(text="You are obese(CLASS 1)!")
                elif (bmi >=35 and bmi <= 39.9):
                    is_healthy_label.config(text="You are obese(CLASS 2)!")
                elif (bmi >=40):
                    is_healthy_label.config(text="You are obese(CLASS 3)!") 
        except  Exception:
                is_healthy_label.config(text="Something went wrong! Try again")
    

    def change_metrics():
        
        label_kg.config(text="Weight(lbs): ")
        label_height.config(text="Height(in): ")
        calculate_button.config(command=calculate_imperial)
        change_to_imperial.config(text="Change to Metric")
        change_to_imperial.config(command=change_to_metrics)
        kg = float(entry_kg.get())
        height = float(entry_height.get())
        lbs = kg * 2.20462262
        inch = height * 39.3700787
        lbs = float("%.2f" %lbs)
        inch = float("%.2f" %inch)
        entry_kg.delete(0, 'end')
        entry_height.delete(0, 'end')
        entry_kg.insert(0, lbs)
        entry_height.insert(0, inch)
    def change_to_metrics():
        
        label_kg.config(text="Weight(kg): ")
        label_height.config(text="Height(m): ")
        calculate_button.config(command=calculate)
        change_to_imperial.config(text="Change to Imperial")
        change_to_imperial.config(command=change_metrics)
        kg = float(entry_kg.get())
        height = float(entry_height.get())
        lbs = kg * 0.45359237
        inch = height * 0.0254
        lbs = float("%.2f" %lbs)
        inch = float("%.2f" %inch)
        entry_kg.delete(0, 'end')
        entry_height.delete(0, 'end')
        entry_kg.insert(0, lbs)
        entry_height.insert(0, inch)
    def calculate_imperial():
        try:
        
            
            
            kg = float(entry_kg.get())
            height = float(entry_height.get())
            bmi = 703 * kg / (height ** 2)
            bmi = float("%.2f" %bmi)
            bmi_text = str(bmi)
            final_label.config(text="BMI: "+bmi_text)
            if height > 106:
                is_healthy_label.config(text="You are way too tall!")
            elif kg > 1312:
                is_healthy_label.config(text="You are way too fat!")
            elif kg > 1312 and height > 106:
                is_healthy_label.config(text="You are way too fat and way too tall!!!")
            elif kg < 22.05:
                is_healthy_label.config(text="You are way too skinny!")
            elif height < 11.81:
                is_healthy_label.config(text="You are way too short!")
            elif height < 11.81 and kg < 22.05:
                is_healthy_label.config(text="You are way too skinny and short!!!")
            else:    
                if (bmi <=18.4):
                    is_healthy_label.config(text="You are under weight!")
                elif (bmi >=18.5 and bmi <=24.9):
                    is_healthy_label.config(text="You have a normal weight!")
                elif (bmi >=25 and bmi <=29.9):
                    is_healthy_label.config(text="You are over weight!")
                elif (bmi >=30 and bmi <=34.9):
                    is_healthy_label.config(text="You are obese(CLASS 1)!")
                elif (bmi >=35 and bmi <= 39.9):
                    is_healthy_label.config(text="You are obese(CLASS 2)!")
                elif (bmi >=40):
                    is_healthy_label.config(text="You are obese(CLASS 3)!") 
        except  Exception:
                is_healthy_label.config(text="Something went wrong! Try again")
    
    canvas = tk.Tk()
    canvas.title("BMI Calculator")
    canvas.geometry("400x100")
    canvas.iconbitmap(r'C:\Users\Utilizador\PycharmProjects\bmi calculator\bmi_image.ico')
    label_kg = tk.Label(canvas, text="Weight(kg): ")
    label_kg.grid(column=0, row=0)
    entry_kg = tk.Entry(canvas)
    entry_kg.grid(column=1, row=0)
    label_height = tk.Label(canvas, text="Height(m): ")
    label_height.grid(column=0, row=1)
    entry_height = tk.Entry(canvas)
    entry_height.grid(column=1, row=1)
    calculate_button = tk.Button(canvas, text="Calculate", command = calculate)
    calculate_button.grid(column=0, row=2)
    final_label = tk.Label(canvas, text="BMI: ")
    final_label.grid(column=1, row=2)
    is_healthy_label = tk.Label(canvas, text="")
    is_healthy_label.grid(column=0, row=3)
    change_to_imperial = tk.Button(canvas, text="Change to Imperial", command=change_metrics)
    change_to_imperial.grid(column=2, row=0)
    canvas.mainloop()
except  Exception:
    print("ERROR")
