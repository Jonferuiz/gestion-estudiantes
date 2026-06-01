# Changelog

Todos los cambios notables en este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere al [Versionado Semántico](https://semver.org/lang/es/).

## [1.0.0] - 2026-06-01

### Añadido
- Inicialización del proyecto de Sistema de Gestión de Estudiantes.
- Archivo `app.py` con el core de la aplicación utilizando FastAPI.
- Endpoint `GET /estudiantes` para obtener el listado general de alumnos.
- Endpoint `POST /estudiantes` para registrar un nuevo alumno con su respectiva calificación de diagnóstico.
- Endpoint `GET /estudiantes/{estudiante_id}` para consultar un alumno específico.
- Archivo `API.yaml` con la documentación técnica del contrato OpenAPI 3.0.3.
- Archivo `README.md` con las instrucciones de instalación y despliegue del entorno virtual.
- Archivo `.gitignore` configurado para proyectos en Python.
- Archivo `LICENSE` con los términos de uso (MIT).