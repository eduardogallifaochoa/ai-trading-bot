# formatters.py

# Format float values into USD string with commas and 2 decimals
def format_usd(value):
    return f"${value:,.2f}"

# Format timestamp (optional, for logs or database entries)
def format_timestamp(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

# Display suggested questions in a friendly way
def print_suggestions(suggestions_dict):
    print("🤖 Jarvis Suggestions (write a number or your own question):")
    for key, text in suggestions_dict.items():
        print(f"  {key}. {text}")
    print("\n💡 Tip: You can just type 1, 2, 3... or write your own question!\n")
