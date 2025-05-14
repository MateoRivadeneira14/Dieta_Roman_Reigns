import pulp

# Crear el problema
prob = pulp.LpProblem("Dieta_Roman_Reigns", pulp.LpMinimize)

# Variables reales
x1 = pulp.LpVariable('Desayuno', lowBound=0)
x2 = pulp.LpVariable('Comida_Entrenamiento', lowBound=0)
x3 = pulp.LpVariable('Pasta', lowBound=0)
x4 = pulp.LpVariable('Batido_Proteina', lowBound=0)
x5 = pulp.LpVariable('Atun_Sandwich', lowBound=0)

# Suplementos
c = pulp.LpVariable('Extra_Carb', lowBound=0)
p = pulp.LpVariable('Extra_Prot', lowBound=0)
g = pulp.LpVariable('Extra_Grasa', lowBound=0)

# Función objetivo: minimizar el costo total
prob += (
    2.50*x1 + 4.00*x2 + 1.00*x3 + 2.00*x4 + 2.80*x5 +
    0.80*c + 1.50*p + 0.70*g
), "Costo_Total"

# Restricciones nutricionales mínimas
prob += 55*x1 + 55*x2 + 75*x3 + 3*x4 + 15*x5 + 10*c >= 287, "Carbohidratos"
prob += 30*x1 + 38*x2 + 13*x3 + 25*x4 + 25*x5 + 10*p >= 288, "Proteinas"
prob += 10*x1 + 5.3*x2 + 1.5*x3 + 2*x4 + 3*x5 + 5*g >= 70, "Grasas"

# Rango de calorías
calorias = (
    400*x1 + 430*x2 + 350*x3 + 150*x4 + 220*x5 +
    40*c + 40*p + 45*g
)
prob += calorias >= 2900, "Calorias_Min"
prob += calorias <= 3000, "Calorias_Max"

# Resolver
prob.solve()

# Mostrar resultados
print(f"Estado: {pulp.LpStatus[prob.status]}")
for v in prob.variables():
    print(f"{v.name}: {v.varValue:.2f}")

print(f"\nCosto total: ${pulp.value(prob.objective):.2f}")
