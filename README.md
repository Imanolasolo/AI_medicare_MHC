### README.md

# MHC_Streamlit_Software

## Descripción

MHC_Streamlit_Software es una aplicación desarrollada para el Manta Hospital Center. Esta aplicación facilita la gestión de usuarios, roles y diferentes módulos específicos del hospital, permitiendo a los administradores y otros roles del hospital interactuar de manera eficiente con el sistema. La aplicación está desarrollada utilizando Streamlit como frontend y SQLite como base de datos, implementando autenticación y autorización mediante JWT.

## Características

- **Autenticación y Autorización**: Gestión de acceso mediante JWT.
- **Roles y Permisos**: Gestión de usuarios y roles con diferentes permisos.
- **Interfaz Amigable**: Interfaz de usuario intuitiva y fácil de usar con Streamlit.
- **Base de Datos**: Uso de SQLite para la gestión de datos.
- **Panel de Administración**: Herramientas y paneles para la gestión de usuarios y roles.
- **Funciones Especializadas por Rol**: Acceso a diferentes módulos y paneles según el rol del usuario.

## Estructura del Proyecto

```
MHC_Streamlit_Software
│   ├── app.py
│   ├── crud.py
│   ├── hospital.db
│   ├── MHC_logo.png
│   ├── README.md
│   ├── requirements.txt
│   ├── admin
│   │   ├── admin_dashboard.py
│   │   └── __init__.py
│   ├── Administrativo
│   │   ├── Administrativo_dashboard.py
│   │   └── __init__.py
│   ├── Admisionista
│   │   ├── Admisionista_dashboard.py
│   │   └── __init__.py
│   ├── Anestesiólogo
│   │   ├── Anestesiologo_dashboard.py
│   │   └── __init__.py
│   ├── Auditor
│   │   ├── Auditor_dashboard.py
│   │   └── __init__.py
│   ├── auth
│   │   ├── jwt_handler.py
│   │   └── __init__.py
│   ├── Cajero
│   │   ├── Cajero_dashboard.py
│   │   └── __init__.py
│   ├── Contable
│   │   ├── Contable_dashboard.py
│   │   └── __init__.py
│   ├── database
│   │   ├── db_setup.py
│   │   ├── hospital.db
│   │   └── __init__.py
│   ├── Enfermera_circulante
│   │   ├── Enfermera_circulante_dashboard.py
│   │   └── __init__.py
│   ├── Enfermera_postoperatorio
│   │   ├── Enfermera_postoperatorio_dashboard.py
│   │   └── __init__.py
│   ├── Enfermera_quirofano
│   │   ├── Enfermeria_quirofano_dashboard.py
│   │   └── __init__.py
│   ├── Enfermeria_emergencias
│   │   ├── Enfermeria_emergencias_dashboard.py
│   │   └── __init__.py
│   ├── Enfermeria_hospitalizacion
│   │   ├── Enfermeria_hospitalizacion_dashboard.py
│   │   └── __init__.py
│   ├── Enfermeria_UCI
│   │   ├── Enfermeria_UCI_dashboard.py
│   │   └── __init__.py
│   ├── Jefe_enfermeria
│   │   ├── Jefe_enfermería_dashboard.py
│   │   └── __init__.py
│   ├── Medico_cirujano
│   │   ├── Medico_cirujano_dashboard.py
│   │   └── __init__.py
│   ├── Medico_emergencias
│   │   ├── Medico_emergencias_dashboard.py
│   │   └── __init__.py
│   ├── Medico_especialista
│   │   ├── Medico_especialista_dashboard.py
│   │   └── __init__.py
│   ├── Medico_general
│   │   ├── Medico_general_dashboard.py
│   │   └── __init__.py
│   ├── Paciente
│   │   ├── Paciente_dashboard.py
│   │   └── __init__.py
│   ├── Prestador_de_servicios_de_farmacia
│   │   ├── Prestador_servicios_farmacia_dashboard.py
│   │   └── __init__.py
│   ├── TIC
│   │   ├── TIC_dashboard.py
│   │   └── __init__.py
│   ├── utils
│   │   ├── check_schema.py
│   │   ├── clear_users.db.py
│   │   ├── hash_password.py
│   │   ├── modify_user.py
└─── __pycache__
```

## Descripción de Archivos y Directorios

- **app.py**: Archivo principal de la aplicación Streamlit.
- **crud.py**: Funciones CRUD para manejar usuarios y roles.
- **hospital.db**: Base de datos SQLite que almacena la información.
- **MHC_logo.png**: Logo del Manta Hospital Center.
- **README.md**: Este archivo.
- **requirements.txt**: Archivo con las dependencias del proyecto.

### Directorios por Roles

Cada directorio corresponde a un rol específico dentro del hospital y contiene su propio panel de control (`dashboard`) y un archivo de inicialización (`__init__.py`):

- **admin**: Panel de administrador.
- **Administrativo**: Panel del personal administrativo.
- **Admisionista**: Panel del personal de admisión.
- **Anestesiólogo**: Panel de anestesiólogos.
- **Auditor**: Panel de auditores.
- **auth**: Manejo de autenticación con JWT.
- **Cajero**: Panel de cajeros.
- **Contable**: Panel de contables.
- **database**: Configuración y manejo de la base de datos.
- **Enfermera_circulante**: Panel de enfermeras circulantes.
- **Enfermera_postoperatorio**: Panel de enfermeras de postoperatorio.
- **Enfermera_quirofano**: Panel de enfermeras de quirófano.
- **Enfermeria_emergencias**: Panel de enfermeras de emergencias.
- **Enfermeria_hospitalizacion**: Panel de enfermeras de hospitalización.
- **Enfermeria_UCI**: Panel de enfermeras de UCI.
- **Jefe_enfermeria**: Panel del jefe de enfermería.
- **Medico_cirujano**: Panel de médicos cirujanos.
- **Medico_emergencias**: Panel de médicos de emergencias.
- **Medico_especialista**: Panel de médicos especialistas.
- **Medico_general**: Panel de médicos generales.
- **Paciente**: Panel de pacientes.
- **Prestador_de_servicios_de_farmacia**: Panel de prestadores de servicios de farmacia.
- **TIC**: Panel del responsable de tecnologías de la información y comunicación.
- **utils**: Scripts utilitarios.

## Instalación

1. Clonar el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/MHC_Streamlit_Software.git
   ```

2. Navegar al directorio del proyecto:
   ```sh
   cd MHC_Streamlit_Software
   ```

3. Crear un entorno virtual:
   ```sh
   python -m venv env
   ```

4. Activar el entorno virtual:
   - En Windows:
     ```sh
     .\env\Scripts\activate
     ```
   - En macOS/Linux:
     ```sh
     source env/bin/activate
     ```

5. Instalar las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

6. Ejecutar la aplicación:
   ```sh
   streamlit run app.py
   ```

## Uso

1. Abrir el navegador web e ir a la dirección `http://localhost:8501` para ver la aplicación en funcionamiento.
2. Iniciar sesión con las credenciales adecuadas para acceder al panel correspondiente según el rol del usuario.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para mejoras o correcciones.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
```

Este archivo README proporciona una visión general del proyecto, instrucciones de instalación, y una guía de uso, que debería ayudarte a empezar rápidamente con el desarrollo y uso del software.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/MHC_Streamlit_Software.git
    cd MHC_Streamlit_Software
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # En Windows
    source venv/bin/activate  # En MacOS/Linux
    ```

3. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

4. Inicializa la base de datos:
    ```bash
    python database/db_setup.py
    ```

## Uso

1. Inicia la aplicación Streamlit:
    ```bash
    streamlit run app.py
    ```

2. Abre tu navegador web y ve a `http://localhost:8501`.

3. Inicia sesión con las credenciales del administrador por defecto:
    - **Usuario**: `admin`
    - **Contraseña**: `Ilargietaeguzki1`

4. Desde el panel de administrador, puedes gestionar usuarios, roles y otros módulos específicos del hospital.

## Funcionalidades del Proyecto

### Panel de Administración

- **Crear Usuario**: Formulario para agregar nuevos usuarios al sistema.
- **Lista de Usuarios**: Visualización de usuarios existentes en formato de tabla.
- **Editar Usuario**: Formulario para editar información de usuarios existentes.
- **Borrar Usuario**: Opción para eliminar usuarios del sistema.

### Manejo de Roles

- **Crear Rol**: Formulario para agregar nuevos roles al sistema.
- **Lista de Roles**: Visualización de roles existentes en formato de tabla.
- **Editar Rol**: Formulario para editar información de roles existentes.
- **Borrar Rol**: Opción para eliminar roles del sistema.

### Funciones Específicas por Rol

#### Administrador
- Gestión completa de usuarios y roles.
- Acceso a todos los módulos del sistema.

#### Responsable de TIC
- Gestión y supervisión de tecnología e información hospitalaria.
- Paneles de monitoreo y estadísticas de sistemas informáticos.
- Herramientas de seguridad informática y gestión de acceso.

#### Otros Roles
- Acceso a módulos específicos según el rol asignado.

## Contribución

Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva funcionalidad (`git checkout -b nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin nueva-funcionalidad`).
5. Abre un Pull Request.

## Soporte

Si tienes alguna pregunta o necesitas ayuda, por favor, abre un issue en el repositorio o contacta con el soporte a través de [aquí](https://wa.me/5930993513082?text=Solicito%20ayuda%20con%20la%20app%20MHC).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

---

¡Gracias por usar MHC_Streamlit_Software!