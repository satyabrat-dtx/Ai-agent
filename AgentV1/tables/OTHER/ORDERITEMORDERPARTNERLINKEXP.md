# DB2ADMIN.ORDERITEMORDERPARTNERLINKEXP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `ENVIRONMENTCODE`, `EXPCOMPANYCODE`, `EXPORDERTYPE`, `EXPORDPRNCUSTOMERSUPPLIERCODE`, `EXPITEMTYPEAFICODE`, `EXPSUBCODE01`, `EXPSUBCODE02`, `EXPSUBCODE03`, `EXPSUBCODE04`, `EXPSUBCODE05`, `EXPSUBCODE06`, `EXPSUBCODE07`, `EXPSUBCODE08`, `EXPSUBCODE09`, `EXPSUBCODE10`, `EXPEXTERNALITEMCODE`, `UNIQUEIDPK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111228

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 1 | `EXPCOMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `EXPORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `EXPORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `EXPITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `EXPSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `EXPSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `EXPSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `EXPSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `EXPSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `EXPSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `EXPSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `EXPSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `EXPSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `EXPSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `EXPEXTERNALITEMCODE` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 16 | `OPERATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 17 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 18 | `UNIQUEIDPK` | BIGINT | NOT NULL | PK | primary_key |  |
| 19 | `FATHERABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 20 | `EVENTEXPDATETIME` | TIMESTAMP |  |  |  |  |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDITEMORDPARTNERLINKEXPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.EXPCOMPANYCODE,
       t.EXPORDERTYPE,
       t.EXPORDPRNCUSTOMERSUPPLIERCODE,
       t.EXPITEMTYPEAFICODE,
       t.EXPSUBCODE01,
       t.EXPSUBCODE02,
       t.EXPSUBCODE03,
       t.EXPSUBCODE04,
       t.EXPSUBCODE05,
       t.EXPSUBCODE06,
       t.EXPSUBCODE07
FROM   DB2ADMIN.ORDERITEMORDERPARTNERLINKEXP t
FETCH FIRST 100 ROWS ONLY;
```
