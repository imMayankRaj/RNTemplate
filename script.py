import subprocess
import optparse
import pathlib

def parse_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-n", "--pname", dest="pname", help="The name of the project")
    parser.add_option("-d", "--directory", dest="directory", help="The directory to install the project")
    (options, arguments) = parser.parse_args()
    if not options.pname:
        parser.error("Project name is missing")
    return options


def installPackages():
    print("[+] Installing react-native cli for project " + pname)
    subprocess.call("react-native init " + pname, shell=True, cwd = workingDirectory)
    print("[+] React native installed. Changing working directory to ./" + pname)
    subprocess.call("chmod -R 777 " + pname, shell=True, cwd = workingDirectory)
    
    #Reading file for external packages
    file = open('./lib.txt', 'r')
    packages = file.readlines()
    for package in packages:
        print("[+] Installing " + package)
        subprocess.call("npm install " + package, shell=True, cwd = workingDirectory + '/' + pname)

    print("[+] Packages installed successfully")


def createTemplateFolders():
    print("[+] Starting creating template folders")
    currentDirectory =  workingDirectory + '/' + pname
    subprocess.call('mkdir -m 777 src', shell=True, cwd = currentDirectory)
    file = open('./template.txt', 'r')
    folders = file.readlines()
    for folder in folders:
        if(folder.rstrip().endswith('.js')):
            subprocess.call("touch " + folder, shell=True, cwd = currentDirectory + '/src')
        else:
            subprocess.call("mkdir " + folder, shell=True, cwd = currentDirectory + '/src')
            subprocess.call("touch " + folder.rstrip() + "/index.js", shell=True, cwd = currentDirectory + '/src')
    print("[+] Template folders created")


def moveCommonFiles():
    print("[+] Moving common files")
    subprocess.call("cp ./commonFiles/* " + workingDirectory + '/' + pname + '/src', shell=True )
    print("[+] Files moved successfully")
    subprocess.call("chmod -R 777 src", shell=True, cwd = workingDirectory + '/' + pname)



if __name__ == '__main__': 
    mOptions = parse_arguments()
    pname = mOptions.pname
    directory = mOptions.directory
    workingDirectory = subprocess.check_output("pwd").rstrip()
    if(directory):
        workingDirectory = directory
        print("[+] Changing working directory to " + workingDirectory)
    installPackages()
    createTemplateFolders()
    moveCommonFiles()

    print("[+] " +pname + " project created")



