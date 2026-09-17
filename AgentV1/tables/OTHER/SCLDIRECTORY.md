# DB2ADMIN.SCLDIRECTORY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `BIC`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 104496

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COUNTRYISOCODE` | CHAR(2) |  |  |  |  |
| 1 | `BIC` | CHAR(11) | NOT NULL | PK | primary_key |  |
| 2 | `DESCRIPTION` | CHAR(100) |  |  | description |  |
| 3 | `SCT` | SMALLINT | NOT NULL |  |  |  |
| 4 | `SDD` | SMALLINT | NOT NULL |  |  |  |
| 5 | `COR1` | SMALLINT | NOT NULL |  |  |  |
| 6 | `B2B` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SCC` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SCLDIRECTORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COUNTRYISOCODE,
       t.BIC,
       t.DESCRIPTION,
       t.SCT,
       t.SDD,
       t.COR1,
       t.B2B,
       t.SCC,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.SCLDIRECTORY t
FETCH FIRST 100 ROWS ONLY;
```
