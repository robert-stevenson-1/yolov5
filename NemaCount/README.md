# The Source of this model is from [NemaCounter](https://github.com/DjampaKozlowski/NemaCounter)
Paper Ref: [A user-friendly software to accurately count and measure cysts from the parasitic nematode Heterodera glycines](https://www.nature.com/articles/s41598-025-88289-6)

- The Yolo5 weights are for a Yolo5-XL model
- Trained on Soybean Nematode Cysts

train command:
```
python train.py --img 1280 --batch 1 --epochs 200 --data datasets/Beet-Cyst-Nematodes.v25-minimal_aug.yolov5pytorch/data.yaml --weights NemaCount/cyst_model.pt --name nemacounter_transfer --patience 25
```