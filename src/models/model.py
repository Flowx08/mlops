import torch.nn as nn

class FCModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv = nn.Sequential(
                nn.Conv2d(1, 10, 3, stride=2, padding=1),
                nn.LayerNorm([10, 14, 14]),
                nn.ReLU(),
                nn.Conv2d(10, 20, 3, stride=2, padding=1),
                nn.LayerNorm([20, 7, 7]),
                nn.ReLU(),
                nn.Conv2d(20, 40, 3, stride=2, padding=1),
                nn.LayerNorm([40, 4, 4]),
                nn.ReLU(),
                )
        self.fc = nn.Sequential(
                nn.Linear(40 * 4 * 4, 10),
                nn.LogSoftmax(dim=1)
                )

    def forward(self, x):
        out = self.conv(x)
        out = out.view(-1, 40 * 4 * 4)
        out = self.fc(out)
        return out

