--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4
-- Dumped by pg_dump version 16.4

-- Started on 2024-11-24 17:30:53

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
-- TOC entry 223 (class 1259 OID 16429)
-- Name: customer_companies; Type: TABLE; Schema: setup! ; Owner: postgres
--

-- Parametrize schema name
-- Parametrize schema name
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM information_schema.schemata
        WHERE schema_name = '{{schema}}'
    ) THEN
        EXECUTE 'CREATE SCHEMA {{schema}}';
    END IF;
END $$;

-- Set search_path to the desired schema
SET search_path TO {{schema}};

CREATE TABLE {{schema}}.customer_companies (
    company_name character varying NOT NULL,
    company_id character varying NOT NULL
);


ALTER TABLE {{schema}}.customer_companies OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16421)
-- Name: customers; Type: TABLE; Schema: {{schema}}; Owner: postgres
--

CREATE TABLE {{schema}}.customers (
    login character varying(10) NOT NULL,
    password character varying(20) NOT NULL,
    name character varying(20),
    company_id character varying(20),
    credit_cards character varying(100),
    user_id character varying NOT NULL
);


ALTER TABLE {{schema}}.customers OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16413)
-- Name: deliveries; Type: TABLE; Schema: {{schema}}; Owner: postgres
--

CREATE TABLE {{schema}}.deliveries (
    id integer NOT NULL,
    order_item_id numeric(20,0) NOT NULL,
    delivered_quantity numeric(20,0) NOT NULL
);


ALTER TABLE {{schema}}.deliveries OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16412)
-- Name: deliveries_id_seq; Type: SEQUENCE; Schema: {{schema}}; Owner: postgres
--

CREATE SEQUENCE {{schema}}.deliveries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE {{schema}}.deliveries_id_seq OWNER TO postgres;

--
-- TOC entry 4809 (class 0 OID 0)
-- Dependencies: 220
-- Name: deliveries_id_seq; Type: SEQUENCE OWNED BY; Schema: {{schema}}; Owner: postgres
--

ALTER SEQUENCE {{schema}}.deliveries_id_seq OWNED BY {{schema}}.deliveries.id;


--
-- TOC entry 219 (class 1259 OID 16406)
-- Name: order_items; Type: TABLE; Schema: {{schema}}; Owner: postgres
--

CREATE TABLE {{schema}}.order_items (
    id integer NOT NULL,
    order_id numeric(20,0) NOT NULL,
    price_per_unit double precision,
    quantity numeric(20,0) NOT NULL,
    product character varying(50)
);


ALTER TABLE {{schema}}.order_items OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16405)
-- Name: order_id_id_seq; Type: SEQUENCE; Schema: {{schema}}; Owner: postgres
--

CREATE SEQUENCE {{schema}}.order_id_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE {{schema}}.order_id_id_seq OWNER TO postgres;

--
-- TOC entry 4810 (class 0 OID 0)
-- Dependencies: 218
-- Name: order_id_id_seq; Type: SEQUENCE OWNED BY; Schema: {{schema}}; Owner: postgres
--

ALTER SEQUENCE {{schema}}.order_id_id_seq OWNED BY {{schema}}.order_items.id;


--
-- TOC entry 217 (class 1259 OID 16399)
-- Name: orders; Type: TABLE; Schema: {{schema}}; Owner: postgres
--

CREATE TABLE {{schema}}.orders (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    order_name character varying(50) NOT NULL,
    customer_id character varying(50) NOT NULL
);


ALTER TABLE {{schema}}.orders OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16398)
-- Name: orders_id_seq; Type: SEQUENCE; Schema: {{schema}}; Owner: postgres
--

CREATE SEQUENCE {{schema}}.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE {{schema}}.orders_id_seq OWNER TO postgres;

--
-- TOC entry 4811 (class 0 OID 0)
-- Dependencies: 216
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: {{schema}}; Owner: postgres
--

ALTER SEQUENCE {{schema}}.orders_id_seq OWNED BY {{schema}}.orders.id;


--
-- TOC entry 4650 (class 2604 OID 16416)
-- Name: deliveries id; Type: DEFAULT; Schema: {{schema}}; Owner: postgres
--

ALTER TABLE ONLY {{schema}}.deliveries ALTER COLUMN id SET DEFAULT nextval('{{schema}}.deliveries_id_seq'::regclass);


--
-- TOC entry 4649 (class 2604 OID 16409)
-- Name: order_items id; Type: DEFAULT; Schema: {{schema}}; Owner: postgres
--

ALTER TABLE ONLY {{schema}}.order_items ALTER COLUMN id SET DEFAULT nextval('{{schema}}.order_id_id_seq'::regclass);


--
-- TOC entry 4648 (class 2604 OID 16402)
-- Name: orders id; Type: DEFAULT; Schema: {{schema}}; Owner: postgres
--

ALTER TABLE ONLY {{schema}}.orders ALTER COLUMN id SET DEFAULT nextval('{{schema}}.orders_id_seq'::regclass);


--
-- TOC entry 4660 (class 2606 OID 16452)
-- Name: customer_companies customer_companies_pkey; Type: CONSTRAINT; Schema: {{schema}}; Owner: postgres
--

ALTER TABLE ONLY {{schema}}.customer_companies
    ADD CONSTRAINT customer_companies_pkey PRIMARY KEY (company_id);


--
-- TOC entry 4658 (class 2606 OID 16450)
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: {{schema}}; Owner: postgres
--

ALTER TABLE ONLY {{schema}}.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (user_id);


--
-- TOC entry 4656 (class 2606 OID 16420)
-- Name: deliveries deliveries_pkey; Type: CONSTRAINT; Schema: {{schema}}; Owner: postgres
--

ALTER TABLE ONLY {{schema}}.deliveries
    ADD CONSTRAINT deliveries_pkey PRIMARY KEY (id);


--
-- TOC entry 4654 (class 2606 OID 16411)
-- Name: order_items order_id_pkey; Type: CONSTRAINT; Schema: {{schema}}; Owner: postgres
--

ALTER TABLE ONLY {{schema}}.order_items
    ADD CONSTRAINT order_id_pkey PRIMARY KEY (id);


--
-- TOC entry 4652 (class 2606 OID 16404)
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: {{schema}}; Owner: postgres
--

ALTER TABLE ONLY {{schema}}.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


-- Completed on 2024-11-24 17:30:53

--
-- PostgreSQL database dump complete
--

