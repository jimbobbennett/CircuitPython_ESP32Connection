import secrets
from esp32connection import Connection

# Create the connection
connection = Connection()

# secrets must be a dictionary containing two values:
# ssid - the ssid of the WiFi to connect to
# password - the password of the WiFi to connect to
connection.connect(secrets)
