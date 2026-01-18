# Ocularis Mose 👁️🖱️

Un sistema de control de ratón mediante seguimiento ocular (eye-tracking) diseñado para permitir la navegación sin manos.

## Características
- **Control por Mirada**: Mueve el cursor del ratón simplemente mirando a diferentes partes de la pantalla.
- **Clic por Parpadeo**: Realiza clics izquierdos parpadeando de forma natural.
- **Calibración Rápida**: Sistema de 5 puntos para adaptar el seguimiento a tu posición y pantalla.
- **Suavizado Adaptativo**: Filtro de movimiento para reducir el temblor natural de los ojos.

## Requisitos
- Python 3.9+
- Webcam
- macOS / Windows / Linux

## Instalación
1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
1. Ejecuta el programa principal:
   ```bash
   python main.py
   ```
2. **Calibración**: Sigue el círculo amarillo en la pantalla y presiona la tecla `ESPACIO` en cada punto (4 esquinas y centro).
3. Una vez calibrado, el ratón seguirá tu mirada.
4. **Parpadeo**: Parpadea con el ojo izquierdo para hacer clic.

## Comandos de Teclado
- `ESPACIO`: Confirmar punto de calibración.
- `c`: Reiniciar calibración.
- `q`: Salir del programa.

---
Desarrollado con ❤️ para Iyari Cancino Gomez.
