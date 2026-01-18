# 🧪 Guía de Testing - Ocularis Mose

## 🎯 Visión General

El sistema de pruebas de Ocularis Mose está diseñado para garantizar la calidad, precisión y robustez del control ocular. Esta guía te ayudará a ejecutar, entender y extender el sistema de pruebas.

## 📊 Estadísticas Actuales

- **23 pruebas** implementadas
- **44% cobertura** de código
- **100% éxito** en todas las pruebas
- **3 categorías** de pruebas (unitarias, integración, manejo de errores)

## 🚀 Inicio Rápido

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar Todas las Pruebas

```bash
# Método 1: Usando el script test runner
python run_tests.py

# Método 2: Usando pytest directamente
pytest tests/

# Método 3: Usando unittest
python -m unittest discover tests/
```

## 📋 Comandos Útiles

### Ejecutar con Cobertura

```bash
python run_tests.py
# o
pytest tests/ --cov=main --cov-report=html
```

### Ejecutar Pruebas Específicas

```bash
# Solo pruebas unitarias
pytest tests/test_ocularis_mose.py

# Solo pruebas de integración
pytest tests/test_integration.py

# Una prueba específica
pytest tests/test_ocularis_mose.py::TestOcularisMose::test_initialization
```

### Modo Verbose

```bash
pytest tests/ -v
pytest tests/ -vv  # Extra verbose
```

### Ver Salida de Print

```bash
pytest tests/ -s
```

### Detener en el Primer Fallo

```bash
pytest tests/ -x
```

## 🧩 Estructura de Pruebas

```
tests/
├── __init__.py              # Inicialización del paquete
├── conftest.py             # Configuración y mocks de pytest
├── test_ocularis_mose.py   # Pruebas unitarias (12 tests)
├── test_integration.py      # Pruebas de integración (11 tests)
└── README.md               # Documentación detallada
```

## ✅ Categorías de Pruebas

### 1. Pruebas Unitarias (12 tests)

**TestOcularisMose** - Funcionalidad básica
- ✅ `test_initialization` - Inicialización correcta
- ✅ `test_calibration_targets` - Objetivos de calibración
- ✅ `test_eye_ratio_calculation` - Cálculo de ratio de ojo
- ✅ `test_calibrate_single_point` - Calibración punto individual
- ✅ `test_calibrate_complete` - Calibración completa
- ✅ `test_smoothing_buffer` - Buffer de suavizado
- ✅ `test_coordinate_normalization` - Normalización de coordenadas
- ✅ `test_blink_threshold` - Umbral de parpadeo
- ✅ `test_click_cooldown` - Cooldown de clics
- ✅ `test_screen_dimensions` - Dimensiones de pantalla

**TestCalibrationSystem** - Sistema de calibración
- ✅ `test_calibration_reset` - Reset de calibración
- ✅ `test_calibration_range_calculation` - Cálculo de rangos

**TestSmoothingSystem** - Sistema de suavizado
- ✅ `test_smoothing_buffer_averaging` - Promediado de buffer
- ✅ `test_buffer_size_limit` - Límite de tamaño
- ✅ `test_buffer_fifo_behavior` - Comportamiento FIFO

### 2. Pruebas de Integración (8 tests)

**TestIntegration** - Flujos completos
- ✅ `test_complete_calibration_workflow` - Workflow de calibración
- ✅ `test_cursor_movement_after_calibration` - Movimiento del cursor
- ✅ `test_smoothing_integration` - Integración de suavizado
- ✅ `test_blink_detection_with_cooldown` - Detección de parpadeo
- ✅ `test_recalibration_workflow` - Re-calibración

**TestErrorHandling** - Manejo de errores
- ✅ `test_eye_ratio_with_minimal_landmarks` - Datos mínimos
- ✅ `test_coordinate_clamping_extreme_values` - Valores extremos
- ✅ `test_empty_smoothing_buffer` - Buffer vacío

## 📈 Reporte de Cobertura

La cobertura actual es del **44%**. Las líneas no cubiertas son principalmente:
- El método `run()` (loop principal de GUI)
- Manejo de eventos de teclado
- Renderizado de OpenCV

Esto es esperado ya que estas partes requieren una GUI activa y no son apropiadas para pruebas unitarias automáticas.

### Ver Reporte HTML

```bash
pytest tests/ --cov=main --cov-report=html
# Abrir htmlcov/index.html en un navegador
```

## 🔍 Debugging de Pruebas

### Ver Traceback Completo

```bash
pytest tests/ --tb=long
```

### Entrar en Debugger al Fallar

```bash
pytest tests/ --pdb
```

### Mostrar Variables Locales

```bash
pytest tests/ -l
```

## 🎨 Escribir Nuevas Pruebas

### Template Básico

```python
def test_nueva_funcionalidad(self):
    """Descripción clara de lo que se prueba"""
    # Arrange - Preparar
    input_data = ...
    
    # Act - Ejecutar
    result = self.mose.some_method(input_data)
    
    # Assert - Verificar
    self.assertEqual(result, expected_value)
```

### Mejores Prácticas

1. **Nombres descriptivos**: `test_calibration_with_five_points` ✅
2. **Una aserción principal**: Facilita identificar fallos
3. **Independencia**: Cada prueba debe ser auto-contenida
4. **Arrange-Act-Assert**: Estructura clara
5. **Datos realistas**: Usar valores que ocurrirían en uso real

### Ejemplo Completo

```python
def test_cursor_position_after_calibration(self):
    """Test that cursor position is correctly mapped after calibration"""
    # Arrange: Complete calibration
    calibration_points = [
        (0.1, 0.1), (0.9, 0.1), (0.1, 0.9), 
        (0.9, 0.9), (0.5, 0.5)
    ]
    for point in calibration_points:
        self.mose.calibrate(point[0], point[1])
    
    # Act: Simulate gaze at center
    gaze_x, gaze_y = 0.5, 0.5
    norm_x = (gaze_x - self.mose.min_x) / (self.mose.max_x - self.mose.min_x)
    
    # Assert: Normalized position should be centered
    self.assertAlmostEqual(norm_x, 0.5, places=1)
    self.assertTrue(self.mose.calibrated)
```

## 🤖 Integración Continua (CI/CD)

El proyecto incluye GitHub Actions para ejecutar pruebas automáticamente:

```yaml
# .github/workflows/tests.yml
- Ejecuta en: Ubuntu, macOS, Windows
- Python: 3.9, 3.10, 3.11, 3.12
- Se activa con: push, pull request
```

### Ver Resultados de CI

Los resultados aparecen en:
- Pull Requests (checks)
- Actions tab en GitHub

## 🐛 Solución de Problemas

### Error: "No module named 'tkinter'"

**Solución**: Los tests usan mocks y no requieren tkinter. Si aparece este error, verifica que `conftest.py` esté presente.

### Error: "DISPLAY not found"

**Solución**: Los mocks en `conftest.py` evitan este problema. Si persiste, verifica la configuración de pytest.

### Pruebas Lentas

**Solución**: 
```bash
# Ejecutar solo pruebas rápidas
pytest tests/ -m "not slow"
```

## 📚 Recursos Adicionales

- [Pytest Documentation](https://docs.pytest.org/)
- [Python unittest](https://docs.python.org/3/library/unittest.html)
- [Coverage.py](https://coverage.readthedocs.io/)

## 🎯 Objetivos Futuros

- [ ] Aumentar cobertura a >60%
- [ ] Agregar pruebas de rendimiento (benchmark)
- [ ] Pruebas de precisión con datasets
- [ ] Pruebas de estrés (sesiones largas)
- [ ] Pruebas de compatibilidad con diferentes webcams

## 🤝 Contribuir

Al agregar nueva funcionalidad:

1. ✍️ Escribe la prueba primero (TDD)
2. 💻 Implementa la funcionalidad
3. ✅ Verifica que pase la prueba
4. 🔄 Verifica que otras pruebas sigan pasando
5. 📊 Mantén la cobertura >40%

---

**Sistema de Testing v1.0**

*"La confianza sin validación es solo esperanza."*

🧿 **Ocularis Mose** - Donde la mirada se encuentra con la acción.
