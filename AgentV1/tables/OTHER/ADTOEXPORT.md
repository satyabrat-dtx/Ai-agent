# DB2ADMIN.ADTOEXPORT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `ENVIRONMENTCODE`, `ENTITYNAME`, `NAMENAME`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3646

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `NAMENAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADENTITY_ENTITY` | `ENTITYNAME` | [`ADENTITY`](../LOCALIZATION/ADENTITY.md) | `NAME` | RESTRICT | `ADTOEXPORT.ENTITYNAME = ADENTITY.NAME` |
| `EXPORTENVIRONMENT_ENVIRONMENT` | `ENVIRONMENTCODE` | [`EXPORTENVIRONMENT`](../PDM/EXPORTENVIRONMENT.md) | `CODE` | RESTRICT | `ADTOEXPORT.ENVIRONMENTCODE = EXPORTENVIRONMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ADTOEXPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.ENTITYNAME,
       t.NAMENAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ADTOEXPORT t
FETCH FIRST 100 ROWS ONLY;
```
