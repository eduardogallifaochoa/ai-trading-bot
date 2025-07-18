import sqlite3

# Conecta con la base de datos
conn = sqlite3.connect("crypto_summaries.db")
cursor = conn.cursor()

# Ejecuta una query para obtener todos los resúmenes
cursor.execute("SELECT created_at, btc_price, eth_price, gpt_analysis FROM summaries ORDER BY created_at DESC")

rows = cursor.fetchall()

# Muestra los resultados
for row in rows:
    print(f"\n🕒 Date: {row[0]}")
    print(f"BTC Price: ${row[1]:,.2f} | ETH Price: ${row[2]:,.2f}")
    print("📈 GPT Summary:\n", row[3])
    print("="*60)

conn.close()
