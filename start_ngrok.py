from pyngrok import ngrok

# Paste your token here
ngrok.set_auth_token("302kEDMsX8i4kZP9KEnQzGuqo1C_2M3afuoj4BFy7k9m2mBic")  # <-- use your actual token here

# Open the tunnel to Flask (running on port 5000)
public_url = ngrok.connect(5000)
print("🚀 Your app is live at:", public_url)

# Keep the tunnel alive
input("Press Enter to exit...")
