# Práctica: Matriz de comparación y selección de modelos

> Diapositivas cubiertas: 18, 19, 20

## Resumen

Este tema te guía por la actividad práctica de **comparar varios modelos de IA y elegir el más adecuado** para una tarea concreta. La idea central es que no existe un "mejor modelo" universal: el modelo correcto depende de qué tan bien cumple los criterios que tú defines (calidad, exactitud, estilo, etc.). Para tomar esa decisión de forma ordenada y justificable, se usan dos herramientas combinadas: una **rúbrica de evaluación** (para puntuar las salidas de cada modelo de manera consistente) y una **matriz de decisión ponderada** (para organizar opciones, criterios y pesos, y calcular un total que indique el ganador). El tema también introduce la idea de tener un **modelo principal y uno de respaldo (fallback)** para que un flujo siga funcionando si el modelo principal falla.

## Conceptos previos

Antes de abordar este tema conviene tener claro:

- **Qué es un modelo de lenguaje (LLM)** y que distintos modelos producen salidas distintas para el mismo prompt.
- **Qué es un prompt** y cómo el mismo prompt se puede enviar a varios modelos para comparar resultados.
- **Idea básica de evaluación**: comparar la salida de un modelo con lo que esperabas que produjera.
- **Noción de criterios**: las cualidades que te importan en una respuesta (por ejemplo, exactitud, completitud, claridad).
- **Operaciones simples**: multiplicar un peso por una puntuación y sumar totales, que es la base de la matriz ponderada.

## Análisis a fondo

### Comparar las salidas de los modelos

El punto de partida es enviar **el mismo prompt a distintos modelos** y comparar lo que devuelven. Una técnica muy común es la **comparación por pares o lado a lado** (side-by-side): se muestran dos respuestas a la misma pregunta y se elige la mejor. Esta forma de comparar es intuitiva y, cuando se hace bien, puede alcanzar **más del 80 % de coincidencia con las preferencias humanas**, lo que la hace muy útil para decidir qué modelo o qué prompt funciona mejor durante el desarrollo.

### Construir una rúbrica de evaluación

Comparar "a ojo" no es suficiente cuando quieres una decisión consistente y justificable. Para eso se usa una **rúbrica**: una guía que define cómo puntuar cada respuesta. Una buena rúbrica especifica cuatro elementos por cada criterio:

1. **La dimensión de evaluación** (qué estás midiendo).
2. **Una definición clara de éxito** (qué cuenta como "bueno").
3. **Una escala de puntuación**.
4. **Evidencia observable** que justifique cada nivel de puntuación.

Un principio importante es **separar dimensiones independientes** en lugar de dar una sola nota mezclada: por ejemplo, evaluar por separado el cumplimiento de la tarea, la exactitud/fundamentación, la completitud, la seguridad y el estilo de comunicación. La escala debe ajustarse a la decisión: **aprobado/reprobado** para requisitos estrictos, una escala de **3 puntos** para decisiones operativas y una de **5 puntos** para seguir mejoras graduales. También conviene distinguir las "puertas duras" (requisitos que se deben cumplir sí o sí) de las preferencias de calidad.

Buenas prácticas al puntuar con rúbrica: evaluar **un criterio a la vez**, aclarar el significado de cada puntuación con definiciones explícitas, usar escalas binarias o de pocas opciones para mayor consistencia y **validar al evaluador** contra un conjunto de datos etiquetado manualmente. En herramientas reales, esto se concreta así: una aserción de rúbrica (por ejemplo, `llm-rubric` en Promptfoo) toma un criterio en lenguaje natural y devuelve un JSON con una **puntuación numérica (0.0–1.0)**, una razón y un resultado de aprobado/reprobado; el resultado solo pasa si supera un umbral configurado.

### Construir la matriz de selección

Una vez que tienes puntuaciones, las organizas en una **matriz de decisión ponderada**, que se construye en unos 7 pasos:

1. Identificar las alternativas (los modelos a comparar) — van en las **filas**.
2. Identificar los criterios — van en las **columnas**.
3. Construir la cuadrícula.
4. Rellenar las puntuaciones (por ejemplo, una escala de 1 a 3 cuando hay poca variación).
5. Añadir los **pesos** a cada criterio.
6. Multiplicar peso × puntuación.
7. Sumar para obtener el total de cada modelo y elegir el más alto.

Los criterios deben ser **relevantes, medibles y reducidos a un conjunto pequeño** (normalmente entre 4 y 8). El total ponderado es lo que **justifica la decisión**: puedes explicar por qué elegiste un modelo señalando los números de la matriz.

### Modelo principal y modelo de respaldo (fallback)

Elegir "el ganador" no significa depender de un solo modelo. Una buena práctica para flujos en producción es definir un **modelo principal y uno de respaldo**: se intenta primero el principal y, si ocurre un **error 500, un límite de velocidad (rate limit) o un tiempo de espera agotado (timeout)**, se cambia automáticamente al primer modelo de respaldo. Cada modelo puede tener su propio número de reintentos y el cambio (failover) se mantiene **transparente para el usuario**.

## Por qué le importa a un Student

Como estudiante, este tema te enseña una habilidad transferible más allá de la IA: **tomar decisiones de forma estructurada y justificable** en lugar de basarte en intuición. Aprender a definir criterios, ponderarlos y puntuar opciones es exactamente el tipo de razonamiento que usarás en proyectos, tesis o cualquier elección técnica. Además, al construir una rúbrica entiendes desde primeros principios **qué significa que una respuesta de IA sea "buena"**, lo que te vuelve un usuario más crítico y consciente. Por último, practicar la comparación lado a lado te ayuda a notar diferencias reales entre modelos en vez de quedarte con el primero que pruebes.

## Errores comunes

- **Usar una sola nota mezclada.** Dar una única puntuación global oculta los puntos fuertes y débiles; separa las dimensiones (exactitud, completitud, estilo, seguridad).
- **Definir demasiados criterios.** Más de 8 criterios vuelve la matriz inmanejable y diluye la decisión; consolida a un conjunto pequeño y relevante.
- **No ponderar.** Si todos los criterios pesan igual, la matriz puede premiar cualidades poco importantes; asigna pesos según lo que de verdad importa.
- **Escala mal elegida.** Usar una escala de 5 puntos para un requisito que en realidad es aprobado/reprobado introduce ambigüedad innecesaria.
- **No validar al evaluador.** Si usas un modelo o rúbrica para puntuar, compáralo contra ejemplos etiquetados a mano; de lo contrario no sabes si tus puntuaciones son confiables.
- **Olvidar el respaldo.** Elegir el mejor modelo sin un fallback deja tu flujo sin red de seguridad si ese modelo falla.

## Fuentes

Fuente general:

- [LLM-as-a-judge: a complete guide to using LLMs for evaluations (Evidently AI)](https://www.evidentlyai.com/llm-guide/llm-as-a-judge) — Panorama general de cómo comparar salidas de modelos: comparación lado a lado, puntuación por criterios y diseño de rúbricas.

Fuentes específicas:

- [How to Write an LLM Evaluation Rubric (Twine)](https://www.twine.net/blog/how-to-write-an-llm-evaluation-rubric/) — Cómo construir rúbricas y mapear tareas a dimensiones independientes y escalas de puntuación.
- [LLM Rubric (Promptfoo docs)](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/) — Mecánica concreta de puntuación con rúbrica: criterio, puntuación 0–1, umbral de aprobación.
- [Decision Matrix Examples: 7 Steps to Build Matrices Fast (Asana)](https://asana.com/resources/decision-matrix-examples) — Cómo construir la matriz de selección ponderada: criterios, pesos, puntuaciones y totales.
- [Model fallbacks: Your safety net for production AI (Mastra)](https://mastra.ai/blog/model-fallback) — Selección de modelo principal vs. de respaldo y failover automático.

## Referencias

1. Evidently AI. *LLM-as-a-judge: a complete guide to using LLMs for evaluations.* https://www.evidentlyai.com/llm-guide/llm-as-a-judge
2. Twine. *How to Write an LLM Evaluation Rubric.* https://www.twine.net/blog/how-to-write-an-llm-evaluation-rubric/
3. Promptfoo. *LLM Rubric (documentación).* https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/
4. Asana. *Decision Matrix Examples: 7 Steps to Build Matrices Fast.* https://asana.com/resources/decision-matrix-examples
5. Mastra. *Model fallbacks: Your safety net for production AI.* https://mastra.ai/blog/model-fallback
