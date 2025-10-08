# Introducción a JUnit y Mockito
- Son dos de las librerías más populares en el ecosistema Java para realizar pruebas unitarias, que permiten verificar el correcto funcionamiento del código y detectar errores de manera temprana., JUnit es un framework para escribir pruebas unitarias de nuestro código y ejecutarlas en la JVM. Utiliza programación funcional y lambda e incluye varios estilos diferentes de pruebas, configuraciones anotaciones, ciclo de vida de las pruebas, etc.

## Ventajas de usar JUnit y Mockito
- Facilitan la creación y ejecución de pruebas unitarias.
- Permiten identificar y corregir errores en el código de manera temprana.
- Mejoran la calidad del código y la confianza en su funcionamiento.
- Fomentan buenas prácticas de desarrollo, como TDD.
- Ayudan a mantener el código limpio y modular.
- Pruebas automatizadas que pueden integrarse en el proceso de desarrollo continuo.

## Tipos de pruebas del software
- **Pruebas Unitarias**: Prueban unidades individuales de código (métodos o clases) para asegurar que funcionan correctamente.
- **Pruebas Depuración**: Pruebas que se realizan para identificar y corregir errores en el código.
- **Pruebas de Integración**: Verifican que diferentes módulos o servicios funcionen juntos correctamente.
- **Pruebas de Sistema**: Prueban el sistema completo para asegurar que cumple con los requisitos especificados.
- **Pruebas de Aceptación**: Validan que el sistema cumple con las expectativas y necesidades del usuario final.
- **Pruebas de Regresión**: Aseguran que los cambios recientes en el código no hayan introducido nuevos errores en funcionalidades existentes.
- **Pruebas de Rendimiento**: Evalúan la velocidad, capacidad de respuesta y estabilidad del sistema bajo carga.
- **Pruebas de Seguridad**: Identifican vulnerabilidades y aseguran que el sistema esté protegido contra amenazas.
- **Pruebas de Usabilidad**: Evalúan la facilidad de uso y la experiencia del usuario con el sistema.
- **Pruebas de Compatibilidad**: Verifican que el sistema funcione correctamente en diferentes entornos, dispositivos y navegadores.

## Flujo de realización de pruebas unitarias
- Input -> Pieza de código -> Output.
- Se verifica que el output sea el esperado para un input dado.

## Arquitectura de Junit 5
- JUnit 5 está compuesto por tres módulos principales:
    - JUnit Platform: Proporciona la infraestructura para ejecutar pruebas y es compatible con diferentes frameworks de pruebas.
    - JUnit Jupiter: Es el módulo que contiene la nueva API de programación y las anotaciones para escribir pruebas en JUnit 5.
    - JUnit Vintage: Permite ejecutar pruebas escritas con versiones anteriores de JUnit (JUnit 3 y JUnit 4).

## Código de JUnit 5
- Assertions: Clase que proporciona métodos estáticos para realizar afirmaciones en las pruebas, como assertEquals, assertTrue, assertFalse, etc.
- Anotaciones: Metadatos que se utilizan para definir el comportamiento de las pruebas, como @Test, @BeforeEach, @AfterEach, @BeforeAll, @AfterAll, etc.
- Ciclo de vida de las pruebas: Define el orden en que se ejecutan los métodos anotados, como la configuración previa a cada prueba y la limpieza posterior a cada prueba.


## Términos comunes en JUnit y Mockito
- Prueba Unitaria (Unit Test): Son un proceso para validar que una pieza de código cumple con ciertas reglas de negocio o funcionalidades específicas.
- Mock (Simulación): Un objeto simulado que imita el comportamiento de un objeto real en pruebas unitarias.
- Junit 5: es una librería java para escribir y ejecutar pruebas unitarias repetibles y predecibles.
- Anotaciones: Son metadatos que proporcionan información adicional sobre el código, como @Test, @BeforeEach, @AfterEach, etc. Java.
- IDE (Entorno de Desarrollo Integrado): Un software que proporciona herramientas para escribir, depurar y ejecutar código.
- Test Case (Caso de Prueba): Una unidad individual de prueba que verifica una funcionalidad específica del código.
- JDK (Java Development Kit): Un conjunto de herramientas necesarias para desarrollar aplicaciones en Java.
- JVM (Java Virtual Machine): Una máquina virtual que ejecuta código Java.
- Framework: Un conjunto de herramientas y bibliotecas que facilitan el desarrollo de software.
- TDD (Test-Driven Development): Una metodología de desarrollo de software que se basa en escribir pruebas antes de escribir el código.
- BDD (Behavior-Driven Development): Una metodología de desarrollo de software que se centra en el comportamiento esperado del sistema desde la perspectiva del usuario.