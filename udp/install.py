# installer for udp
# Copyright 2016 Riccardo Stagni

from setup import ExtensionInstaller

def loader():
    return UDPInstaller()

class UDPInstaller(ExtensionInstaller):
    def __init__(self):
        super(UDPInstaller, self).__init__(
            version="1",
            name='udp',
            description='Emit loop or archive data in UDP format.',
            author="Riccardo Stagni",
            author_email="unriccio@email.it",
            process_services='user.udp.UDP',
            config={
                'UDP': {
                    'port': '42666'}},
            files=[('bin/user', ['bin/user/udp.py'])]
            )
