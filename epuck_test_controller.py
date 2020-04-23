from controller import Robot, DistanceSensor, Motor
import math

#Time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.28

PERIOD = 10

#Create the Robot instance.
robot = Robot()

#Initialize devices
ps = []
psNames = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]

for i in range(8):
    ps.append(robot.getDistanceSensor(psNames[i]))
    ps[i].enable(TIME_STEP)

leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

ticker = 0

#Feedback loop: Step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:

    #Step ticker
    motorAngle = math.cos(ticker/PERIOD)
    ticker += 1
    
    #Read sensors outputs
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())

    #Initialize motor speeds at 50% of MAX_SPEED.
    leftSpeed  = 0.5 * MAX_SPEED
    rightSpeed = 0.5 * MAX_SPEED

    #If between threshold, calculate cosine wave
    if ticker > 32 and ticker < 224:
        leftSpeed += motorAngle * 0.25 * MAX_SPEED
        rightSpeed += -1 * motorAngle * 0.25 * MAX_SPEED

    #Write actuators inputs
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
