# DB2ADMIN.WRKEMPLEAVECHECK

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `ATTENDANCEDATE`, `EMPCODE`, `DAYSESSION`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170619

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ATTENDANCEDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `EMPCODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 4 | `DAYSESSION` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKEMPLEAVECHECKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.ATTENDANCEDATE,
       t.EMPCODE,
       t.DAYSESSION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WRKEMPLEAVECHECK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
