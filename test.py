import data_image 

CIFAT10_data = data_image.CIFAT10('D:\\Qian\\GitHub\\workspace\\tensorflow-DCGAN\\cifar-10-python.tar\\')
# CIFAT10_data.next_batch_file()
batch_im = CIFAT10_data.next_batch(60000)
batch_im = CIFAT10_data.next_batch(60000)
print(CIFAT10_data.epochs_completed)