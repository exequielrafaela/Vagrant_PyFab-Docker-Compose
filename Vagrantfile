
# Specify Vagrant version, Vagrant API version, and desired clone location
Vagrant.require_version '>= 1.8.0'
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  if !Vagrant.has_plugin?("vagrant-fabric")
       	system('vagrant plugin install vagrant-fabric')

       raise("vagrant-fabric installed. Run command \"vagrant up\" again.");
  end

  if !Vagrant.has_plugin?("vagrant-hostmanager")
       	system('vagrant plugin install vagrant-hostmanager')

       raise("vagrant-hostmanager installed. Run command \"vagrant up\" again.");
  end

  # Assign additional private network, w/ auto-configure and DHCP
  config.vm.network "private_network", type: "dhcp"
  config.hostmanager.enabled = true
  config.hostmanager.ip_resolver = proc do |vm, resolving_vm|
	  if vm.id
		    `VBoxManage guestproperty get #{vm.id} "/VirtualBox/GuestInfo/Net/1/V4/IP"`.split()[1]
	  end
  end

  # Create and configure the VM
  config.vm.define :server do |srv|
    srv.vm.box = "geerlingguy/centos7"
    srv.vm.synced_folder ".", "/lemp_docker_demo", create: true
    # Configure CPU & RAM per settings
    srv.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
      vb.cpus = 1
    end
    srv.vm.hostname = "dockerserver"
    # Provisioner Python Fabric
    srv.vm.provision :fabric do |fabric|
      fabric.fabfile_path = "./fabfile.py"
      fabric.tasks = ["server", ]
    end
  end
end
