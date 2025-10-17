import pybullet as p
import pybullet_data
import time
import math

# Conexión al motor físico con interfaz gráfica
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Configurar gravedad y plano base
p.setGravity(0, 0, -9.8)
plane = p.loadURDF("plane.urdf")

# Cargar un brazo robótico URDF (modelo KUKA)
robot = p.loadURDF("kuka_iiwa/model.urdf", useFixedBase=True)

# Posicionar la cámara
p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=90, cameraPitch=-30, cameraTargetPosition=[0, 0, 0])

# Control simple: mover una articulación con sinusoide
num_joints = p.getNumJoints(robot)

print("Número de articulaciones:", num_joints)

t = 0
while True:
    # Movimiento suave del brazo (articulaciones 1 y 2)
    target1 = 0.5 * math.sin(t)
    target2 = 0.5 * math.cos(t)
    p.setJointMotorControl2(robot, 2, p.POSITION_CONTROL, targetPosition=target1)
    p.setJointMotorControl2(robot, 3, p.POSITION_CONTROL, targetPosition=target2)
    p.stepSimulation()
    t += 0.02
    time.sleep(1. / 240.)
