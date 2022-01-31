/*
    Postgreql Script to generate the tables and relations for Code Joy
*/

BEGIN;

SET client_encoding = 'UTF8';
SELECT pg_catalog.set_config('search_path', '', false);

CREATE DATABASE code_joy WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_CA.UTF-8';

ALTER DATABASE code_joy OWNER TO postgres;

\connect code_joy

SET default_tablespace = '';
SET default_table_access_method = heap;

CREATE TABLE public.commit_files (
    id integer NOT NULL,
    commit_id character varying(255) NOT NULL,
    file_name character varying(1023) NOT NULL
);

ALTER TABLE public.commit_files OWNER TO postgres;

CREATE SEQUENCE public.commit_files_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.commit_files_id_seq OWNER TO postgres;
ALTER SEQUENCE public.commit_files_id_seq OWNED BY public.commit_files.id;

CREATE TABLE public.commits (
    sha character varying(255) NOT NULL,
    short_sha character varying(8) NOT NULL,
    subject character varying(1023),
    body text,
    rating integer NOT NULL,
    location character varying(1023),
    git_location character varying(1023),
    branch character varying(255) NOT NULL,
    author_id integer,
    committer_id integer,
    commit_date timestamp with time zone DEFAULT now()
);

ALTER TABLE public.commits OWNER TO postgres;

CREATE TABLE public.people (
    id integer NOT NULL,
    name character varying(1023) NOT NULL,
    email character varying(1023)
);

ALTER TABLE public.people OWNER TO postgres;

CREATE SEQUENCE public.people_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.people_id_seq OWNER TO postgres;
ALTER SEQUENCE public.people_id_seq OWNED BY public.people.id;

ALTER TABLE ONLY public.commit_files ALTER COLUMN id SET DEFAULT nextval('public.commit_files_id_seq'::regclass);
ALTER TABLE ONLY public.people ALTER COLUMN id SET DEFAULT nextval('public.people_id_seq'::regclass);

ALTER TABLE ONLY public.commit_files
    ADD CONSTRAINT commit_files_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.commits
    ADD CONSTRAINT commit_pkey PRIMARY KEY (sha);

ALTER TABLE ONLY public.people
    ADD CONSTRAINT people_pkey PRIMARY KEY (id);

CREATE INDEX fki_commiter_fk ON public.commits USING btree (committer_id);

ALTER TABLE ONLY public.commits
    ADD CONSTRAINT author_fk FOREIGN KEY (author_id) REFERENCES public.people(id) NOT VALID;

ALTER TABLE ONLY public.commit_files
    ADD CONSTRAINT commit_fk FOREIGN KEY (commit_id) REFERENCES public.commits(sha);

ALTER TABLE ONLY public.commits
    ADD CONSTRAINT committer_fk FOREIGN KEY (committer_id) REFERENCES public.people(id) NOT VALID;

END;
