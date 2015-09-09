# plugin_elastisearch_nagios
## Es un plugin hecho en python que permite monitorear la salud del un cluster de elasticsearch.
La consulta que usa para obtener los datos para el caso en que el cluster sea localhost es:
http://localhost:9200/_cluster/health?pretty</p>

**Requisitos**

Python 2.7 o superior

**Instalacion**

***Cliente***

Ir a descargas
P.e. cd ~/Downloads

Descomprimir
P.e. unzip plugin_elastisearch_nagios*

Ir a carpeta
P.e. cd plugin_elastisearch_nagios*

Copiar plugin_elastisearch_nagios.py a directorio de plugins
P.e. cp plugin_elastisearch_nagios.py /usr/lib/nagios/plugins/

Permisos de ejecucion al plugin
P.e. chmod +x plugin_elastisearch_nagios.py

Prueba local
P.e. cd /usr/lib/nagios/plugins/
./plugin_elastisearch_nagios.py

Registrar command
P.e. vim /etc/nagios/nrpe.cfg

Pegar: command[check_elasticsearch]=/usr/lib/nagios/plugins/plugin_elastisearch_nagios.py
Reinicio nrpe
P.e. service nagios-nrpe-server restart

***Servidor***

Prueba
P.e. /usr/lib/nagios/plugins/check_nrpe -H ip_cliente -c check_elasticsearch




