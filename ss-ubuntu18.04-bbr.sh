export LC_ALL=en_US.UTF-8
apt install python-pip -y
pip install setuptools
pip install wheel
pip install shadowsocks

sed -i "s/EVP_CIPHER_CTX_cleanup/EVP_CIPHER_CTX_reset/g" /usr/local/lib/python2.7/dist-packages/shadowsocks/crypto/openssl.py

echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p

ssserver -p 18400 -k lwjxxxx18400 -m aes-256-cfb -t 600 --workers 2 -d start
