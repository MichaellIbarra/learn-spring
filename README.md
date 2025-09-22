# Introducción a Spring Boot
- Spring Framework es un marco de trabajo de Java que se utiliza para crear aplicaciones empresariales, su uso es muy común en el desarrollo de aplicaciones web.
- Spring Boot es un subproyecto de Spring Framework que se utiliza para crear aplicaciones autónomas y autoconfigurables, es decir, que no requieren de configuraciones adicionales ya que Spring Boot las realiza automáticamente, como la configuración de la base de datos, la configuración de la seguridad, servicios REST, etc.


# Comandos de Java
## mvn - es un comando de Maven, una herramienta de gestión de proyectos y construcción de Java.
- mvn clean : Elimina los archivos generados por la construcción anterior.
- mvn compile : Compila el código fuente del proyecto.
- mvn test : Ejecuta las pruebas unitarias del proyecto.
- mvn package : Empaqueta el proyecto en un archivo JAR o WAR.
- mvn install : Instala el archivo JAR o WAR en el repositorio local de Maven.
- mvn spring-boot:run : Ejecuta la aplicación Spring Boot.
- mvn dependency:tree : Muestra el árbol de dependencias del proyecto.
- mvn dependency:analyze : Analiza las dependencias del proyecto y muestra las dependencias no utilizadas.
- mvn dependency:purge-local-repository : Elimina las dependencias del repositorio local de Maven.
- mvn dependency:copy-dependencies : Copia las dependencias del proyecto en un directorio específico.
- mvn dependency:resolve : Resuelve las dependencias del proyecto y las descarga en el repositorio local de Maven.
- mvn -Dfile.encoding=UTF-8 clean package : Configura la codificación de caracteres a UTF-8 al empaquetar el proyecto.
- mvn -DskipTests=true clean package : Omite la ejecución de pruebas al empaquetar el proyecto.
- mvn -Dmaven.test.skip=true clean package : Omite la ejecución de pruebas y la compilación de pruebas al empaquetar el proyecto.
- mvn -DskipTests clean package : Omite la ejecución de pruebas al empaquetar el proyecto.
- mvn -Dmaven.test.skip=true clean package : Omite la ejecución de pruebas y la compilación de pruebas al empaquetar el proyecto.
- mvn -DskipTests clean install : Omite la ejecución de pruebas al instalar el proyecto.
- mvn -Dmaven.test.skip=true clean install : Omite la ejecución de pruebas y la compilación de pruebas al instalar el proyecto.
- mvn -DskipTests=true clean install : Omite la ejecución de pruebas al instalar el proyecto.
#mvn "-Dfile.encoding=UTF-8" clean package
#mvn clean package "-Dfile.encoding=UTF-8"
## gradle - es un sistema de automatización de construcción que utiliza un lenguaje de dominio específico (DSL) basado en Groovy o Kotlin.
- gradle clean : Elimina los archivos generados por la construcción anterior.
- gradle build : Compila el código fuente del proyecto y genera un archivo JAR o WAR.
- gradle test : Ejecuta las pruebas unitarias del proyecto.
- gradle bootRun : Ejecuta la aplicación Spring Boot.
- gradle dependencies : Muestra el árbol de dependencias del proyecto.
- gradle dependencyInsight : Muestra información detallada sobre una dependencia específica en el proyecto.
- gradle dependencyReport : Genera un informe de las dependencias del proyecto.
- gradle dependencyUpdates : Muestra las actualizaciones disponibles para las dependencias del proyecto.
- gradle dependencyCheck : Realiza un análisis de seguridad de las dependencias del proyecto.
- gradle dependencyUpdates -Drevision=release : Muestra las actualizaciones disponibles para las dependencias del proyecto, filtrando por versiones de lanzamiento.|
- gradle dependencyUpdates -Drevision=milestone : Muestra las actualizaciones disponibles para las dependencias del proyecto, filtrando por versiones de hitos.
- gradle dependencyUpdates -Drevision=snapshot : Muestra las actualizaciones disponibles para las dependencias del proyecto, filtrando por versiones de instantáneas.
- gradle dependencyUpdates -Drevision=release -DoutputFormatter=json : Muestra las actualizaciones disponibles para las dependencias del proyecto, filtrando por versiones de lanzamiento y generando un informe en formato JSON.

-D es un parámetro que se utiliza para pasar propiedades del sistema
-Dserver.port=8002 : Cambia el puerto del servidor a 8000.
-Dspring.profiles.active=dev : Activa el perfil de desarrollo.
-Dspring.profiles.active=prod : Activa el perfil de producción.
-Dspring.profiles.active=test : Activa el perfil de prueba.

### Términos comunes en Spring Boot
- packaging : Especifica cómo se empaquetará la aplicación, por ejemplo, en un archivo JAR o WAR.
- Diferencias entre JAR y WAR : Un archivo JAR es un archivo que contiene clases de Java y otros recursos, mientras que un archivo WAR es un archivo que contiene archivos JAR, archivos de propiedades, archivos XML, archivos de clase, etc. y se utiliza para distribuir una colección de archivos Java.
- hibernate : Es un marco de trabajo de Java que se utiliza para mapear objetos de Java a una base de datos relacional.
- JPA : Java Persistence API es una especificación de Java que se utiliza para mapear objetos de Java a una base de datos relacional.
- Diferencia entre Hibernate y JPA : JPA es una especificación de Java que define cómo se deben mapear los objetos de Java a una base de datos relacional, mientras que Hibernate es una implementación de JPA que se utiliza para mapear objetos de Java a una base de datos relacional.
- REST : Representational State Transfer es un estilo de arquitectura de software que se utiliza para crear servicios web.
- RESTful : Es un servicio web que sigue los principios de REST.
- JpaRepository y CrudRepository : Son interfaces de Spring Data JPA que se utilizan para realizar operaciones CRUD en una base de datos, la diferencia entre JpaRepository y CrudRepository es que JpaRepository proporciona métodos adicionales que son tipos como paginación, clasificación, etc, mientras que CrudRepository proporciona métodos CRUD básicos.
- extends y implements : extends se utiliza para heredar una clase y implements se utiliza para implementar una interfaz.
- Put y Patch : diferencia entre PUT y PATCH es que PUT se utiliza para actualizar un recurso completo, mientras que PATCH se utiliza para actualizar un recurso parcial.
- Spring WebFlux : Es un framework de programación reactiva para construir aplicaciones web en Java utilizando el ecosistema de Spring. WebFlux permite crear aplicaciones asíncronas y no bloqueantes, lo que mejora la escalabilidad y el rendimiento al manejar múltiples solicitudes simultáneamente. Utiliza el modelo de programación reactiva y se basa en la especificación Reactive Streams para gestionar flujos de datos de manera eficiente, HttpHandler y Api WebHandler son componentes clave en la arquitectura de Spring WebFlux. HttpHandler es una interfaz que define cómo manejar las solicitudes HTTP y enviar respuestas, mientras que Api WebHandler es una implementación específica de HttpHandler que se utiliza para gestionar las solicitudes y respuestas en una API RESTful. Estos componentes permiten crear aplicaciones web reactivas y no bloqueantes, mejorando la eficiencia y el rendimiento al manejar múltiples solicitudes simultáneamente.
- Spring MVC Es un módulo del framework Spring que se utiliza para desarrollar aplicaciones web basadas en el patrón Modelo-Vista-Controlador (MVC). Spring MVC facilita la creación de aplicaciones web estructuradas y escalables al separar la lógica de negocio, la presentación y el control de flujo. Proporciona herramientas y anotaciones para gestionar solicitudes HTTP, renderizar vistas y manejar la interacción entre el modelo y la vista, que son tipos sincrónicas y bloqueantes.
- Spring Boot: Es un framework basado en Spring que simplifica el proceso de desarrollo de aplicaciones Java al proporcionar una configuración automática y convenciones predeterminadas. Spring Boot permite crear aplicaciones independientes y listas para producción con facilidad, eliminando la necesidad de configuraciones complejas y facilitando la integración con otros módulos de Spring y bibliotecas de terceros.
- Junit : Es un marco de trabajo de pruebas unitarias para Java que permite escribir y ejecutar pruebas automatizadas. JUnit facilita la creación de pruebas para verificar el comportamiento de las clases y métodos, asegurando que el código funcione correctamente y cumpla con los requisitos especificados. Es una herramienta fundamental en el desarrollo ágil y la integración continua, ya que ayuda a detectar errores y mantener la calidad del software a lo largo del ciclo de vida del desarrollo.
- Mockito : Es una biblioteca de Java que se utiliza para crear objetos simulados (mocks) en pruebas unitarias. Mockito permite simular el comportamiento de dependencias externas, como servicios o bases de datos, lo que facilita la prueba de clases y métodos de manera aislada. Al utilizar Mockito, los desarrolladores pueden verificar interacciones, definir comportamientos esperados y asegurarse de que el código funcione correctamente sin depender de implementaciones reales.
- Spring Security : Es un módulo del framework Spring que proporciona funcionalidades de seguridad para aplicaciones Java. Permite gestionar la autenticación y autorización de usuarios, proteger recursos y aplicar políticas de seguridad en aplicaciones web. Spring Security es altamente configurable y se integra fácilmente con otros módulos de Spring, lo que facilita la implementación de medidas de seguridad en aplicaciones empresariales.
- Java Development Kit (JDK) : Es un conjunto de herramientas y bibliotecas necesarias para desarrollar aplicaciones Java. Incluye el compilador Java, la máquina virtual Java (JVM), herramientas de depuración y bibliotecas estándar de Java. El JDK es esencial para compilar, ejecutar y depurar aplicaciones Java, y es utilizado por desarrolladores para crear software en el lenguaje de programación Java.
- Java Runtime Environment (JRE) : Es un entorno de ejecución que permite ejecutar aplicaciones Java. Incluye la máquina virtual Java (JVM) y las bibliotecas estándar de Java, pero no incluye el compilador ni las herramientas de desarrollo. El JRE es necesario para ejecutar aplicaciones Java, pero no es suficiente para desarrollar software en Java, ya que no proporciona las herramientas necesarias para compilar y depurar código.
- Java Virtual Machine (JVM) : Es una máquina virtual que permite ejecutar aplicaciones Java en diferentes plataformas. La JVM interpreta y ejecuta el bytecode Java, que es el código intermedio generado por el compilador Java. La JVM proporciona un entorno de ejecución independiente de la plataforma, lo que permite que las aplicaciones Java sean portátiles y se ejecuten en cualquier sistema operativo que tenga una JVM compatible.
- Spring Data JPA : Es un proyecto de Spring que simplifica el acceso a bases de datos mediante la implementación de la especificación JPA (Java Persistence API). Proporciona una capa de abstracción sobre JPA y facilita la creación de repositorios para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en entidades persistentes. Spring Data JPA permite a los desarrolladores centrarse en la lógica de negocio sin preocuparse por la implementación detallada del acceso a datos.
- Spring Data REST : Es un proyecto de Spring que permite crear servicios RESTful a partir de repositorios de Spring Data. Proporciona una forma rápida y sencilla de exponer entidades JPA como recursos REST, lo que facilita la creación de API RESTful sin necesidad de escribir controladores personalizados. Spring Data REST se integra con Spring Data JPA y utiliza convenciones para generar automáticamente los endpoints REST, lo que acelera el desarrollo de aplicaciones web y servicios.
- Spring Boot DevTools : Es un conjunto de herramientas que facilitan el desarrollo de aplicaciones Spring Boot. Proporciona características como recarga automática de clases, reinicio rápido de la aplicación y soporte para la depuración. DevTools mejora la productividad del desarrollador al permitir realizar cambios en el código y ver los resultados de inmediato sin necesidad de reiniciar manualmente la aplicación. También incluye herramientas para mejorar la experiencia de desarrollo, como la configuración automática de propiedades y la gestión de dependencias.
- Hibernate Validator : Es una implementación de la especificación Bean Validation (JSR 380) para Java. Proporciona un marco para validar objetos Java mediante anotaciones y reglas de validación. Hibernate Validator permite definir restricciones en las propiedades de los objetos, como longitud mínima, formato de correo electrónico, valores únicos, entre otros. Al utilizar Hibernate Validator, los desarrolladores pueden garantizar que los datos cumplan con las reglas de negocio antes de ser persistidos en la base de datos o procesados por la aplicación.
- Hibernate ORM : Es un marco de trabajo de mapeo objeto-relacional (ORM) para Java que facilita la interacción entre aplicaciones Java y bases de datos relacionales. Hibernate permite mapear clases Java a tablas de bases de datos y gestionar la persistencia de objetos de manera sencilla. Proporciona características
- R2DBC : Es una API de Java que permite la programación reactiva con bases de datos relacionales. R2DBC proporciona un enfoque no bloqueante y asíncrono para interactuar con bases de datos, lo que mejora la escalabilidad y el rendimiento de las aplicaciones al permitir manejar múltiples solicitudes simultáneamente sin bloquear el hilo principal. R2DBC es especialmente útil en aplicaciones reactivas construidas con Spring WebFlux, ya que permite aprovechar al máximo las capacidades reactivas del framework.
- Spring Cloud : Es un conjunto de herramientas y proyectos que facilitan el desarrollo de aplicaciones distribuidas y microservicios en la nube. Proporciona soluciones para la configuración centralizada, descubrimiento de servicios, balanceo de carga, gestión de circuitos, mensajería y seguridad en entornos de microservicios. Spring Cloud se integra fácilmente con otros proyectos de Spring y permite a los desarrolladores crear aplicaciones escalables y resilientes en la nube.
- JAR y WAR : Son formatos de archivo utilizados para empaquetar aplicaciones Java. Un archivo JAR (Java Archive) es un archivo comprimido que contiene clases Java, bibliotecas y recursos, mientras que un archivo WAR (Web Application Archive) es un archivo JAR que contiene una aplicación web completa, incluyendo archivos JSP, servlets y otros recursos necesarios para ejecutar la aplicación en un servidor web. La principal diferencia entre ambos es que los archivos WAR están diseñados específicamente para aplicaciones web y contienen la estructura necesaria para ser desplegados en un servidor de aplicaciones.
- Injección de dependencias : Es un patrón de diseño que permite a los objetos recibir sus dependencias en lugar de crearlas por sí mismos. En el contexto de Spring, la inyección de dependencias se utiliza para gestionar la creación y el ciclo de vida de los objetos, lo que facilita la separación de preocupaciones y mejora la mantenibilidad del código. Spring proporciona diferentes formas de inyección de dependencias, como la inyección por constructor, la inyección por método y la inyección por campo.
- Spring Boot Starter : Es un conjunto de dependencias preconfiguradas que facilitan la configuración y el uso de diferentes módulos de Spring en una aplicación Spring Boot. Los starters permiten a los desarrolladores agregar rápidamente funcionalidades específicas a sus aplicaciones sin necesidad de configurar manualmente cada dependencia. Por ejemplo, el starter "spring-boot-starter-web" incluye todas las dependencias necesarias para crear una aplicación web con Spring MVC y Tomcat.
- interfaz : Es una colección de métodos abstractos que definen un contrato que las clases deben cumplir. Las interfaces permiten la creación de código más flexible y reutilizable al permitir que diferentes clases implementen la misma interfaz de diferentes maneras. En Java, una clase puede implementar múltiples interfaces, lo que permite la herencia múltiple de comportamientos.
- extends : Es una palabra clave en Java que se utiliza para indicar que una clase hereda de otra clase. La herencia permite a una clase (subclase) heredar propiedades y métodos de otra clase (superclase), lo que promueve la reutilización del código y la creación de jerarquías de clases. En Java, una clase solo puede extender una única superclase, lo que significa que no se permite la herencia múltiple de clases.
- implements : Es una palabra clave en Java que se utiliza para indicar que una clase implementa una o más interfaces. Al implementar una interfaz, una clase debe proporcionar implementaciones concretas para todos los métodos abstractos definidos en la interfaz. Esto permite a las clases cumplir con contratos específicos y promueve la reutilización del código al permitir que diferentes clases implementen la misma interfaz de diferentes maneras.
- @Autowired : Es una anotación de Spring que se utiliza para inyectar dependencias en una clase. Al utilizar @Autowired, Spring busca automáticamente un bean compatible en el contexto de la aplicación y lo inyecta en la propiedad o constructor anotado. Esto facilita la inyección de dependencias y promueve la separación de preocupaciones en el diseño de aplicaciones.
- @Component : Es una anotación de Spring que se utiliza para marcar una clase como un componente de Spring. Al anotar una clase con @Component, Spring la detecta automáticamente durante el escaneo de componentes y la registra como un bean en el contexto de la aplicación. Esto permite que la clase sea gestionada por el contenedor de Spring y facilita la inyección de dependencias.
- @Service : Es una anotación de Spring que se utiliza para marcar una clase como un servicio de negocio. Al anotar una clase con @Service, Spring la detecta automáticamente durante el escaneo de componentes y la registra como un bean en el contexto de la aplicación. Esto permite que la clase sea gestionada por el contenedor de Spring y facilita la inyección de dependencias. La anotación @Service se utiliza principalmente para indicar que una clase contiene lógica de negocio y puede ser utilizada por otros componentes de la aplicación.
- Pipeline : Es un patrón de diseño que se utiliza para procesar datos en etapas secuenciales. En el contexto de Spring, el término "pipeline" se refiere a la forma en que los datos fluyen a través de diferentes componentes o capas de una aplicación. Cada etapa del pipeline puede realizar una transformación o procesamiento específico en los datos antes de pasarlos a la siguiente etapa. Este enfoque permite crear aplicaciones modulares y escalables al separar las responsabilidades y facilitar la reutilización de componentes.
- WebFlux y Spring MVC : Son dos enfoques diferentes para desarrollar aplicaciones web en el ecosistema de Spring. WebFlux es un framework reactivo que permite crear aplicaciones asíncronas y no bloqueantes, mientras que Spring MVC es un framework tradicional basado en el patrón Modelo-Vista-Controlador (MVC) que utiliza un enfoque sincrónico y bloqueante. WebFlux es ideal para aplicaciones que requieren alta escalabilidad y rendimiento, mientras que Spring MVC es adecuado para aplicaciones más convencionales y basadas en solicitudes/respuestas.
T → tipo del valor original en el flujo (Flux<T>)

V → tipo del valor transformado

Function<T, V> → función que toma un valor de tipo T y lo convierte en uno de tipo V

Function<T, Publisher<V>> → función que toma un valor de tipo T y devuelve un flujo (Publisher) de tipo V, es decir, una secuencia en lugar de un valor simple
 ¿Qué es un Publisher<T>?
🔹 Es una fuente de datos que emite 0 o más elementos de tipo T de forma reactiva/asíncrona.

👉 Es como un productor o emisor de datos.

Ejemplos de Publisher:
Flux<T> → emite muchos elementos (0, 1 o más)

Mono<T> → emite un solo elemento o ninguno

👂 ¿Qué es un Subscriber<T>?
🔹 Es el consumidor de los datos que emite un Publisher<T>.

👉 Es quien se suscribe al Publisher y reacciona a los datos emitidos.

Métodos clave del Subscriber:
onNext(T item) → se llama cuando se recibe un nuevo dato

onComplete() → se llama cuando ya no habrá más datos

onError(Throwable t) → se llama si ocurre un error
Publisher<T>	Fuente de datos reactiva (emite datos)	Lista que emite datos uno por uno
Subscriber<T>	Quien recibe los datos	Receptor de eventos
Iterable<T>	Estructura que se puede recorrer (for-each)	List<T>, Set<T>
Function<T, V>	Función de conversión sincrónica	x -> x * 2
Function<T, Publisher<V>>	Función que devuelve un flujo	x -> Flux.just(x, x*2)
Flux.just(...)	Varios valores separados por coma	Datos conocidos en tiempo de compilación
Flux.fromIterable	Una lista, conjunto u otro Iterable	Cuando ya tienes una colección o lista