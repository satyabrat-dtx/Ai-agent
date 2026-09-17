# DB2ADMIN.ADDRESSGST

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'ADDRESS')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121131

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `GSTINNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `GSTDATE` | DATE |  |  |  |  |
| 3 | `STATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `PROVISIONALGSTINNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 5 | `PROVISIONALGSTDATE` | DATE |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `STATE_STATE` | `STATECODE` | [`STATE`](../HR/STATE.md) | `CODE` | RESTRICT | `ADDRESSGST.STATECODE = STATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADDRESSGSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.GSTINNUMBER,
       t.GSTDATE,
       t.STATECODE,
       t.PROVISIONALGSTINNUMBER,
       t.PROVISIONALGSTDATE,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.ADDRESSGST t
FETCH FIRST 100 ROWS ONLY;
```
