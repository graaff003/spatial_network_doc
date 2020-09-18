# Loop- en fietsnetwerk documentatie

Het loop- en fietsnetwerk is afgeleid uit Openstreetmap (OSM) en Basisregistratie Grootschalige Topografie (BGT).
Alle woningen in Amsterdam met adressen (POI) zijn gekoppeld aan dit netwerk.

De dataset bestaat uit drie layers:
 - [adam_netwerk_voetfiets_edges](edges.md)
 - [adam_netwerk_voetfiets_nodes_poi](nodes_poi.md)
 - [adam_netwerk_voetfiets_poi_adressen](poi_adressen.md)

Aantallen (afgerond):

 - adressen:   606,500 
 - edges:    1,985,000
 - nodes:    1,454,500

De dataset is te dowladen via [data.amsterdam.nl](https://data.amsterdam.nl/datasets/7hGzsRXqWSGqHw/loop-en-fietsnetwerk-amsterdam/)

De **edges** (aslijnen wegen) zijn gerelateerd aan de nodes via:
edges.node_startpoint = nodes_poi.node_id en
edges.node_endpoint = nodes_poi.node_id

De nodes en pois zijn geintegreerd 1 in tabel, **nodes_poi**.
Alle pois van het type vot_cluster, ligplaats en standplaats hebben een relatie naar **poi_adressen**. Deze relatie loopt als volgt:
nodes_poi.poi_id = poi_adressen.poi_id.

De pois van het type vot_cluster (cluster van verblijfsobjecten) hebben vaak een relatie van 1:n. Een cluster heeft een relatie met meerdere adressen.

In de onderstaande afbeelding worden de relaties schematisch weergegeven.

![relaties](relations.png)
