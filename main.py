import torch
import random
from tqdm import tqdm
import wandb
import time
import os

wandb.init(project='')

os.environ['WANDB_API_KEY'] = ''
os.environ['WANDB_USERNAME'] = ''

acc = []
for epoch in tqdm(range(1000)):
    acc.append(random.randint(0,100))
    time.sleep(0.2)
    if epoch % 50 == 0:
        print("Epoch:", epoch, "Accuracy:", acc[epoch])
        wandb.log({
            "Epoch": epoch,
            "Accuracy": acc[epoch]
        })
