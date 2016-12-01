from fabric.api import run, sudo, settings, hide, cd, env
from fabric.contrib.files import exists
from termcolor import colored

env.user = "root"
env.password = "vagrant"

with settings(warn_only=False):
    print colored('################################################################', 'red', attrs=['bold'])
    print colored('################################################################', 'red', attrs=['bold'])

    print colored(' ____             _               ____                           ', 'blue', attrs=['bold'])
    print colored('|  _ \  ___   ___| | _____ _ __  / ___|  ___ _ ____   _____ _ __ ', 'blue', attrs=['bold'])
    print colored('| | | |/ _ \ / __| |/ / _ \  __| \___ \ / _ \  __\ \ / / _ \  __|', 'blue', attrs=['bold'])
    print colored('| |_| | (_) | (__|   <  __/ |     ___) |  __/ |   \ V /  __/ |   ', 'blue', attrs=['bold'])
    print colored('|____/ \___/ \___|_|\_\___|_|    |____/ \___|_|    \_/ \___|_|   ', 'blue', attrs=['bold'])

    print colored('                                                                  ', 'blue')
    print colored('                                                                  ', 'blue')

    print colored('                                 xMMMMMMc', 'cyan')
    print colored('                                 xMMMMMMc', 'cyan')
    print colored('                                 xMMMMMMc', 'cyan')
    print colored('                  ......  ...... ;dddddd ', 'cyan')
    print colored('                 oWWWWWWo0NNNNNN,dNNNNNN:                     dOl.', 'cyan')
    print colored('                 dMMMMMMdXMMMMMM,xMMMMMMc                    kMMMWd.', 'cyan')
    print colored('                 dMMMMMMdXMMMMMM,xMMMMMMc                   cMMMMMMO.', 'cyan')
    print colored('                ,,,,,, :xxxxxx;oxxxxxx.:xxxxxx .,,,,,,.           xMMMMMMMO. ....', 'cyan')
    print colored('                .XMMMMMW,dMMMMMMdXMMMMMM,xMMMMMMckMMMMMMc           lMMMMMMMMXNWMWWX0x:.', 'cyan')
    print colored('        .XMMMMMW,dMMMMMMdXMMMMMM,dMMMMMMckMMMMMMc           .0MMMMMMMMMMMMMMMMK.', 'cyan')
    print colored('        .XMMMMMW,dMMMMMMdXMMMMMM,xMMMMMMckMMMMMMc            ;NMMMMMMMMMMMMMWk.', 'cyan')
    print colored(',;;;;;;:dddddddclddddddloddddddclddddddcoddddddl;;;;;;:cldOKWMMMMMMMMMWXOdc.', 'cyan')
    print colored('WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWc''..', 'cyan')
    print colored('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNc', 'cyan')
    print colored('WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN;', 'cyan')
    print colored('0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.', 'cyan')
    print colored(':WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd', 'cyan')
    print colored(' dMMMMMMMMMMMMMMMMMMW0KxKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:', 'cyan')
    print colored('  dMMMMMMMMMMMMMMMMMNOKO0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx,', 'cyan')
    print colored('   oWMMMMMMMMMWWX0ONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.', 'cyan')
    print colored('    .d0o .......    0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOc.', 'cyan')
    print colored('      .dOl.          lNMMMMMMMMMMMMMMMMMMMMMMMMMNOc.', 'cyan')
    print colored('        .:odo:.       .lKWMMMMMMMMMMMMMMMMMWKxc,.', 'cyan')
    print colored('            .;dxxxoc:;, .ckXMMMMMMMMWX0xo: .', 'cyan')
    print colored('                     cxOKNWWWWWWNXKOxo; .', 'cyan')

    print colored('                                                                  ', 'blue')
    print colored('                                                                  ', 'blue')

    print colored('              cd.                                ,dc', 'blue')
    print colored('              XMo                                kMW.', 'blue')
    print colored('     .,:cc: . XMo     .;ccc;.           :ccc;.   kMW.   ;;       :llc;.         . ;:,', 'blue')
    print colored('   c0WW0OOKWW0WMo  .dXMN0OOXMNx.    ,OWWKOO0NW:  kMW..dNMO   ,OWMKOk0NMKl.    :0WWK0x', 'blue')
    print colored('  OMXc     .cXMMo  NMO,      xWN;  oMNo.         kMWONWk,   oWNl.     xMMK  .0MK:.', 'blue')
    print colored(' cMW         .WMo OMk         oMN.,MM:           kMMWx.    ;MM;    .lKM0l.  dMX.', 'blue')
    print colored(' cMN.        .NMl 0Mx         lMW.,MM,           kMMWl     :MM,  ,OWM0;     kM0', 'blue')
    print colored(' .KMO'      '0MK. :WWo.      cNMd  xMK;          kMMXMXl.   xMKl0WXd        kM0', 'blue')
    print colored('  .xWMKdooxKMWd.   ,0MWOdlokNMX:    lNMNkdodOK;  kMW.;0MNo   cXMMNxoxOK:    kM0', 'blue')
    print colored('    .;ldxxdl,        .:oxxxo:.        ,ldxxdo;   ,dl    do      cdxxxo;     ;x:', 'blue')

    print colored('                                                                  ', 'blue')
    print colored('                                                                  ', 'blue')

    print colored('===================================================================', 'blue')
    print colored('DEPENDENCIES PROVISIONING                          ', 'blue', attrs=['bold'])
    print colored('===================================================================', 'blue')
    sudo('yum clean all')
    sudo('yum install -y epel-release python-devel')

    print colored('===================================================================', 'blue')
    print colored('INSTALLING PYTHON PIP                              ', 'blue', attrs=['bold'])
    print colored('===================================================================', 'blue')
    sudo('yum install -y python-pip')
    sudo('pip install --upgrade pip')

    print colored('===================================================================', 'blue')
    print colored('DOCKER ENGINE PROVISIONING                         ', 'blue', attrs=['bold'])
    print colored('===================================================================', 'blue')

    with settings(warn_only=True):
        docker_version = run('docker -v')
        docker_version.strip()
        if "Docker version" not in docker_version:
            # Run the Docker installation script.
            sudo('curl -fsSL https://get.docker.com/ | sh')
        else:
            print colored('===================================================================', 'blue')
            print colored('DOCKER ' + docker_version + ' INSTALLED          ', 'blue', attrs=['bold'])
            print colored('===================================================================', 'blue')

    # Enable the service.
    sudo('systemctl enable docker.service')
    # Start the Docker daemon.
    sudo('systemctl start docker')
    # Verify docker is installed correctly by running a test image in a container.
    sudo('docker run --rm hello-world')
    # Configure the Docker daemon to start automatically when the host starts:
    sudo('systemctl enable docker')

    # The docker daemon binds to a Unix socket instead of a TCP port.
    # By default that Unix socket is owned by the user root and other users can access it with sudo.
    # For this reason, docker daemon always runs as the root user.
    # To avoid having to use sudo when you use the docker command, create a Unix group called
    # docker and add users to it. When the docker daemon starts, it makes the ownership of
    # the Unix socket read/writable by the docker group. Uncoment the sudo() lines below if you like
    # to achieve this result
    with settings(warn_only=True):
        # Create the docker group
        sudo('groupadd docker')
        # Add your user to docker group.
        sudo('usermod -aG docker ' + username)

    print colored('===================================================================', 'blue')
    print colored('DOCKER COMPOSE PROVISIONING                         ', 'blue', attrs=['bold'])
    print colored('===================================================================', 'blue')

    sudo('pip install docker-compose')

    print colored('===================================================================', 'blue')
    print colored('DOCKER MACHINE PROVISIONING                         ', 'blue', attrs=['bold'])
    print colored('===================================================================', 'blue')

    with settings(warn_only=True):
        docker_machine_version = run('docker-machine -v')
        print colored(docker_machine_version, 'red', attrs=['bold'])
        docker_machine_version.strip()
        if "docker-machine version" not in docker_machine_version:
            # Run the Docker installation script.
            sudo('curl -L https://github.com/docker/machine/releases/download/v0.8.2/'
                 'docker-machine-`uname -s`-`uname -m` '
                 '>/usr/local/bin/docker-machine && chmod +x /usr/local/bin/docker-machine')
        else:
            print colored('===================================================================', 'blue')
            print colored('DOCKER ' + docker_machine_version + ' INSTALLED     ', 'blue', attrs=['bold'])
            print colored('===================================================================', 'blue')

def server():
    with settings(warn_only=False):
        sudo('yum install -y git python-devel epel-release python-pip')
        sudo('pip install --upgrade pip')
        sudo('pip install fabric')
        sudo('pip install termcolor')
        sudo('pip install iptools')
        sudo('pip install passlib')
        sudo('pip install --upgrade backports.ssl-match-hostname')
        with cd('/home/vagrant'):
            if exists('/home/vagrant/proton', use_sudo=True):
                with cd('/home/vagrant/proton'):
                    sudo('fab -R local install_docker_centos7:vagrant')
            else:
                run('git clone https://github.com/exequielrafaela/proton.git')
                with cd('/home/vagrant/proton'):
                    sudo('fab -R local install_docker_centos7:vagrant')

        with cd('/lemp_docker_demo'):
            run('docker-compose up -d')

        print colored('===================================================================', 'blue')
        print colored('FIREWALL - NAT TABLE STATUS:                       ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')
        with hide('output'):
            fw = sudo('iptables -t nat -L')
        print colored(fw, 'red')

        print colored('===================================================================', 'blue')
        print colored('FIREWALL - FILTER TABLE STATUS:   ', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')
        with hide('output'):
            fw = sudo('iptables -L')
        print colored(fw, 'red')

        print colored('===================================================================', 'blue')
        print colored('## NETWORK CONFIGURATION #', 'blue', attrs=['bold'])
        print colored('===================================================================', 'blue')
        with hide('output'):
            netconf = sudo('ip addr show')
        print colored(netconf, 'yellow')