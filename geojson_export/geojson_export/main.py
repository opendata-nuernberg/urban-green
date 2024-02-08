import argparse
import glob
import logging
import os
import tempfile

import geobuf
import geopandas as gpd

log = logging.getLogger("GeoJSON")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='GeoJSON Exporter',
                    description='This program exports GeoPackage data to GeoJSON.',
                    epilog='Thanks for using it :-)')
    parser.add_argument('--input-folder', default='../data/segmentation-ir')
    parser.add_argument('--output-folder', default='../data/segmentation-ir')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-c', '--compress', action='store_true')

    args = parser.parse_args()
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    assert os.path.exists(args.input_folder), f"Input folder not found: {args.input_folder}"
    gpkg_files = glob.glob(os.path.join(args.input_folder, "**/*.gpkg"), recursive=True)
    assert len(gpkg_files) > 0, f"No .gpkg files found in {args.input_folder}"
    for input_filepath in gpkg_files:
        log.info(f"Processing {input_filepath} ...")
        basename = os.path.basename(os.path.splitext(input_filepath)[0])
        output_filepath = os.path.join(args.output_folder, basename)
        gdf = gpd.read_file(filename=input_filepath)
        if args.compress:
            geo_json = gdf.to_json()
            with open(f"{output_filepath}.pbf", 'w') as f:
                f.write(geobuf.encode(geo_json))
        else:
            gdf.to_file(f"{output_filepath}.geojson", driver="GeoJSON")