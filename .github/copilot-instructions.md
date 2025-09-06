# Instrucciones para GitHub Copilot (repo base_koryx_agent)

Este fichero contiene recomendaciones y ejemplos para usar GitHub Copilot / Copilot Chat con este repositorio.

Propósito
- Proveer a colaboradores guías y prompts reutilizables para obtener respuestas más útiles de Copilot.
- Centralizar modos de conversación y prompts para tareas comunes (revisión de código, diseño, generación de tests, etc.).

Recomendaciones rápidas
- Instala y autoriza la extensión GitHub Copilot en VS Code.
- Activa las sugerencias en línea (ya hay ajustes en `.vscode/settings.json`).
- Usa los `chatmodes` para escenarios repetibles (por ejemplo: revisión de código).
- Reutiliza los prompts en `.github/prompts/` para solicitudes consistentes.

Formato y convención
- `chatmodes/` contiene descripciones cortas de modos (human-readable) que puedes pegar en Copilot Chat.
- `prompts/` contiene prompts reutilizables (plantillas) para PRs, issues, tareas de diseño o generación de tests.
- `workflow/` contiene plantillas y notas para automatizar tareas relacionadas con asistentes o integración con herramientas.

Ejemplos rápidos
- Revisión de código: copia el contenido de `chatmodes/code-review.md` en Copilot Chat y añade el PR/archivo que quieres revisar.
- Nuevo feature: usa `prompts/new-feature.md` para describir requerimientos y obtener un plan de implementación.

Privacidad
- No incluyas secretos, tokens o datos sensibles en los prompts o archivos dentro de este repositorio.

Contribuciones
- Si añades nuevas plantillas o modos, explica el propósito en el README correspondiente y añade ejemplos de uso.
