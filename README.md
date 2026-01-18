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

## 🧪 Testing

MOSE incluye un sistema de pruebas completo con 23 tests:

```bash
# Ejecutar todas las pruebas
python run_tests.py

# O con pytest
pytest tests/

# Ver cobertura
pytest tests/ --cov=main --cov-report=html
```

Para más información, consulta [TESTING.md](TESTING.md).

---

## 🌌 ¿Por qué existe MOSE?

Porque:

* No todos pueden usar un mouse tradicional
* La tecnología debe adaptarse al humano, no al revés
* El cuerpo es una interfaz válida
* Mirar **también** es una forma de actuar

MOSE es un paso pequeño hacia interfaces más **orgánicas, accesibles y humanas**.

---

## 🌌 Hacia dónde vamos

MOSE no es un mouse alternativo.
Es un intento de demostrar que el cuerpo ya es una interfaz.

Próximas etapas visualizadas:

* 🧠 **Aprendizaje por usuario** → Calibración persistente que mejora con el tiempo
* 👁️ **Gesto ocular compuesto** → Doble parpadeo, mirada sostenida, patrones de movimiento
* 🔌 **API para aplicaciones externas** → Otros programas pueden recibir eventos oculares
* 🤖 **Integración con asistentes IA** → "Mirar + comando" = cyborg vibes
* 🌐 **Modo navegación web** → Navegar internet sin manos, con gestos específicos
* 🎨 **Modo creación** → Herramientas optimizadas para diseño, dibujo y edición

Cuando mirar sea suficiente para actuar, la pantalla dejará de ser un objeto
y se convertirá en extensión del sistema nervioso.

---

## 🧬 Estado del proyecto

MOSE está vivo, funciona y evoluciona.

Para ver la hoja de ruta completa, consulta la sección **"Hacia dónde vamos"** arriba.

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
