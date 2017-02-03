from ScopeFoundry.base_app import BaseMicroscopeApp
#from ScopeFoundry.helper_funcs import sibling_path, load_qt_ui_file
import logging

logging.basicConfig(level=logging.INFO)

# Define your App that inherits from BaseMicroscopeApp
class FancyMicroscopeApp(BaseMicroscopeApp):
    
    # this is the name of the microscope that ScopeFoundry uses 
    # when displaying your app and saving data related to it    
    name = 'fancy_microscope'

    # You must define a setup() function that adds all the 
    # capabilities of the microscope and sets default settings    
    def setup(self):

        #Add App wide settings
        #self.settings.New('test1', dtype=int, initial=0)
        
        #Add Hardware components
        from ScopeFoundryHW.virtual_function_gen.vfunc_gen_hw import VirtualFunctionGenHW
        self.add_hardware(VirtualFunctionGenHW(self))


        #Add Measurement components
        from ScopeFoundryHW.virtual_function_gen.sine_wave_measure import SineWavePlotMeasure
        self.add_measurement(SineWavePlotMeasure(self))
        
        
        # load side panel UI        
        #quickbar_ui_filename = sibling_path(__file__, "quickbar.ui")        
        #self.add_quickbar( load_qt_ui_file(quickbar_ui_filename) )
        
        # Connect quickbar ui elements to settings
        # self.quickbar.foo_pushButton.connect(self.on_foo)
        
        # load default settings from file
        #self.settings_load_ini(sibling_path(__file__, "defaults.ini"))
        
if __name__ == '__main__':
    
    import sys
    app = FancyMicroscopeApp(sys.argv)
    sys.exit(app.exec_())
    