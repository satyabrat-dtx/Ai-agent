# DB2ADMIN.INTERCOMPANYTRANSACTIONLINK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `SALTRANSACTIONCOMPANYCODE`, `SALTRNTRANSACTIONNUMBER`, `SALTRNTRANSACTIONDETAILNUMBER`, `PURTRANSACTIONCOMPANYCODE`, `PURTRNTRANSACTIONNUMBER`, `PURTRNTRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 29767

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALTRANSACTIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `SALTRNTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `SALTRNTRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `PURTRANSACTIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `PURTRNTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `PURTRNTRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INTERCOMPANYTRNLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALTRANSACTIONCOMPANYCODE,
       t.SALTRNTRANSACTIONNUMBER,
       t.SALTRNTRANSACTIONDETAILNUMBER,
       t.PURTRANSACTIONCOMPANYCODE,
       t.PURTRNTRANSACTIONNUMBER,
       t.PURTRNTRANSACTIONDETAILNUMBER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.INTERCOMPANYTRANSACTIONLINK t
FETCH FIRST 100 ROWS ONLY;
```
