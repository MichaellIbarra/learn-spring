# Introducción Jenkins para Integración Continua y Entrega Continua (CI/CD)
- Jenkins es una herramienta de automatización de código abierto que facilita la integración continua (CI) y la entrega continua (CD) en el desarrollo de software. Permite a los desarrolladores automatizar la construcción, prueba y despliegue de aplicaciones, mejorando la eficiencia y reduciendo errores humanos, lo que resulta en un ciclo de desarrollo más rápido y confiable, es una aplicación basada en servidor y requiere un servidor web como Apache Tomcat para ejecutarse. Viendo el seguimiento de tareas repetidas que surgen durante el desarrollo de un proyecto de software.

## Ventajas de usar Jenkins para CI/CD
- Automatización: Jenkins automatiza tareas repetitivas como la construcción, prueba y despliegue de aplicaciones.
- Integración con múltiples herramientas: Jenkins se integra con una amplia variedad de herramientas y tecnologías, lo que facilita su adopción en diferentes entornos de desarrollo.
- Flexibilidad: Jenkins es altamente configurable y extensible mediante plugins, lo que permite adaptarlo a las necesidades específicas de cada proyecto.
- Comunidad activa: Al ser una herramienta de código abierto, Jenkins cuenta con una comunidad activa que contribuye con plugins, soporte y mejoras continuas.


## Integración continua (CI)
- Nace por problemas en el desarrollo de software donde los desarrolladores integran su código con frecuencia, lo que puede causar conflictos y errores si no se gestionan adecuadamente, En práctica de desarrollo que require a los desarrolladores integrar el código en el que trabajan, actualizan y modifican a un repositorio comaprtido, varias veces al día.
- Jenkins automatiza la integración del código, ejecutando pruebas y validaciones cada vez que se

## Despliegue Continuo (CD)
- Es la práctica de liberar y entregar cada build o compilación que pasa las pruebas automatizadas a un entorno de producción o pre-producción.
- Jenkins facilita el despliegue continuo al automatizar el proceso de entrega de aplicaciones, asegurando que las versiones estables del software estén disponibles para los usuarios finales de manera rápida y confiable.

## Etapa de Integración Continua
- **Automatización del proceso de build o compilación**: Jenkins puede automatizar la construcción del código fuente en artefactos ejecutables, para asegurar que el código se compile correctamente.
- **Ejecución de pruebas automatizadas**: Jenkins puede ejecutar pruebas unitarias, de integración y funcionales automáticamente para validar la calidad del código.
- **Mantener un solo source repository**: Jenkins fomenta el uso de un único repositorio de código fuente para evitar conflictos y facilitar la gestión del código. se realiza un cambio, lo que ayuda a identificar y resolver problemas de manera temprana.
- **No complicar las cosas**: Como desarrolladores deben evitar hacer cambios demasiado complejos o grandes en una sola integración, para minimizar el riesgo de conflictos y errores.
- **La visibilidad de qué está pasando**: Jenkins proporciona informes y dashboards que permiten a los desarrolladores y equipos de proyecto tener visibilidad sobre el estado de las integraciones, pruebas y despliegues.
- **Despliegue automático**: Jenkins puede automatizar el despliegue de aplicaciones en entornos de desarrollo, pruebas o producción, facilitando la entrega continua.

## Para lograr una integración continua exitosa con Jenkins, es importante seguir buenas prácticas como:
- 1. Los desarrolladores deben trabajar en su propio espacio de trabajo o rama, y realizar integraciones frecuentes con el repositorio compartido.
- 2. Cuando finalizan o realizar algún cambio significativo, deben confirmar los cambios en el repositorio.
- 3. Deben configurar el server CI que se va a encargar de controlar el repositorio y chequear los cambios cuando estos ocurran.
- 4. Configurar el server CI para que compile o realice el "build" del proyecto y que ejecute las pruebas unitarias llamadas en ingles unit and integration tests.
- 5. El server CI se encarga de desplegar los artefactos para que la prueba, en ingles conocido como deployable artifacts.
- 6. El server CI asigna un build label, o número de compilación a la versión ejecutable que se acaba de realizar.
- 7. El server CI notifica a los desarrolladores sobre el estado de la integración, ya sea éxito o fallo, para que puedan tomar las acciones necesarias. realizan cambios en el código, lo que ayuda a identificar y resolver problemas de manera temprana.
- 8. El equipo de encarga de encontrar y arreglar el problema en una etapa inicial y antees que sea tarde.

# Inicializar jenkins con docker compose
```
docker compose up -d
docker exec -it jenkins bash
```

# Arquitectura de Jenkins
- Jenkins sigue una arquitectura maestro-agente, donde el servidor maestro gestiona la configuración, los trabajos y la coordinación de los agentes que ejecutan las tareas asignadas. Esta arquitectura permite distribuir la carga de trabajo y mejorar la escalabilidad del sistema.
- El servidor maestro es responsable de gestionar la interfaz web, almacenar la configuración y coordinar la ejecución de trabajos. Los agentes son nodos remotos que ejecutan las tareas asignadas por el maestro, permitiendo distribuir la carga de trabajo y mejorar la eficiencia del proceso de CI/CD.

## Términos comunes
- Merge Conflict: Ocurre cuando dos desarrolladores han realizado cambios en la misma parte del código y Jenkins no puede fusionarlos automáticamente. intentan integrar su código.
- Build: Proceso de compilar y ensamblar el código
- Merge Hell: Situación en la que los desarrolladores enfrentan múltiples conflictos de fusión debido a integraciones frecuentes y cambios simultáneos en el código.
- Pipeline: Secuencia de pasos automatizados que definen el proceso de construcción, prueba y despliegue de una aplicación en Jenkins. realiza una integración, lo que ayuda a identificar y resolver problemas de manera temprana.
- Self-hosted: Jenkins puede ser instalado y ejecutado en servidores propios, lo que permite un mayor control y personalización del entorno de CI/CD.
- On premise: Jenkins puede ser desplegado en infraestructuras locales, lo que es ideal para organizaciones que requieren cumplir con políticas de seguridad y privacidad estrictas. realizan cambios en el código, lo que ayuda a identificar y resolver problemas de manera temprana.
- jenkins job: tareas ejecutables que son supervisadas y controladas por Jenkins para automatizar procesos de desarrollo de software.
- jenkins agent: componente de Jenkins que se ejecuta en nodos remotos para ejecutar tareas y trabajos asignados por el servidor maestro de Jenkins.
- jenkins master: servidor principal de Jenkins que gestiona la configuración, los trabajos y la coordinación de los agentes para ejecutar tareas de CI/CD.
- jenkins slave: son máquinas programadas para construir los proyectos que el maestro le requiere.
- jenkins executor: un ejecutor es una secuencia separada de compilaciones que se ejecutarán en un nodo en paralelo.
- plugin: es una parte de software adicional a la funcionalidad básica del jenkins server.
- #!/bin/bash: es una línea que se encuentra al inicio de un script de bash y que indica al sistema operativo que debe utilizar el intérprete de comandos bash para ejecutar el script, llamado shebang.
- sleep 5: es un comando en bash que pausa la ejecución del script durante 5 segundos.
- opt: es un directorio en sistemas Unix/Linux que se utiliza para almacenar software adicional o paquetes opcionales que no forman parte del sistema base.
- parametrizado: se refiere a la capacidad de un proceso o sistema para aceptar parámetros o variables de entrada que pueden modificar su comportamiento o resultados.