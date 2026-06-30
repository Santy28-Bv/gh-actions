import os

name = os.getenv("NAME")
age = int(os.getenv("EDAD"))

print("=" * 40)
print("RESULTADO DE LA VALIDACIÓN")
print("=" * 40)
print(f"Nombre: {name}")
print(f"Edad: {age}")

if age >= 18:
    print(f"✅ {name} es MAYOR de edad")
else:
    print(f"❌ {name} es MENOR de edad")