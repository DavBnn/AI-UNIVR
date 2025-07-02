import sys
import os
import torch

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            'code'
        )
    )
)


from model import SimpleMLP



def test_model_forward_pass():
    model = SimpleMLP()
    dummy_input = torch.randn(1, 1, 28, 28)
    output = model(dummy_input)
    assert output.shape == (1, 10)  # Deve avere 10 output, uno per classe
