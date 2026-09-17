# DB2ADMIN.QUALITYCHARACTERISTICDETAIL

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `QUALITYCHARCOMPANYCODE`, `QUALITYCHARACTERISTICTYPECODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111556

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `QUALITYCHARCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `QUALITYCHARACTERISTICTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUBCODENR` | INTEGER | NOT NULL |  |  |  |
| 5 | `ADSUBCODEMIN` | CHAR(50) |  |  |  |  |
| 6 | `ADSUBCODEMAX` | CHAR(50) |  |  |  |  |
| 7 | `ADSUBCODESTD` | CHAR(50) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYCHARACTERISTICDETAIL.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND QUALITYCHARACTERISTICDETAIL.ITEMTYPECODE = ITEMTYPE.CODE` |
| `QUALITYCHARACTERISTICTYPE_DETAIL` | `QUALITYCHARCOMPANYCODE`, `QUALITYCHARACTERISTICTYPECODE` | [`QUALITYCHARACTERISTICTYPE`](../QUALITY/QUALITYCHARACTERISTICTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYCHARACTERISTICDETAIL.QUALITYCHARCOMPANYCODE = QUALITYCHARACTERISTICTYPE.COMPANYCODE AND QUALITYCHARACTERISTICDETAIL.QUALITYCHARACTERISTICTYPECODE = QUALITYCHARACTERISTICTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUALITYCHARACTERISTICDLTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.QUALITYCHARCOMPANYCODE,
       t.QUALITYCHARACTERISTICTYPECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODENR,
       t.ADSUBCODEMIN,
       t.ADSUBCODEMAX,
       t.ADSUBCODESTD,
       t.ABSUNIQUEID
FROM   DB2ADMIN.QUALITYCHARACTERISTICDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
