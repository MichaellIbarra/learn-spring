# Introducción Pruebas de Carga y Pruebas de Rendimiento con Apache JMeter
- Apache JMeter es una herramienta de código abierto diseñada para realizar pruebas de carga y rendimiento en aplicaciones web y otros servicios.

## Ventajas de hacer pruebas de carga y estrés con JMeter
- **Simulación de Usuarios Concurrentes**: Permite simular múltiples usuarios accediendo a la aplicación al mismo tiempo, lo que ayuda a evaluar su rendimiento bajo carga.
- **Código Abierto**: JMeter es gratuito y de código abierto, lo que permite a los usuarios modificar y adaptar la herramienta según sus necesidades.
- **Prevención de Fallos**: Identifica cuellos de botella y problemas de rendimiento antes de que afecten a los usuarios finales.
- **Cuellos de Botella**: Ayuda a identificar las partes del sistema que limitan el rendimiento, permitiendo optimizaciones específicas.
- **Escalabilidad**: Permite probar aplicaciones en diferentes niveles de carga, desde unos pocos usuarios hasta miles, para evaluar cómo se comporta el sistema en diversas condiciones.
- **Informes Detallados**: Proporciona informes y gráficos detallados que facil


## Tipos de pruebas
- **Pruebas de Carga**: Determina la capacidad de una aplicación bajo condiciones de uso simuladas, específicamente para entender cómo maneja grandes volúmenes de solicitudes simultáneas, asegurar que la aplicación funcionará de manera eficiente cuando se encuentre en su punto máximo de demanda real.
- **Pruebas de Rendimiento**: Evalúa la velocidad, capacidad de respuesta y estabilidad de una aplicación bajo una carga específica, ayudando a identificar cuellos de botella y áreas de mejora en el rendimiento general del sistema.
- **Pruebas de Estrés**: Es un tipo de prueba de rendimiento diseñadas para determinar la robustez de un sistema bajo condiciones extremas y no sostenibles a largo plazo. El objetivo de estas pruebas es identificar el punto de ruptura de un sistema.

## Formas de hacer las pruebas
- **Pruebas de cargas estáticas**: Simulan una carga constante durante un período de tiempo determinado.
- **Pruebas de cargas dinámicas**: Simulan cargas que varían con el tiempo, imitando patrones de uso reales.
- **Pruebas de cargas estres**: Incrementan la carga hasta que el sistema falla, para identificar su límite máximo de capacidad.

## Flujo de realización de pruebas con JMeter
1. **Definición de Objetivos**: Establecer qué se quiere medir (tiempos de respuesta, carga máxima, etc.).
2. **Diseño del Escenario de Prueba**: Crear un plan de prueba que incluya los casos de uso y las condiciones de carga.
3. **Configuración de JMeter**: Ajustar los parámetros de JMeter para simular la carga deseada.
4. **Ejecución de Pruebas**: Correr las pruebas y recopilar datos.
5. **Análisis de Resultados**: Evaluar los resultados para identificar problemas de rendimiento y áreas de mejora.


## Términos comunes
- 