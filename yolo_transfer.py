import torch
from models.yolo import Model

pretrained_model = torch.load('yolov5n.pt', map_location='cuda:0')['model']

print(f"{pretrained_model}")

altered_model = Model(cfg='./custom_arch/nematode-yolov5n.yaml')

# Copy weights from pretrained to modified where shapes match
for name, param in altered_model.named_parameters():
    if name in pretrained_model.state_dict() and param.shape == pretrained_model.state_dict()[name].shape:
        param.data.copy_(pretrained_model.state_dict()[name])

# Save the new model with transferred weights
torch.save({'model': altered_model}, 'beet_cyst_init.pt')