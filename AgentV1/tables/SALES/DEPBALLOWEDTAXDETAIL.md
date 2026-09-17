# DB2ADMIN.DEPBALLOWEDTAXDETAIL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `DEPBDEFAULTCOMPANYCODE`, `DEPBDEFAULTDIVISIONCODE`, `ITAXCODE`, `ITAXEFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 136961

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DEPBDEFAULTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DEPBDEFAULTDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITAXCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITAXEFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DEPBDEFAULT_DETAIL2` | `DEPBDEFAULTCOMPANYCODE`, `DEPBDEFAULTDIVISIONCODE` | [`DEPBDEFAULT`](../SALES/DEPBDEFAULT.md) | `COMPANYCODE`, `DIVISIONCODE` | RESTRICT | `DEPBALLOWEDTAXDETAIL.DEPBDEFAULTCOMPANYCODE = DEPBDEFAULT.COMPANYCODE AND DEPBALLOWEDTAXDETAIL.DEPBDEFAULTDIVISIONCODE = DEPBDEFAULT.DIVISIONCODE` |
| `ITAX_ITAX` | `DEPBDEFAULTCOMPANYCODE`, `ITAXCODE`, `ITAXEFFECTIVEFROMDATE` | [`ITAX`](../SALES/ITAX.md) | `COMPANYCODE`, `CODE`, `EFFECTIVEFROMDATE` | RESTRICT | `DEPBALLOWEDTAXDETAIL.DEPBDEFAULTCOMPANYCODE = ITAX.COMPANYCODE AND DEPBALLOWEDTAXDETAIL.ITAXCODE = ITAX.CODE AND DEPBALLOWEDTAXDETAIL.ITAXEFFECTIVEFROMDATE = ITAX.EFFECTIVEFROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DEPBALLOWEDTAXDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DEPBDEFAULTCOMPANYCODE,
       t.DEPBDEFAULTDIVISIONCODE,
       t.ITAXCODE,
       t.ITAXEFFECTIVEFROMDATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DEPBALLOWEDTAXDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
