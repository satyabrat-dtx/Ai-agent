# DB2ADMIN.DYNAMICFIELDSCONFIGDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `DYNAMICFIELDSCONFIGCOMPANYCODE`, `DYNAMICFIELDSCONFIGCODE`, `ADENTITYNAME`, `ADNAME`, `UIXMLATTRABSUIXMLPATH`, `UIXMLATTRABSUIXMLNAME`, `UIXMLATTRNAME`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 94764

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DYNAMICFIELDSCONFIGCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DYNAMICFIELDSCONFIGCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ADENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `ADNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `UIXMLATTRABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 5 | `UIXMLATTRABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 6 | `UIXMLATTRNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DYNAMICFIELDSCONFIG_DETAIL` | `DYNAMICFIELDSCONFIGCOMPANYCODE`, `DYNAMICFIELDSCONFIGCODE` | [`DYNAMICFIELDSCONFIG`](../OTHER/DYNAMICFIELDSCONFIG.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DYNAMICFIELDSCONFIGDETAIL.DYNAMICFIELDSCONFIGCOMPANYCODE = DYNAMICFIELDSCONFIG.COMPANYCODE AND DYNAMICFIELDSCONFIGDETAIL.DYNAMICFIELDSCONFIGCODE = DYNAMICFIELDSCONFIG.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DYNAMICFIELDSCONFIGDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DYNAMICFIELDSCONFIGCOMPANYCODE,
       t.DYNAMICFIELDSCONFIGCODE,
       t.ADENTITYNAME,
       t.ADNAME,
       t.UIXMLATTRABSUIXMLPATH,
       t.UIXMLATTRABSUIXMLNAME,
       t.UIXMLATTRNAME,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DYNAMICFIELDSCONFIGDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
