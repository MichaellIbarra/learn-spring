# Introducción a Keycloak
- Keycloak es una solución de código abierto para la gestión de identidad y acceso. Proporciona autenticación y autorización para aplicaciones y servicios, permitiendo a los desarrolladores centrarse en la lógica de negocio sin preocuparse por la seguridad.


## configuraciones en Keycloak
- realm -> Un realm es un espacio de nombres que agrupa usuarios, roles, clientes y configuraciones. Permite gestionar la autenticación y autorización de manera aislada para diferentes aplicaciones o grupos de usuarios.
    ### Realm Settings
    - General: Aquí se configuran las opciones generales del realm, como el nombre, la descripción y el estado del realm (activo o inactivo).
    - Login: Configura las opciones de inicio de sesión, como el nombre del formulario de inicio de sesión y las políticas de contraseña.
    - Themes: Permite personalizar la apariencia del formulario de inicio de sesión y otros elementos visuales del realm.
    - Tokens: Configura la duración de los tokens de acceso, actualización y otros parámetros relacionados con la seguridad.
- General Settings -> Aquí se configuran el tipo de cliente y las opciones de seguridad del realm.
    ### Client Settings
    - Client Type: OpenID Connect (OIDC) es el tipo de cliente más común utilizado en Keycloak. Permite la autenticación y autorización de aplicaciones web y móviles, SAML es otro tipo de cliente utilizado principalmente para aplicaciones empresariales y federación de identidades.
    - Client ID: Es un identificador único para el cliente dentro del realm. Se utiliza para identificar la aplicación que está solicitando autenticación.

- clients -> Un cliente en Keycloak representa una aplicación o servicio que necesita autenticación y autorización. Los clientes pueden ser aplicaciones web, móviles, servicios backend, etc.
    ### Capability Config
    - Client Authentication: Configura cómo los cliente se autentican ante Keycloak. Puede ser mediante un secreto compartido, certificados o sin autenticación.
    - Authorization: Permite a los clientes solicitar permisos específicos para acceder a recursos protegidos. Esto es útil para aplicaciones que necesitan acceder a APIs o servicios protegidos.
    - Standard Flow: Este es el flujo de autenticación predeterminado que utiliza Keycloak. Permite a los usuarios iniciar sesión mediante un formulario de inicio de sesión.
    - Direct Access Grants: Permite a las aplicaciones obtener tokens de acceso directamente, sin necesidad de un navegador.
    - Implicit Flow: Este flujo es utilizado principalmente por aplicaciones de una sola página (SPA) que necesitan obtener tokens de acceso sin redirigir al usuario a un formulario de inicio de sesión.
    - Service Accounts Roles: Permite a los clientes tener cuentas de servicio que pueden ser utilizadas para acceder a recursos protegidos sin necesidad de un usuario humano.
- login settings -> Aquí se configura direccionamiento de los usuarios después de iniciar sesión, el tiempo de espera de la sesión y otras opciones relacionadas con la experiencia del usuario.
    ### URL de redirección
    - Root URL: La URL a la que se redirigirá a los usuarios después de iniciar sesión.
    - Home URL: La URL que se utilizará como página de inicio después de que el usuario inicie sesión.
    - Valid Redirect URIs: Las URL a las que se permite redirigir después de la autenticación. Esto es importante para evitar ataques de redirección maliciosos.
    - Valid Post Logout Redirect URIs: Las URL a las que se permite redirigir después de que el usuario cierre sesión. Esto asegura que los usuarios sean redirigidos a un lugar seguro después de la autenticación.
    - Web Origins: Las URL de origen web que se permiten para solicitudes CORS (Cross-Origin Resource Sharing) es decir, las URL desde las que se permiten solicitudes a Keycloak. Esto es importante para aplicaciones que se ejecutan en diferentes dominios y necesitan interactuar con Keycloak.


curl http://144.126.140.79:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "quien es el presidente del Perú?",
  "stream": false,
  "context": [],
  "options": {
    "num_predict": 80,
    "temperature": 0.1,
    "top_p": 0.5,
    "top_k": 5,
    "repeat_penalty": 1.05,
    "num_ctx": 512,
    "num_batch": 64,
    "num_thread": 4
  }
}'