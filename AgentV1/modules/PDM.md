# Module: PDM

Product data management tables (PDM* prefix). Terse legacy naming (PDMDB1H, PDMSUP0); meaning not derivable from the DDL alone.

> **This module label is a low-confidence inference** from table-name prefixes. Do not present it to a user as the system's own terminology.

- **Tables**: 34
- **Label basis**: table-name prefix matching
- **Per-table confidence**: {'low': 5, 'medium': 29}

## Most-referenced tables in this module

| Table | Inbound FKs | Columns | Primary key |
|---|---|---|---|
| [`SIZES`](../tables/PDM/SIZES.md) | 6 | 15 | SIZESTYPECOMPANYCODE, SIZESTYPECODE, CODE |
| [`EXPORTENVIRONMENT`](../tables/PDM/EXPORTENVIRONMENT.md) | 4 | 10 | CODE |
| [`SIZESTYPE`](../tables/PDM/SIZESTYPE.md) | 3 | 13 | COMPANYCODE, CODE |
| [`PDMSUP0`](../tables/PDM/PDMSUP0.md) | 2 | 26 | COMPANYCODE, AFRECTYCODE, AFTPREC, AFCITEM, AFVERNR, AFVERST, CSTSUPPCUSTOMERSUPPLIERTYPE, CSTSUPPCUSTOMERSUPPLIERCODE |
| [`PDMDB1`](../tables/PDM/PDMDB1.md) | 2 | 51 | PDMDB1HCOMPANYCODE, PDMDB1HDBRECTYCODE, PDMDB1HDBTPREC, PDMDB1HDBCITEM, PDMDB1HDBVERNR, PDMDB1HDBVERST, PDMDB1HDBSUBFX, DBLINEN |
| [`PDMDB1H`](../tables/PDM/PDMDB1H.md) | 1 | 21 | COMPANYCODE, DBRECTYCODE, DBTPREC, DBCITEM, DBVERNR, DBVERST, DBSUBFX |
| [`PDMCUSTOMIZEDOPTIONS`](../tables/PDM/PDMCUSTOMIZEDOPTIONS.md) | 1 | 21 | COMPANYCODE |
| [`PDMCO1`](../tables/PDM/PDMCO1.md) | 1 | 14 | COMPANYCODE, CORECTYCODE, COTPREC, COCITEM, COVERNR, COVERST, COGRPCO, COCDCOL |
| [`EXPORTENTITY`](../tables/PDM/EXPORTENTITY.md) | 0 | 13 | ENVIRONMENTCODE, ENTITYNAME, COMPANYCODE, TEMPLATECODE, ITEMTYPECODE |
| [`PDMARB0`](../tables/PDM/PDMARB0.md) | 0 | 17 | COMPANYCODE, ITEMTYPECODE, SUBCODE01, SUBCODE02, SUBCODE03, SUBCODE04, SUBCODE05, SUBCODE06, SUBCODE07, SUBCODE08, SUBCODE09, SUBCODE10, COUNTER |
| [`PDMDB2`](../tables/PDM/PDMDB2.md) | 0 | 23 | PDMDB1PDMDB1HCOMPANYCODE, PDMDB1PDMDB1HDBRECTYCODE, PDMDB1PDMDB1HDBTPREC, PDMDB1PDMDB1HDBCITEM, PDMDB1PDMDB1HDBVERNR, PDMDB1PDMDB1HDBVERST, PDMDB1PDMDB1HDBSUBFX, PDMDB1DBLINEN, DMCOLORUSERGENGROUPTYPECODE, DMCOLORCODE, DMLINKEDCOLORUSERGENGRPTYPECOD, DMLINKEDCOLORCODE |
| [`PDMDB6`](../tables/PDM/PDMDB6.md) | 0 | 26 | PDMDB1PDMDB1HCOMPANYCODE, PDMDB1PDMDB1HDBRECTYCODE, PDMDB1PDMDB1HDBTPREC, PDMDB1PDMDB1HDBCITEM, PDMDB1PDMDB1HDBVERNR, PDMDB1PDMDB1HDBVERST, PDMDB1PDMDB1HDBSUBFX, PDMDB1DBLINEN, DSSIZFASIZESTYPECODE, DSSIZFACODE, DSLINKEDSIZFASIZESTYPECODE, DSLINKEDSIZFACODE |
| [`PDMDB2BEAN`](../tables/PDM/PDMDB2BEAN.md) | 0 | 24 | IMPORTAUTOCOUNTER |
| [`PDMDB6BEAN`](../tables/PDM/PDMDB6BEAN.md) | 0 | 25 | IMPORTAUTOCOUNTER |
| [`PDMFULLITEM`](../tables/PDM/PDMFULLITEM.md) | 0 | 14 | COMPANYCODE, ITEMTYPECODE, SUBCODE01, SUBCODE02, SUBCODE03, SUBCODE04, SUBCODE05, SUBCODE06, SUBCODE07, SUBCODE08, SUBCODE09, SUBCODE10 |

## All tables

- [`EXPORTENTITY`](../tables/PDM/EXPORTENTITY.md) — 13 cols
- [`EXPORTENVIRONMENT`](../tables/PDM/EXPORTENVIRONMENT.md) — 10 cols
- [`PDMAR4`](../tables/PDM/PDMAR4.md) — 41 cols
- [`PDMAR4BEAN`](../tables/PDM/PDMAR4BEAN.md) — 50 cols  ⛔ not for business queries
- [`PDMARB0`](../tables/PDM/PDMARB0.md) — 17 cols
- [`PDMARB0BEAN`](../tables/PDM/PDMARB0BEAN.md) — 28 cols  ⛔ not for business queries
- [`PDMCO1`](../tables/PDM/PDMCO1.md) — 14 cols
- [`PDMCO1BEAN`](../tables/PDM/PDMCO1BEAN.md) — 25 cols  ⛔ not for business queries
- [`PDMCO2`](../tables/PDM/PDMCO2.md) — 11 cols
- [`PDMCO2BEAN`](../tables/PDM/PDMCO2BEAN.md) — 15 cols  ⛔ not for business queries
- [`PDMCONFIGURATION`](../tables/PDM/PDMCONFIGURATION.md) — 11 cols
- [`PDMCUSTOMIZEDOPTIONS`](../tables/PDM/PDMCUSTOMIZEDOPTIONS.md) — 21 cols
- [`PDMCUSTOMIZEDOPTIONSBEAN`](../tables/PDM/PDMCUSTOMIZEDOPTIONSBEAN.md) — 36 cols  ⛔ not for business queries
- [`PDMDB1`](../tables/PDM/PDMDB1.md) — 51 cols
- [`PDMDB1BEAN`](../tables/PDM/PDMDB1BEAN.md) — 52 cols  ⛔ not for business queries
- [`PDMDB1H`](../tables/PDM/PDMDB1H.md) — 21 cols
- [`PDMDB1HBEAN`](../tables/PDM/PDMDB1HBEAN.md) — 31 cols  ⛔ not for business queries
- [`PDMDB2`](../tables/PDM/PDMDB2.md) — 23 cols
- [`PDMDB2BEAN`](../tables/PDM/PDMDB2BEAN.md) — 24 cols  ⛔ not for business queries
- [`PDMDB6`](../tables/PDM/PDMDB6.md) — 26 cols
- [`PDMDB6BEAN`](../tables/PDM/PDMDB6BEAN.md) — 25 cols  ⛔ not for business queries
- [`PDMFULLITEM`](../tables/PDM/PDMFULLITEM.md) — 14 cols
- [`PDMFULLITEMBEAN`](../tables/PDM/PDMFULLITEMBEAN.md) — 26 cols  ⛔ not for business queries
- [`PDMNOWITEMKEYLINK`](../tables/PDM/PDMNOWITEMKEYLINK.md) — 21 cols
- [`PDMNOWITEMKEYLINKBEAN`](../tables/PDM/PDMNOWITEMKEYLINKBEAN.md) — 29 cols  ⛔ not for business queries
- [`PDMSUP0`](../tables/PDM/PDMSUP0.md) — 26 cols
- [`PDMSUP0BEAN`](../tables/PDM/PDMSUP0BEAN.md) — 35 cols  ⛔ not for business queries
- [`PDMSUP1`](../tables/PDM/PDMSUP1.md) — 15 cols
- [`PDMSUP1BEAN`](../tables/PDM/PDMSUP1BEAN.md) — 18 cols  ⛔ not for business queries
- [`PDMSUP2`](../tables/PDM/PDMSUP2.md) — 17 cols
- [`PDMSUP2BEAN`](../tables/PDM/PDMSUP2BEAN.md) — 19 cols  ⛔ not for business queries
- [`QAEXPORTENTITY`](../tables/PDM/QAEXPORTENTITY.md) — 11 cols
- [`SIZES`](../tables/PDM/SIZES.md) — 15 cols
- [`SIZESTYPE`](../tables/PDM/SIZESTYPE.md) — 13 cols