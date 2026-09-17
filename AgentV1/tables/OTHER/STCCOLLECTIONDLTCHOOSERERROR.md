# DB2ADMIN.STCCOLLECTIONDLTCHOOSERERROR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `ERRORTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 5105

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ERRORTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 3 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COLLECTIONDLTCHOOSERERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ERRORTIMESTAMP,
       t.LINE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.STCCOLLECTIONDLTCHOOSERERROR t
FETCH FIRST 100 ROWS ONLY;
```
