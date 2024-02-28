import os
import cv2

IMAGE_BEFORE_LOCATION = './IMAGE_BEFORE'
IMAGE_AFTER_LOCATION = './IMAGE_AFTER'

# Check existence of folders under current directory
before_dir_exist = os.path.exists(IMAGE_BEFORE_LOCATION)
after_dir_exist = os.path.exists(IMAGE_AFTER_LOCATION)

if not before_dir_exist:
	print(f'The JPG / PNG input storage folder {IMAGE_BEFORE_LOCATION} does not exist. Create a new folder for you.')
	os.makedirs(IMAGE_BEFORE_LOCATION)
if not after_dir_exist:
	print(f'The augmented JPG / PNG output storage folder {IMAGE_AFTER_LOCATION} does not exist. Create a new folder for you.')
	os.makedirs(IMAGE_AFTER_LOCATION)
print(f'Folders {IMAGE_BEFORE_LOCATION} and {IMAGE_AFTER_LOCATION} are ready. Please place the JPG / PNG image files under {IMAGE_BEFORE_LOCATION}')

im_list = os.listdir(IMAGE_BEFORE_LOCATION)
im_list.sort()
print(f'Currently the folder {IMAGE_BEFORE_LOCATION} contains {len(im_list)} files.')
print(f'Please place the JPG / PNG image files that you want to convert under {IMAGE_BEFORE_LOCATION}.')


def augmentation_task(im):
	im_location = os.path.join(IMAGE_BEFORE_LOCATION, im)
	im_details = cv2.imread(im_location)

	scale_percent = 50
	width = int(im_details.shape[1] * scale_percent / 100)
	height = int(im_details.shape[0] * scale_percent / 100)
	im_dim = (width, height)
	action_dict = {
		0: cv2.GaussianBlur(im_details, (5, 5), 0),
		1: cv2.GaussianBlur(im_details, (7, 7), 0),	
		2: cv2.GaussianBlur(im_details, (9, 9), 0),
		3: cv2.cvtColor(im_details, cv2.COLOR_BGR2GRAY),
		4: cv2.resize(im_details, im_dim, interpolation = cv2.INTER_AREA)	
	}
	action_str = {0:"blur1", 1:"blur2", 2:"blur3",3:"gray", 4:"resize"}
	key_list = list(action_dict.keys())

	for num in key_list:
		new_im_name = im.split(".")[0] + "_" + action_str[num] + "." + im.split(".")[-1]
		final_path = os.path.join(IMAGE_AFTER_LOCATION, new_im_name)
		cv2.imwrite(final_path, action_dict[num])
		print(f'The augmented image of {im} : {new_im_name} is created and saved at {final_path}')

def rotation_task(im):
	im_location = os.path.join(IMAGE_AFTER_LOCATION, im)
	im_details = cv2.imread(im_location)

	rotation_action_dict = {
	0: cv2.rotate(im_details, cv2.ROTATE_90_CLOCKWISE),
	1: cv2.rotate(im_details, cv2.ROTATE_180),		
	2: cv2.rotate(im_details, cv2.ROTATE_90_COUNTERCLOCKWISE)
	}
	rotate_str = {0: '090', 1:'180', 2:'270'}
	rotation_key_list = list(rotation_action_dict.keys())

	for num in rotation_key_list:
		new_im_name = im.split(".")[0] + "_" + rotate_str[num] + "." + im.split(".")[-1]
		final_path = os.path.join(IMAGE_AFTER_LOCATION, new_im_name)
		cv2.imwrite(final_path, rotation_action_dict[num])
		print(f'The rotated image of {im} : {new_im_name} is created and saved at {final_path}')

for im in im_list:
	if im.endswith('.jpg') or im.endswith('.png'):
		augmentation_task(im)

rotate_choice = input('Rotate the augmented images as well? (Y/N): ')

if rotate_choice == 'Y':
	im_after_list = os.listdir(IMAGE_AFTER_LOCATION)
	im_after_list.sort()

	for im in im_after_list:
		if im.endswith('.jpg') or im.endswith('.png'):
			rotation_task(im)



