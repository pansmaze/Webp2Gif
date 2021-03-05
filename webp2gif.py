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
    
    
    def get_source_location():
        
        print("File path of .WEBP to convert")
        
        file = input()
        if not os.path.exists(file) or not file.endswith(".webp"):
            
            print("The specified file is not a .webp image. Check your spelling and try again\n")
            get_source_location()
            
        return(file)
        
    def get_output_location():
        
        print("Destination Path of .GIF")
        
        file = input()
        
        if not os.path.exists(file) and file != "":
            print("The specified file path is invalid. Check your spelling and try again\n")
            get_output_location()
            
        return(file)
        
    
    convert(get_source_location(), get_output_location())


if __name__ == "__main__":
    
    print("WEBP to GIF\n©2021 Robert Sammataro\n\n")
    initiate_convert()