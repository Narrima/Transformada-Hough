import sys
import cv2 as cv
import numpy as np


def main(argv):
    ## [load]
    default_file = 'sudoku.jpg'
    filename = argv[0] if len(argv) > 0 else default_file

    # Carrega uma imagem
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)

    # Verifica se a imagem está carregada corretamente
    if src is None:
        print('Erro ao abrir umagem!')
        print('Uso: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1
    ## [load]

    ## [edge_detection]
    # Detecção de bordas
    dst = cv.Canny(src, 70, 190, None, 3)
    ## [edge_detection]

    # Copia as bordas para as imagens que exibirão os resultados em RGB
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)


    ## [draw_lines]

    ## [hough_lines_p]
    # Probabilistic Line Transform
    linesP = cv.HoughLinesP(dst, 1, np.pi / 280, 110, None, 50, 10)
    ## [hough_lines_p]
    ## [draw_lines_p]
    # Desenha as linhas
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    ## [draw_lines_p]
    ## [imshow]
    # Exibe reultados
    cv.imshow("Fonte", src)
    cv.imshow("Deteccao de linhas - Standard Hough Line Transform", cdst)
    cv.imshow("Deteccao de linhas(em vermelho) - Probabilistic Line Transform", cdstP)
    ## [imshow]
    ## [exit]
    # Espere e saia
    cv.waitKey()
    return 0
    return 0
    ## [exit]

if __name__ == "__main__":
    main(sys.argv[1:])

