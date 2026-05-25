# Niveles de modelos, precios y el iceberg de costos

## Resumen

Los modelos de lenguaje grandes (LLM) se ofrecen en distintos "niveles" (tiers) que equilibran capacidad y precio: modelos insignia (flagship) muy potentes y caros, modelos balanceados de uso general, y modelos ligeros (lightweight) baratos y rápidos. El precio se cobra por token, y casi siempre los tokens de salida cuestan varias veces más que los de entrada. Sin embargo, el precio por token no cuenta toda la historia: existe un "iceberg de costos" formado por gastos ocultos como reintentos, instrucciones de sistema largas, infraestructura, mantenimiento y el costo de cambiar de proveedor. Este tema (diapositivas 13, 14 y 15) explica cómo leer los precios, cómo elegir el nivel adecuado y qué costos se esconden bajo la superficie.

## Conceptos previos

Antes de profundizar conviene entender lo siguiente:

- **Token:** la unidad mínima de texto que procesa un LLM (aproximadamente una palabra corta o un fragmento de palabra). El precio se mide por millón de tokens (MTok).
- **Tokens de entrada vs. de salida:** la entrada es el texto que envías al modelo (la pregunta + contexto); la salida es el texto que el modelo genera como respuesta.
- **Prompt e instrucción de sistema:** el "prompt" es lo que pides; la instrucción de sistema es el texto fijo que define el comportamiento del modelo y que se envía en cada llamada.
- **API:** la interfaz por la que un programa llama al modelo y por la que se factura el uso.
- **Modelo alojado (hosted) vs. autoalojado (self-hosted):** usar el modelo de un proveedor por API frente a ejecutarlo en tu propia infraestructura (GPUs).

## Análisis a fondo

### 1. Niveles de modelos (tiers)

Los proveedores publican varios modelos pensados para distintas necesidades. Tomando los precios oficiales de Claude (por millón de tokens) como ejemplo claro de la estructura por niveles:

- **Insignia (flagship) — máxima capacidad:** Claude Opus, 5 USD de entrada / 25 USD de salida. Para el razonamiento más complejo.
- **Balanceado — uso general:** Claude Sonnet, 3 USD de entrada / 15 USD de salida. Para la mayoría de las cargas de trabajo en producción.
- **Ligero (lightweight) — rápido y económico:** Claude Haiku, 1 USD de entrada / 5 USD de salida. Para tareas simples y de alto volumen.

La recomendación del propio proveedor es clara: usa Haiku para tareas simples, Sonnet para la mayoría de los casos y Opus solo para el razonamiento más exigente. En todo el mercado de 2026 los precios van desde ~0,10 USD por millón de tokens de entrada en modelos económicos hasta ~30 USD en los modelos frontera de razonamiento.

### 2. Precios: entrada vs. salida

Los tokens de salida cuestan entre 2 y 6 veces más que los de entrada, porque generar texto exige más cómputo que comprenderlo. Por eso una respuesta larga puede salir mucho más cara que una pregunta larga. Existen además descuentos importantes:

- **Caché de prompts (prompt caching):** reutilizar contexto repetido puede reducir su costo a un 10 % del precio normal de entrada.
- **API por lotes (Batch API):** procesar solicitudes de forma diferida ofrece un 50 % de descuento tanto en entrada como en salida.

### 3. El iceberg de costos

El modelo más barato por token no es necesariamente el más barato por tarea. Bajo la línea de flotación se esconden costos reales:

- **Sobrecarga del prompt:** las instrucciones de sistema suelen consumir entre el 35 % y el 50 % de los tokens de entrada.
- **Reintentos:** una respuesta mala o un error obliga a repetir la llamada, multiplicando el costo.
- **Estrategia de niveles y enrutamiento (routing):** dirigir cada solicitud al modelo más adecuado según su complejidad (nivel económico ~0,25–4 USD/M, medio ~3–15 USD/M, premium ~15–75 USD/M) ha logrado reducciones de costo del 30 % al 70 % manteniendo la calidad. El enrutamiento puede fallar, eso sí, en tareas que necesitan razonamiento profundo o cuando hay muchos reintentos de respaldo (fallbacks).
- **Costo total de propiedad (TCO):** autoalojar un modelo de 7B en GPUs H100 puede costar ~0,013 USD por cada 1.000 tokens, pero la ventaja desaparece si la utilización de la GPU cae por debajo de ~70 %. A esto se suman personal de MLOps (~1 ingeniero por cada 4–6 GPUs), redundancia (10–15 %) y cumplimiento normativo. Como regla práctica: por debajo de ~50.000 USD/año de gasto en API conviene un modelo alojado barato; por encima de ~500.000 USD/año el autoalojamiento casi siempre gana en costo.
- **Dependencia del proveedor (vendor lock-in):** cambiar de proveedor es más costoso que en el software SaaS habitual, porque la lógica de negocio queda codificada en prompts y comportamientos específicos del modelo. Hay seis puntos de fricción: reescritura de prompts, diferencias en llamadas a herramientas/JSON, acoplamiento al API/SDK, reindexación de embeddings, dependencias operativas y deriva de comportamiento (behavior drift).

## Por qué le importa a un Student

Como estudiante, este tema te da la base para razonar sobre los costos antes de construir nada. Tres ideas para llevarte:

1. **No persigas el precio por token más bajo:** aprende a estimar el costo por tarea completa (entrada + salida + reintentos), no por token aislado.
2. **Elige el nivel según la dificultad:** practicar con un modelo ligero te deja experimentar mucho con poco presupuesto; reserva los modelos insignia para problemas que de verdad lo necesiten.
3. **Piensa en el largo plazo:** conceptos como TCO y dependencia del proveedor explican por qué las decisiones técnicas tienen consecuencias económicas. Entenderlos desde primeros principios te servirá tanto en proyectos personales como profesionales.

## Errores comunes

- **Confundir "más barato por token" con "más barato por tarea":** ignora el iceberg (prompts largos, reintentos) y la factura real te sorprenderá.
- **Olvidar que la salida cuesta más:** generar respuestas largas e innecesarias dispara el costo más que enviar mucho contexto.
- **No aprovechar los descuentos:** ignorar la caché de prompts (90 % de ahorro en contexto repetido) o la API por lotes (50 %) deja dinero sobre la mesa.
- **Usar siempre el modelo insignia "por seguridad":** pagar precio premium para tareas simples es desperdicio; el enrutamiento por niveles existe justamente para evitarlo.
- **Subestimar el costo de autoalojar:** el precio por token de tu propia GPU parece bajo, pero personal, redundancia y baja utilización pueden hacerlo más caro que un modelo alojado.
- **Quedar atado a un proveedor sin saberlo:** codificar todo en prompts específicos de un modelo encarece muchísimo un cambio futuro.

## Fuentes

Fuente general:
- [LLM API Pricing Comparison In 2026 (CloudZero)](https://www.cloudzero.com/blog/llm-api-pricing-comparison/) — panorama general de precios de LLM en 2026: entrada vs. salida, rango de precios y la idea del iceberg de costos.

Fuentes específicas:
- [Precios — Documentación de Claude (Anthropic)](https://platform.claude.com/docs/en/about-claude/pricing) — precios oficiales por niveles (Opus/Sonnet/Haiku), tarifas de entrada/salida, caché de prompts y descuentos por lotes.
- [AI Cost Controls: Budgets, Throttling & Model Tiering (Clarifai)](https://www.clarifai.com/blog/ai-cost-controls) — estrategia de niveles (económico/medio/premium) y reducción de costos del 30–70 % por enrutamiento.
- [LLM routing: overview, strategies, and tools (Merge.dev)](https://www.merge.dev/blog/llm-routing) — enrutamiento de solicitudes hacia el modelo más adecuado según complejidad y sus límites (razonamiento profundo, reintentos de respaldo).
- [LLM Total Cost of Ownership 2025 (Ptolemay)](https://www.ptolemay.com/post/llm-total-cost-of-ownership) — costos de infraestructura GPU, personal MLOps y umbrales de "construir vs. comprar".
- [Avoid LLM Vendor Lock-in (CustomGPT)](https://customgpt.ai/how-to-avoid-llm-vendor-lock-in/) — costos de cambio de proveedor, portabilidad de prompts y seis puntos de fricción.

## Referencias

1. CloudZero. *LLM API Pricing Comparison In 2026: Every Major Model, Ranked By Cost.* https://www.cloudzero.com/blog/llm-api-pricing-comparison/
2. Anthropic / Claude Docs. *Pricing.* https://platform.claude.com/docs/en/about-claude/pricing
3. Clarifai. *AI Cost Controls: Budgets, Throttling & Model Tiering.* https://www.clarifai.com/blog/ai-cost-controls
4. Merge.dev. *LLM routing: overview, strategies, and tools.* https://www.merge.dev/blog/llm-routing
5. Ptolemay. *LLM Total Cost of Ownership 2025: Build vs Buy Math.* https://www.ptolemay.com/post/llm-total-cost-of-ownership
6. CustomGPT. *Avoid LLM Vendor Lock-in: A Guide To Portability.* https://customgpt.ai/how-to-avoid-llm-vendor-lock-in/
