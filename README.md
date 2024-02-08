# urban-green
Segmentation of aerial images and GeoJSON export.

## GeoJSON export
- Run GeoJSON export: `poetry run python geojson_export/main.py`

## File Formate
* \data\segmentation-ir\*.tiff (Rasterbild in Graustufen (7 Stufen))
- 1 Starke Rückstrahlung (Laubbäume, Dichtevegetation)
- 2 Straße
- 3 Haus
- 4 Mittlerte Rückstrahlung (Wiese, Geräten Nadelbäume)
- 5 Ungenutzt
- 6 Schwache Rückstrahlung (Schwache Rückstrahlung, Beschattete Wiesen und Bäume, Teilbegrünte Hi
- 7 Schatten auf vegetationslosem Gebiet