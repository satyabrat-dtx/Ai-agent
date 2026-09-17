# DB2ADMIN.ABSINDEXCUSTOMIZEDOPTIONS

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 189832

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `NOTE` | VARCHAR(500) |  |  |  |  |
| 2 | `DONOTCREATE` | SMALLINT | NOT NULL |  |  |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 7 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 8 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSINDEXCUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.NOTE,
       t.DONOTCREATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSINDEXCUSTOMIZEDOPTIONS t
FETCH FIRST 100 ROWS ONLY;
```
