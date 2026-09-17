# DB2ADMIN.BANKVSAD

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `BBBANKCOUNTRYCODE`, `BBCODE`, `BBBRANCHCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181880

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BBBANKCOUNTRYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `BBCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `BBBRANCHCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 3 | `ADCODE` | CHAR(15) |  |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BANKVSADUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BBBANKCOUNTRYCODE,
       t.BBCODE,
       t.BBBRANCHCODE,
       t.ADCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BANKVSAD t
FETCH FIRST 100 ROWS ONLY;
```
