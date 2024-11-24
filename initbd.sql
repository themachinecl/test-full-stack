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

CREATE TABLE {{schema}}.customers (
    login character varying(10) NOT NULL,
    password character varying(20) NOT NULL,
    name character varying(20),
    company_id character varying(20),
    credit_cards character varying(100),
    user_id character varying NOT NULL
);


ALTER TABLE {{schema}}.customers OWNER TO postgres;


CREATE TABLE {{schema}}.deliveries (
    id integer NOT NULL,
    order_item_id numeric(20,0) NOT NULL,
    delivered_quantity numeric(20,0) NOT NULL
);


ALTER TABLE {{schema}}.deliveries OWNER TO postgres;



CREATE SEQUENCE {{schema}}.deliveries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE {{schema}}.deliveries_id_seq OWNER TO postgres;



ALTER SEQUENCE {{schema}}.deliveries_id_seq OWNED BY {{schema}}.deliveries.id;



CREATE TABLE {{schema}}.order_items (
    id integer NOT NULL,
    order_id numeric(20,0) NOT NULL,
    price_per_unit double precision,
    quantity numeric(20,0) NOT NULL,
    product character varying(50)
);


ALTER TABLE {{schema}}.order_items OWNER TO postgres;



CREATE SEQUENCE {{schema}}.order_id_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE {{schema}}.order_id_id_seq OWNER TO postgres;



ALTER SEQUENCE {{schema}}.order_id_id_seq OWNED BY {{schema}}.order_items.id;




CREATE TABLE {{schema}}.orders (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    order_name character varying(50) NOT NULL,
    customer_id character varying(50) NOT NULL
);


ALTER TABLE {{schema}}.orders OWNER TO postgres;



CREATE SEQUENCE {{schema}}.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE {{schema}}.orders_id_seq OWNER TO postgres;



ALTER SEQUENCE {{schema}}.orders_id_seq OWNED BY {{schema}}.orders.id;




ALTER TABLE ONLY {{schema}}.deliveries ALTER COLUMN id SET DEFAULT nextval('{{schema}}.deliveries_id_seq'::regclass);




ALTER TABLE ONLY {{schema}}.order_items ALTER COLUMN id SET DEFAULT nextval('{{schema}}.order_id_id_seq'::regclass);




ALTER TABLE ONLY {{schema}}.orders ALTER COLUMN id SET DEFAULT nextval('{{schema}}.orders_id_seq'::regclass);



ALTER TABLE ONLY {{schema}}.customer_companies
    ADD CONSTRAINT customer_companies_pkey PRIMARY KEY (company_id);




ALTER TABLE ONLY {{schema}}.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (user_id);




ALTER TABLE ONLY {{schema}}.deliveries
    ADD CONSTRAINT deliveries_pkey PRIMARY KEY (id);




ALTER TABLE ONLY {{schema}}.order_items
    ADD CONSTRAINT order_id_pkey PRIMARY KEY (id);



ALTER TABLE ONLY {{schema}}.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);

