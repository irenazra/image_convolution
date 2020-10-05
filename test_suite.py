from convolution import perform_convolution 
import numpy as np


#tests the convolution of a 3x3 image with a 2x2 kernel and a stride of 1
def imagea_kernela_stride_one(imagea,kernela):
    answer = perform_convolution(imagea,kernela,1)
    assert answer[0][0] == 30
    assert answer[0][1] == 23
    assert answer[0][2] == 0
    assert answer[1][0] == 20
    assert answer[1][1] == 17
    assert answer[1][2] == 0
    assert answer[2][0] == 0
    assert answer[2][1] == 0
    assert answer[2][2] == 0

#tests the convolution of a 3x3 image with a 2x2 kernel and a stride of 2
def imagea_imagea_stride_one(imagea,kernela):
    answer = perform_convolution(imagea,imagea,1)
    assert answer[0][0] == 17
    assert answer[0][1] == 29
    assert answer[0][2] == 23
    assert answer[1][0] == 26
    assert answer[1][1] == 49
    assert answer[1][2] == 26
    assert answer[2][0] == 23
    assert answer[2][1] == 29
    assert answer[2][2] == 17

#tests the convolution of a 3x3 image with a 3x3 kernel and a stride of 2
def imagea_kernelb_stride_two(imagea,kernelb):
    result = perform_convolution(imagea,kernelb,2)
    assert result[0][0] ==13
    assert result[0][1] ==26
    assert result[1][0] ==24
    assert result[1][1] ==18


#tests the convolution of a 4x4 image with a 2x2 kernel and a stride of 2
def imageb_kernela_stride_two(imageb,kernela):
    result = perform_convolution(imageb,kernela,2)
    assert result[0][0] ==30
    assert result[0][1] ==28
    assert result[1][0] ==17
    assert result[1][1] ==7

#tests the convolution of a 4x4 image with a 3x3 kernel and a stride of 1
def imageb_kernelb_stride_one(imageb,kernelb) :
    result = perform_convolution(imageb,kernelb,1)
    assert result[0][0] == 13
    assert result[0][1] == 29
    assert result[0][2] == 27
    assert result[0][3] == 35
    assert result[1][0] == 36
    assert result[1][1] == 37
    assert result[1][2] == 39
    assert result[1][3] == 26
    assert result[2][0] == 28
    assert result[2][1] == 27
    assert result[2][2] == 21
    assert result[2][3] == 9
    assert result[3][0] == 19
    assert result[3][1] == 25
    assert result[3][2] == 16
    assert result[3][3] == 11

#tests the convolution of a 4x4 image with a 3x3 filter and a stride of 2
def imageb_kernelb_stride_two(imageb,kernelb) :
    result = perform_convolution(imageb,kernelb,2)
    assert result[0][0] ==13
    assert result[0][1] ==27
    assert result[1][0] ==28
    assert result[1][1] ==21

    
if __name__ == "__main__":
    #2x2 numpy array
    kernela = np.zeros((2,2))
    kernela[0][0] = 1
    kernela[0][1] = 3
    kernela[1][0] = 4
    kernela[1][1] = 2

    #3x3 numpy array
    kernelb = np.zeros((3,3))
    kernelb[0][0] = 1
    kernelb[0][1] = 2
    kernelb[0][2] = 1
    kernelb[1][0] = 3
    kernelb[1][1] = 7
    kernelb[1][2] = 0
    kernelb[2][0] = 0
    kernelb[2][1] = 1
    kernelb[2][2] = 1
  
    #3x3 numpy array
    imagea = np.zeros((3,3))
    imagea[0][0] = 1
    imagea[0][1] = 3
    imagea[0][2] = 2
    imagea[1][0] = 4
    imagea[1][1] = 2
    imagea[1][2] = 3
    imagea[2][0] = 2
    imagea[2][1] = 1
    imagea[2][2] = 1

    #4x4 numpy array
    imageb = np.zeros((4,4))
    imageb[0][0] = 1
    imageb[0][1] = 3
    imageb[0][2] = 2
    imageb[0][3] = 4
    imageb[1][0] = 4
    imageb[1][1] = 2
    imageb[1][2] = 3
    imageb[1][3] = 1
    imageb[2][0] = 2
    imageb[2][1] = 1
    imageb[2][2] = 1
    imageb[2][3] = 0
    imageb[3][0] = 2
    imageb[3][1] = 2
    imageb[3][2] = 1
    imageb[3][3] = 1

   
    #Calls the tests
    imagea_kernela_stride_one(imagea,kernela)
    imagea_imagea_stride_one(imagea,imagea)
    imagea_kernelb_stride_two(imagea,kernelb)
    imageb_kernela_stride_two(imageb,kernela)
    imageb_kernelb_stride_one(imageb,kernelb)
    imageb_kernelb_stride_two(imageb,kernelb)


    print()
    print("ALL TESTS PASSED")
    print()