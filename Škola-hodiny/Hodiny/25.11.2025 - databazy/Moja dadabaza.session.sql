-- CREATE TABLE spoluziaci (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     meno TEXT,
--     priezvisko TEXT,
--     oci INTEGER,
--     nohy INTEGER
-- );

-- CREATE TABLE oci (
--     id_oci INTEGER PRIMARY KEY AUTOINCREMENT,
--     farba TEXT
-- );

SELECT t1.meno, t2.farba FROM spoluziaci AS t1 INNER JOIN oci AS t2 ON (t1.oci = t2.id_oci)