
| kenmerk                        | omschrijving                                                                                                     | bron                                     |
|--------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| datum_extractie                | datum creatie bestand                                                                                            | afgeleid                                 |
| fid_pk                         | technische sleutel                                                                                               | afgeleid                                 |
| straatnaam                     | straatnaam uit OSM                                                                                               | openStreetmap (OSM)                      |
| ind_voetfiets                  | indicatie geschikt voor voetganger                                                                               | OSM                                      |
| wegklasse                      | wegklassen afgeleid uit BGT, OSM en afleidingen                                                                  | OSM                                      |
| hoogteniveau                   | relatieve hoogte: 0=maaiveld                                                                                     | BGT voor voetpaden, overig openStreetmap |
| ind_brug                       | indicatie of de aslijn samenvalt met een brug                                                                    | OSM                                      |
| ind_tunnel                     | indicatie of de aslijn samenvalt met een tunnel                                                                  | OSM                                      |
| ind_ov_bus                     | indicatie mede bedoeld voor busverkeer                                                                           | OSM                                      |
| ind_ov_spoor                   | idicatie of het een spoorbaan betreft                                                                            | OSM                                      |
| ind_toegankelijkheid           | toegankelijk voor niet gemotoriseerd verkeer                                                                     | OSM                                      |
| max_snelheid                   | maximun toegestane snelheid                                                                                      | OSM                                      |
| ov_veer_route                  | indicatie route veerpont                                                                                         | OSM                                      |
| van_blok_id                    | identificatie groepering aslijnen (intern gebruik)                                                               | afgeleid                                 |
| naar_blok_id                   | identificatie groepering aslijnen (intern gebruik)                                                               | afgeleid                                 |
| min_breedte                    | laagste waarde voorkomende breedte bij aslijn, komt alleen voor bij voetpaden                                    | BGT                                      |
| max_breedte                    | hoogste waarde voorkomende breedte bij aslijn, komt alleen voor bij voetpaden                                    | BGT                                      |
| gewogen_gemiddelde_breedte     | gewogen gemiddelde waarde voorkomende breedte bij aslijn, komt alleen voor bij voetpaden                         | BGT                                      |
| poi_id                         | identificatie point of interest, komt alleen voor bij verbindingslijn poi -weg                                   | afgeleid                                 |
| poi_type                       | typering poi: cluster verblijfsobject, ligplaats, standplaats, school                                            | BAG, scholenbestand                      |
| lengte_intersectie_water       | lengte van het lijnstuk dat overlapt met water. komt alleen voor bij verbindingslijnen tussen poi en weg         | BGT                                      |
| lengteklasse_intersectie_water | breedteklasse, van het lijnstuk dat overlapt met water. komt alleen voor bij verbindingslijnen tussen poi en weg | BGT                                      |
| geometrie                      | vorm en ligging van het lijnstuk in het stelsel van Rijksdriehoeksmeting (RD), epsg:28992                        | BGT, OSM                                 |
| weight                         | weight van de edge als functie van de afstand , nu: weight=1 X afstand in Meter                                  | BGT, OSM                                 |
| node_startpoint                | relatie naar beginpunt (node)                                                                                    | BGT, OSM                                 |
| node_endpoint                  | relatie naar eindpunt (node)                                                                                     | BGT, OSM                                 |