from pathlib import Path

import torch
import torch.nn as nn
from PIL import Image
from torchvision import transforms


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


def read_and_preproces_image(pil_image):
    """
    This function takes as input an image openened by PIL.Image.open(). It loads and preprocesses the
    image such that it is ready to use by our model
    """
    # Reshape a PIL image to (224, 224) and return a pytorch tensor
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        # transforms.RandomResizedCrop(224),
        # transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
    ])

    # transform the image
    img_array = transform(img)

    # change shape of the array from (C, H, W) -> (B, C, H, W)
    # such that our model can consume the image
    img_batch = img_array.unsqueeze(dim=0)
    return img_batch


def load_model():
    loaded_model = Cnn()
    loaded_model.load_state_dict(torch.load("./cats_vs_dogs.pth", map_location=torch.device("cpu")))
    loaded_model.eval()
    return loaded_model


def predict(img_batch):
    idx_to_classes = {0: "cat", 1: "dog"}

    # load model
    loaded_model = load_model()

    # forward pass
    logits = loaded_model(img_batch)

    # determine the class and the calculate probability
    probs = logits.softmax(dim=1)
    pred = probs.argmax(dim=1).item()

    # create a dictionary that returns the predicted class and probability
    result = {"prediction": idx_to_classes[pred], "prob": probs.detach().numpy()[0][pred]}
    return result


if __name__ == "__main__":
    # REPLACE THIS CODE TO handle by FLASK
    # list of all paths to test images
    test_path = Path('./test_images')
    # select one image
    test_list = list(test_path.glob("./*"))
    print(len(test_list))
    test_path = test_list[1]
    print(test_path)
    img = Image.open(test_path)
    img.show()

    # Flask should import these function and
    # execute the code
    img_batch = read_and_preproces_image(img)
    prediction = predict(img_batch)
    print(prediction)