import firebase_admin
from firebase_admin import credentials, auth

# Inisialisasi Firebase Admin
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Verifikasi token ID dari Firebase
def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        print(f"Error: {e}")
        return None
