# 🌱 Good First Issues — Ideas para Primeros Contribuidores

¿Nuevo en MOSE o en contribuciones open-source? 
¡Estos son excelentes puntos de entrada!

---

## 🎨 Categoría: Documentación

### 1. Traducir README al Inglés
**Dificultad**: 🟢 Fácil  
**Skills**: Español + Inglés  
**Descripción**: Crear un `README_EN.md` traduciendo el README actual. El proyecto es bilingüe pero falta documentación completa en inglés.  
**Archivos**: `README.md` → `README_EN.md`

### 2. Crear Tutorial en Video
**Dificultad**: 🟡 Medio  
**Skills**: Grabación de pantalla, edición básica  
**Descripción**: Grabar un video de 2-3 minutos mostrando: instalación, calibración, y uso básico de MOSE.  
**Resultado**: Video demo para YouTube/README

### 3. Documentar API de Eventos
**Dificultad**: 🟢 Fácil  
**Skills**: Python, Markdown  
**Descripción**: Crear ejemplos adicionales de uso del módulo `mose.events` con diferentes casos de uso.  
**Archivos**: `examples/api_usage_*.py`

### 4. Mejorar Comentarios en Español
**Dificultad**: 🟢 Fácil  
**Skills**: Español, lectura de código  
**Descripción**: Algunos módulos tienen comentarios en inglés. Traducir a español para consistencia.  
**Archivos**: Varios en `mose/`

---

## 💻 Categoría: Código

### 5. Agregar Tests para EventStream
**Dificultad**: 🟡 Medio  
**Skills**: Python, pytest  
**Descripción**: El nuevo módulo `mose/events.py` necesita tests unitarios. Crear `tests/test_events.py`.  
**Archivos**: Nuevo `tests/test_events.py`

### 6. Implementar Logging System
**Dificultad**: 🟡 Medio  
**Skills**: Python logging  
**Descripción**: MOSE actualmente usa prints. Migrar a sistema de logging profesional con niveles configurables.  
**Archivos**: Todos los módulos en `mose/`

### 7. Agregar Configuración de Smoothing
**Dificultad**: 🟡 Medio  
**Skills**: Python, configuración  
**Descripción**: Exponer parámetros de suavizado del cursor en `config.ini` para que usuarios puedan ajustarlos.  
**Archivos**: `mose/config.py`, `config.ini`

### 8. Crear Modo "Demo"
**Dificultad**: 🟢 Fácil  
**Skills**: Python básico  
**Descripción**: Agregar flag `--demo` que muestre MOSE funcionando con datos simulados (sin cámara). Útil para testing.  
**Archivos**: `main.py`, crear `mose/demo.py`

---

## 🎯 Categoría: Características Pequeñas

### 9. Agregar Sonido de Click
**Dificultad**: 🟡 Medio  
**Skills**: Python, audio  
**Descripción**: Reproducir sonido sutil cuando se detecta un parpadeo-click. Ayuda con feedback sensorial.  
**Archivos**: `mose/core/blink_detector.py`  
**Dependencia**: Agregar librería de audio (ej: `playsound`)

### 10. Contador de Parpadeos
**Dificultad**: 🟢 Fácil  
**Skills**: Python básico  
**Descripción**: Mostrar en pantalla cuántos parpadeos se han detectado (útil para calibrar sensibilidad).  
**Archivos**: `mose/ui/feedback_overlay.py`

### 11. Hotkey para Pausar
**Dificultad**: 🟢 Fácil  
**Skills**: Python, keyboard events  
**Descripción**: Agregar tecla para pausar/reanudar MOSE sin cerrarlo (ej: `P` para pause).  
**Archivos**: `main.py`

### 12. Modo Oscuro en Calibración
**Dificultad**: 🟢 Fácil  
**Skills**: OpenCV, UI básico  
**Descripción**: Los círculos amarillos de calibración pueden ser brillantes. Agregar variante oscura/suave.  
**Archivos**: `mose/ui/calibration.py`

---

## ♿ Categoría: Accesibilidad

### 13. Indicador Visual de Estado
**Dificultad**: 🟡 Medio  
**Skills**: OpenCV, UI  
**Descripción**: Mostrar claramente si MOSE está: sin calibrar, calibrado, tracking activo, o en pausa.  
**Archivos**: `mose/ui/feedback_overlay.py`

### 14. Ajuste de Contraste en Preview
**Dificultad**: 🟢 Fácil  
**Skills**: OpenCV  
**Descripción**: Agregar opción para aumentar contraste de video preview (ayuda en condiciones de poca luz).  
**Archivos**: `main.py`, `config.ini`

### 15. Comandos de Voz Básicos
**Dificultad**: 🔴 Difícil  
**Skills**: Python, speech recognition  
**Descripción**: Integrar reconocimiento de voz para comandos como "calibrar", "pausar", "salir".  
**Archivos**: Nuevo módulo `mose/voice.py`  
**Dependencia**: `speech_recognition`

---

## 🧪 Categoría: Testing & CI

### 16. Agregar Pre-commit Hooks
**Dificultad**: 🟢 Fácil  
**Skills**: Git, pre-commit  
**Descripción**: Configurar pre-commit para formateo automático (black, isort).  
**Archivos**: `.pre-commit-config.yaml`

### 17. GitHub Action para Tests
**Dificultad**: 🟡 Medio  
**Skills**: GitHub Actions, CI/CD  
**Descripción**: Crear workflow que corra tests automáticamente en cada PR.  
**Archivos**: `.github/workflows/test.yml`

### 18. Aumentar Cobertura de Tests
**Dificultad**: 🟡 Medio  
**Skills**: Python, pytest  
**Descripción**: Cobertura actual ~70%. Meta: 85%+. Agregar tests faltantes.  
**Archivos**: `tests/`

---

## 📦 Categoría: Infraestructura

### 19. Preparar para PyPI
**Dificultad**: 🟡 Medio  
**Skills**: Python packaging  
**Descripción**: Verificar que `setup.py` esté completo y publicar MOSE en PyPI.  
**Archivos**: `setup.py`, crear `pyproject.toml`  
**Resultado**: `pip install mose` funcionando

### 20. Crear Docker Image
**Dificultad**: 🔴 Difícil  
**Skills**: Docker, Linux  
**Descripción**: Containerizar MOSE para facilitar deployment. Desafío: acceso a cámara en Docker.  
**Archivos**: `Dockerfile`, `docker-compose.yml`

---

## 🎓 Cómo Empezar

1. **Elige un issue** que te llame la atención
2. **Comenta en el issue** diciendo que te gustaría trabajar en ello
3. **Fork el repo** y crea una branch
4. **Haz tus cambios** siguiendo [CONTRIBUTING.md](CONTRIBUTING.md)
5. **Abre un PR** con descripción clara

**¿Dudas?** Pregunta en [Discussions](https://github.com/Blackmvmba88/Mose/discussions) o en el issue mismo.

---

## 🏆 Reconocimiento

Todos los contribuidores serán:
- Listados en `CONTRIBUTORS.md`
- Mencionados en release notes
- Parte de la historia de MOSE

No necesitas ser experto. **Todos empezamos por algún lado.** 🌱

---

**MOSE** — Construido por la comunidad, para la comunidad. 🧿👁️
