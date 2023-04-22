import datetime
import os
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend

path = os.environ.get('SSL_CERTIFICATE_PATH')
if not os.path.exists(path):
    os.makedirs(path)

# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Create a certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u'My Self-Signed Certificate'),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u'My Organization'),
    x509.NameAttribute(NameOID.COUNTRY_NAME, u'US'),
])
cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    x509.BasicConstraints(ca=True, path_length=None),
    critical=True,
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u'localhost')]),
    critical=False,
).sign(private_key, hashes.SHA256(), default_backend())

# Write the private key and certificate to disk
with open(path + "/my_cert.key", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open(path + "/my_cert.crt", "wb") as f:
    f.write(cert.public_bytes(encoding=serialization.Encoding.PEM))
