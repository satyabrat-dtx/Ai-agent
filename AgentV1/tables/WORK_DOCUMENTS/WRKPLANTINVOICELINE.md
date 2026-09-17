# DB2ADMIN.WRKPLANTINVOICELINE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 58
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`, `PLANTINVOICECODE`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 145233

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `POLINEABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 3 | `PLANTINVOICECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `SUBCODE1` | CHAR(20) |  |  |  |  |
| 7 | `SUBCODE2` | CHAR(10) |  |  |  |  |
| 8 | `SUBCODE3` | CHAR(10) |  |  |  |  |
| 9 | `SUBCODE4` | CHAR(10) |  |  |  |  |
| 10 | `SUBCODE5` | CHAR(10) |  |  |  |  |
| 11 | `SUBCODE6` | CHAR(10) |  |  |  |  |
| 12 | `SUBCODE7` | CHAR(10) |  |  |  |  |
| 13 | `SUBCODE8` | CHAR(10) |  |  |  |  |
| 14 | `SUBCODE9` | CHAR(10) |  |  |  |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 18 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `SECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 20 | `BASEPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `BASEPRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 22 | `BASESECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 23 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `BASESECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 25 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 26 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 27 | `ITEMDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `QUANTITYSQMTS` | DECIMAL(15,5) |  |  |  |  |
| 29 | `BEDITAXCODE` | CHAR(3) |  |  |  |  |
| 30 | `BEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `BEDCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 32 | `ECITAXCODE` | CHAR(3) |  |  |  |  |
| 33 | `ECVALUE` | DECIMAL(18,5) |  |  |  |  |
| 34 | `ECCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 35 | `CSITAXCODE` | CHAR(3) |  |  |  |  |
| 36 | `CSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `CSCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 38 | `SSITAXCODE` | CHAR(3) |  |  |  |  |
| 39 | `SSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 40 | `SSCALCULATEDVALUERCC` | DECIMAL(18,5) |  |  |  |  |
| 41 | `TOTALDUTY` | DECIMAL(18,5) |  |  |  |  |
| 42 | `TARIFFCODE` | CHAR(20) |  |  |  |  |
| 43 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 44 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 45 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 46 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 47 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 48 | `COUNTSTDETAIL` | INTEGER | NOT NULL |  |  |  |
| 49 | `TAV` | DECIMAL(18,5) |  |  |  |  |
| 50 | `CALCULATEDVALUERCCFORSYS` | DECIMAL(18,5) |  |  |  |  |
| 51 | `CALCULATEDVALUERCCFOROTH` | DECIMAL(18,5) |  |  |  |  |
| 52 | `OTHVALUE` | DECIMAL(18,5) |  |  |  |  |
| 53 | `CHAPTERID` | CHAR(5) |  |  |  |  |
| 54 | `BEDDESC` | VARCHAR(200) |  |  |  |  |
| 55 | `CSDDESC` | VARCHAR(200) |  |  |  |  |
| 56 | `ECDESC` | VARCHAR(200) |  |  |  |  |
| 57 | `SSDDESC` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.POLINEABSUNIQUEID,
       t.PLANTINVOICECODE,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE1,
       t.SUBCODE2,
       t.SUBCODE3,
       t.SUBCODE4,
       t.SUBCODE5,
       t.SUBCODE6
FROM   DB2ADMIN.WRKPLANTINVOICELINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
