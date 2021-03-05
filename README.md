# WEBP2GIF
 Simple Tool For Converting Animated WEBP Files to Animated GIF Files

Script based off of functions in the PIL Library. WEBP2GIF adds a simple
user interface allowing users to individually convert WEBP files. Can
also be imported and automatically batch convert large numbers of WEBP files.

How to Use:

For use with the User Interface, call initiate_convert(). This function will
have the user enter the desired source and destination paths and automatically
convert the specified file. Batch support is not implemented in this version

For use in tandem with another script, convert(file, output) handles the
conversion of files. Parameter file represents the path of the .webp to be
converted while output represents the destination path of the resulting .gif.

Note:

- If no value is entered for output, the .gif will be created in the same
  directory as the source file

- If output is entered as a path ending with '\' at the end, the output will
  be created as output.gif in the specified directory

- If output is entered as a path without a '\' at the end, the output will    
  be created at OUTPUTPATH.gif (WEBP2GIF will tack on a '.gif' to the end of
  parameter output and use that as the absolute path.)  


WEBP2GIF by Robert Sammataro
Built with the PIL library
