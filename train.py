import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'
from ultralytics import YOLO

def main():
    model = YOLO('yolo11n.pt')

    # Inicia o treinamento
    results = model.train(
        data='trees_dataset.yaml',
        epochs=150,
        imgsz=640,
        batch=10, # Mantenha o maior valor que sua GPU aguentar sem dar erro de memória
        name='yolov11_trees', # Mude o nome para não sobrescrever o anterior

        augment=True,
        fliplr=0.5,         # Espelhamento horizontal
        hsv_h=0.015,        # Variação de Matiz (cor)
        hsv_s=0.7,          # Variação de Saturação
        hsv_v=0.4,          # Variação de Valor (brilho)
        degrees=10.0,       # Rotação
        translate=0.1,      # Translação
        scale=0.1,          # Zoom

        lr0=0.01,           # Taxa de aprendizagem inicial (o padrão já é ótimo)
        lrf=0.01            # Fator da taxa de aprendizagem final (Final LR = lr0 * lrf)
    )

if __name__ == '__main__':
    main()