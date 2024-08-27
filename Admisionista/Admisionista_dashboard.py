import streamlit as st
import pandas as pd
from Admisionista.admisionista_crud import create_patient, read_patients, update_patient, delete_patient, create_companion, read_companions, update_companion, delete_companion

def manage_patients():
    st.title("Gestión de Pacientes")
    
    option = st.selectbox("Seleccionar una opción", ["Crear", "Leer", "Actualizar", "Eliminar"])
    
    if option == "Crear":
        st.subheader("Crear Paciente")
        data = {
            'primer_apellido': st.text_input("Primer Apellido"),
            'segundo_apellido': st.text_input("Segundo Apellido"),
            'primer_nombre': st.text_input("Primer Nombre"),
            'segundo_nombre': st.text_input("Segundo Nombre"),
            'tipo_documento_identificacion': st.selectbox("Tipo de Documento de Identificación", ['cédula de ciudadanía', 'cédula de identidad', 'pasaporte', 'carnet de refugiado', 'S/D']),
            'estado_civil': st.text_input("Estado Civil"),
            'sexo': st.selectbox("Sexo", ['Masculino', 'Femenino']),
            'telefono_fijo': st.text_input("Teléfono Fijo"),
            'telefono_celular': st.text_input("Teléfono Celular"),
            'correo_electronico': st.text_input("Correo Electrónico"),
            'lugar_nacimiento': st.text_input("Lugar de Nacimiento"),
            'nacionalidad': st.text_input("Nacionalidad"),
            'edad': st.number_input("Edad", min_value=0),
            'condicion_edad': st.selectbox("Condición Edad", ['H', 'D', 'M', 'A']),
            'autocertificacion_etnica': st.text_input("Autocertificación Étnica"),
            'nacionalidad_etnica': st.text_input("Nacionalidad Étnica"),
            'pueblos': st.text_input("Pueblos"),
            'nivel_educacion': st.text_input("Nivel de Educación"),
            'estado_nivel_educacion': st.text_input("Estado Nivel de Educación"),
            'ocupacion': st.text_input("Ocupación"),
            'tipo_empresa_trabajo': st.text_input("Tipo de Empresa de Trabajo"),
            'seguro_salud_principal': st.text_input("Seguro de Salud Principal"),
            'tipo_bono_recibe': st.text_input("Tipo de Bono que Recibe"),
            'provincia': st.text_input("Provincia"),
            'canton': st.text_input("Cantón"),
            'parroquia': st.text_input("Parroquia"),
            'barrio_sector': st.text_input("Barrio o Sector"),
            'calle_principal': st.text_input("Calle Principal"),
            'calle_secundaria': st.text_input("Calle Secundaria"),
            'referencia': st.text_input("Referencia")
        }
        if st.button("Crear Paciente"):
            create_patient(tuple(data.values()))
            st.success("Paciente creado con éxito")

    elif option == "Leer":
        st.subheader("Leer Pacientes")
        patients = read_patients()
        if patients:
            # Convertir los datos de pacientes a un DataFrame
            df_patients = pd.DataFrame(patients, columns=[
                'ID', 'Primer Apellido', 'Segundo Apellido', 'Primer Nombre', 'Segundo Nombre',
                'Tipo Documento Identificación', 'Estado Civil', 'Sexo', 'Teléfono Fijo', 'Teléfono Celular',
                'Correo Electrónico', 'Lugar de Nacimiento', 'Nacionalidad', 'Edad', 'Condición Edad',
                'Autocertificación Étnica', 'Nacionalidad Étnica', 'Pueblos', 'Nivel de Educación',
                'Estado Nivel de Educación', 'Ocupación', 'Tipo de Empresa de Trabajo', 'Seguro de Salud Principal',
                'Tipo de Bono que Recibe', 'Provincia', 'Cantón', 'Parroquia', 'Barrio o Sector',
                'Calle Principal', 'Calle Secundaria', 'Referencia'
            ])
            st.dataframe(df_patients)
        else:
            st.write("No hay pacientes registrados.")

    elif option == "Actualizar":
        st.subheader("Actualizar Paciente")
        patient_id = st.number_input("ID del Paciente", min_value=1)
        patient_data = next((p for p in read_patients() if p[0] == patient_id), None)
        if patient_data:
            data = {
                'primer_apellido': st.text_input("Primer Apellido", value=patient_data[1]),
                'segundo_apellido': st.text_input("Segundo Apellido", value=patient_data[2]),
                'primer_nombre': st.text_input("Primer Nombre", value=patient_data[3]),
                'segundo_nombre': st.text_input("Segundo Nombre", value=patient_data[4]),
                'tipo_documento_identificacion': st.selectbox("Tipo de Documento de Identificación", ['cédula de ciudadanía', 'cédula de identidad', 'pasaporte', 'carnet de refugiado', 'S/D'], index=['cédula de ciudadanía', 'cédula de identidad', 'pasaporte', 'carnet de refugiado', 'S/D'].index(patient_data[5])),
                'estado_civil': st.text_input("Estado Civil", value=patient_data[6]),
                'sexo': st.selectbox("Sexo", ['Masculino', 'Femenino'], index=['Masculino', 'Femenino'].index(patient_data[7])),
                'telefono_fijo': st.text_input("Teléfono Fijo", value=patient_data[8]),
                'telefono_celular': st.text_input("Teléfono Celular", value=patient_data[9]),
                'correo_electronico': st.text_input("Correo Electrónico", value=patient_data[10]),
                'lugar_nacimiento': st.text_input("Lugar de Nacimiento", value=patient_data[11]),
                'nacionalidad': st.text_input("Nacionalidad", value=patient_data[12]),
                'edad': st.number_input("Edad", min_value=0, value=patient_data[13]),
                'condicion_edad': st.selectbox("Condición Edad", ['H', 'D', 'M', 'A'], index=['H', 'D', 'M', 'A'].index(patient_data[14])),
                'autocertificacion_etnica': st.text_input("Autocertificación Étnica", value=patient_data[15]),
                'nacionalidad_etnica': st.text_input("Nacionalidad Étnica", value=patient_data[16]),
                'pueblos': st.text_input("Pueblos", value=patient_data[17]),
                'nivel_educacion': st.text_input("Nivel de Educación", value=patient_data[18]),
                'estado_nivel_educacion': st.text_input("Estado Nivel de Educación", value=patient_data[19]),
                'ocupacion': st.text_input("Ocupación", value=patient_data[20]),
                'tipo_empresa_trabajo': st.text_input("Tipo de Empresa de Trabajo", value=patient_data[21]),
                'seguro_salud_principal': st.text_input("Seguro de Salud Principal", value=patient_data[22]),
                'tipo_bono_recibe': st.text_input("Tipo de Bono que Recibe", value=patient_data[23]),
                'provincia': st.text_input("Provincia", value=patient_data[24]),
                'canton': st.text_input("Cantón", value=patient_data[25]),
                'parroquia': st.text_input("Parroquia", value=patient_data[26]),
                'barrio_sector': st.text_input("Barrio o Sector", value=patient_data[27]),
                'calle_principal': st.text_input("Calle Principal", value=patient_data[28]),
                'calle_secundaria': st.text_input("Calle Secundaria", value=patient_data[29]),
                'referencia': st.text_input("Referencia", value=patient_data[30])
            }
            if st.button("Actualizar Paciente"):
                update_patient(patient_id, tuple(data.values()))
                st.success("Paciente actualizado con éxito")

    elif option == "Eliminar":
        st.subheader("Eliminar Paciente")
        patient_id = st.number_input("ID del Paciente", min_value=1)
        if st.button("Eliminar Paciente"):
            delete_patient(patient_id)
            st.success("Paciente eliminado con éxito")

def manage_companions():
    st.title("Gestión de Acompañantes")
    
    option = st.selectbox("Seleccionar una opción", ["Crear", "Leer", "Actualizar", "Eliminar"])
    
    if option == "Crear":
        st.subheader("Crear Acompañante")
        data = {
            'en_caso_necesario_llamar_a': st.text_input("En caso necesario llamar a"),
            'parentesco': st.text_input("Parentesco"),
            'direccion': st.text_input("Dirección"),
            'telefono_acompanante': st.text_input("Teléfono Acompañante"),
            'nombre_apellido_representante': st.text_input("Nombre y Apellido del Representante"),
            'identificacion_representante': st.text_input("Número de Identificación del Representante"),
            'telefono_representante': st.text_input("Teléfono del Representante")
        }
        if st.button("Crear Acompañante"):
            create_companion(tuple(data.values()))
            st.success("Acompañante creado con éxito")

    elif option == "Leer":
        st.subheader("Leer Acompañantes")
        companions = read_companions()
        if companions:
            # Convertir los datos de acompañantes a un DataFrame
            df_companions = pd.DataFrame(companions, columns=[
                'ID', 'En caso necesario llamar a', 'Parentesco', 'Dirección', 'Teléfono Acompañante',
                'Nombre y Apellido del Representante', 'Número de Identificación del Representante',
                'Teléfono del Representante'
            ])
            st.dataframe(df_companions)
        else:
            st.write("No hay acompañantes registrados.")

    elif option == "Actualizar":
        st.subheader("Actualizar Acompañante")
        companion_id = st.number_input("ID del Acompañante", min_value=1)
        companion_data = next((c for c in read_companions() if c[0] == companion_id), None)
        if companion_data:
            data = {
                'en_caso_necesario_llamar_a': st.text_input("En caso necesario llamar a", value=companion_data[1]),
                'parentesco': st.text_input("Parentesco", value=companion_data[2]),
                'direccion': st.text_input("Dirección", value=companion_data[3]),
                'telefono_acompanante': st.text_input("Teléfono Acompañante", value=companion_data[4]),
                'nombre_apellido_representante': st.text_input("Nombre y Apellido del Representante", value=companion_data[5]),
                'identificacion_representante': st.text_input("Número de Identificación del Representante", value=companion_data[6]),
                'telefono_representante': st.text_input("Teléfono del Representante", value=companion_data[7])
            }
            if st.button("Actualizar Acompañante"):
                update_companion(companion_id, tuple(data.values()))
                st.success("Acompañante actualizado con éxito")

    elif option == "Eliminar":
        st.subheader("Eliminar Acompañante")
        companion_id = st.number_input("ID del Acompañante", min_value=1)
        if st.button("Eliminar Acompañante"):
            delete_companion(companion_id)
            st.success("Acompañante eliminado con éxito")

def admisionista_dashboard():
    st.sidebar.title("Panel de Admisión")
    option = st.sidebar.selectbox("Seleccionar un módulo", ["Gestión de Pacientes", "Gestión de Acompañantes"])
    
    if option == "Gestión de Pacientes":
        manage_patients()
    elif option == "Gestión de Acompañantes":
        manage_companions()
