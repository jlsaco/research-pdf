# Las seis familias de modelos

## Resumen

Este tema presenta las seis grandes familias de modelos de lenguaje (LLM) que
verás una y otra vez en el ecosistema de la IA: **Claude** (de Anthropic),
**GPT y la serie o** (de OpenAI), **Gemini** (de Google), **DeepSeek**, **Llama**
(de Meta) y **Grok** (de xAI). Cada familia la fabrica una empresa distinta, se
organiza en varios "tamaños" o variantes, y destaca en cosas diferentes: algunas
son las mejores para escribir y programar, otras para razonar paso a paso, otras
por ser baratas y otras por poder descargarse y ejecutarse en tu propia máquina.

A un nivel muy general, **ChatGPT (GPT) es la opción todoterreno más amplia**,
**Claude lidera en escritura técnica de formato largo y en programación
agéntica**, **Gemini encaja bien en el ecosistema de Google**, **Grok destaca
para contexto en vivo de la red X**, **DeepSeek está entre los modelos capaces
más baratos** y **Llama es la opción de pesos abiertos más conocida**.

## Conceptos previos

Antes de comparar las familias, conviene entender cinco ideas que las distinguen:

- **Modelos de pesos abiertos vs. cerrados/propietarios.** Los modelos de
  *pesos abiertos* (open-weight) permiten descargar los parámetros entrenados y
  ejecutarlos por tu cuenta. Los modelos *cerrados/propietarios* (Claude, GPT,
  Gemini) solo se usan a través de una API y los usuarios finales no pueden
  afinarlos.
- **Modelos de razonamiento ("pensamiento extendido").** Algunos modelos
  generan un razonamiento interno paso a paso antes de dar la respuesta final, lo
  que mejora la resolución de problemas complejos.
- **Multimodalidad.** Capacidad de un modelo para recibir más de un tipo de
  entrada (texto, imágenes, audio, vídeo, PDF) y no solo texto.
- **Anclaje web (web grounding).** Herramientas que permiten al modelo consultar
  la web o búsquedas en tiempo real para responder sobre hechos actuales.
- **Autoalojamiento (self-hosting) y afinado (fine-tuning).** Ejecutar un modelo
  de pesos abiertos en tu propia infraestructura y/o reentrenarlo con tus datos.

## Análisis a fondo

### Anthropic — Claude
Claude se organiza en tres niveles: **Opus** (el más capaz, para razonamiento
complejo y programación agéntica), **Sonnet** (el mejor equilibrio entre
velocidad e inteligencia) y **Haiku** (el más rápido, con inteligencia cercana a
la frontera). Todos los modelos actuales de Claude aceptan entrada de texto e
imagen, producen texto, son multilingües y tienen visión; los modelos punteros
ofrecen una ventana de contexto de 1M de tokens, mientras que Haiku ofrece 200k.
Claude es un modelo cerrado/propietario, de uso vía API.

### OpenAI — GPT y la serie o
OpenAI divide su catálogo en dos grupos: los **modelos GPT de propósito general**
(por ejemplo, GPT-4o para multimodalidad en tiempo real, GPT-4.1 para contexto
largo) y los **modelos de razonamiento de la serie o** (o3, o4-mini),
especializados en razonamiento lógico profundo de varios pasos y en el uso de
herramientas. GPT es la familia más versátil y la más conocida del público
general.

### Google — Gemini
Gemini se ofrece en variantes **Pro / Flash / Flash-Lite**, es nativamente
multimodal (texto, imagen, audio, vídeo y PDF) y trae herramientas integradas de
anclaje, como búsqueda en Google, ejecución de código y contexto por URL. Encaja
especialmente bien con flujos de trabajo dentro del ecosistema de Google.

### DeepSeek
**DeepSeek-R1** es un modelo de razonamiento de **pesos abiertos con licencia
MIT**, con un rendimiento a la par del o1 de OpenAI. Sus salidas pueden usarse
libremente para afinado y destilación, y su precio de API es de aproximadamente
$0.14–$0.55 por millón de tokens de entrada y $2.19 por millón de salida, lo que
lo sitúa entre los modelos capaces más económicos.

### Meta — Llama
Llama es una familia **de pesos abiertos / "source-available"**: los pesos se
pueden descargar bajo una licencia comunitaria con una política de uso aceptable.
Se puede afinar y autoalojar (por ejemplo, mediante `llama.cpp`). Su etiqueta de
"código abierto" es discutida por la Open Source Initiative, por lo que es más
preciso llamarlo "de pesos abiertos". Es la opción de pesos abiertos más conocida.

### xAI — Grok
**Grok**, de xAI (empresa fundada por Elon Musk en marzo de 2023), pone el foco
en el razonamiento más el **acceso en tiempo real a la plataforma X** y al resto
de la web para anclar respuestas en hechos actuales. Admite entrada multimodal
(texto, imágenes y voz).

### Idea clave: "pesos abiertos" no es lo mismo que "código abierto"
*Pesos abiertos* significa que los parámetros entrenados son descargables y
ejecutables; el verdadero *código abierto* incluiría además los datos y el código
de entrenamiento. Los modelos cerrados (Claude, GPT, Gemini) solo se usan vía API
y no pueden afinarse, mientras que los de pesos abiertos (DeepSeek, Llama) pueden
autoalojarse y afinarse. Autoalojar mantiene los datos dentro de tu propia
infraestructura y puede reducir mucho el coste por inferencia a gran escala, a
cambio de tener que gestionar tu propia infraestructura de GPU.

## Por qué le importa a un Student

Como estudiante, no necesitas memorizar cada número de versión (cambian muy
rápido), sino entender **el mapa**: quién fabrica qué y para qué sirve cada
familia. Eso te permite elegir la herramienta adecuada para cada tarea —por
ejemplo, un modelo de razonamiento para un problema lógico difícil, uno
multimodal para analizar una imagen, o un modelo de pesos abiertos gratuito si
quieres experimentar en tu propio equipo. Comprender la diferencia entre modelos
abiertos y cerrados también te ayuda a razonar sobre el coste, la privacidad de
los datos y qué puedes (o no) personalizar.

## Errores comunes

- **Confundir "pesos abiertos" con "código abierto".** Llama y DeepSeek liberan
  los pesos, pero no necesariamente los datos y el código de entrenamiento; la
  etiqueta "open source" para Llama es discutida.
- **Pensar que todos los modelos razonan paso a paso.** El razonamiento
  extendido es una capacidad específica (la serie o de OpenAI, R1 de DeepSeek,
  el modo de pensamiento de Claude), no algo que todo modelo haga por defecto.
- **Asumir que el modelo más grande siempre es la mejor opción.** A menudo una
  variante más rápida y barata (Haiku, Flash, o4-mini) resuelve la tarea igual
  de bien y a menor coste.
- **Fijarse solo en los números de versión.** Las versiones cambian
  constantemente; lo que perdura es para qué destaca cada familia.
- **Creer que un modelo cerrado se puede afinar.** Claude, GPT y Gemini se usan
  vía API y no permiten afinado por el usuario final; para eso necesitas un
  modelo de pesos abiertos.

## Fuentes

Fuente general:
- [Best AI Models 2026: ChatGPT vs Claude vs Gemini vs Grok vs DeepSeek vs Llama (T-Minus AI)](https://www.tminusai.com/models)

Fuentes específicas:
- [Models overview — Claude API Docs (Anthropic)](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Extended thinking — Claude API Docs (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
- [Models — Gemini API (Google AI for Developers)](https://ai.google.dev/gemini-api/docs/models)
- [Practical Guide for Model Selection (OpenAI Cookbook)](https://developers.openai.com/cookbook/examples/partners/model_selection_guide/model_selection_guide)
- [DeepSeek-R1 Release — DeepSeek API Docs](https://api-docs.deepseek.com/news/news250120)
- [Llama (language model) — Wikipedia](https://en.wikipedia.org/wiki/Llama_(language_model))
- [The Complete Guide to Grok AI (DataNorth AI)](https://datanorth.ai/blog/the-complete-guide-to-grok-ai)
- [Open-Source vs Closed-Source AI Models (MindStudio)](https://www.mindstudio.ai/blog/open-source-vs-closed-source-ai-models-agentic-workflows)

## Referencias

1. T-Minus AI. *Best AI Models 2026: ChatGPT vs Claude vs Gemini vs Grok vs DeepSeek vs Llama.* https://www.tminusai.com/models
2. Anthropic. *Models overview — Claude API Docs.* https://platform.claude.com/docs/en/about-claude/models/overview
3. Anthropic. *Extended thinking — Claude API Docs.* https://platform.claude.com/docs/en/build-with-claude/extended-thinking
4. Google AI for Developers. *Models — Gemini API.* https://ai.google.dev/gemini-api/docs/models
5. OpenAI. *Practical Guide for Model Selection (OpenAI Cookbook).* https://developers.openai.com/cookbook/examples/partners/model_selection_guide/model_selection_guide
6. DeepSeek. *DeepSeek-R1 Release — DeepSeek API Docs.* https://api-docs.deepseek.com/news/news250120
7. Wikipedia. *Llama (language model).* https://en.wikipedia.org/wiki/Llama_(language_model)
8. DataNorth AI. *The Complete Guide to Grok AI.* https://datanorth.ai/blog/the-complete-guide-to-grok-ai
9. MindStudio. *Open-Source vs Closed-Source AI Models.* https://www.mindstudio.ai/blog/open-source-vs-closed-source-ai-models-agentic-workflows
