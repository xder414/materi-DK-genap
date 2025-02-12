def konversi_suhu(celcius, ke="fahrenheit"):
    return (celcius * 9/5) + 32 if ke.lower() == "fahrenheit" else celcius + 273.15

# Contoh penggunaan
print(f"25°C = {konversi_suhu(25, 'fahrenheit')}°F")
print(f"25°C = {konversi_suhu(25, 'kelvin')}K")