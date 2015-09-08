# plugin_elastisearch_nagios
<h3>Es un plugin hecho en python que permite monitorear la salud del un cluster de elasticsearch.</h3>
<p>La consulta que usa para obtener los datos para el caso en que el cluster sea localhost es:</br>
http://localhost:9200/_cluster/health?pretty</p>

<h3>Requisitos</h3>
<ul>
<li>Python 2.7 o superior</li>
</ul>
<h3>Instalacion</h3>
<ul>
<strong>Cliente</strong></br>
</li>Ir a descargas</br>
P.e. cd ~/Downloads</li>
<li>Descomprimir</br>
P.e. unzip plugin_elastisearch_nagios*</li>
<li>Ir a carpeta</br>
P.e. cd plugin_elastisearch_nagios* </li>
<li>Copiar plugin_elastisearch_nagios.py a directorio de plugins</br>
P.e. cp plugin_elastisearch_nagios.py /usr/lib/nagios/plugins/</li>
<li>Permisos de ejecucion al plugin</br>
P.e. chmod +x plugin_elastisearch_nagios.py </li>
<li>Prueba local</br>
P.e. cd /usr/lib/nagios/plugins/<br>
./plugin_elastisearch_nagios.py </li>
<li>Registrar command</br>
P.e. vim /etc/nagios/nrpe.cfg</br>
Pegar: command[check_elasticsearch]=/usr/lib/nagios/plugins/plugin_elastisearch_nagios.py</br></li>
<li>Reinicio nrpe</br>
P.e. service nagios-nrpe-server restart</br>
</li></br>
<strong>Servidor</strong></br>
<li>Prueba</br>
P.e. /usr/lib/nagios/plugins/check_nrpe -H ip_cliente -c check_elasticsearch</li>
</ul>




