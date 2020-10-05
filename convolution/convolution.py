#Carrying out convolutions! 
import numpy as np
from PIL import Image
import math 

#takes an image (numpy array), and a padding number (integer). 
#adds a padding number amount of extra layer of zeros around the image
def add_padding(image,paddingNumber):
	answer = np.zeros((image.shape[0] + (2*paddingNumber), image.shape[1] + (2*paddingNumber)))
	answer[paddingNumber:image.shape[0] + paddingNumber,paddingNumber:image.shape[1] + paddingNumber] = image
	return answer


#takes an image (numpy array), kernel (numpy array), stride (integer)
#performs the convolution operation on the image and returns the result
#adds padding to keep the size of the input and the output image the same with a stride of 1
def perform_convolution (image, kernel, stride):
	assert kernel.shape[0] == kernel.shape[1], "kernel should be a square"
	h = image.shape[0]
	w = image.shape[1]
	k_size = kernel.shape[0]

	#padding to keep the size of the output the same as the input if stride is 1
	padding = math.floor((k_size-1)/2)
	padded_image = add_padding(image,padding)
	padded_image_height = padded_image.shape[0]
	padded_image_width = padded_image.shape[1]



	#calculating the output size and creating a numpy array to hold the answer
	a = (int)(h + stride - 1) // stride
	b = (int)(w + stride - 1) // stride
	answer = np.zeros((a,b))

	hindex = -1
	windex = 0
	
	#Go through the image and calculate the convolution for each window
	for height in range(0,padded_image_height - k_size + 1 ,stride):
		hindex = hindex + 1
		windex = 0
		for width in range(0,padded_image_width - k_size + 1,stride):
			#Get the current window of the image, multiply it with the kernel
			#Calculate the sum of all the values
			current = padded_image[height:height + k_size, width: width + k_size]
			calculate = current * kernel
			total = calculate.sum()

			#Record the answer
			answer[hindex][windex] = max(0,min(250,total)) #clamping values to [0,250]
			windex = windex + 1
		
	return answer

#taken a line starting with the name of the kernel, followed by kernel values from top to bottom, left to right
#returns the name of the filter, and a numpy array representing the kernel
def get_filter(filterString):
	elements = filterString.split()
	assert len(elements) > 0, "There seems to be an empty line in the filters.txt file. Make sure that you do not leave any empty lines in the file."
	filter_name = elements.pop(0)
	numbers = [int(i) for i in elements]
	almostW = np.array(numbers)
	side = math.floor(math.sqrt(len(numbers)))
	W = np.reshape(almostW,(side,side))
	
	return filter_name, W

	
if __name__ == "__main__":

	#Get stride value from the user
	stride = int(input("Please enter a stride value:  "))
	assert stride > 0, "stride needs to be a positive integer"

	#Get the name of the file containing the image, load it, turn it into a numpy array
	image_name = input("Please enter the image you would like to perform the convolution on:  ")
	image = Image.open(image_name)
	numpy_image = np.asarray(image)

	#Keep track of number of channels depending on the type of the image
	channel_number = 3
	if image.mode == 'L':
		numpy_image = numpy_image.reshape(numpy_image.shape[0],numpy_image.shape[1],1)
		channel_number = 1

	#Read the file containing the filters, collect all the filters in a list
	filter_file = "./filters.txt"
	open_file = open(filter_file,"r")
	filters = open_file.readlines()
	filter_number = len(filters)

	#Go through all of the filters and apply them to the image
	for fi in range(0, filter_number) :
		current_filter, W = get_filter(filters[fi])
		print("Working on " + current_filter)
		output = np.zeros(((numpy_image.shape[0] + stride - 1) // stride,(numpy_image.shape[1] + stride - 1)// stride , channel_number),dtype=np.uint8)

		for channel in range(0,channel_number):
			output[0:,0:,channel] = perform_convolution(numpy_image[...,channel],W,stride)
		
	
	if (channel_number == 1):
		output = output.reshape((numpy_image.shape[0],numpy_image.shape[1]))

	final_image = Image.fromarray(np.uint8(output * 255))

	#Let the user choose between a colored or black and white image
	black = input("If you would like the results to be black and white type b, if not enter.")
	if (black == "b") :
		final_image = final_image.convert("L")

	#Ask the user where to save the results and save them.
	saving_name = input("What do you want the name of the output file to be? Please type without the file extension :  ")
	final_image.save(saving_name +".jpg")




