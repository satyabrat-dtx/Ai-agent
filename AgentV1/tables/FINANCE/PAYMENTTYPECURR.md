# DB2ADMIN.PAYMENTTYPECURR

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 1 of 1 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 3
- **Primary key**: `PAYMENTTYPECODE`, `CURRCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93943

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PAYMENTTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CURRCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURR` | `CURRCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `PAYMENTTYPECURR.CURRCODE = CURRENCY.CODE` |
| `PAYMENTTYPE_CURRENCIES` | `PAYMENTTYPECODE` | [`PAYMENTTYPE`](../FINANCE/PAYMENTTYPE.md) | `CODE` | RESTRICT | `PAYMENTTYPECURR.PAYMENTTYPECODE = PAYMENTTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PAYMENTTYPECURRUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PAYMENTTYPECODE,
       t.CURRCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PAYMENTTYPECURR t
FETCH FIRST 100 ROWS ONLY;
```
