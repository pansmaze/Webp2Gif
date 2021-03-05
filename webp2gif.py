from PIL import Image
import os

def convert(file, output=""):
    
    filepath = str(file)
    output_path = str(output)
    
    if output_path == "":
        output_path = filepath[:-5]+".gif"
        
    if not output_path.endswith(".gif"):
        
        if not output_path.endswith('\\'):
            
            output_path += "\\"
        
        output_path += "\\output.gif"
        
    image = Image.open(filepath)
    image.info.pop('background', None)
    image.save(output_path, 'gif', save_all = True)
    
    print("\nSuccess. File Created At:",output_path)



def initiate_convert():

    print("File path of .WEBP to convert")
    file = input()
    print("\nDestination Path of .GIF")
    output = input()
    
    #Check to make sure file is an webp
    if not file.endswith(".webp"):
        print("The specified file is not an .webp image. Check your spelling and try again\n")
        initiate_convert()
        
    if not os.path.exists(file):
        print("The specified file cannot be located. Check your spelling and try again\n")

    else:
        convert(file.lower(), output.lower())


if __name__ == "__main__":
    
    print("WEBP to GIF\n©2021 Robert Sammataro\n\n")
    initiate_convert()