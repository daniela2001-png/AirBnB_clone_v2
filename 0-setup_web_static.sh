#!/usr/bin/env bash
#configuramos el servidor para hacer el desplegue

#instalamos nginx
sudo apt-get -y update
sudo apt-get -y install nginx

#creo los directorios
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#contenido falso
echo "HOLA SOY DANI LOKS" >> /data/web_static/releases/test/index.html

# creamos un link simbolico entre current y releases
# usamos el flag f -- force remove file if this exists still y el -s que crea uno simbolico y no hard!
ln -sf /data/web_static/releases/test/ /data/web_static/current

# doy permisos al grupo y suario ubuntu al dir /data
sudo chown -R ubuntu:ubuntu /data

#enrutamiento usamos alias en vez de roor
sudo sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default


# reinciamos el servicio de nginx :3
sudo service nginx restart
