#!/usr/bin/python3

#---[Metadata]--------------------------------------------------------------#
#  Filename ~ setup.py                      [Update: 2022-03-12 | 12:26 PM] #
#---[Info]------------------------------------------------------------------#
#  {The OmegaDSToolkit is a product of Delta_Society™ by MyMeepSQL}         #
#                                                                           #
#  The SetupTool for ODST                                                   #
#  Language  ~  Python3                                                     #
#---[Author]----------------------------------------------------------------#
#  Thomas Pellissier ~ @MyMeepSQL                                           #
#  Copyright (C) 2022 MyMeepSQL - © Delta_Society™                          #
#---[Operating System]------------------------------------------------------#
#  Developed for linux                                                      #
#---[Licence]---------------------------------------------------------------#
#  GNU General Public License v3.0                                          #
#  -------------------------------                                          #
#                                                                           #
#  This program is free software; you can redistribute it and/or modify     #
#  it under the terms of the GNU General Public License as published by     #
#  the Free Software Foundation; either version 2 of the License, or        #
#  (at your option) any later version.                                      #
#                                                                           #
#  This program is distributed in the hope that it will be useful,          #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#  GNU General Public License for more details.                             #
#                                                                           #
#  You should have received a copy of the GNU General Public License along  #
#  with this program; if not, write to the Free Software Foundation, Inc.,  #
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.              #
#---------------------------------------------------------------------------#

# Import Section
import os,sys
from setuptools import setup,find_packages
from time import sleep
####

# Colors
red = '\033[1;31m'
lime = '\033[1;32m'
blue = '\033[1;34m'
reset = '\033[0m'
####

# Check if the user have a Internet connexion
import urllib.request
def connection(host='https://google.com'):              #
    import urllib.request                               #
    try:                                                #
        urllib.request.urlopen(host)                    #
        return True                                     #
    except:                                             #
        return False                                    #
####

# The SetupTool
try:
    if os.getuid() != 0:                                                            #   check if the user run ODST with root privilege
        print("The OmegaDSToolkit's setup could be run with root privilege")        #
        print("Re-run the setup.py with sudo")                                      #
        print('Run "sudo python3 setup.py install"')                                #
        sys.exit()                                                                  #
# If the user tries to run ODST from a non-Linux machine
except AttributeError:
    print()
    criticalmsg = blue+"["+red+"CRITICAL"+blue+"]"+red+" You tried to run ODST on a no-linux machine, ODST can be run only on a Linux kernel"+reset#
    exit(criticalmsg)
else:
    try:
        print()
        print("""
███████╗███████╗████████╗██╗   ██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║
███████╗█████╗     ██║   ██║   ██║██████╔╝   ██║   ██║   ██║██║   ██║██║
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝    ██║   ██║   ██║██║   ██║██║
███████║███████╗   ██║   ╚██████╔╝██║        ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝""")    # Police = ANSI Shadow from https://www.coolgenerator.com/ascii-text-generator
        print("+ ------------------ !* Welcome to the ODST setuptool. *! ------------------ +")
        print()
        print("+ ----------------------------------- +")
        print("  Checking for internet connection...")
        print("+ ----------------------------------- +")
        print()


                
        # try:
        #     urllib.request.urlopen('http://google.com')
        #     connection = True
        # except:
        #     connection =  False

        if connection() == True:
            print("Internet status.......... "+lime+"Connected"+reset)
            pass
        else:
            print("Internet status.......... "+red+"Not connected"+reset)
            print("Not Internet connexion found, please check you are connected to Internet and retry.")
            sys.exit()

        print('The setup will install all pip packages that ODST needs and copy the OemgaDSToolkit path to "/usr/share/OmegaDSToolkit"')
        yn = str(input("Do you want to continue? [Y/n] "))

        if yn != 'y' and yn != 'Y':
            print("Abort.")
            sys.exit()
        elif not yn:
            print("Abort.")
            sys.exit()
        else:
            pass

        requirements = ["requests"]
        setup_requirements = ["requests"]
        test_requirements = ["requests"]
        setup(classifiers=[
                "Copyright                          :: Copyright (C) 2022, Thomas Pellissier aka MyMeepSQL from © Delta_Society™",
                "Author                             :: Thomas Pellissier",
                "Developed for                      :: Linux",
                "Development Status                 :: 2 - In Development",
                "Natural Language                   :: English",
                "Environment                        :: Terminal",
                "Intended Audience                  :: Developers, Sec.",
                "Programming Language               :: Python :: 3.10-3.10.X",
                "Programming Language compatible    :: Python :: 3.1-3.x.x",
                "Other Programming Language         :: Bash (Linux)",
            ],
            name='OmegaDSToolkit',
            description='A massive penetration testing toolkit',
            url='https://github.com/MyMeepSQL/OmegaDSToolkit',
            author='MyMeepSQL',
            author_email='thomas.pellissier@outlook.com',
            license='GNU-GPL-3.0',
            keywords="omegadstoolkit",
            version='0.0.1.3',
            python_requires='>=3.1.0',
            packages=find_packages(),
            zip_safe=False,
            include_package_data=True,
            install_requires=[
                'progress', 'colored'
            ],
        )

        print('Create OmegaDSToolkit folder to "/usr/share/OmegaDSToolkit"...')
        os.system("sudo mkdir /usr/share/OmegaDSToolkit")
        print("Done for the folder.\n")

        print('Copy the OmegaDSToolkit to "/usr/share/OmegaDSToolkit"...')
        os.system("sudo cp -r * /usr/share/OmegaDSToolkit")
        print("Done for the OmegaDSToolkit's copy.\n")

        print('Create the alias "sudo " and "omegadstoolkit"...')
        user = str(input("Type your current usernme: "))
        # make the alias for run odst just by typing "omegadstoolkit" to the current user ".bashrc" (home)
        if user != "root":
            print(f"You username : {user} (not root user)")
            print(f"Writing alias into your /home/{user}/.bashrc")

            # # For remove the alias if already exist
            # with open(f"/home/{user}/.bashrc", "r") as fp:
            #     lines = fp.readlines()

            # # Delete text "alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py"
            # with open(f"/home/{user}/.bashrc", "w") as fp:
            #     for line in lines:
            #         if line.strip("\n") != "alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'":
            #             fp.write(line)

            # # Delete text "alias sudo='sudo '"
            # with open(f"/home/{user}/.bashrc", "w") as fp:
            #     for line in lines:
            #         if line.strip("\n") != "alias sudo='sudo ''":
            #             fp.write(line)

            # Writing the alias
            alias =["alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'\n", "alias sudo='sudo '\n"]
            with open(f"/home/{user}/.bashrc", "a") as aliasfile:
                # Writing data to a file
                aliasfile.writelines(alias)
            with open(f"/home/{user}/.zshrc", "a") as aliasfile:
                # Writing data to a file
                aliasfile.writelines(alias)

            ## write to the "/root/.bashrc"
            root_alias = "alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'\n"
            with open("/root/.bashrc", "a") as aliasfile:
                # Writing data to a file
                aliasfile.writelines(root_alias)
        else:
            # make the alias for run odst just by typing "omegadstoolkit" to the root user ".bashrc" (root)
            print(f"You username : {user} (root)")
            print(f'Writing alias into your "/root/.bashrc"')

            # For remove the alias if already exist
            # with open("/root/.bashrc", "r") as fp:
            #     lines = fp.readlines()

            # # Delete text "alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py"
            # with open("/root/.bashrc", "w") as fp:
            #     for line in lines:
            #         if line.strip("\n") != "alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'":
            #             fp.write(line)

            ## write to the "/root/.bashrc"
            root_alias = "alias omegadstoolkit='python3 /usr/share/OmegaDSToolkit/OmegaDSToolkit.py'\n"
            with open("/root/.bashrc", "a") as aliasfile:
                # Writing data to a file
                aliasfile.writelines(root_alias)
            with open("/root/.zshrc", "a") as aliasfile:
                # Writing data to a file
                aliasfile.writelines(root_alias)

        print("Done for alias'.")

        print()
        print("All done.")
        print()

        print("+ --------------------------------------------------------------------------------------------------------------------------------- +")
        print('   Done! All packages are install, now you can run OmegaDSToolkit with "sudo omegadstoolkit" (you can run omegadstoolkit anywhere) ')
        print("+ --------------------------------------------------------------------------------------------------------------------------------- +")

    except EOFError:
        print()
        print("Abort.")
        sys.exit()

    except KeyboardInterrupt:
        print()
        print("Abort.")
        sys.exit()
###
