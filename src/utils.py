import ssl

def create_server_context():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="certs/server.pem", keyfile="certs/server.key")
    context.load_verify_locations(cafile="certs/ca.pem")

    context.verify_mode = ssl.CERT_REQUIRED  # mTLS
    context.minimum_version = ssl.TLSVersion.TLSv1_3

    return context


def create_client_context():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_cert_chain(certfile="certs/client.pem", keyfile="certs/client.key")
    context.load_verify_locations(cafile="certs/ca.pem")

    context.check_hostname = False
    context.minimum_version = ssl.TLSVersion.TLSv1_3

    return context
