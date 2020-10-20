| kenmerk              | omschrijving                                                                                | bron          |
|----------------------|---------------------------------------------------------------------------------------------|---------------|
| datum_extractie      | datum creatie bestand                                                                       | afgeleid      |
| poi_id               | identificatie point of interest, komt alleen voor bij verbindingslijn poi -weg              | afgeleid,BAG  |
| poi_type             | typering poi: cluster verblijfsobject, ligplaats, standplaats, school                       | afgeleid      |
| obj_type             | type bag object (verblijfsobject, ligplaats, standplaats)                                   | BAG           |
| obj_id               | identificerend kenmerk zoals bekend in de bron                                              | BAG           |
| obj_status           | status van het object zoals vastgelegd in de BAG                                            | BAG           |
| obj_gebruik          | gebruiksdoel van het object zoals vastgelegd in de BAG                                      | BAG           |
| hoofdadres           | identificerend kenmerk hoofdadres zoals bekend in de bron                                   | BAG           |
| openbareruimtenaam   | naam openbare ruimte zoals bekend in de bron                                                | BAG           |
| huisnummer           | huisnummer zoals bekend in de bron                                                          | BAG           |
| huisletter           | huisletter zoals bekend in de bron                                                          | BAG           |
| huisnummertoevoeging | huisnummertoevoeging zoals bekend in de bron                                                | BAG           |
| postcode             | postcode zoals bekend in de bron                                                            | BAG           |
| woonplaatsnaam       | naam woonplaats zoals bekend in de bron                                                     | BAG           |
| gemeentenaam         | naam gemeente zoals bekend in de bron                                                       | BAG/BRK       |
| geom                 | vorm en ligging van het puntobject in het stelsel van Rijksdriehoeksmeting (RD), epsg:28992 | BAG           |
| pnd_id               | identificerend kenmerk van het pand waarin het verblijfsobject ruimtelijk ligt              | BAG,afgeleid  |
| vot_pnd_cluster      | identificerend kenmerk afgeleid cluster van verblijfsobjecten                               | BAG, afgeleid |