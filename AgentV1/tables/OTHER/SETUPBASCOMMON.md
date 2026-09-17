# DB2ADMIN.SETUPBASCOMMON

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 1513

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ID` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 1 | `ACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `CUSTOMIZEDOPTIONS` | SMALLINT | NOT NULL |  |  |  |
| 3 | `COUNTERTYPE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `PERIODIZEDCALENDARTYPE` | SMALLINT | NOT NULL |  |  |  |
| 5 | `FINANCIALACCOUNTINGTYPE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `EXTENDEDFUNCTION` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SETUPBASCOMMONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ID,
       t.ACTIVE,
       t.CUSTOMIZEDOPTIONS,
       t.COUNTERTYPE,
       t.PERIODIZEDCALENDARTYPE,
       t.FINANCIALACCOUNTINGTYPE,
       t.EXTENDEDFUNCTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SETUPBASCOMMON t
FETCH FIRST 100 ROWS ONLY;
```
