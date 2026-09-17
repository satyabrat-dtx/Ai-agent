# DB2ADMIN.WRKPMVALIDATEPR

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`, `LINENO`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89588

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `WORKORDERCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 4 | `WORKORDERCODE` | CHAR(15) |  |  |  |  |
| 5 | `PRCOUNTERCODE` | CHAR(15) |  |  |  |  |
| 6 | `PRNO` | CHAR(15) |  |  |  |  |
| 7 | `QTYRAISED` | DECIMAL(15,5) |  |  |  |  |
| 8 | `RECEIPT` | CHAR(1) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPMVALIDATEPRUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.WORKORDERCOUNTERCODE,
       t.WORKORDERCODE,
       t.PRCOUNTERCODE,
       t.PRNO,
       t.QTYRAISED,
       t.RECEIPT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WRKPMVALIDATEPR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
