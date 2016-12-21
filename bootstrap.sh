#!/bin/bash

apt-get update
apt-get install -y postgresql libpq-dev
apt-get install -y python3-pip
su ubuntu <<'EOF'
  echo 'export LC_ALL=C' >> /home/ubuntu/.bashrc
  source /home/ubuntu/.bashrc
  sudo pip3 install --upgrade pip
  sudo pip3 install psycopg2
EOF
