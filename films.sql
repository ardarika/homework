--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1
-- Dumped by pg_dump version 15.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    actor_id integer NOT NULL,
    actor_lname character varying(50),
    actor_fname character varying(50),
    birh_year integer,
    film_id integer,
    director_id integer
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_actor_id_seq OWNER TO postgres;

--
-- Name: actors_actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_actor_id_seq OWNED BY public.actors.actor_id;


--
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    director_id integer NOT NULL,
    director_lname character varying(50),
    director_fname character varying(50),
    birh_year integer,
    films_amount integer,
    film_id integer,
    actor_id integer
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- Name: directors_director_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.directors_director_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directors_director_id_seq OWNER TO postgres;

--
-- Name: directors_director_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.directors_director_id_seq OWNED BY public.directors.director_id;


--
-- Name: films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.films (
    film_id integer NOT NULL,
    film_name character varying(150),
    director_lname character varying(50),
    director_fname character varying(50),
    release_year integer,
    imdb numeric,
    actor_id integer,
    director_id integer
);


ALTER TABLE public.films OWNER TO postgres;

--
-- Name: films_film_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.films_film_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.films_film_id_seq OWNER TO postgres;

--
-- Name: films_film_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.films_film_id_seq OWNED BY public.films.film_id;


--
-- Name: actors actor_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN actor_id SET DEFAULT nextval('public.actors_actor_id_seq'::regclass);


--
-- Name: directors director_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors ALTER COLUMN director_id SET DEFAULT nextval('public.directors_director_id_seq'::regclass);


--
-- Name: films film_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.films ALTER COLUMN film_id SET DEFAULT nextval('public.films_film_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (actor_id, actor_lname, actor_fname, birh_year, film_id, director_id) FROM stdin;
1	Reeves	Keanu	1964	2	1
2	McAvoy	James	1979	1	4
3	Fraser	Brendan	1968	4	3
4	Freeman	Morgan	1937	3	2
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors (director_id, director_lname, director_fname, birh_year, films_amount, film_id, actor_id) FROM stdin;
1	Wachowsky	Lana	1965	21	2	1
2	Fincher	David	1962	19	3	4
3	Sommers	Stephen	1962	15	4	3
4	Baird	Jon	1972	11	1	2
\.


--
-- Data for Name: films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.films (film_id, film_name, director_lname, director_fname, release_year, imdb, actor_id, director_id) FROM stdin;
1	Filth	Baird	Jon	2013	7.0	2	4
2	The Matrix	Wachowsky	Lana	1999	8.7	1	1
3	Se7en	Fincher	David	1995	8.6	4	2
4	The Mummy	Sommers	Stephen	1999	7.1	3	3
\.


--
-- Name: actors_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_actor_id_seq', 4, true);


--
-- Name: directors_director_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.directors_director_id_seq', 4, true);


--
-- Name: films_film_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.films_film_id_seq', 4, true);


--
-- PostgreSQL database dump complete
--

