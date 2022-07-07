from mmaction.apis import inference_recognizer, init_recognizer
import numpy as np

# Inicialização do recognizer utilizado
config = './mmaction2/configs/recognition/tsn/tsn_r50_video_inference_1x1x3_100e_kinetics400_rgb.py'
# Carregamento dos pesos
checkpoint = './checkpoints/tsn_r50_1x1x3_100e_kinetics400_rgb_20200614-e508be42.pth'


class ModeloML():
    def __init__(self) -> None:
        self.modelo = init_recognizer(config, checkpoint, device='cpu')

    def evaluate(self, f):
        video = f
        label = './mmaction2/tools/data/kinetics/label_map_k400.txt'
        results = inference_recognizer(self.modelo, video)
        labels = open(label).readlines()
        labels = [x.strip() for x in labels]
        results = [(labels[k[0]], k[1]) for k in results]
        return (f'{results[0][0]:}', results[0][1])

    def evaluateAll(self, f):
        video = f
        label = './mmaction2/tools/data/kinetics/label_map_k400.txt'
        results = inference_recognizer(self.modelo, video)
        labels = open(label).readlines()
        labels = [x.strip() for x in labels]
        results = [(labels[k[0]], k[1]) for k in results]
        return (results)
