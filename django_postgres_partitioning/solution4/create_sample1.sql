SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;


CREATE TABLE sample_sample1 (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    description text NOT NULL
) PARTITION BY RANGE (id);



ALTER TABLE sample_sample1 OWNER TO postgres;


CREATE SEQUENCE new_sample_sample1_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE new_sample_sample1_id_seq OWNER TO postgres;


ALTER SEQUENCE new_sample_sample1_id_seq OWNED BY sample_sample1.id;


ALTER TABLE ONLY sample_sample1 ALTER COLUMN id SET DEFAULT nextval('new_sample_sample1_id_seq'::regclass);
