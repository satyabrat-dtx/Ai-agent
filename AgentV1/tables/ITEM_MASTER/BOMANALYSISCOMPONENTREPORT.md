# DB2ADMIN.BOMANALYSISCOMPONENTREPORT

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 39
- **Primary key**: `IDENTIFIER`, `PROGRESSIVE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 20963

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `PROGRESSIVE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 19 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 20 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 21 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 22 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 23 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 24 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 25 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 26 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 27 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 28 | `BOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 29 | `TECHNICALBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 30 | `PRODUCTIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 31 | `COSTCALCULATIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 32 | `GENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 33 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 34 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 35 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 36 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 37 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.PROGRESSIVE,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.BOMANALYSISCOMPONENTREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
