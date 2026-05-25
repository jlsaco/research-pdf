# El marco de selección de 6 dimensiones

## Resumen

Elegir el modelo de lenguaje (LLM) adecuado no se reduce a "cuál parece mejor": es una decisión que equilibra varios factores a la vez. Este tema presenta un **marco de selección de 6 dimensiones**, una forma estructurada de comparar modelos según criterios como la calidad, la velocidad, el precio, la latencia, la ventana de contexto y el ajuste a tus requisitos. La idea central es que **ningún modelo gana en todas las dimensiones**: cada uno implica compromisos (trade-offs), y la mejor elección depende de las prioridades de tu caso de uso. Para tomar la decisión de forma objetiva, el marco se apoya en una herramienta clásica de priorización —la **matriz de decisión ponderada**— donde defines tus criterios, les asignas pesos según su importancia, puntúas cada modelo y eliges el que obtiene la puntuación total más alta.

## Conceptos previos

Antes de aplicar el marco conviene entender estas ideas:

- **Tokens y ventana de contexto.** Un token es la unidad básica de texto que procesa un modelo (una palabra, una sub-palabra o un signo de puntuación). La ventana de contexto es la cantidad de tokens que el modelo puede considerar a la vez, e incluye tanto la entrada como la salida.
- **Latencia y "time-to-first-token" (TTFT).** La latencia mide cuánto tarda el modelo en responder. El TTFT es el tiempo hasta el primer token (qué tan rápido empieza a responder), mientras que la latencia de extremo a extremo (E2EL) abarca hasta el último token.
- **Precio por tokens.** El costo de los modelos suele expresarse por millón de tokens (precio por 1M de tokens), lo que permite comparar el costo entre modelos distintos.
- **Matriz de decisión ponderada.** Una técnica de priorización que coloca las opciones en filas y los criterios en columnas, asigna pesos a cada criterio, puntúa cada opción y suma los totales ponderados para elegir la mejor.

## Análisis a fondo

### Las dimensiones que se equilibran

La selección de un LLM consiste en balancear múltiples dimensiones. Una formulación común nombra cinco: **calidad, velocidad, precio, latencia y ventana de contexto**. Un sexto criterio suele añadir el **ajuste a tus requisitos** (qué tan bien encaja el modelo con la tarea concreta) o bien separa la velocidad de la latencia como dimensiones distintas. La clave es que estas dimensiones compiten entre sí: un modelo muy potente puede ser caro y lento, mientras que uno más barato y rápido puede sacrificar precisión.

Por eso **no existe una sola métrica que capture qué hace "buena" a una respuesta**. La selección requiere equilibrar las dimensiones según las prioridades del caso de uso: para una aplicación crítica, la exactitud puede pesar más que el costo; para tareas rutinarias, el costo y la velocidad pueden ganar.

### Elegir con datos, no con "vibras"

Una selección bien hecha **define primero los criterios de evaluación**, antes de mirar los modelos. El proceso recomendado es:

1. Definir los criterios y requisitos de la tarea.
2. Construir un conjunto de datos de referencia (ground truth) que represente tu problema real.
3. Ejecutar evaluaciones comparativas de los modelos sobre los mismos puntos de referencia.
4. Decidir a partir de los datos, en lugar de basarse en la impresión subjetiva.

### La matriz de decisión ponderada en la práctica

La herramienta que convierte estas dimensiones en una decisión concreta es la matriz de decisión ponderada. Funciona así:

- Lista las **opciones** (los modelos candidatos) como filas.
- Lista los **criterios** (las 6 dimensiones) como columnas.
- Asigna a cada criterio un **peso** según su importancia.
- Puntúa cada opción en cada criterio.
- Multiplica puntuación × peso y **suma** para obtener un total por opción.
- Elige la opción con el total más alto.

La ponderación garantiza que los criterios más importantes influyan más en la decisión final (por ejemplo, ponderar el costo por encima de otros factores cuando el presupuesto es la prioridad). En la práctica, manejar entre **5 y 8 criterios** es un punto de equilibrio razonable: suficiente para cubrir lo importante sin volverse inmanejable —y encaja de forma natural con un marco de 6 dimensiones.

### Por qué importan los detalles técnicos

Comprender las dimensiones técnicas ayuda a puntuarlas con criterio:

- Las **ventanas de contexto** han crecido enormemente (de unos 2.048 tokens en GPT-3 a unos 128.000 tokens en Llama 3.1 8B), lo que cambia cuánta información puede procesar un modelo de una vez.
- El **TTFT** determina la sensación de capacidad de respuesta, mientras que el tiempo por token de salida (TPOT) determina la velocidad percibida. Dos sistemas con la misma latencia total pueden sentirse muy distintos según cuándo empiezan a generar la salida.

## Por qué le importa a un Student

Como estudiante, este marco te da algo más valioso que una lista de modelos "recomendados": te da un **método de razonamiento** que seguirá siendo válido aunque los modelos cambien cada pocos meses. Aprender a descomponer una decisión en dimensiones, asignar pesos y puntuar de forma estructurada es una habilidad transferible a muchas otras decisiones técnicas (elegir una base de datos, un framework, un proveedor de nube). Además, entender los conceptos subyacentes —tokens, ventana de contexto, latencia, precio por millón de tokens— te permite leer con sentido crítico las comparativas y los benchmarks que verás constantemente en el mundo de la IA.

## Errores comunes

- **Mirar solo una dimensión.** Elegir el modelo "más potente" o "más barato" sin ponderar el resto suele llevar a malas decisiones; el objetivo es el equilibrio según tu caso de uso.
- **Decidir por "vibras".** Confiar en la impresión subjetiva en lugar de definir criterios y evaluar con un conjunto de datos de referencia produce elecciones difíciles de justificar.
- **Confundir velocidad con latencia.** El TTFT (cuándo empieza a responder) y la latencia total no son lo mismo; dos modelos con la misma latencia total pueden sentirse muy diferentes.
- **Ignorar que la ventana de contexto incluye entrada y salida.** Subestimar el espacio de tokens disponible puede truncar respuestas o cortar información importante.
- **Usar demasiados o muy pocos criterios.** Menos de 5 puede dejar fuera factores clave; muchos más de 8 vuelve la matriz difícil de manejar y diluye los pesos.

## Fuentes

**General**
- [How to Choose LLM Models: Balancing Quality, Speed, Price, Latency, and Context Window (Mehmet Ozkaya, Medium)](https://mehmetozkaya.medium.com/how-to-choose-llm-models-balancing-quality-speed-price-latency-and-context-window-c6c2bcf0f296)

**Específicas**
- [Beyond vibes: How to properly select the right LLM for the right task (AWS Machine Learning Blog)](https://aws.amazon.com/blogs/machine-learning/beyond-vibes-how-to-properly-select-the-right-llm-for-the-right-task/)
- [Weighted decision matrix: A tool for pro-level prioritization (airfocus)](https://airfocus.com/blog/weighted-decision-matrix-prioritization/)
- [Decision Matrix Examples: 7 Steps to Build Matrices Fast (Asana)](https://asana.com/resources/decision-matrix-examples)
- [Tokens and Context Windows in LLMs (GeeksforGeeks)](https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/)
- [Key metrics for LLM inference — LLM Inference Handbook (BentoML)](https://bentoml.com/llm/inference-optimization/llm-inference-metrics)

## Referencias

1. Ozkaya, M. *How to Choose LLM Models: Balancing Quality, Speed, Price, Latency, and Context Window.* Medium. https://mehmetozkaya.medium.com/how-to-choose-llm-models-balancing-quality-speed-price-latency-and-context-window-c6c2bcf0f296
2. AWS Machine Learning Blog. *Beyond vibes: How to properly select the right LLM for the right task.* https://aws.amazon.com/blogs/machine-learning/beyond-vibes-how-to-properly-select-the-right-llm-for-the-right-task/
3. airfocus. *Weighted decision matrix: A tool for pro-level prioritization.* https://airfocus.com/blog/weighted-decision-matrix-prioritization/
4. Asana. *Decision Matrix Examples: 7 Steps to Build Matrices Fast.* https://asana.com/resources/decision-matrix-examples
5. GeeksforGeeks. *Tokens and Context Windows in LLMs.* https://www.geeksforgeeks.org/artificial-intelligence/tokens-and-context-windows-in-llms/
6. BentoML. *Key metrics for LLM inference — LLM Inference Handbook.* https://bentoml.com/llm/inference-optimization/llm-inference-metrics
