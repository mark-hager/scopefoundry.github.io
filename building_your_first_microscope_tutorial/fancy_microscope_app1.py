# handy python 2/3 compatiblity
from __future__ import division, print_function, absolute_import

# import the base class from ScopeFoundry that you 
# will subclass for your for your microscope
from ScopeFoundry import BaseMicroscopeApp


class FancyMicroscopeApp(BaseMicroscopeApp):

    # this is the name of the microscope that ScopeFoundry uses 
    # when storing data
    name = 'fancy_microscope'
    
    # You must define a setup function that adds all the 
    #capaiblities of the microscope and sets default settings
    def setup(self):
        
        #Add App wide settings
        
        #Add hardware components
        print("Adding Hardware Components")

        #Add measurement components
        print("Create Measurement objects")

        # Connect to custom gui
        
        # load side panel UI
        
        # show ui
        self.ui.show()
        self.ui.activateWindow()
        
        #self.settings_load_ini("fancy_settings.ini")


if __name__ == '__main__':
    import sys
    
    app = FancyMicroscopeApp(sys.argv)
    sys.exit(app.exec_())