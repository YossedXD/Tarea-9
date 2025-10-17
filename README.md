## Proyecto de Simulación en Docker: Brazo Robótico y Pista de Carreras

##  Descripción general
Este proyecto implementa dos simulaciones interactivas en Python utilizando **Tkinter** y **PyBullet**, ambas desplegadas en contenedores **Docker**.

1. **Pista de Carreras (Tkinter):** un entorno gráfico con una pista pentagonal y un carro que se mueve automáticamente.  
2. **Brazo Robótico (PyBullet):** simulación 3D de un brazo KUKA IIWA controlado por movimiento sinusoidal.

---

## Requisitos previos

### En Windows
1. Instalar Docker Desktop desde: https://www.docker.com/products/docker-desktop/
2. Instalar VcXsrv desde: https://sourceforge.net/projects/vcxsrv/
3. Al iniciar VcXsrv, marcar la opción “Disable access control”.

### En Linux
1. Instalar Docker desde el gestor de paquetes.
2. Habilitar la conexión al servidor X11:
   xhost +local:docker

---

##  Construcción y ejecución

### Pista de Carreras (Tkinter)

Dockerfile:
FROM python:3.10-slim

RUN apt-get update && apt-get install -y python3-tk python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY piiista.py .

CMD ["python", "piiista.py"]

Construir la imagen:
docker build -t pista-pentagono .

Ejecutar (Windows):
docker run -it --rm -e DISPLAY=host.docker.internal:0.0 pista-pentagono

Ejecutar (Linux):
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix pista-pentagono

---

### Brazo Robótico (PyBullet)

Dockerfile.brazo:
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    xvfb \
    x11-apps \
    libgl1-mesa-glx \
    && pip install pybullet \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY brazo.py .

CMD ["python", "brazo.py"]

Construir la imagen:
docker build -t brazo-pybullet -f Dockerfile.brazo .

Ejecutar (Windows):
1. Abrir VcXsrv (Disable access control).
2. Ejecutar:
   docker run -it --rm -e DISPLAY=host.docker.internal:0.0 brazo-pybullet

Ejecutar (Linux):
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix brazo-pybullet

---

## Resultados esperados
- Pista: una ventana Tkinter que muestra una pista pentagonal y un carro rojo moviéndose automáticamente por el borde.  
- Brazo: una ventana de PyBullet GUI con el modelo KUKA IIWA realizando movimientos suaves de articulaciones.

---

##  Solución de problemas
- Error: “failed to build: the Dockerfile cannot be empty” → Asegúrate de que el archivo Dockerfile tenga contenido.
- No se ve la ventana gráfica en Windows → abrir VcXsrv con “Disable access control”.
- No se ve en Linux → ejecutar xhost +local:docker antes del docker run.

---

##  Referencias
- PyBullet Documentation: https://pybullet.org/wordpress/  
- Tkinter Python Docs: https://docs.python.org/3/library/tkinter.html  
- Docker Docs: https://docs.docker.com/

---

## Autores
Yossed Riaño  
Jeferson Hernández  
Miguel Montaña  
Proyecto de Simulación en Docker – 2025  
Universidad Santo Tomás

---

