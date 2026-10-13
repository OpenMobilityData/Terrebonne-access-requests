#!/usr/bin/env python3
"""Find which snow-removal contract sector(s) contain rue de Terrebonne, and
list that sector's loading days.

Inputs
  --geojson   secteurs_deneigement_saison_YYYY-YYYY.geojson from
              https://donnees.montreal.ca/dataset/secteur-deneigement (CC-BY 4.0)
  --cache     the daily table written by snow_loading.py build
  --points    "lat,lon" pairs along the street (default: five points on
              Terrebonne between St-Ignatius and Girouard; verify against a map)

Pure Python point-in-polygon (ray casting), so no shapely/geopandas needed.

Example
  python3 terrebonne_sector.py --geojson data/snow_loading/secteurs_deneigement_saison_2025-2026.geojson \
      --cache data/snow_loading/loading_daily.csv --season 2025-2026
"""
import argparse, json, sys
import pandas as pd

# Points along rue de Terrebonne (lat, lon). The three measured ones are the
# Telraam sensors at King-Edward and Royal and the Eco-Counter at Kensington
# (coordinates from the BikeStat source registry); the others are extrapolated
# toward the ends of the lane and should be verified against a map.
DEFAULT_POINTS = [
    (45.4575, -73.6430),   # near Cavendish (extrapolated)
    (45.46392, -73.63756), # Telraam 9794, King-Edward (measured)
    (45.47022, -73.63204), # Eco-Counter, Kensington (measured)
    (45.47303, -73.62965), # Telraam 10045, Royal (measured)
    (45.4755, -73.6250),   # toward Girouard (extrapolated; check)
]


def point_in_ring(lon, lat, ring):
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if ((yi > lat) != (yj > lat)) and (lon < (xj - xi) * (lat - yi) / ((yj - yi) or 1e-12) + xi):
            inside = not inside
        j = i
    return inside


def point_in_geometry(lon, lat, geom):
    t = geom['type']
    polys = geom['coordinates'] if t == 'MultiPolygon' else [geom['coordinates']] if t == 'Polygon' else []
    for poly in polys:
        if point_in_ring(lon, lat, poly[0]) and not any(point_in_ring(lon, lat, hole) for hole in poly[1:]):
            return True
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--geojson', required=True)
    ap.add_argument('--cache')
    ap.add_argument('--season')
    ap.add_argument('--points', nargs='*', help='lat,lon pairs')
    ap.add_argument('--min-loads', type=int, default=25)
    ap.add_argument('--list-fields', action='store_true', help='print the attribute names and exit')
    a = ap.parse_args()

    gj = json.load(open(a.geojson, encoding='utf-8'))
    feats = gj['features']
    if a.list_fields:
        print(sorted(feats[0]['properties'].keys())); print(feats[0]['properties']); return

    pts = [tuple(map(float, p.split(','))) for p in a.points] if a.points else DEFAULT_POINTS
    hits = {}
    for lat, lon in pts:
        found = [f['properties'] for f in feats if point_in_geometry(lon, lat, f['geometry'])]
        names = sorted({str(p.get('NOM_SECTEUR') or p.get('NomSecteur') or p.get('nom_secteur') or p.get('SECTEUR') or p) for p in found})
        print(f'({lat:.4f}, {lon:.4f}) -> {names or "no sector"}')
        for nme in names: hits[nme] = hits.get(nme, 0) + 1
    if not hits:
        sys.exit('No sector contains the given points; check the coordinates or the field names (--list-fields).')
    sectors = sorted(hits, key=hits.get, reverse=True)
    print('\nSectors containing Terrebonne points:', ', '.join(f'{s} ({hits[s]} pts)' for s in sectors))

    if a.cache:
        t = pd.read_csv(a.cache, parse_dates=['day'])
        if a.season: t = t[t['season'] == a.season]
        for s in sectors:
            d = t[t['NomSecteur'] == s].groupby(['season', 'day']).agg(loads=('loads', 'sum'), m3=('m3', 'sum')).reset_index()
            d = d[d['loads'] >= a.min_loads]
            print(f'\n# sector {s}: {len(d)} days with >= {a.min_loads} loads')
            print(d.to_csv(index=False))


if __name__ == '__main__':
    main()
