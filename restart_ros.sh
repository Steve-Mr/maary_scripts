#! /bin/bash
echo @Noetic0802, | sshpass -p @Noetic0802, ssh -tt -o StrictHostKeyChecking=no maary@39.105.151.205 'sudo reboot -h now'
echo "starting waiting..."
sleep 30
echo "starting roslaunch..."
sshpass -p @Noetic0802, ssh maary@39.105.151.205 "/home/maary/script.sh"
sleep 5
exit 0