DROP TABLE IF EXISTS ports CASCADE;
CREATE TABLE ports (
    code text NOT NULL,
    name text NOT NULL
);

DROP TABLE IF EXISTS prices CASCADE;
CREATE TABLE prices (
    orig_code text NOT NULL,
    dest_code text NOT NULL,
    day date NOT NULL,
    price integer NOT NULL
);
