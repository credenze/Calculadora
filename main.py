
import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculadoraRectificado:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Profesional de Rectificado")
        self.root.geometry("800x900")

        # Variables
        self.diametro_muela = tk.DoubleVar(value=550)
        self.ancho_muela = tk.DoubleVar(value=100)
        self.rpm_muela = tk.DoubleVar(value=500)
        self.diametro_cilindro = tk.DoubleVar(value=619)
        self.longitud_cilindro = tk.DoubleVar(value=1925)
        self.avance_z = tk.DoubleVar(value=1)
        self.rpm_cilindro = tk.DoubleVar(value=30)
        self.relacion_q = tk.DoubleVar(value=30)

        # Estilo
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Subtitle.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Info.TLabel', font=('Arial', 10))

        # Título principal
        ttk.Label(root, text="Calculadora Profesional de Rectificado", style='Title.TLabel').pack(pady=10)

        # Marco para parámetros de la muela
        self.crear_seccion_muela()
        
        # Marco para parámetros del cilindro
        self.crear_seccion_cilindro()

        # Marco para resultados
        self.crear_seccion_resultados()

        # Botón de cálculo
        ttk.Button(root, text="Calcular", command=self.calcular_todo).pack(pady=10)

    def crear_seccion_muela(self):
        frame = ttk.LabelFrame(self.root, text="Parámetros de la Muela", padding=10)
        frame.pack(fill="x", padx=10, pady=5)

        # Diámetro de muela
        self.crear_control_numerico(frame, "Diámetro de muela (mm):", self.diametro_muela, 550, 915)
        
        # Ancho de muela
        self.crear_control_numerico(frame, "Ancho de muela (mm):", self.ancho_muela, 0, 200)
        
        # RPM muela
        self.crear_control_numerico(frame, "RPM muela:", self.rpm_muela, 0, 1000)

    def crear_seccion_cilindro(self):
        frame = ttk.LabelFrame(self.root, text="Parámetros del Cilindro", padding=10)
        frame.pack(fill="x", padx=10, pady=5)

        # Diámetro del cilindro
        self.crear_control_numerico(frame, "Diámetro del cilindro (mm):", self.diametro_cilindro, 619, 705)
        
        # Longitud del cilindro
        self.crear_control_numerico(frame, "Longitud del cilindro (mm):", self.longitud_cilindro, 0, 2000)
        
        # Avance Z
        self.crear_control_numerico(frame, "Avance Z (mm/min):", self.avance_z, 0, 100)
        
        # RPM cilindro
        self.crear_control_numerico(frame, "RPM cilindro:", self.rpm_cilindro, 0, 60)
        
        # Relación Q
        self.crear_control_numerico(frame, "Relación Q:", self.relacion_q, 30, 35)

    def crear_control_numerico(self, parent, label_text, variable, min_val, max_val):
        frame = ttk.Frame(parent)
        frame.pack(fill="x", pady=2)
        
        ttk.Label(frame, text=label_text).pack(side="left")
        
        def disminuir():
            actual = variable.get()
            if actual > min_val:
                variable.set(actual - 1)

        def aumentar():
            actual = variable.get()
            if actual < max_val:
                variable.set(actual + 1)

        ttk.Button(frame, text="-", width=3, command=disminuir).pack(side="left", padx=5)
        entry = ttk.Entry(frame, textvariable=variable, width=10)
        entry.pack(side="left", padx=5)
        ttk.Button(frame, text="+", width=3, command=aumentar).pack(side="left", padx=5)
        ttk.Label(frame, text=f"(Min: {min_val}, Max: {max_val})").pack(side="left", padx=5)

    def crear_seccion_resultados(self):
        self.resultado_frame = ttk.LabelFrame(self.root, text="Resultados y Fórmulas", padding=10)
        self.resultado_frame.pack(fill="x", padx=10, pady=5)
        
        self.resultado_text = tk.Text(self.resultado_frame, height=15, width=70)
        self.resultado_text.pack(pady=10)

    def calcular_todo(self):
        # Limpiar resultados anteriores
        self.resultado_text.delete(1.0, tk.END)
        
        # Velocidad de corte de la muela
        v_muela = (math.pi * self.diametro_muela.get() * self.rpm_muela.get()) / 60000  # m/s
        
        # Velocidad de corte del cilindro
        v_cilindro = (math.pi * self.diametro_cilindro.get() * self.rpm_cilindro.get()) / 60000  # m/s
        
        # Relación Q real
        q_real = v_muela / v_cilindro if v_cilindro != 0 else 0
        
        resultados = f"""Resultados del cálculo:

1. Velocidad de corte de la muela:
   • Fórmula: v = (π × d × rpm) / 60000
   • Resultado: {v_muela:.2f} m/s

2. Velocidad de corte del cilindro:
   • Fórmula: v = (π × d × rpm) / 60000
   • Resultado: {v_cilindro:.2f} m/s

3. Relación Q real:
   • Fórmula: Q = v_muela / v_cilindro
   • Resultado: {q_real:.2f}

Recomendaciones:
• La relación Q debe mantenerse entre 30-35 para un rectificado óptimo
• Velocidad de corte recomendada: 25-35 m/s
• Verificar la velocidad máxima permitida de la muela

Aspectos importantes:
• Refrigeración adecuada
• Inspección regular del desgaste de la muela
• Control de vibraciones
"""
        self.resultado_text.insert(1.0, resultados)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraRectificado(root)
    root.mainloop()
