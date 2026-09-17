# DB2ADMIN.USAACCOUNTINGJOURNALEXP

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPTRANSACTIONNUMBER`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107521

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPTRANSACTIONNUMBER` | CHAR(16) | NOT NULL | PK | primary_key |  |
| 3 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 5 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USAACCOUNTINGJOURNALEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPTRANSACTIONNUMBER,
       t.OPERATIONTYPE,
       t.STATUS,
       t.UNIQUEIDPK,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USAACCOUNTINGJOURNALEXP t
FETCH FIRST 100 ROWS ONLY;
```
