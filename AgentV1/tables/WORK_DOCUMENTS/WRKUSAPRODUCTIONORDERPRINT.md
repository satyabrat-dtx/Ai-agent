# DB2ADMIN.WRKUSAPRODUCTIONORDERPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 50
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108121

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 7 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 8 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 9 | `SKEYRECIPEGROUPNUMBER` | CHAR(100) |  |  |  |  |
| 10 | `SKEYSEQUENCE` | CHAR(100) |  |  |  |  |
| 11 | `SKEYALTERNATIVE` | VARCHAR(500) |  |  |  |  |
| 12 | `SKEYSUBSEQUENCE` | CHAR(100) |  |  |  |  |
| 13 | `RESERVATIONLINE` | DECIMAL(5,0) |  |  |  |  |
| 14 | `SKEYRECIPENUMBERID` | CHAR(100) |  |  |  |  |
| 15 | `GROUPLINE` | INTEGER | NOT NULL |  |  |  |
| 16 | `RCPGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 17 | `RCPSEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 18 | `RCPALTERNATIVE` | CHAR(3) |  |  |  |  |
| 19 | `RCPSUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 20 | `WAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 21 | `LASTRECIPENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 22 | `LASTRECIPEGROUPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 23 | `LASTRECIPESEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 24 | `LASTRECIPEALTERNATIVE` | CHAR(3) |  |  |  |  |
| 25 | `LASTRECIPESUBSEQUENCE` | DECIMAL(3,0) |  |  |  |  |
| 26 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 27 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 28 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 38 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 39 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 40 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 41 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 42 | `RCPRECIPENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 43 | `SRCRECIPENUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 44 | `GROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 45 | `COMMENTLINE` | CHAR(50) |  |  |  |  |
| 46 | `COMPONENTUOMCODE` | CHAR(3) |  |  |  |  |
| 47 | `CONSUMPTION` | DECIMAL(15,5) |  |  |  |  |
| 48 | `LONGDESCRIPTION` | VARCHAR(100) |  |  | description | Long human-readable label. |
| 49 | `ORIGINALCREATIONTIMESTAMP` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANYCODE,
       t.PRODUCTIONORDERCODE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.STEPNUMBER,
       t.GROUPSTEPNUMBER,
       t.SKEYRECIPEGROUPNUMBER,
       t.SKEYSEQUENCE,
       t.SKEYALTERNATIVE
FROM   DB2ADMIN.WRKUSAPRODUCTIONORDERPRINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
