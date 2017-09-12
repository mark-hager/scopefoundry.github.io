```python
from ScopeFoundry.data_browser import DataBrowserView
import pyqtgraph as pg
import numpy as np
from scipy.misc import imread
import os

#scipy imread uses the Python Imaging Library (PIL) to read an image

class ScipyImreadView(DataBrowserView):

    # This name is used in the GUI for the DataBrowser
    name = 'scipy_imread_view'
    
    def setup(self):
        # create the GUI and viewer settings, runs once at program start up
        # self.ui should be a QWidget of some sort, here we use a pyqtgraph ImageView
        self.ui = self.imview = pg.ImageView()

    def is_file_supported(self, fname):
    	 # Tells the DataBrowser whether this plug-in would likely be able
    	 # to read the given file name
    	 # here we are using the file extension to make a guess
        _, ext = os.path.splitext(fname)
        return ext.lower() in ['.png', '.tif', '.tiff', '.jpg']

        
    def on_change_data_filename(self, fname):
        #  A new file has been selected by the user, load and display it
        try:
            self.data = imread(fname)
            self.imview.setImage(self.data.swapaxes(0,1))
        except Exception as err:
        	  # When a failure to load occurs, zero out image
        	  # and show error message
            self.imview.setImage(np.zeros((10,10)))
            self.databrowser.ui.statusbar.showMessage(
            	"failed to load %s:\n%s" %(fname, err))
            raise(err)


##########

from ScopeFoundry.data_browser import DataBrowser
import sys

app = DataBrowser(sys.argv)

# views are loaded in order of more generic to more specific.
## ie the last loaded views are checked first for compatibility

# if you have ScipyImreadView in a separate file, you may need to import it, like this:
# from viewers.images import ScipyImreadView

# Load your new view into the DataBrowser App
app.load_view(ScipyImreadView(app))
    
# More views here

sys.exit(app.exec_())
```