import streamlit as st
import sqlite3
import bcrypt
from auth.jwt_handler import generate_token, decode_token
from admin.admin_dashboard import admin_dashboard
from database.db_setup import init_db
from crud import create_user, read_users, update_user, delete_user

# Inicializar la base de datos
init_db()

def login():
    col1, col2 = st.columns([1,2])

    with col1:
        st.image('MHC_logo.png', width= 200)
    with col2:
        st.header('Bienvenido/a a la plataforma MHC')
    st.text('Introduzca sus datos para comenzar a interactuar con la plataforma, por favor.')
    username = st.text_input('Nombre de usuario')
    password = st.text_input('Contraseña', type='password')
    
    if st.button('Ingreso'):
        conn = sqlite3.connect('hospital.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
            token = generate_token(user[0], user[3])  # Genera el token JWT con user_id y role
            st.session_state['token'] = token
            st.session_state['role_name'] = user[3]  # Guarda el nombre del rol en la sesión
            st.success('Ingreso exitoso')
            st.experimental_rerun()
        else:
            st.error('Usuario o contraseña incorrectos')
        
        conn.close()

    # Botón de logout para iniciar el proceso de login de nuevo
    if st.button('Salir'):
        st.session_state.clear()  # Limpiar la sesión
        st.experimental_rerun()

        
def main():
    if 'token' not in st.session_state:
        login()
    else:
        payload = decode_token(st.session_state['token'])
        if payload:
            role_name = st.session_state['role_name']  # Obtener el nombre del rol desde la sesión
            st.sidebar.image('MHC_logo.png', width=150)
            st.sidebar.success(f'Ingreso como {role_name}')
            
            # Botón para cambiar de usuario
            
            if st.sidebar.button('Cambio usuario', key='switch_user_button'):
                st.session_state.clear()  # Limpiar la sesión
                st.experimental_rerun()
            
            # Mostrar dashboard según el rol
            if role_name == 'admin':
                admin_dashboard()
            elif role_name == 'TIC':
                st.write('Panel TIC')
            elif role_name == 'Enfermera de hospitalizacion':
                st.write('Panel Enfermera de hospitalizacion')
            elif role_name == 'Medico General':
                st.write('Panel Medico General')
            elif role_name == 'Admisionista':
                st.write('Panel Admisionista')
            elif role_name == 'Enfermera UCI':
                st.write('Panel Enfermera UCI')
            elif role_name == 'Cajero':
                st.write('Panel Cajero')
            elif role_name == 'Médico emergenciólogo':
                st.write('Panel Médico emergenciólogo ')
            elif role_name == 'Enfermera emergencia':
                st.write('Panel Enfermera emergencia')
            elif role_name == 'Anestesiólogo':
                st.write('Panel Anestesiólogo')
            elif role_name == 'Paciente':
                st.write('Panel Paciente')
            elif role_name == 'Médico especialista':
                st.write('Panel Médico especialista')
            elif role_name == 'Enfermera quirófano':
                st.write('Panel Enfermera quirófano')
            elif role_name == 'Médico cirujano':
                st.write('Panel Médico cirujano')
            elif role_name == 'Jefe enfermería':
                st.write('Panel Jefe enfermería')
            elif role_name == 'Enfermera postoperatorio':
                st.write('Panel Enfermera postoperatorio')
            elif role_name == 'Enfermera circulante':
                st.write('Panel Enfermera circulante')
            elif role_name == 'Prestador de servicios de farmacia':
                st.write('Panel Prestador de servicios de farmacia')
            elif role_name == 'Administrativo':
                st.write('Panel Administrativo')
            elif role_name == 'Contable':
                st.write('Panel Contable')
            elif role_name == 'Auditor':
                st.write('Panel Auditor')
           
                        
            # Agrega más roles y dashboards según sea necesario
        else:
            st.error('Sesión finalizada, por favor ingrese de nuevo')
            login()

if __name__ == '__main__':
    main()

