# DB2ADMIN.STOCKTAKEUSETEMPLATELINE

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 6
- **Primary key**: `STOCKTAKEUSETMPCOMPANYCODE`, `STOCKTAKEUSETEMPLATECODE`, `TEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 12786

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `STOCKTAKEUSETMPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `STOCKTAKEUSETEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 4 | `TEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `STOCKTAKEUSETEMPLATE_TEMPLATE` | `STOCKTAKEUSETMPCOMPANYCODE`, `STOCKTAKEUSETEMPLATECODE` | [`STOCKTAKEUSETEMPLATE`](../INVENTORY/STOCKTAKEUSETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STOCKTAKEUSETEMPLATELINE.STOCKTAKEUSETMPCOMPANYCODE = STOCKTAKEUSETEMPLATE.COMPANYCODE AND STOCKTAKEUSETEMPLATELINE.STOCKTAKEUSETEMPLATECODE = STOCKTAKEUSETEMPLATE.CODE` |
| `STOCKTRANSACTIONTEMPLATE_TEMPLATE` | `TEMPLATECOMPANYCODE`, `TEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STOCKTAKEUSETEMPLATELINE.TEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND STOCKTAKEUSETEMPLATELINE.TEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTAKEUSETEMPLATELINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.STOCKTAKEUSETMPCOMPANYCODE,
       t.STOCKTAKEUSETEMPLATECODE,
       t.TEMPLATECODE,
       t.SEQUENCE,
       t.TEMPLATECOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.STOCKTAKEUSETEMPLATELINE t
FETCH FIRST 100 ROWS ONLY;
```
