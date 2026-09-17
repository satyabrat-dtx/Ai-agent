# DB2ADMIN.WRKGARMENTBILLOFMATERIAL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 128212

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(20) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(20) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(20) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(20) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(20) |  |  | generic_classification_code |  |
| 15 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKGARMENTBILLOFMATERIALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.NUMBERID,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.WRKGARMENTBILLOFMATERIAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
