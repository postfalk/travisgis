try:
    from pyspatialite import dbapi2 as sqlite3
except ImportError:
    import sqlite3


class Point(object):
    """Some simple spatial SQLite."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def connection(self):
        conn = sqlite3.connect('test.db')
        try:
            conn.enable_load_extension(True)
        except:
            pass
        try:
            conn.load_extension('libspatialite.so')  # Ubuntu
        except sqlite3.OperationalError:
            try:
                conn.load_extension('mod_spatialite')  # OSX
            except:
                pass
        return conn.cursor()

    def create_schema(self):
        c = self.connection()
        c.execute('SELECT InitSpatialMetadata()')
        sql = ("CREATE TABLE IF NOT EXISTS test ("
               "PK INTEGER PRIMARY KEY AUTOINCREMENT);")
        c.execute(sql)
        sql = ("SELECT AddGeometryColumn("
               "'test', 'geometry', 4326, 'POINT', 'XY')")
        c.execute(sql)

    def save(self):
        c = self.connection()
        sql = (
            "INSERT INTO test (geometry) "
            "VALUES (GeomFromText('POINT({} {})', 4326));".format(
                self.x, self.y))
        c.execute(sql)
