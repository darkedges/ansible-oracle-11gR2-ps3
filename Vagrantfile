# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	file_to_disk = File.realpath(".").to_s+"/disk.vdi"
	
	# Ansible configuration
	config.vm.provision "ansible" do |ansible|
		ansible.playbook = "infrastructure.yml" 
		ansible.verbose = ""
		ansible.raw_ssh_args = ['-o ControlMaster=no']
		ansible.groups = {
			"all"  => ["uom.all"],
		}
		#ansible.tags = "tmp"
	end	 
	
	config.vm.define "R2PS3b" , autostart: true, primary: true do |uomdirectory2|
		uomdirectory2.vm.box = "oraclelinux-7.1-x86_64"
		uomdirectory2.vm.synced_folder "d:/dev/installFiles/R2PS3", "/install"
		uomdirectory2.vm.network :private_network, ip: "192.168.50.100"

		#VirtualBox settings
		uomdirectory2.vm.provider "virtualbox" do |vb|
			vb.customize ["modifyvm", :id, "--memory", "13312"]
			vb.customize ["modifyvm", :id, "--name", "r2ps3b"]
			vb.customize ["modifyvm", :id, "--cpus", "2"]
			vb.customize ["modifyvm", :id, "--ioapic", "on"]
			vb.customize ["modifyvm", :id, "--cpuexecutioncap", "75"]

			# Add Extra Disk
			unless File.exist?(file_to_disk)
				vb.customize ["createhd","--filename", file_to_disk,"--size",30 * 1024]
				vb.customize ["storageattach", :id, "--storagectl", "SATA", "--port", 1, "--device", 0, "--type", "hdd", "--medium", file_to_disk]
			end
		end	
		uomdirectory2.vbguest.auto_update = true
	end
 end

