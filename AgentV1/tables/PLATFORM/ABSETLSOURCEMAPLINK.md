# DB2ADMIN.ABSETLSOURCEMAPLINK

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `ABSETLSOURCESOURCEID`, `ABSETLSOURCEMAPPINGTARGETFIELD`, `FATHERFIELD`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93726

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSETLSOURCESOURCEID` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ABSETLSOURCEMAPPINGTARGETFIELD` | CHAR(65) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FATHERFIELD` | CHAR(65) | NOT NULL | PK | primary_key |  |
| 3 | `CHILDFIELD` | CHAR(65) |  |  |  |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSETLSOURCEMAPPING_LINKS` | `ABSETLSOURCESOURCEID`, `ABSETLSOURCEMAPPINGTARGETFIELD` | [`ABSETLSOURCEMAPPING`](../PLATFORM/ABSETLSOURCEMAPPING.md) | `ABSETLSOURCESOURCEID`, `TARGETFIELD` | RESTRICT | `ABSETLSOURCEMAPLINK.ABSETLSOURCESOURCEID = ABSETLSOURCEMAPPING.ABSETLSOURCESOURCEID AND ABSETLSOURCEMAPLINK.ABSETLSOURCEMAPPINGTARGETFIELD = ABSETLSOURCEMAPPING.TARGETFIELD` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSETLSOURCEMAPLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSETLSOURCESOURCEID,
       t.ABSETLSOURCEMAPPINGTARGETFIELD,
       t.FATHERFIELD,
       t.CHILDFIELD,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSETLSOURCEMAPLINK t
FETCH FIRST 100 ROWS ONLY;
```
