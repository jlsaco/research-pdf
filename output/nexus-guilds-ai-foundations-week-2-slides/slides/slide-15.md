# Diapositiva 15 — El iceberg del costo

## Qué dice esta diapositiva

La diapositiva usa la metáfora del iceberg para mostrar que el precio por tokens es solo la parte visible del costo. Por debajo hay cuatro capas. **Costos de API:** se cobran por millón de tokens (entrada y salida por separado), y los tokens de salida suelen costar entre 3 y 5 veces más que los de entrada. **Costos de infraestructura:** para modelos autoalojados, servidores con GPU de 10.000 a 50.000+ dólares al año cada uno. **Costos de integración:** tiempo de desarrollo para construir y mantener integraciones de API, manejo de errores y monitoreo. **Costos de cambio:** una vez que prompts, flujos de trabajo e integraciones se construyen para un modelo, cambiar requiere rehacer trabajo; esto es el "vendor lock-in" (dependencia del proveedor).

La conclusión clave: elegir el nivel correcto dentro de una familia es tan importante como elegir la familia correcta.

## Conceptos clave

- **Costo total de propiedad (TCO):** el precio por tokens es la punta del iceberg.
- **Tokens de salida más caros:** suelen costar 3-5x más que los de entrada.
- **Infraestructura del autoalojamiento:** GPUs costosas que el "peso gratis" no incluye.
- **Costos de integración:** desarrollo, mantenimiento, manejo de errores y monitoreo.
- **Costos de cambio y vendor lock-in:** migrar de modelo implica rehacer mucho trabajo.

## Temas relacionados

- [Niveles y costo](../topics/04-tiers-and-cost.md)

## Notas para el estudiante

Esta diapositiva enseña a pensar como alguien que toma decisiones, no solo como usuario. Cuando leas que un modelo es "más barato" o de "peso gratuito", entrénate a preguntar: ¿barato en qué capa del iceberg? Un modelo de código abierto sin costo de licencia puede salir carísimo en GPUs e ingeniería. Comprender el vendor lock-in también te ayudará en proyectos futuros: cuanto más acoplado esté tu trabajo a un proveedor, más difícil será cambiar, así que vale la pena diseñar pensando en la portabilidad desde el inicio.
