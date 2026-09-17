# DB2ADMIN.LOTEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPITEMTYPECODE`, `EXPDECOSUBCODE01`, `EXPDECOSUBCODE02`, `EXPDECOSUBCODE03`, `EXPDECOSUBCODE04`, `EXPDECOSUBCODE05`, `EXPDECOSUBCODE06`, `EXPDECOSUBCODE07`, `EXPDECOSUBCODE08`, `EXPDECOSUBCODE09`, `EXPDECOSUBCODE10`, `EXPCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 76817

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `EXPDECOSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `EXPDECOSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `EXPDECOSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `EXPDECOSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `EXPDECOSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `EXPDECOSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `EXPDECOSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `EXPDECOSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `EXPDECOSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `EXPDECOSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `EXPCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 14 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 15 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 16 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 19 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOTEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPITEMTYPECODE,
       t.EXPDECOSUBCODE01,
       t.EXPDECOSUBCODE02,
       t.EXPDECOSUBCODE03,
       t.EXPDECOSUBCODE04,
       t.EXPDECOSUBCODE05,
       t.EXPDECOSUBCODE06,
       t.EXPDECOSUBCODE07,
       t.EXPDECOSUBCODE08,
       t.EXPDECOSUBCODE09
FROM   DB2ADMIN.LOTEXP t
FETCH FIRST 100 ROWS ONLY;
```
