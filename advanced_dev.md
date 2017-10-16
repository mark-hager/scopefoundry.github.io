# Advanced Development


## Development Environment

[anaconda_dl]: https://www.continuum.io/downloads
[Eclipse]: http://www.eclipse.org
[PyDev]: http://www.pydev.org
[conda_env]: http://conda.pydata.org/docs/using/envs.html

### Python via Anaconda

To have a consistent python environment for using and developing ScopeFoundry, we recommend the [Anaconda][anaconda_dl] python distribution and using [conda environments][conda_env] to manage packages.

* Download and Install [Anaconda][anaconda_dl]. Recommended Python version is 3.6, but 2.7 may work, but is not currently tested. If you are developing hardware or measurement plug-ins to be shared, it is a good idea to check to make sure your code works on both Python 2 and 3 by using libraries such as [six](https://pythonhosted.org/six/).

* Create an [conda environment][conda_env] includes ScopeFoundry and its dependencies. Open an Anaconda prompt and run the following commands:

```
$ conda create -n scopefoundry python=3.6 anaconda
$ source activate scopefoundry
(scopefoundry) $ pip install pyqtgraph
```	

**Note:** On Windows `source activate scopefoundry` should be replaced by `activate scopefoundry`


If you would like a more minimal environment, without all the default packages from Anaconda:

```
$ conda create -n scopefoundry python=3.6
$ source activate scopefoundry
(scopefoundry) $ conda install numpy pyqt qtpy h5py
(scopefoundry) $ pip install pyqtgraph
```	


If you are interested in using the latest development version of ScopeFoundry, instead of the most recent release on [PyPI](https://pypi.python.org/pypi/ScopeFoundry), you can install via git.
To install the latest development version of ScopeFoundry from github:

```
(scopefoundry) $ pip install git+git://github.com/ScopeFoundry/ScopeFoundry.git
```



### Eclipse + PyDev IDE

![Eclipse](http://www.eclipse.org/eclipse.org-common/themes/solstice/public/images/logo/eclipse-426x100.png)
![PyDev](http://www.pydev.org/images/pydev_banner3.png)

For an IDE we recommend [Eclipse] with the [PyDev] plugin. While the setup is more complicated than many other IDE's, there is one very useful feature available in PyDev that not available elsewhere: [**Live code reloading**](http://www.pydev.org/manual_adv_debugger_auto_reload.html). This allows a developer to modify any function in ScopeFoundry from within Eclipse and have that new version of the function injected into the running ScopeFoundry App. 

- To install, download [Eclipse Neon Installer](http://www.eclipse.org/downloads/).
- Install Eclipse for Java developers
- Open Eclipse, go to `Eclipse Marketplace...` menu item
- Search for "PyDev" and install
- [Configure](http://www.pydev.org/manual_101_interpreter.html) your PyDev python interpreter. Make sure to point it at your `scopefoundry` conda environment.
- Run your App script in Eclipse's Debug Mode ![Debug Icon](debug_exc.gif) to enable live code reloading

## Keep track of history

It is a good idea to use a version-control system (VCS) to keep track of the code that runs your experiment. This allows you to have a record of the software used to acquire data on a specific day of experiments. It also protects against accidental and untraceable changes to code on your microscope that could affect how data is acquired. The current recommended VCS for ScopeFoundry projects is [Git](https://git-scm.com). 


Lets create a git repository to store the code for the microscope app

```
mkdir fancy_microscope
cd fancy_microscope
git init
```

We add files using:

```
git add fancy_microscope_app.py
```
And commit changes to perminanet history using

```git commit -m "cool changes happen here"```

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

## Where to Find Out More

For questions about this documentation or ScopeFoundry in general, please visit and post on the ScopeFoundry [project mailing list and forum](https://groups.google.com/forum/#!forum/scopefoundry).

For source code of all ScopeFoundry projects visit our [GitHub page](https://github.com/scopefoundry/).

ScopeFoundry is available to download from [PyPI](https://pypi.python.org/pypi/ScopeFoundry) or install via `pip install ScopeFoundry`.

