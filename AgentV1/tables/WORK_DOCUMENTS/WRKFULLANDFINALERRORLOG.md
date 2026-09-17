# DB2ADMIN.WRKFULLANDFINALERRORLOG

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `COMPANYCODE`, `EMPLOYEECODE`, `SNO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169635

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 2 | `SNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ERRORAT` | CHAR(100) |  |  |  |  |
| 4 | `REMARKS` | VARCHAR(250) |  |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFULLANDFINALERRORLOGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EMPLOYEECODE,
       t.SNO,
       t.ERRORAT,
       t.REMARKS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WRKFULLANDFINALERRORLOG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
