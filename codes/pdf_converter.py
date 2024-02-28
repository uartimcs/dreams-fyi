import os
from pdf2image import convert_from_path

# Default location under current directory.
print(f'Current Directory:  {os.getcwd()}')
PDF_LOCATION = './INPUT_PDF'
JPG_LOCATION = './OUTPUT_JPG'

# Check existence of folders under current directory
source_dir_exist = os.path.exists(PDF_LOCATION)
dest_dir_exist = os.path.exists(JPG_LOCATION)

if not source_dir_exist:
	print(f'The PDF input storage folder {PDF_LOCATION} does not exist. Create a new folder for you.')
	os.makedirs(PDF_LOCATION)

if not source_dir_exist:
	print(f'The JPG output storage folder {JPG_LOCATION} does not exist. Create a new folder for you.')
	os.makedirs(JPG_LOCATION)

print(f'Folders {PDF_LOCATION} and {JPG_LOCATION} are ready. Please place the pdf files under {PDF_LOCATION}')

file_doc_list = os.listdir(PDF_LOCATION)
print(f'Currently the folder {PDF_LOCATION} contains {len(file_doc_list)} files.')
print(f'Please place pdf files that you want to convert under {PDF_LOCATION}.')
print(f'This program assumes that poppler is not installed in PATH. Please place the location of popple bin file directory...')

poppler_location = input('Please input the path of POPPLER bin: Leave empty if well-installed.')

DEFAULT_PAGE = 1

for doc_x in file_doc_list:
	if doc_x.endswith("pdf"):

		if len(poppler_location) != 0:
			pages =convert_from_path(os.path.join(PDF_LOCATION, doc_x), poppler_path = poppler_location)
		else:
			pages = convert_from_path(os.path.join(PDF_LOCATION, doc_x))

		DEFAULT_PAGE = len(pages)
		print(f'The PDF file {doc_x} contains {len(pages)} page(s). Only the first {DEFAULT_PAGE} will be extracted.')
		for i in range(0, DEFAULT_PAGE):
			doc_name = doc_x.split('.')[0] + "_" + str(i+1) + ".jpg"
			dest_path = os.path.join(JPG_LOCATION, doc_name)
			pages[i].save(dest_path)
			print(f'The {i+1} page of the PDF document {doc_x} has been coverted to {doc_name} and saved at {dest_path}')

print(f'The conversion has completed.')