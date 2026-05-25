# Estructura del curso, entregable y puente hacia la Semana 3

_Cubre las diapositivas: 1, 3, 4, 16, 17, 21, 22._

## Resumen

Este tema explica cómo está organizado el curso y hacia dónde te lleva. La Semana 2 cierra los fundamentos de la inteligencia artificial y prepara el terreno para la Semana 3, donde el foco se mueve hacia el **desarrollo asistido por IA**: usar herramientas que convierten descripciones en lenguaje natural en aplicaciones funcionales. El entregable del curso es el momento en que aplicas lo aprendido construyendo algo real, normalmente con un constructor de aplicaciones sin código o un entorno de programación con agentes. El "puente" hacia la Semana 3 consiste en familiarizarte de antemano con el vocabulario y las herramientas (Replit, Cursor, Lovable, GitHub Copilot, Claude Code) que usarás para pasar de entender la IA a construir con ella.

## Conceptos previos

Antes de abordar este tema conviene tener claros estos conceptos:

- **Modelo de lenguaje grande (LLM):** un sistema de IA que genera texto —incluido código fuente— a partir de instrucciones escritas en lenguaje natural.
- **Vibe coding (programación por intención):** describir un proyecto en lenguaje natural a un LLM para que genere automáticamente el código; el término fue acuñado por Andrej Karpathy en febrero de 2025.
- **Constructores de aplicaciones sin código (no-code):** plataformas que permiten a personas no programadoras crear aplicaciones completas a partir de un *prompt* (por ejemplo, Bolt.new o Replit Agent).
- **Entornos de programación con agentes:** herramientas que leen una base de código, editan archivos y ejecutan comandos de forma autónoma (por ejemplo, Cursor y Claude Code).
- **Nociones básicas de GitHub/control de versiones:** la idea de guardar cambios, crear ramas y abrir solicitudes de incorporación de cambios (*pull requests*).

## Análisis a fondo

La estructura del curso sigue una progresión lógica: primero entender qué es la IA y cómo funciona (fundamentos), y luego usarla para construir software (desarrollo asistido por IA). El entregable y el puente hacia la Semana 3 son las dos piezas que conectan ambas mitades.

**El cambio de fundamentos a construir.** El *vibe coding* es el concepto que articula este cambio. Consiste en describir lo que quieres en lenguaje natural y dejar que un LLM genere el código por ti; en la práctica, quien programa así suele aceptar la salida de la IA e iterar mediante nuevas indicaciones de seguimiento. El término ganó tanta tracción que fue la Palabra del Año 2025 del Collins English Dictionary. Para un estudiante, lo importante es que ya no necesitas dominar la sintaxis de un lenguaje para crear una primera aplicación funcional.

**El entregable: construir con herramientas sin código.** El entregable del curso te pide aplicar lo aprendido construyendo algo real. Las herramientas sin código hacen esto posible: permiten enviar aplicaciones de pila completa (*full-stack*) partiendo de un *prompt*. Gartner proyecta que las herramientas de bajo código representarán el 75 % del desarrollo de nuevas aplicaciones en 2026, lo que muestra por qué el curso invierte en enseñarlas. Dos ejemplos concretos:

- **Bolt.new** está optimizado para prototipos rápidos y compartibles; su capa Bolt Cloud (lanzada a mediados de 2025) añadió alojamiento, bases de datos y autenticación.
- **Replit Agent** convierte descripciones en inglés sencillo en aplicaciones que funcionan: escribe el código, configura la infraestructura, prueba y despliega, sin necesidad de saber programar. Ofrece un modo Plan y modos de construcción Lite/Economy/Power.

**El puente hacia la Semana 3: entornos con agentes y GitHub.** Más allá de los constructores sin código, la Semana 3 introduce entornos de programación con agentes, donde la IA trabaja directamente sobre una base de código real:

- **Claude Code** es una herramienta de programación con agentes que lee tu base de código, edita archivos, ejecuta comandos y se integra con tus herramientas de desarrollo en la terminal, el IDE, el escritorio y la web. Trabaja directamente con git: prepara cambios, redacta mensajes de confirmación (*commits*), crea ramas y abre *pull requests*, e incluso puede automatizar revisiones mediante GitHub Actions. De ahí que la preparación del entorno de GitHub forme parte del puente.
- **Cursor**, en cambio, está centrado en el IDE (es una bifurcación de VS Code con autocompletado, diferencias en línea y chat multimodelo). Claude Code está centrado en el agente (refactorización autónoma de varios archivos, terminal/CLI). Los usuarios avanzados a menudo usan ambas juntas, en un patrón de programación en pareja (*pair programming*).

En conjunto, este tema te da el mapa: sabes qué construir (el entregable), con qué herramientas (sin código y con agentes) y por qué (el paso de comprender la IA a desarrollar con ella en la Semana 3).

## Por qué le importa a un Student

Como estudiante, este tema responde a la pregunta práctica "¿qué tengo que entregar y cómo me preparo?". Saber de antemano que la Semana 3 usará herramientas como Replit, Cursor, Lovable y Claude Code te permite explorar sus versiones gratuitas con tiempo, en lugar de aprenderlas bajo presión. Además, entender el *vibe coding* desde el principio te quita el miedo: no necesitas ser programador experto para completar el entregable; necesitas saber describir con claridad lo que quieres y aprender a iterar sobre lo que la IA genera. Esa habilidad —comunicar intención y refinar resultados— es transferible a casi cualquier herramienta de IA que uses después.

## Errores comunes

- **Confiar ciegamente en lo que genera la IA.** El *vibe coding* invita a aceptar la salida e iterar, pero conviene leer y entender lo que se produce; aceptar código sin revisarlo lleva a errores difíciles de corregir.
- **Confundir las categorías de herramientas.** Los constructores sin código (Bolt.new, Replit Agent) sirven para crear aplicaciones desde un *prompt*; los entornos con agentes (Cursor, Claude Code) trabajan sobre una base de código existente. Elegir la herramienta equivocada para tu entregable cuesta tiempo.
- **Dejar la configuración de GitHub para el final.** Parte del puente hacia la Semana 3 es tener listo el entorno de control de versiones; posponerlo bloquea el trabajo con agentes que abren ramas y *pull requests*.
- **Pensar que "sin código" significa "sin esfuerzo".** Sigues necesitando una idea clara, *prompts* bien redactados y varias iteraciones para llegar a un resultado útil.

## Fuentes

Fuente general:
- [Vibe coding — Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding)

Fuentes específicas:
- [Best AI App Builders in 2026 (guía de Lovable)](https://lovable.dev/guides/best-ai-app-builders)
- [Replit Agent (documentación oficial)](https://docs.replit.com/replitai/agent)
- [Claude Code: Overview (documentación oficial de Claude)](https://code.claude.com/docs/en/overview)
- [Claude Code vs Cursor: comparación 2026 (Builder.io)](https://www.builder.io/blog/cursor-vs-claude-code)

## Referencias

1. Wikipedia. *Vibe coding*. https://en.wikipedia.org/wiki/Vibe_coding
2. Lovable. *Best AI App Builders in 2026*. https://lovable.dev/guides/best-ai-app-builders
3. Replit. *Replit Agent (documentación oficial)*. https://docs.replit.com/replitai/agent
4. Claude Docs. *Claude Code: Overview*. https://code.claude.com/docs/en/overview
5. Builder.io. *Claude Code vs Cursor: 2026 comparison*. https://www.builder.io/blog/cursor-vs-claude-code
