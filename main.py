import pandas as pd

# Tehdään pieni DataFrame
df = pd.DataFrame({
    "Nimi": ["Anna", "Bertta", "Cecilia"],
    "Pisteet": [90, 85, 92]
})

print("Pandas toimii! DataFrame näyttää tältä:")
print(df)

# Tarkistetaan pandas-versio
print("\nKäytössä oleva pandas-versio:")
print(pd.__version__)
