# DB2ADMIN.WRKSTCCOLLECTIONDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 25110

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TYPE` | CHAR(1) |  |  |  |  |
| 4 | `STATUS` | CHAR(1) |  |  |  |  |
| 5 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 6 | `COLLECTIONCODE` | CHAR(6) |  |  |  |  |
| 7 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 9 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.COMPANYCODE,
       t.TYPE,
       t.STATUS,
       t.STATISTICALGROUPCODE,
       t.COLLECTIONCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03
FROM   DB2ADMIN.WRKSTCCOLLECTIONDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
