import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from GonumMatrixIO import GonumIO
import argparse

simulationData = pd.read_parquet("data/BestAgentSimulation.pq")
animationSavePath = "data/animation.mp4"

GAME_X_DIMENSION = 1.0
GAME_Y_DIMENSION = 0.5
PADDLE_SIZE = 0.2

parser = argparse.ArgumentParser(description="Pong Visualization Argument Parser")
parser.add_argument("--save", help="Save animation to file, rather than showing", action="store_true")
parser.add_argument("--numFrames", help="Determine the number of frames to render. If not given, render the entire simulation", action="store", type=int, default=None)
args = parser.parse_args()

if args.numFrames == None or args.numFrames > len(simulationData):
    numFrames = len(simulationData)
else:
    numFrames = args.numFrames

print(f"BEST CHROMOSOME:\n{GonumIO.loadMatrix('data/bestAgentChromosome.bin')}")


def update(index):
    stateVector = simulationData.loc[index, "StateVector"]
    ballX = stateVector[0]
    ballY = stateVector[1]
    ballXVelocity = stateVector[2]
    ballYVelocity = stateVector[3]
    paddle0Position = stateVector[4]
    paddle1Position = stateVector[5]
    # print(ballX,ballY,ballXVelocity,ballYVelocity,paddle0Position,paddle1Position,)

    ball.set_xdata([ballX])
    ball.set_ydata([ballY])
    paddle0.set_ydata([paddle0Position-PADDLE_SIZE, paddle0Position+PADDLE_SIZE])
    paddle1.set_ydata([paddle1Position-PADDLE_SIZE, paddle1Position+PADDLE_SIZE])
    return ball, paddle0, paddle1,

fig, ax = plt.subplots()
plt.title("Genetic Algorithm: Pong Visualization")
plt.xlim(-1.1*GAME_X_DIMENSION, 1.1*GAME_X_DIMENSION)
plt.ylim(-1.1*GAME_Y_DIMENSION, 1.1*GAME_Y_DIMENSION)
paddle0, = ax.plot([-GAME_X_DIMENSION,-GAME_X_DIMENSION],[-PADDLE_SIZE, PADDLE_SIZE], linewidth=5)
paddle1, = ax.plot([GAME_X_DIMENSION,GAME_X_DIMENSION],[-PADDLE_SIZE, PADDLE_SIZE], linewidth=5)
ball, = ax.plot(0,0,marker="o", markersize=10)

anim = animation.FuncAnimation(fig, update, frames=numFrames, interval=1)
if args.save:
    writer = animation.FFMpegWriter(fps=60)
    anim.save(animationSavePath, writer=writer)
else:
    plt.show()
