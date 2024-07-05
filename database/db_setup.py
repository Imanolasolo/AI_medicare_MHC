import sys
import os
import sqlite3
import bcrypt

# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crud import generate_token  # Importar generate_token desde crud.py

def init_db():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            dni TEXT NOT NULL,  -- Nueva columna para DNI
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS roles (
            id INTEGER PRIMARY KEY,
            role_name TEXT UNIQUE NOT NULL,
            permissions TEXT NOT NULL
        )
    ''')

    # Crear usuario administrador por defecto
    admin_username = 'admin'
    admin_password = 'Ilargietaeguzki1'  # Contraseña inicial
    admin_role = 'admin'

    # Comprobar si el usuario administrador ya existe
    c.execute('SELECT * FROM users WHERE username = ?', (admin_username,))
    if not c.fetchone():
        hashed_password = bcrypt.hashpw(admin_password.encode('utf-8'), bcrypt.gensalt())
        admin_id = generate_token(admin_username, admin_role)  # Usar el nombre de usuario para generar el token
        c.execute('INSERT INTO users (id, dni, username, password, role) VALUES (?, ?, ?, ?, ?)', 
                  (admin_id, 'admin_dni', admin_username, hashed_password.decode('utf-8'), admin_role))
        print("Usuario administrador creado con éxito.")
    else:
        print("Usuario administrador ya existe.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
