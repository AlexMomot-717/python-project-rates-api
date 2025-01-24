SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

CREATE TABLE ports (
    code text NOT NULL,
    name text NOT NULL
);

CREATE TABLE prices (
    orig_code text NOT NULL,
    dest_code text NOT NULL,
    day date NOT NULL,
    price integer NOT NULL
);

COPY ports (code, name) FROM stdin;
NLRTM	Rotterdam
CNSGH	Shanghai
RULED	Saint-Petersburg
NOOSL	Oslo
\.


--
-- Data for Name: prices; Type: TABLE DATA; Schema: tasks; Owner: -
--

COPY prices (orig_code, dest_code, day, price) FROM stdin;
CNSGH	RULED	2016-01-01	1900
CNSGH	RULED	2016-01-01	2212
CNSGH	RULED	2016-01-01	1915
CNSGH	RULED	2016-01-02	1900
CNSGH	RULED	2016-01-02	2212
CNSGH	RULED	2016-01-02	1915
CNSGH	RULED	2016-01-03	1900
CNSGH	RULED	2016-01-03	2212
CNSGH	RULED	2016-01-03	1915
CNSGH	RULED	2016-01-04	1900
CNSGH	RULED	2016-01-04	2212
CNSGH	RULED	2016-01-04	1915
CNSGH	RULED	2016-01-05	1900
CNSGH	RULED	2016-01-05	2212
CNSGH	RULED	2016-01-05	1915
CNSGH	RULED	2016-01-06	1900
CNSGH	RULED	2016-01-06	2212
CNSGH	RULED	2016-01-06	1915
CNSGH	RULED	2016-01-07	1900
CNSGH	RULED	2016-01-07	2212
CNSGH	RULED	2016-01-07	1915
CNSGH	RULED	2016-01-08	1900
CNSGH	RULED	2016-01-08	2212
CNSGH	RULED	2016-01-08	1915
CNSGH	RULED	2016-01-09	1900
CNSGH	RULED	2016-01-09	2212
CNSGH	RULED	2016-01-09	1915
CNSGH	RULED	2016-01-10	1900
CNSGH	RULED	2016-01-10	2212
CNSGH	RULED	2016-01-10	1915
CNSGH	RULED	2016-01-11	1900
CNSGH	RULED	2016-01-11	2212
CNSGH	RULED	2016-01-11	1915
CNSGH	RULED	2016-01-12	1900
CNSGH	RULED	2016-01-12	2212
CNSGH	RULED	2016-01-12	1915
CNSGH	RULED	2016-01-13	1900
CNSGH	RULED	2016-01-13	2212
CNSGH	RULED	2016-01-13	1915
CNSGH	RULED	2016-01-14	1900
CNSGH	RULED	2016-01-14	2212
CNSGH	RULED	2016-01-14	1915
CNSGH	RULED	2016-01-15	1900
CNSGH	RULED	2016-01-15	2212
CNSGH	RULED	2016-01-15	1915
CNSGH	RULED	2016-01-16	1900
CNSGH	RULED	2016-01-16	2212
CNSGH	RULED	2016-01-16	1915
CNSGH	RULED	2016-01-17	1900
CNSGH	RULED	2016-01-17	2212
CNSGH	RULED	2016-01-17	1915
CNSGH	RULED	2016-01-18	1900
CNSGH	RULED	2016-01-18	2212
CNSGH	RULED	2016-01-18	1915
CNSGH	RULED	2016-01-19	1900
CNSGH	RULED	2016-01-19	2212
CNSGH	RULED	2016-01-19	1915
CNSGH	RULED	2016-01-20	1900
CNSGH	RULED	2016-01-20	2212
CNSGH	RULED	2016-01-20	1915
CNSGH	RULED	2016-01-21	1900
CNSGH	RULED	2016-01-21	2212
CNSGH	RULED	2016-01-21	1915
CNSGH	RULED	2016-01-22	1900
CNSGH	RULED	2016-01-22	2212
CNSGH	RULED	2016-01-22	1915
CNSGH	RULED	2016-01-23	1900
CNSGH	RULED	2016-01-23	2212
CNSGH	RULED	2016-01-23	1915
CNSGH	RULED	2016-01-24	1900
CNSGH	RULED	2016-01-24	2212
CNSGH	RULED	2016-01-24	1915
CNSGH	RULED	2016-01-25	1900
CNSGH	RULED	2016-01-25	2212
CNSGH	RULED	2016-01-25	1915
CNSGH	RULED	2016-01-26	1900
CNSGH	RULED	2016-01-26	2212
CNSGH	RULED	2016-01-26	1915
CNSGH	RULED	2016-01-27	1900
CNSGH	RULED	2016-01-27	2212
CNSGH	RULED	2016-01-27	1915
CNSGH	RULED	2016-01-28	1900
CNSGH	RULED	2016-01-28	2212
CNSGH	RULED	2016-01-28	1915
CNSGH	RULED	2016-01-29	1900
CNSGH	RULED	2016-01-29	2212
CNSGH	RULED	2016-01-29	1915
CNSGH	RULED	2016-01-30	1900
CNSGH	RULED	2016-01-30	2212
CNSGH	RULED	2016-01-30	1915
CNSGH	RULED	2016-01-31	1900
CNSGH	RULED	2016-01-31	2212
CNSGH	RULED	2016-01-31	1915
CNSGH	NOOSL	2016-01-01	1619
CNSGH	NOOSL	2016-01-01	1776
CNSGH	NOOSL	2016-01-01	1719
CNSGH	NOOSL	2016-01-02	1619
CNSGH	NOOSL	2016-01-02	1775
CNSGH	NOOSL	2016-01-02	1719
CNSGH	NOOSL	2016-01-03	1619
CNSGH	NOOSL	2016-01-03	1776
CNSGH	NOOSL	2016-01-03	1719
CNSGH	NOOSL	2016-01-04	1619
CNSGH	NOOSL	2016-01-04	1775
CNSGH	NOOSL	2016-01-04	1719
CNSGH	NOOSL	2016-01-05	1618
CNSGH	NOOSL	2016-01-05	1774
CNSGH	NOOSL	2016-01-05	1719
CNSGH	NOOSL	2016-01-06	1392
CNSGH	NOOSL	2016-01-06	1773
CNSGH	NOOSL	2016-01-06	1718
CNSGH	NOOSL	2016-01-07	1393
CNSGH	NOOSL	2016-01-07	1424
CNSGH	NOOSL	2016-01-07	1719
CNSGH	NOOSL	2016-01-08	1393
CNSGH	NOOSL	2016-01-08	1424
CNSGH	NOOSL	2016-01-08	1419
CNSGH	NOOSL	2016-01-09	1393
CNSGH	NOOSL	2016-01-09	1425
CNSGH	NOOSL	2016-01-09	1419
CNSGH	NOOSL	2016-01-10	1394
CNSGH	NOOSL	2016-01-10	1425
CNSGH	NOOSL	2016-01-10	1419
CNSGH	NOOSL	2016-01-11	1218
CNSGH	NOOSL	2016-01-11	1224
CNSGH	NOOSL	2016-01-11	1219
CNSGH	NOOSL	2016-01-12	1218
CNSGH	NOOSL	2016-01-12	1225
CNSGH	NOOSL	2016-01-12	1219
CNSGH	NOOSL	2016-01-13	1219
CNSGH	NOOSL	2016-01-13	1225
CNSGH	NOOSL	2016-01-13	1219
CNSGH	NOOSL	2016-01-14	1220
CNSGH	NOOSL	2016-01-14	1227
CNSGH	NOOSL	2016-01-14	1220
CNSGH	NOOSL	2016-01-15	1219
CNSGH	NOOSL	2016-01-15	1226
CNSGH	NOOSL	2016-01-15	1219
CNSGH	NOOSL	2016-01-16	1219
CNSGH	NOOSL	2016-01-16	1126
CNSGH	NOOSL	2016-01-16	1119
CNSGH	NOOSL	2016-01-17	1219
CNSGH	NOOSL	2016-01-17	1126
CNSGH	NOOSL	2016-01-17	1119
CNSGH	NOOSL	2016-01-18	1218
CNSGH	NOOSL	2016-01-18	1075
CNSGH	NOOSL	2016-01-18	1119
CNSGH	NOOSL	2016-01-19	1219
CNSGH	NOOSL	2016-01-19	1076
CNSGH	NOOSL	2016-01-19	1119
CNSGH	NOOSL	2016-01-20	1219
CNSGH	NOOSL	2016-01-20	1075
CNSGH	NOOSL	2016-01-20	1119
CNSGH	NOOSL	2016-01-21	1060
CNSGH	NOOSL	2016-01-21	1076
CNSGH	NOOSL	2016-01-21	1119
CNSGH	NOOSL	2016-01-22	1061
CNSGH	NOOSL	2016-01-22	1077
CNSGH	NOOSL	2016-01-22	920
CNSGH	NOOSL	2016-01-23	1061
CNSGH	NOOSL	2016-01-23	927
CNSGH	NOOSL	2016-01-23	920
CNSGH	NOOSL	2016-01-24	1061
CNSGH	NOOSL	2016-01-24	928
CNSGH	NOOSL	2016-01-24	920
CNSGH	NOOSL	2016-01-25	986
CNSGH	NOOSL	2016-01-25	877
CNSGH	NOOSL	2016-01-25	870
CNSGH	NOOSL	2016-01-26	987
CNSGH	NOOSL	2016-01-26	878
CNSGH	NOOSL	2016-01-26	870
CNSGH	NOOSL	2016-01-27	937
CNSGH	NOOSL	2016-01-27	879
CNSGH	NOOSL	2016-01-27	870
CNSGH	NOOSL	2016-01-28	938
CNSGH	NOOSL	2016-01-28	880
CNSGH	NOOSL	2016-01-28	871
CNSGH	NOOSL	2016-01-29	887
CNSGH	NOOSL	2016-01-29	879
CNSGH	NOOSL	2016-01-29	870
CNSGH	NOOSL	2016-01-30	887
CNSGH	NOOSL	2016-01-30	829
CNSGH	NOOSL	2016-01-30	870
CNSGH	NOOSL	2016-01-31	887
CNSGH	NOOSL	2016-01-31	829
CNSGH	NOOSL	2016-01-31	870
CNSGH	NLRTM	2016-01-01	736
CNSGH	NLRTM	2016-01-01	710
CNSGH	NLRTM	2016-01-01	1200
CNSGH	NLRTM	2016-01-02	736
CNSGH	NLRTM	2016-01-02	710
CNSGH	NLRTM	2016-01-02	1200
CNSGH	NLRTM	2016-01-03	736
CNSGH	NLRTM	2016-01-03	710
CNSGH	NLRTM	2016-01-03	1200
CNSGH	NLRTM	2016-01-04	736
CNSGH	NLRTM	2016-01-04	710
CNSGH	NLRTM	2016-01-04	1200
CNSGH	NLRTM	2016-01-05	736
CNSGH	NLRTM	2016-01-05	710
CNSGH	NLRTM	2016-01-05	1200
CNSGH	NLRTM	2016-01-06	736
CNSGH	NLRTM	2016-01-06	710
CNSGH	NLRTM	2016-01-06	1200
CNSGH	NLRTM	2016-01-07	736
CNSGH	NLRTM	2016-01-07	710
CNSGH	NLRTM	2016-01-07	1200
CNSGH	NLRTM	2016-01-08	736
CNSGH	NLRTM	2016-01-08	560
CNSGH	NLRTM	2016-01-08	1200
CNSGH	NLRTM	2016-01-09	736
CNSGH	NLRTM	2016-01-09	560
CNSGH	NLRTM	2016-01-09	1200
CNSGH	NLRTM	2016-01-10	736
CNSGH	NLRTM	2016-01-10	560
CNSGH	NLRTM	2016-01-10	1200
CNSGH	NLRTM	2016-01-11	736
CNSGH	NLRTM	2016-01-11	560
CNSGH	NLRTM	2016-01-11	1200
CNSGH	NLRTM	2016-01-12	736
CNSGH	NLRTM	2016-01-12	560
CNSGH	NLRTM	2016-01-12	1200
CNSGH	NLRTM	2016-01-13	736
CNSGH	NLRTM	2016-01-13	560
CNSGH	NLRTM	2016-01-13	1200
CNSGH	NLRTM	2016-01-14	736
CNSGH	NLRTM	2016-01-14	560
CNSGH	NLRTM	2016-01-14	1200
CNSGH	NLRTM	2016-01-15	736
CNSGH	NLRTM	2016-01-15	560
CNSGH	NLRTM	2016-01-15	1200
CNSGH	NLRTM	2016-01-16	736
CNSGH	NLRTM	2016-01-16	560
CNSGH	NLRTM	2016-01-16	1200
CNSGH	NLRTM	2016-01-17	736
CNSGH	NLRTM	2016-01-17	560
CNSGH	NLRTM	2016-01-17	1200
CNSGH	NLRTM	2016-01-18	736
CNSGH	NLRTM	2016-01-18	560
CNSGH	NLRTM	2016-01-18	1200
CNSGH	NLRTM	2016-01-19	736
CNSGH	NLRTM	2016-01-19	560
CNSGH	NLRTM	2016-01-19	1200
CNSGH	NLRTM	2016-01-20	736
CNSGH	NLRTM	2016-01-20	560
CNSGH	NLRTM	2016-01-20	1200
CNSGH	NLRTM	2016-01-21	736
CNSGH	NLRTM	2016-01-21	560
CNSGH	NLRTM	2016-01-21	1200
CNSGH	NLRTM	2016-01-22	736
CNSGH	NLRTM	2016-01-22	560
CNSGH	NLRTM	2016-01-22	1200
CNSGH	NLRTM	2016-01-23	736
CNSGH	NLRTM	2016-01-23	560
CNSGH	NLRTM	2016-01-23	1200
CNSGH	NLRTM	2016-01-24	686
CNSGH	NLRTM	2016-01-24	560
CNSGH	NLRTM	2016-01-24	1200
CNSGH	NLRTM	2016-01-25	686
CNSGH	NLRTM	2016-01-25	560
CNSGH	NLRTM	2016-01-25	1200
CNSGH	NLRTM	2016-01-26	686
CNSGH	NLRTM	2016-01-26	560
CNSGH	NLRTM	2016-01-26	1200
CNSGH	NLRTM	2016-01-27	686
CNSGH	NLRTM	2016-01-27	560
CNSGH	NLRTM	2016-01-27	1200
CNSGH	NLRTM	2016-01-28	686
CNSGH	NLRTM	2016-01-28	560
CNSGH	NLRTM	2016-01-28	1200
CNSGH	NLRTM	2016-01-29	636
CNSGH	NLRTM	2016-01-29	560
CNSGH	NLRTM	2016-01-29	1200
CNSGH	NLRTM	2016-01-30	636
CNSGH	NLRTM	2016-01-30	560
CNSGH	NLRTM	2016-01-30	1200
CNSGH	NLRTM	2016-01-31	636
CNSGH	NLRTM	2016-01-31	560
CNSGH	NLRTM	2016-01-31	1200
\.

-- Make Jan 3 have no prices at all
DELETE FROM prices WHERE day = date'2016-01-03';

--
-- Create database copy for tests:
--

CREATE DATABASE testapi_db TEMPLATE task;
