# DB2ADMIN.CARTONTRANSACTIONDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `CARTONCOMPANYCODE`, `CARTONPREFIX`, `CARTONSTARTINGNUM`, `TRANSACTIONNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126722

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CARTONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CARTONPREFIX` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CARTONSTARTINGNUM` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `TRANSACTIONMODE` | CHAR(1) |  |  |  |  |
| 5 | `CARTONCODE` | CHAR(15) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CARTON_LINE1` | `CARTONCOMPANYCODE`, `CARTONPREFIX`, `CARTONSTARTINGNUM` | [`CARTON`](../CORE_MASTER/CARTON.md) | `COMPANYCODE`, `PREFIX`, `STARTINGNUM` | RESTRICT | `CARTONTRANSACTIONDETAIL.CARTONCOMPANYCODE = CARTON.COMPANYCODE AND CARTONTRANSACTIONDETAIL.CARTONPREFIX = CARTON.PREFIX AND CARTONTRANSACTIONDETAIL.CARTONSTARTINGNUM = CARTON.STARTINGNUM` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CARTONTRANSACTIONDETAILUID` (ABSUNIQUEID)
- `IDX_CRTTRANDTL` (CARTONCOMPANYCODE, CARTONCODE, TRANSACTIONMODE)

## Starter query

```sql
SELECT t.CARTONCOMPANYCODE,
       t.CARTONPREFIX,
       t.CARTONSTARTINGNUM,
       t.TRANSACTIONNUMBER,
       t.TRANSACTIONMODE,
       t.CARTONCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.CARTONTRANSACTIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
