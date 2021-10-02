from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.filesystems import UnixFilesystem


def main():
    # authorizers = UnixAuthorizer(rejected_users=['root'], require_valid_shell=True)
    authorizers = DummyAuthorizer()

    authorizers.add_user('usuario', 'senha', 'diretorio', perm='elradfmwMT')
    handler = FTPHandler
    handler.authorizer = authorizers
    handler.banner = "pyftpdlib FTP lido"
    # handler.abstracted_fs = UnixFilesystem
    endereco = ('192.168.0.13', 2121)
    server = FTPServer(endereco, handler)

    server.max_cons = 5
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == '__main__':
    main() 