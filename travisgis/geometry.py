try:
    from pyspatialite import dbapi2 as sqlite3
except ImportError:
    import sqlite3
from osgeo import ogr

class Geometry(object):
    """Some simple spatial SQLite."""

    def __init__(self, geom):
        self.geom = geom

    def create_schema(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        try:
            conn.enable_load_extension(True)
            conn.load_extension('mod_spatialite')
        except:
            pass
        c.execute('SELECT InitSpatialMetadata()')
        sql = ("CREATE TABLE IF NOT EXISTS test ("
               "PK INTEGER PRIMARY KEY AUTOINCREMENT);")
        c.execute(sql)
        sql = ("SELECT AddGeometryColumn("
               "'test', 'geometry', 4326, 'POINT', 'XY')")
        c.execute(sql)

    def save(self):
        point = ogr.Geometry(ogr.wkbPoint)
        point.AddPoint(1198054.34, 648493.09)
        print(point.ExportToWkt())
