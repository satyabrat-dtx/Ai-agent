# DB2ADMIN.WRKGARMENTCARTONDETAIL

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `CREATIONTIMESTAMP`, `CARTONITEMTYPECODE`, `CARTONSUBCODE01`, `CARTONCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197202

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `CARTONCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 4 | `CARTONHEADERNUMBERID` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 5 | `CARTONITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `CARTONSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 7 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKGARMENTCARTONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CHOOSE,
       t.CARTONCODE,
       t.ABSUNIQUEID,
       t.CARTONHEADERNUMBERID,
       t.CARTONITEMTYPECODE,
       t.CARTONSUBCODE01,
       t.LOGICALWAREHOUSECODE
FROM   DB2ADMIN.WRKGARMENTCARTONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
