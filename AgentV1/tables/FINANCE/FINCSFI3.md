# DB2ADMIN.FINCSFI3

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `RCFTID2RCFCONFID`, `RCFTLNG`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103704

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RCFTID2RCFCONFID` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `RCFTLNG` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `RCFTLAB` | VARCHAR(100) |  |  |  |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCSFI3UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RCFTID2RCFCONFID,
       t.RCFTLNG,
       t.RCFTLAB,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINCSFI3 t
FETCH FIRST 100 ROWS ONLY;
```
