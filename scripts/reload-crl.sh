cat '/etc/pki/CA/intermediate/certs/mozipo-intermediate.cert.pem' '/etc/pki/CA/certs/mozipo-ca.cert.pem' > 'ca-chain.cert.pem'
openssl ca -config /etc/pki/CA/openssl.cnf -gencrl -out /etc/pki/CA/crl/mozipo-ca.crl.pem
openssl crl -in /etc/pki/CA/crl/mozipo-ca.crl.pem -noout -text | less
cat '/etc/pki/CA/intermediate/crl/mozipo-intermediate.crl.pem' '/etc/pki/CA/crl/mozipo-ca.crl.pem'  > '/etc/pki/CA/intermediate/crl/crl-chain.crl.pem' 
openssl crl -in '/etc/pki/CA/intermediate/crl/crl-chain.crl.pem' -noout -text | less
systemctl reload nginx
