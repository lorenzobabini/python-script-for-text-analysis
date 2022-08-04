# download a Poppler software in your machine for your specific operating system (https://pypi.org/project/pdf2image/)
# install pdf2image with pip using cmd ("pip install pdf2image")


from pdf2image import convert_from_path


pdf_file = ''  # insert the path of the pdf to convert

#we retrieve the filename from the path of the pdf_file to use it for the image files we are creating
fileName = pdf_file.rsplit('/')[-1]
fileName = fileName.rsplit('.')[0]

# To use the Poppler, you must specify the path of the /bin folder as an argument for "convert_from_path" function (or insert the path in the system environment variables: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)
images = convert_from_path(pdf_file, poppler_path = r"") #in the quotes you must insert the path of the Poppler's /bin folder

# This step saves images as files:
## For each PIL image object:
for i in range(len(images)):
    
    # Write the folder name where you want to store the images.
    folder = ''

    # Create a file name that includes the folder, file name, and a file number, as well as the file extension.
    image_fileName = folder + fileName + str(i) +'.jpg'

    # Save each PIL image object using the file name created above and declare the image's file format. (Try also PNG or TIFF.)
    images[i].save(image_fileName, 'JPEG')

# Success message
print('PDF converted successfully')
