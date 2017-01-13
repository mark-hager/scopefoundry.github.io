# Advanced Development

## Keep track of history

It is a good idea to use a version-control system (VCS) to keep track of the code that runs your experiement. This allows you to have a record of the software used to acquire data on a specific day of experiements. It also protects against accidental and untracable changes to code on your microscope that could affect how data is acquired. The current recommended VCS for ScopeFoundry projects is [Git](https://git-scm.com). 


Lets create a git repository to store the code for the microscope app

```
mkdir fancy_microscope
cd fancy_microscope
git init
```

We add files using:```
git add fancy_microscope_app.py
```
And commit changes to perminanet history using ```git commit -m "cool changes happen here"```

There are are many tutorials on web that address how to use git effectively, so we will not repeat that here.

There are also good graphical interfaces to Git that you may want to check out. One recommendation [SourceTree](https://www.sourcetreeapp.com) which is available for no cost.



## Git subtree to modify plugins

If we want to modify existing hardware or  measurements plug-ins we can use `git subtree` to import plugins into a git repository, track local changes to the plugin , and finally push these plug-in changes upstream.


If we have a microscope repository `fancy_microscope` that we would like to modify the code for `ascom_camera` we can at it locally to our microscope with:

```
cd fancy_microscope
git subtree add --prefix ScopeFoundryHW/ascom_camera/ \
	https://github.com/ScopeFoundry/HW_ascom_camera.git master
```

After modification of the plugin we can push the changes in the plugin subdirectory. 

```
git subtree push --prefix ScopeFoundryHW/ascom_camera/ \
		https://user@github.com/ScopeFoundry/HW_ascom_camera.git master
```

You will need commit access to do this, but you can always fork the plug-in repo, and submit pull-requests via the [ScopeFoundry GitHub page](https://github.com/ScopeFoundry/).

