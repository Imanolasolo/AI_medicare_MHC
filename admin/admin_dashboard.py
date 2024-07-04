import streamlit as st
from crud import create_user, read_users, update_user, delete_user
from crud import create_role, read_roles, update_role, delete_role

def admin_dashboard():
    st.sidebar.title("Panel de Administrador")

    st.sidebar.header("Manejo de usuarios")
    user_task = st.sidebar.selectbox("Seleccione tarea de usuario", ["Crear usuario", "Lista de usuarios", "Editar usuario", "Borrar usuario"])

    st.sidebar.header("Manejo Roles")
    role_task = st.sidebar.selectbox("Seleccione atrea de rol", ["Crear Rol", "Lista de roles", "Editar rol", "Borrar rol"])

    st.sidebar.write("---")

    if user_task == "Crear usuario":
        create_user_page()
    elif user_task == "Lista de usuarios":
        read_users_page()
    elif user_task == "Editar usuario":
        update_user_page()
    elif user_task == "Borrar usuario":
        delete_user_page()

    if role_task == "Crear Rol":
        create_role_page()
    elif role_task == "Lista de roles":
        read_roles_page()
    elif role_task == "Editar rol":
        update_role_page()
    elif role_task == "Borrar rol":
        delete_role_page()

#if st.sidebar.button("Switch User"):
        #st.experimental_rerun()  # Reiniciar la app para volver a la página de login

import streamlit as st
from crud import read_roles, create_user

def create_user_page():
    st.title("Crear Usuario")
    username = st.text_input("Nombre de usuario", key="create_user_username")
    password = st.text_input("Contraseña", type="password", key="create_user_password")
    roles = read_roles()  # Obtener la lista de roles actualizados
    role_names = [role[1] for role in roles]  # Obtener nombres de roles (suponiendo que el nombre está en la posición 1)
    role = st.selectbox("Role", role_names, key="create_user_role")  # Mostrar nombres de roles en el selector
    selected_role_id = roles[role_names.index(role)][0]  # Obtener ID del rol seleccionado por su nombre
    if st.button("Crear", key="create_user_button"):
        if create_user(username, password, selected_role_id):  # Pasar el ID del rol seleccionado
            st.success("Usuario creado exitosamente")
        else:
            st.error("Usuario ya existe")


def read_users_page():
    st.title("Usuarios")
    users = read_users()
    for user in users:
        st.write(f"ID: {user[0]}, Username: {user[1]}, Role: {user[2]}")

def update_user_page():
    st.title("Editar usuario")
    user_id = st.text_input("ID usuario", key="update_user_id")
    username = st.text_input("Nombre de usuario", key="update_user_username")
    password = st.text_input("Contraseña", type="password", key="update_user_password")
    role = st.selectbox("Role", ["admin", "doctor", "nurse"], key="update_user_role")  # Agrega más roles según sea necesario
    if st.button("Editar", key="update_user_button"):
        update_user(user_id, username, password, role)
        st.success("Usuario editado exitosamente")

def delete_user_page():
    st.title("Borrar usuario")
    user_id = st.text_input("ID usuario", key="delete_user_id")
    if st.button("Borrar", key="delete_user_button"):
        delete_user(user_id)
        st.success("Usuario borrado exitosamente")

def create_role_page():
    st.title("Crear Rol")
    role_name = st.text_input("Nombre rol", key="create_role_name")
    permissions = st.text_area("Permisos (separados por coma)", key="create_role_permissions")
    if st.button("Crear", key="create_role_button"):
        if create_role(role_name, permissions):
            st.success("Rol creado exitosamente")
        else:
            st.error("El rol ya existe")

def read_roles_page():
    st.title("Lista de roles")
    roles = read_roles()
    for role in roles:
        st.write(f"ID: {role[0]}, Role Name: {role[1]}, Permissions: {role[2]}")

def update_role_page():
    st.title("Editar Rol")
    role_id = st.text_input("ID de Role ", key="update_role_id")
    role_name = st.text_input("Nombre de role", key="update_role_name")
    permissions = st.text_area("Permisos (separados po coma)", key="update_role_permissions")
    if st.button("Editar", key="update_role_button"):
        update_role(role_id, role_name, permissions)
        st.success("Rol editado exitosamente")

def delete_role_page():
    st.title("Borrar Rol")
    role_id = st.text_input("ID de rol", key="delete_role_id")
    if st.button("Borrar", key="delete_role_button"):
        delete_role(role_id)
        st.success("Rol borrado exitosamente")

