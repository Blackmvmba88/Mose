# 🧿 MOSE — El ratón que obedece a la mirada

> **Controla la computadora sin manos.
> Sin hardware especial.
> Solo tus ojos.**

---

## ⚔️ ¿Qué es MOSE?

**MOSE** no es solo un programa.
Es una **extensión del cuerpo humano**.

Un sistema de **control de cursor por seguimiento ocular** que convierte tu mirada en movimiento y tus parpadeos en acción.
Mirar es apuntar.
Parpadear es decidir.

MOSE nace donde convergen:

* Visión por computadora 👁️
* Neurociencia práctica 🧠
* Accesibilidad real ♿
* Y una pizca de rebeldía tecnológica 🚀

---

## 🧠 ¿Cómo funciona?

MOSE utiliza la cámara de tu computadora para:

1. Detectar tu rostro en tiempo real
2. Seguir la posición de tus ojos con precisión
3. Traducir la dirección de tu mirada en movimiento del cursor
4. Interpretar parpadeos como **clics conscientes**

Todo ocurre **en tiempo real**, sin sensores externos, sin cascos, sin implantes.
Solo tú y la máquina llegando a un acuerdo.

---

## 🎯 Características principales

• 🖱️ Movimiento del cursor controlado por la mirada
• 👀 Clic mediante parpadeo
• 🎯 Sistema de **calibración en 5 puntos**
• 🌊 Suavizado adaptativo del movimiento
• 🧪 Hecho en **Python 3.9+**
• 💻 Compatible con **Windows, macOS y Linux**

---

## 🔧 Requisitos

* Python **3.9 o superior**
* Cámara web funcional (480p mínimo, 720p+ recomendado)
* Un entorno con buena iluminación
* 4GB RAM mínimo (8GB recomendado)

---

## 📦 Instalación

### Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/Blackmvmba88/Mose.git
cd Mose

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar MOSE
python main.py
```

### Instalación Detallada

Para instrucciones completas específicas de tu plataforma (Windows/macOS/Linux), 
consulta **[INSTALLATION.md](INSTALLATION.md)**.

---

## 🚀 Uso

### Inicio Rápido

```bash
# Versión original (monolítica)
python main.py

# O versión modular (mejor organizada)
python main_modular.py
```

> **Nota**: Ambas versiones funcionan de la misma manera. La versión modular (`main_modular.py`) 
> tiene mejor organización del código pero la funcionalidad es idéntica. Usa la que prefieras.

### Calibración

1. Presiona **'c'** para iniciar la calibración
2. Aparecerán 5 círculos amarillos en la pantalla
3. Mira directamente cada círculo y presiona **ESPACIO**
4. Repite para los 5 puntos (esquinas y centro)
5. ¡Calibración completa! Ahora controla el cursor con tu mirada

### Controles

- **'c'**: Iniciar/reiniciar calibración
- **'q'**: Salir de MOSE
- **Parpadeo rápido**: Hacer clic

### Consejos para Mejor Rendimiento

- Mantén tu rostro bien iluminado
- Evita luz directa detrás de ti (contraluz)
- Mantén distancia de 40-80cm de la cámara
- Mantén tu cabeza relativamente estable
- Si el cursor está nervioso, aumenta el `smoothing_buffer_size` en `config.ini`
- Si hay mucho lag, reduce el `smoothing_buffer_size`

---

## 🌌 ¿Por qué existe MOSE?

Porque:

* No todos pueden usar un mouse tradicional
* La tecnología debe adaptarse al humano, no al revés
* El cuerpo es una interfaz válida
* Mirar **también** es una forma de actuar

MOSE es un paso pequeño hacia interfaces más **orgánicas, accesibles y humanas**.

---

## 📚 Documentación

- **[README.md](README.md)**: Este archivo - visión general del proyecto
- **[INSTALLATION.md](INSTALLATION.md)**: Guía de instalación detallada para todas las plataformas
- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Documentación técnica del sistema
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Guía para contribuir al proyecto
- **[CHANGELOG.md](CHANGELOG.md)**: Historial de cambios y versiones

---

## 🏗️ Arquitectura del Proyecto

MOSE está organizado en módulos:

```
mose/
├── core/                    # Funcionalidad principal
│   ├── face_detection.py   # Detección facial con MediaPipe
│   ├── eye_tracking.py     # Seguimiento de iris
│   ├── blink_detector.py   # Detección de parpadeos
│   └── gaze_to_cursor.py   # Mapeo mirada→cursor
└── ui/                      # Interfaz de usuario
    ├── calibration.py      # Sistema de calibración
    └── feedback_overlay.py # Retroalimentación visual
```

**Tecnologías Clave:**
- **MediaPipe Face Mesh**: Detección de 478 puntos faciales
- **OpenCV**: Procesamiento de video
- **PyAutoGUI**: Control del cursor y clics
- **NumPy**: Procesamiento numérico

Para detalles técnicos completos, consulta **[ARCHITECTURE.md](ARCHITECTURE.md)**.

---

## ⚙️ Configuración

Puedes ajustar el comportamiento de MOSE editando `config.ini`:

```ini
[blink]
threshold = 0.0045        # Sensibilidad de clic (menor = más fácil)
cooldown = 0.3            # Tiempo entre clics (segundos)

[gaze]
smoothing_buffer_size = 8 # Suavizado (mayor = más suave, más lag)
```

---

## 🧬 Estado del proyecto

MOSE está vivo, funciona y evoluciona.

### Versión Actual: 1.1.0

**Completado:**
- ✅ Sistema de seguimiento ocular funcional
- ✅ Calibración de 5 puntos
- ✅ Detección de parpadeos para clics
- ✅ Arquitectura modular
- ✅ Documentación completa

**Roadmap:**

#### v1.2 (Próximo)
- [ ] Filtro de Kalman para mejor suavizado
- [ ] Soporte multi-idioma (ES/EN/PT)
- [ ] Tutorial en video
- [ ] Métricas de rendimiento

#### v2.0 (Futuro)
- [ ] Soporte multi-monitor
- [ ] Doble parpadeo y otros gestos
- [ ] Calibración adaptativa
- [ ] Zonas configurables
- [ ] Retroalimentación auditiva

Ver **[CHANGELOG.md](CHANGELOG.md)** para historial completo.

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Ya sea reportando bugs, sugiriendo mejoras, 
o contribuyendo código.

**Formas de contribuir:**
- 🐛 Reportar bugs usando las [plantillas de issues](.github/ISSUE_TEMPLATE/)
- 💡 Sugerir nuevas funcionalidades
- 📖 Mejorar la documentación
- 🔧 Enviar pull requests
- 🌍 Ayudar con traducciones

Lee **[CONTRIBUTING.md](CONTRIBUTING.md)** para más detalles.

---

## 🏷️ Etiquetas del Proyecto

`accessibility` `assistive-technology` `eye-tracking` `computer-vision` 
`mediapipe` `opencv` `hci` `human-computer-interaction` `python` 
`gaze-tracking` `assistive-tech` `disability-support` `open-source`

---

## 📸 Screenshots y Demo

*[Próximamente: Video demo y capturas de pantalla del proceso de calibración]*

### Cómo usar MOSE

1. **Iniciar**: Ejecuta `python main.py`
2. **Calibrar**: Mira los 5 puntos y presiona ESPACIO en cada uno
3. **¡Controlar!**: Mueve tu mirada para mover el cursor, parpadea para hacer clic

---

## 🔬 Para Investigadores

MOSE incluye documentación técnica detallada sobre:
- Parámetros temporales de detección de parpadeo
- Algoritmos de suavizado (Moving Average, futuro: Kalman)
- Métricas de precisión y rendimiento
- Pipeline de procesamiento completo

Consulta **[ARCHITECTURE.md](ARCHITECTURE.md)** para información científica y técnica.

---

## ❤️ Dedicatoria

Este proyecto está hecho con amor y dedicación.
Dedicado a **Iyari Cancino Gomez**.

Para cada persona que alguna vez sintió que la tecnología no estaba diseñada para ellos.
Este templo también es tuyo.

---

## 📜 Licencia

MOSE está licenciado bajo **GNU General Public License v3.0 (GPL-3.0)**.

Esto significa que:
- ✅ Puedes usarlo libremente
- ✅ Puedes estudiarlo y modificarlo
- ✅ Puedes redistribuirlo
- ✅ Puedes distribuir versiones modificadas

Bajo la condición de que tus modificaciones también sean GPL-3.0.

Ver [LICENSE](LICENSE) para el texto completo.

---

## 🙏 Agradecimientos

- **MediaPipe**: Por la increíble tecnología de Face Mesh
- **OpenCV**: Por las herramientas de visión por computadora
- **La comunidad de código abierto**: Por hacer esto posible

---

## 📞 Contacto y Soporte

- **Issues**: [GitHub Issues](https://github.com/Blackmvmba88/Mose/issues)
- **Discusiones**: [GitHub Discussions](https://github.com/Blackmvmba88/Mose/discussions)
- **Email**: [Próximamente]

---

**MOSE** — Donde la mirada se encuentra con la acción. 🧿👁️

*Versión 1.1.0 - Actualizado: Enero 2026*
