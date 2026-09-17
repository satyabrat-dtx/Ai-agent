# DB2ADMIN.ABSGB

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `ABSUIXMLPATH`, `ABSUIXMLNAME`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29005

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `DESCRIPTION` | VARCHAR(250) | NOT NULL |  | description |  |
| 4 | `DATA` | CLOB(1000000) |  |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSGB_AUTHORIZATIONS` | [`ABSGBAUTH`](../PLATFORM/ABSGBAUTH.md) | `ABSGBABSUIXMLPATH`, `ABSGBABSUIXMLNAME`, `ABSGBCODE` | `ABSGBAUTH.ABSGBABSUIXMLPATH = ABSGB.ABSUIXMLPATH AND ABSGBAUTH.ABSGBABSUIXMLNAME = ABSGB.ABSUIXMLNAME AND ABSGBAUTH.ABSGBCODE = ABSGB.CODE` |
| `ABSGB_GB` | [`ABSUIPROCESS`](../PLATFORM/ABSUIPROCESS.md) | `UIXMLPATH`, `UIXMLNAME`, `GBCODE` | `ABSUIPROCESS.UIXMLPATH = ABSGB.ABSUIXMLPATH AND ABSUIPROCESS.UIXMLNAME = ABSGB.ABSUIXMLNAME AND ABSUIPROCESS.GBCODE = ABSGB.CODE` |
| `ABSGB_DEFAULTGB` | [`ABSUIXMLAUTH`](../PLATFORM/ABSUIXMLAUTH.md) | `ABSUIXMLPATH`, `ABSUIXMLNAME`, `DEFAULTGBCODE` | `ABSUIXMLAUTH.ABSUIXMLPATH = ABSGB.ABSUIXMLPATH AND ABSUIXMLAUTH.ABSUIXMLNAME = ABSGB.ABSUIXMLNAME AND ABSUIXMLAUTH.DEFAULTGBCODE = ABSGB.CODE` |

## Indexes

- `ABSGBUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLPATH,
       t.ABSUIXMLNAME,
       t.CODE,
       t.DESCRIPTION,
       t.DATA,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.ABSGB t
FETCH FIRST 100 ROWS ONLY;
```
