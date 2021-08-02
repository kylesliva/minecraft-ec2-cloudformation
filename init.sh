#init steps
# morph this into cfn-init
mkdir /mnt/minecraft
# if this is your first run you must format /dev/nvme1n1 as ext4
mount /dev/nvme1n1 /mnt/minecraft/

# jdk install process from https://docs.aws.amazon.com/corretto/latest/corretto-16-ug/generic-linux-install.html
# test both ways between installing java as a cmd or in pkgs block
rpm --import https://yum.corretto.aws/corretto.key 
curl -L -o /etc/yum.repos.d/corretto.repo https://yum.corretto.aws/corretto.repo
yum install -y java-16-amazon-corretto-devel

# manage cfg here perhaps?
wget https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar -P /tmp/
cd /mnt/minecraft/; java -Xms256M -Xmx1024M -XX:+UseG1GC -server -jar /tmp/server.jar nogui

# post-init commands
# check cfn-init status
tail -f /var/log/cfn-init.log


# gotta run this to push tags to github
git push --tags