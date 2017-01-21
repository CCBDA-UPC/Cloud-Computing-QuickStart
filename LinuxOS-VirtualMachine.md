# Run a Linux OS in a Virtual Machine

Due that many hands-on are assuming a Linux OS environment we suggest to use VirtualBox in order to run a Linux in a separate virtual machine if you have a Windows environment.

- You can download and install a VirtualBox from [https://www.virtualbox.org](https://www.virtualbox.org).
- Ubuntu is a Debian-based Linux operating system, with Unity as its default desktop environment. It is based on free software. You can download a 64-bit Ubuntu Linux ISO from http://www.ubuntu.com/download/desktop.
 

Once VirtualBox is installed and the Ubuntu ISO is downloaded, you can proceed with set up and installation:

- Launch VirtualBox and create a new virtual machine (“New” button) , name it and set the Operating System to “Linux”
- Set the base memory to at least 2048MB.
- Create a new “virtual hard disk now”. Click “Continue” and choose VDI as the disk type. Set the storage details to be “Dynamically allocated” to preserve some initial disk space. Name the virtual disk something obvious or use the default suggested name and make it at least 80GB  and click “Create” to produce the virtual hard drive.
- At the VirtualBox Manager screen, select the newly created virtual machine and click on the “Settings” button. Click on the “Storage” tab and next to “Controller: IDE” click the + icon that looks like a CD (in the same line) to add a new IDE Controller. Click “Choose Disk” and locate the Ubuntu ISO (named something like ”ubuntu-14.04.4-desktop-amd64.iso”) that you downloaded earlier, then click “OK” and close out of Settings.

Back at the VirtualBox Manager screen, select the Linux virtual machine and click on “Start” to begin booting the VM. Let the VM boot and choose “Install Ubuntu” at the welcome screen, create a login and user name, set time zones, and click through the simple installation process until it begins. When finished, Ubuntu Linux will boot into the desktop.
