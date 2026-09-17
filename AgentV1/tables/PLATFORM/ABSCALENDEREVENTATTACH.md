# DB2ADMIN.ABSCALENDEREVENTATTACH

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `ABSCALENDAREVENTINVUUID`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117723

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSCALENDAREVENTINVUUID` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `IDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `NAME` | VARCHAR(60) |  |  |  |  |
| 3 | `USERDESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 4 | `CONTENTTYPE` | CHAR(150) |  |  |  |  |
| 5 | `DATA` | BLOB(25000000) | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSCALENDAREVENT_ATTACHMENTS` | `ABSCALENDAREVENTINVUUID` | [`ABSCALENDAREVENT`](../PLATFORM/ABSCALENDAREVENT.md) | `INVUUID` | RESTRICT | `ABSCALENDEREVENTATTACH.ABSCALENDAREVENTINVUUID = ABSCALENDAREVENT.INVUUID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSCALENDEREVENTATTACHUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSCALENDAREVENTINVUUID,
       t.IDENTIFIER,
       t.NAME,
       t.USERDESCRIPTION,
       t.CONTENTTYPE,
       t.DATA,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSCALENDEREVENTATTACH t
FETCH FIRST 100 ROWS ONLY;
```
