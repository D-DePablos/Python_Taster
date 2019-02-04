# Python_Taster
Python Taster MSSL Session 2019

Total Time of Installation: ~ 5 minutes

Instructions Based on https://openastronomy.org/rcsc18/setup-instructions/
Refer there if any issues arise.

We will allow some minutes at the start of the workshop to get everything ready.

How-to get ready:

1 - Miniconda version of Python 3: https://conda.io/en/latest/miniconda.html

        Download the Python 3.7 version corresponding to your system.

        We encourage the use of the .pkg file if on macOS, or the .exe on Windows.

        Run the installer with the default values or select a different
        installation directory if preferred

        If on Linux (no explicit installer), or wanting to use the .sh file,
        run the .sh script via opening a console, changing into the directory
        of the downloaded file and run "bash "filename".sh",
        it will then prompt you to accept terms and conditions,
        and allow you to type a location for the installation (choose wisely!)




        Once Installed, open a new terminal, now running:

                conda list

        should return a few packages that come with Miniconda, including Python.


2 - Getting Python Package Sources:

        Getting packages that are stored in either the Anaconda or Python library is easy,
        we just need to do the following on a Terminal:

            i/ Add the repository where the packages are contained:

                 conda config --append channels conda-forge

            ii/ Now we can install any packages we require by using the expression:

                 conda install package1 package2 package3 package...


            Note: It is more efficient to install multiple packages at once!


3- Installing the Packages:


    The packages which we need for the tutorial are the following:

    - scipy
    - numpy
    - matplotlib
    - sunpy
    - astropy


        So we may run the following command:

             conda install scipy numpy matplotlib sunpy astropy

        And be ready for the tutorial!


4 - Checking our setup:

        The last thing to get ready is to run "idle3" in our console, and write
        in the following commands:

             import sunpy.map
             help(sunpy.map)

        And it should come up with some information about the package contents


        If any issues arise, check that you have installed the proper packages
        if it still does not work, contact either of us.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------


 5 - Getting started Early:

        If you do have some time prior to the session, the tutorial made by
        the guys from openastronomy is pretty good,
        do remember to use the instructor version, as it contains all the info!

            - https://github.com/OpenAstronomy/rcsc18_lessons
