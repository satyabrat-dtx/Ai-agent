# DB2ADMIN.WRKCOSTANALYSISSELECTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 41
- **Primary key**: `UNIQUEID`, `SEQUENCE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 17381

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 2 | `PRODUCTINDEX` | DECIMAL(11,0) |  |  |  |  |
| 3 | `GROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 4 | `EXPLOSIONLEVEL` | INTEGER | NOT NULL |  |  |  |
| 5 | `CONSINDEX` | BIGINT | NOT NULL |  |  |  |
| 6 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 7 | `SELECTED` | CHAR(1) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 10 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 11 | `COSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 12 | `COSTSCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 13 | `ROUTEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 14 | `BOMDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 15 | `COST` | DECIMAL(18,5) |  |  |  |  |
| 16 | `ROUTEITEMCODE` | VARCHAR(120) |  |  |  |  |
| 17 | `ROUTEINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 18 | `BOMITEMCODE` | VARCHAR(120) |  |  |  |  |
| 19 | `BOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 20 | `ROUTENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 21 | `BOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 22 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `EXPLODE` | SMALLINT | NOT NULL |  |  |  |
| 33 | `QUANTITY` | DECIMAL(20,10) |  |  |  |  |
| 34 | `SELLINGPRICE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `UOMCODE` | CHAR(3) |  |  |  |  |
| 36 | `ISPRODUCTLEVEL` | SMALLINT | NOT NULL |  |  |  |
| 37 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 38 | `PLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `SUBUNIQUEID` | INTEGER | NOT NULL |  |  |  |
| 40 | `FATHERSEQUENCE` | DECIMAL(5,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.UNIQUEID,
       t.SEQUENCE,
       t.PRODUCTINDEX,
       t.GROUPNUMBER,
       t.EXPLOSIONLEVEL,
       t.CONSINDEX,
       t.COMPANYCODE,
       t.SELECTED,
       t.ITEMTYPECODE,
       t.ITEMCODE,
       t.PLANTCODE,
       t.COSTGROUPCODE
FROM   DB2ADMIN.WRKCOSTANALYSISSELECTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
