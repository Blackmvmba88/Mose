# 🧪 Sistema de Pruebas - Ocularis Mose

## 📋 Descripción

Este sistema de pruebas proporciona una cobertura completa para validar la funcionalidad del sistema de seguimiento ocular Ocularis Mose. El sistema está diseñado para garantizar la calidad, precisión y robustez del código.

## 🎯 Objetivos

1. **Validar funcionalidad core**: Asegurar que todos los componentes principales funcionan correctamente
2. **Garantizar precisión**: Verificar que los cálculos de coordenadas y mapeo son exactos
3. **Prevenir regresiones**: Detectar errores cuando se realizan cambios en el código
4. **Documentar comportamiento**: Las pruebas sirven como documentación ejecutable

## 🏗️ Estructura de Pruebas

```
tests/
├── __init__.py                 # Inicialización del paquete de pruebas
├── test_ocularis_mose.py       # Pruebas unitarias de componentes individuales
├── test_integration.py         # Pruebas de integración de flujos completos
└── README.md                   # Esta documentación
```

## 🧩 Tipos de Pruebas

### 1. Pruebas Unitarias (`test_ocularis_mose.py`)

Validan componentes individuales de forma aislada:

- **TestOcularisMose**: Pruebas de inicialización y configuración básica
  - Inicialización correcta de parámetros
  - Objetivos de calibración
  - Cálculo de ratio de ojos (detección de parpadeo)
  - Sistema de calibración por puntos
  - Buffer de suavizado
  - Normalización de coordenadas
  - Umbrales de detección

- **TestCalibrationSystem**: Pruebas del sistema de calibración
  - Reset de calibración
  - Cálculo de rangos min/max
  - Validación de puntos de calibración

- **TestSmoothingSystem**: Pruebas del sistema de suavizado
  - Promediado de buffer
  - Límites de tamaño del buffer
  - Comportamiento FIFO (First In First Out)

### 2. Pruebas de Integración (`test_integration.py`)

Validan flujos de trabajo completos:

- **TestIntegration**: Flujos de trabajo end-to-end
  - Workflow completo de calibración
  - Movimiento del cursor post-calibración
  - Integración del sistema de suavizado
  - Detección de parpadeo con cooldown
  - Re-calibración

- **TestErrorHandling**: Manejo de casos extremos
  - Cálculo con datos mínimos
  - Valores extremos de coordenadas
  - Buffers vacíos

## 🚀 Ejecución de Pruebas

### Método 1: Usando el script de test runner (Recomendado)

```bash
# Ejecutar todas las pruebas con reporte de cobertura
python run_tests.py

# Ejecutar solo pruebas unitarias
python run_tests.py tests/test_ocularis_mose.py

# Ejecutar solo pruebas de integración
python run_tests.py tests/test_integration.py

# Ejecutar con más verbosidad
python run_tests.py -vv

# Ejecutar una prueba específica
python run_tests.py tests/test_ocularis_mose.py::TestOcularisMose::test_initialization
```

### Método 2: Usando pytest directamente

```bash
# Ejecutar todas las pruebas
pytest tests/

# Con reporte de cobertura
pytest tests/ --cov=main --cov-report=term-missing

# Ejecutar solo pruebas que coincidan con un patrón
pytest tests/ -k "calibration"

# Modo verbose
pytest tests/ -v

# Detener en el primer fallo
pytest tests/ -x

# Mostrar print statements
pytest tests/ -s
```

### Método 3: Usando unittest directamente

```bash
# Ejecutar archivo de pruebas específico
python -m unittest tests.test_ocularis_mose

# Ejecutar clase de pruebas específica
python -m unittest tests.test_ocularis_mose.TestOcularisMose

# Ejecutar prueba individual
python -m unittest tests.test_ocularis_mose.TestOcularisMose.test_initialization
```

## 📊 Cobertura de Código

El sistema de pruebas genera reportes de cobertura para identificar áreas no probadas:

```bash
# Generar reporte de cobertura
pytest tests/ --cov=main --cov-report=html

# Ver el reporte
# Abrir htmlcov/index.html en un navegador
```

### Métricas de Cobertura

- **Objetivo**: >80% de cobertura de líneas
- **Crítico**: 100% en funciones de calibración y detección
- **Reporte**: Generado automáticamente en `htmlcov/`

## �� Interpretación de Resultados

### Ejemplo de salida exitosa:

```
============================= test session starts ==============================
collected 20 items

tests/test_ocularis_mose.py::TestOcularisMose::test_initialization PASSED [ 5%]
tests/test_ocularis_mose.py::TestOcularisMose::test_calibration_targets PASSED [10%]
...
========================== 20 passed in 2.34s ===============================
```

### Ejemplo de salida con fallo:

```
FAILED tests/test_ocularis_mose.py::TestOcularisMose::test_initialization
AssertionError: False != True
```

## 🛠️ Agregar Nuevas Pruebas

### Template para prueba unitaria:

```python
def test_nueva_funcionalidad(self):
    """Descripción de lo que prueba"""
    # Arrange: Preparar datos de prueba
    input_data = ...
    
    # Act: Ejecutar la función a probar
    result = self.mose.nueva_funcion(input_data)
    
    # Assert: Verificar el resultado
    self.assertEqual(result, expected_value)
```

### Buenas prácticas:

1. **Nombres descriptivos**: `test_calibration_with_five_points` mejor que `test1`
2. **Una aserción principal por prueba**: Facilita identificar fallos
3. **Arrange-Act-Assert**: Estructura clara en tres pasos
4. **Datos de prueba realistas**: Usar valores que ocurrirían en uso real
5. **Independencia**: Cada prueba debe poder ejecutarse sola

## 🐛 Debugging de Pruebas

### Ver más detalles de fallos:

```bash
pytest tests/ -vv --tb=long
```

### Ejecutar con debugger:

```bash
pytest tests/ --pdb
```

### Ver output de print:

```bash
pytest tests/ -s
```

## ⚙️ Configuración

La configuración de pytest está en `pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

## 🎯 Métricas de Éxito

Las pruebas validan los siguientes criterios:

- ✅ **Inicialización**: Sistema inicia en estado correcto
- ✅ **Calibración**: 5 puntos mapean correctamente el rango
- ✅ **Precisión**: Coordenadas se normalizan correctamente
- ✅ **Suavizado**: Buffer mantiene tamaño y promedia correctamente
- ✅ **Detección**: Parpadeos detectados respetan cooldown
- ✅ **Robustez**: Sistema maneja casos extremos sin fallar

## 📈 Mejoras Futuras

- [ ] Pruebas de rendimiento (FPS, latencia)
- [ ] Pruebas con datos de cámara simulados
- [ ] Pruebas de compatibilidad multiplataforma
- [ ] Pruebas de estrés con sesiones prolongadas
- [ ] Benchmarking de precisión con datasets estándar

## 🤝 Contribuir

Al agregar nueva funcionalidad:

1. Escribir la prueba primero (TDD)
2. Implementar la funcionalidad
3. Verificar que la prueba pasa
4. Verificar que todas las demás pruebas siguen pasando
5. Mantener cobertura >80%

## 📚 Referencias

- [pytest documentation](https://docs.pytest.org/)
- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [Python testing best practices](https://docs.python-guide.org/writing/tests/)

---

**Sistema de Pruebas Ocularis Mose v1.0**

*"La confianza sin validación es solo esperanza."*
