# Dev Notes

 run `python train.py --img 1280 --batch 4 --epochs 50 --data datasets/Beet-Cyst-Nematodes.v25-minimal_aug.yolov5pytorch/data.yaml --weights yolov5n.pt --patience 25`

 that paper's modified version (from scratch): `python train.py --img 1280 --batch 2 --epochs 100 --data datasets/Beet-Cyst-Nematodes.v25-minimal_aug.yolov5pytorch/data.yaml --weights '' --name BCN_Paper_scratch --cfg custom_arch/nematode-yolov5n.yaml --patience 25`

 that paper's modified version: `python train.py --img 1280 --batch 2 --epochs 10 --data datasets/Beet-Cyst-Nematodes.v25-minimal_aug.yolov5pytorch/data.yaml --weights beet_cyst_init.pt --name BCN_Paper --cfg custom_arch/nematode-yolov5n.yaml --patience 25`