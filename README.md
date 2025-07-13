# Daz Product Uninstaller
This python script was written to remove files from a library based on the contents of a zip file.

#Notice: This is a first draft, and it's my first Python script, so if you don't know Python you might want to wait until I get some feedback on what's wrong with it.

#Why?
While DIM can cover Daz3D products, only a few vendors outside of them use the DIM format.  The rest of the files come as .zip files that have to manually extracted to our Libraries.  But what if you don't want those files anymore?  What if the morphs are bogging down your Genesis loads and the textures are bloating your drive?  You can try and hunt down all the files, but good luck with that!
Introduce this little script.  It takes a zip file and looks inside.  It builds a list of all the files inside.  It takes that list to your Library folder and moves all those files into a seperate directory.  It doesn't delete them (yet).  

Syntax:
python.exe DazProductUninstaller.py [path_to_zip_file] [path_to_libary] [path_to_destination]

Example:
Python.exe DazProductUninstaller.py c:\users\windamyre\downloads\Product.zip c:\users\windamyre\documents\Daz\Library c:\users\windamyre\documents\LibraryTrash

Yeah, it's a lot but it's my first time working with this.

#Future Plans:
-Improve Error Handling and Sanity Checks
-GUI interface
-default paths
-Send to recycle/trash

Ideally, I'd like to put something together that scans the whole library and compiles a list of products and the files associated with them.  This would allow removing a product more easily and detect shared files, leaving them in place.  Put gotta start somewhere.
