# DB2ADMIN.WRKMILSTOCKORDER

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `SESSIONID`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 36039

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL |  | audit |  |
| 1 | `SESSIONID` | CHAR(65) | NOT NULL | PK | primary_key |  |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `DETAILTYPE` | CHAR(1) |  |  |  |  |
| 4 | `SELECTED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 7 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 8 | `CUSTOMERDESCRIPTION` | VARCHAR(40) |  |  |  |  |
| 9 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 10 | `COLLECTIONCODE` | CHAR(6) |  |  |  |  |
| 11 | `PRICELISTORDERTYPE` | CHAR(1) |  |  |  |  |
| 12 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 13 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 14 | `DELIVERYPOINTUNIQUEID` | BIGINT |  |  |  |  |
| 15 | `DELIVERYPOINTCODE` | CHAR(8) |  |  |  |  |
| 16 | `DESCRIPTION` | VARCHAR(100) |  |  | description |  |
| 17 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 19 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 30 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 31 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 32 | `CURRENTDATE` | DATE |  |  |  |  |
| 33 | `AVAILABILITYDATEIMMEDIATE` | DATE |  |  |  |  |
| 34 | `AVAILABLE` | DECIMAL(15,5) |  |  |  |  |
| 35 | `AVAILABILITYDATE01` | DATE |  |  |  |  |
| 36 | `AVAILABLE01` | DECIMAL(15,5) |  |  |  |  |
| 37 | `AVAILABILITYDATE02` | DATE |  |  |  |  |
| 38 | `AVAILABLE02` | DECIMAL(15,5) |  |  |  |  |
| 39 | `ORDERONBALANCE` | DECIMAL(15,5) |  |  |  |  |
| 40 | `ORDERONAVAIL01` | DECIMAL(15,5) |  |  |  |  |
| 41 | `ORDERONAVAIL02` | DECIMAL(15,5) |  |  |  |  |
| 42 | `DATETIME` | TIMESTAMP |  |  |  |  |
| 43 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKMILSTOCKORDERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.SESSIONID,
       t.LINE,
       t.DETAILTYPE,
       t.SELECTED,
       t.COMPANYCODE,
       t.CUSTOMERTYPE,
       t.CUSTOMERCODE,
       t.CUSTOMERDESCRIPTION,
       t.STATISTICALGROUPCODE,
       t.COLLECTIONCODE,
       t.PRICELISTORDERTYPE
FROM   DB2ADMIN.WRKMILSTOCKORDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
