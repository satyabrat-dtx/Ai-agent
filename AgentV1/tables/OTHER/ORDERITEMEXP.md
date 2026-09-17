# DB2ADMIN.ORDERITEMEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPORDERTYPE`, `EXPITEMTYPECODE`, `EXPSUBCODE01`, `EXPSUBCODE02`, `EXPSUBCODE03`, `EXPSUBCODE04`, `EXPSUBCODE05`, `EXPSUBCODE06`, `EXPSUBCODE07`, `EXPSUBCODE08`, `EXPSUBCODE09`, `EXPSUBCODE10`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111165

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `EXPITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `EXPSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 5 | `EXPSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `EXPSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `EXPSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `EXPSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `EXPSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `EXPSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `EXPSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `EXPSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `EXPSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 15 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 16 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 17 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 18 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDERITEMEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPORDERTYPE,
       t.EXPITEMTYPECODE,
       t.EXPSUBCODE01,
       t.EXPSUBCODE02,
       t.EXPSUBCODE03,
       t.EXPSUBCODE04,
       t.EXPSUBCODE05,
       t.EXPSUBCODE06,
       t.EXPSUBCODE07,
       t.EXPSUBCODE08
FROM   DB2ADMIN.ORDERITEMEXP t
FETCH FIRST 100 ROWS ONLY;
```
