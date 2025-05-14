# 🥗💪 Modelo de Programación Lineal: Dieta de Roman Reigns

Este proyecto modela un problema clásico de **programación lineal** basado en la dieta real del campeón de la WWE, **Roman Reigns**, popularizada por el youtuber de fitness **Aseel Soueid**.

---

## 📜 Contexto

Aseel Soueid es conocido por replicar las intensas rutinas y dietas de celebridades del mundo del fitness. En uno de sus vídeos, decide seguir durante un día completo la dieta de Roman Reigns, quien consume:

- 🍽️ **6 comidas limpias**
- 🔥 Cerca de **3,000 calorías diarias**
- ⚖️ Un reparto de macronutrientes:  
  - 🥖 40% carbohidratos  
  - 🥩 40% proteínas  
  - 🥑 20% grasas

El objetivo es encontrar una **combinación óptima de comidas** que satisfaga los requerimientos nutricionales de Reigns **al menor costo posible**, incluyendo alimentos como avena, arroz, pechuga de pollo, pasta, atún, batidos de proteína, y suplementos.

---

## 🧠 Formulación del Problema

Se define un **modelo de programación lineal** con:

- ✅ **Variables de decisión**: porciones de distintos alimentos y suplementos.
- 🎯 **Función objetivo**: minimizar el costo total diario.
- 📏 **Restricciones**:
  - Mínimos requerimientos de **carbohidratos, proteínas y grasas**.
  - Calorías totales entre **2900 y 3000 kcal**.

También se incluyen **suplementos nutricionales** para cubrir déficits si los alimentos no son suficientes.

---

## 📂 Estructura del Proyecto

- `modelo_dieta.py` → Script principal con el modelo usando `PuLP`.
- `README.md` → Descripción general del problema y solución.
- `requirements.txt` → Dependencias necesarias para ejecutar el modelo.

---

## 🧪 Ejecución

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
