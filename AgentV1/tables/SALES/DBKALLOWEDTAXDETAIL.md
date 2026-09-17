# DB2ADMIN.DBKALLOWEDTAXDETAIL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `DBKDEFAULTCOMPANYCODE`, `DBKDEFAULTDIVISIONCODE`, `ITAXCODE`, `ITAXEFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 136688

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DBKDEFAULTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DBKDEFAULTDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITAXCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITAXEFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DBKDEFAULT_DETAIL2` | `DBKDEFAULTCOMPANYCODE`, `DBKDEFAULTDIVISIONCODE` | [`DBKDEFAULT`](../SALES/DBKDEFAULT.md) | `COMPANYCODE`, `DIVISIONCODE` | RESTRICT | `DBKALLOWEDTAXDETAIL.DBKDEFAULTCOMPANYCODE = DBKDEFAULT.COMPANYCODE AND DBKALLOWEDTAXDETAIL.DBKDEFAULTDIVISIONCODE = DBKDEFAULT.DIVISIONCODE` |
| `ITAX_ITAX` | `DBKDEFAULTCOMPANYCODE`, `ITAXCODE`, `ITAXEFFECTIVEFROMDATE` | [`ITAX`](../SALES/ITAX.md) | `COMPANYCODE`, `CODE`, `EFFECTIVEFROMDATE` | RESTRICT | `DBKALLOWEDTAXDETAIL.DBKDEFAULTCOMPANYCODE = ITAX.COMPANYCODE AND DBKALLOWEDTAXDETAIL.ITAXCODE = ITAX.CODE AND DBKALLOWEDTAXDETAIL.ITAXEFFECTIVEFROMDATE = ITAX.EFFECTIVEFROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DBKALLOWEDTAXDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DBKDEFAULTCOMPANYCODE,
       t.DBKDEFAULTDIVISIONCODE,
       t.ITAXCODE,
       t.ITAXEFFECTIVEFROMDATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.DBKALLOWEDTAXDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
