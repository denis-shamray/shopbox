Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty32"
  config.vm.network "forwarded_port", guest_ip: "127.0.0.1", guest: 8000, host_ip: "127.0.0.1", host: 8080
  config.vm.provider "virtualbox" do |vb|
#    vb.name = "shopbox0.1"
    vb.memory = 512
    vb.cpus = 2
  end
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install git -y
    sudo apt-get install python-setuptools -y
    sudo easy_install pip
    sudo pip install -r /vagrant/requirements.txt
    cd /vagrant
    python manage.py migrate
  SHELL
end
