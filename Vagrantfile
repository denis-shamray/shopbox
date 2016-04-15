Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty32"
  config.vm.network "forwarded_port", guest: 8000, host_ip: "127.0.0.1", host: 8080
  config.vm.provider "virtualbox" do |vb|
#    vb.name = "shopbox"
    vb.memory = 512
    vb.cpus = 1
  end
  config.vm.provision "shell", run: "always", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install htop screen mc git python-setuptools libjpeg-dev zlib1g-dev python-dev -y
    sudo easy_install pip
    sudo pip install -r /vagrant/requirements.txt
    cd /vagrant
    python manage.py migrate
    python manage.py loaddata main/fixtures/goods.json
    sudo -su vagrant screen -dmS django bash -c 'python manage.py runserver 0.0.0.0:8000' && echo "Django server has been started"
  SHELL
end
