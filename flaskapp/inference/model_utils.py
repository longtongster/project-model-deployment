import torch

import torch
import torch.nn as nn
from torchvision import transforms
from pathlib import Path
from PIL import Image


class Cnn(nn.Module):
    def __init__(self):
        super(Cnn, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=0, stride=1),
            nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=3, padding=0, stride=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer3 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=3, padding=0, stride=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.layer4 = nn.Sequential(
            nn.Conv2d(64, 64, kernel_size=3, padding=0, stride=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc1 = nn.Linear(12 * 12 * 64, 512)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(512, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = out.view(out.size(0), -1)
        out = self.relu(self.fc1(out))
        out = self.fc2(out)
        return out

if __name__ == "__main__":
    loaded_model = Cnn()
    loaded_model.load_state_dict(torch.load("./cats_vs_dogs.pth", map_location=torch.device("cpu")))
    loaded_model.eval()
    # Reshape a PIL image to (224, 224) and return a pytorch tensor
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        #transforms.RandomResizedCrop(224),
        #transforms.RandomHorizontalFlip(),
        transforms.ToTensor()])


    test_path = "./test_images/6.jpg"
    print(test_path)
    img = Image.open(test_path)
    img.show()
    img_array=transform(img)
    print(img_array.shape)
    img_batch = img_array.unsqueeze(dim=0)
    print(img_batch.shape)


    idx_to_classes = {0:"cat", 1: "dog"}

    logits = loaded_model(img_batch)
    probs = logits.softmax(dim=1)
    pred = probs.argmax(dim=1).item()
    #print(idx_to_classes[pred])
    result = {"prediction": idx_to_classes[pred], "prob": probs.detach().numpy()[0][pred]}
    print(result)