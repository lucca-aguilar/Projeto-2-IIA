import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'
from ultralytics import YOLO

def main():
    # Carrega um modelo pré-treinado.
    # 'yolov8n.pt' é o menor e mais rápido. Outras opções: yolov8s, yolov8m, yolov8l, yolov8x.
    # O YOLO irá baixar o modelo automaticamente na primeira vez que você rodar.
    model = YOLO('yolov8n.pt')

    # Inicia o treinamento
    # Todos os parâmetros importantes estão aqui.
    results = model.train(
        data='trees_dataset.yaml',  # Caminho para o seu arquivo .yaml
        epochs=100,                 # Número de épocas para treinar
        imgsz=640,                  # Tamanho das imagens (altura e largura)
        batch=8,                    # Número de imagens por lote (reduza se tiver erro de memória)
        name='yolov8n_trees_custom' # Nome do experimento (os resultados serão salvos em 'runs/detect/yolov8n_trees_custom')
    )

if __name__ == '__main__':
    main()