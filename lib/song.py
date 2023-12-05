from __init__ import CONN, CURSOR

class Song:
    
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        with CONN:
            CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        with CONN:
            CURSOR.execute(sql, (self.name, self.album))
            self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song