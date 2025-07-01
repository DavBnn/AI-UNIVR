import torch
from model import SimpleMLP


def test_model_forward_pass():
    model = SimpleMLP()
    dummy_input = torch.randn(1, 1, 28, 28)
    output = model(dummy_input)
    assert output.shape == (1, 10)
