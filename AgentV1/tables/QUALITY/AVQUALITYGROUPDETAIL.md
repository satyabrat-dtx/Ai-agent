# DB2ADMIN.AVQUALITYGROUPDETAIL

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 1 of 1 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `AVQUALITYGROUPCOMPANYCODE`, `AVQUALITYGROUPCODE`, `QUALITYITEMTYPECODE`, `QUALITYCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 89778

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AVQUALITYGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `AVQUALITYGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `QUALITYITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `QUALITYCODE` | DECIMAL(2,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AVQUALITYGROUP_DETAIL` | `AVQUALITYGROUPCOMPANYCODE`, `AVQUALITYGROUPCODE` | [`AVQUALITYGROUP`](../QUALITY/AVQUALITYGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `AVQUALITYGROUPDETAIL.AVQUALITYGROUPCOMPANYCODE = AVQUALITYGROUP.COMPANYCODE AND AVQUALITYGROUPDETAIL.AVQUALITYGROUPCODE = AVQUALITYGROUP.CODE` |
| `QUALITYLEVEL_QUALITY` | `QUALITYITEMTYPECOMPANYCODE`, `QUALITYITEMTYPECODE`, `QUALITYCODE` | [`QUALITYLEVEL`](../QUALITY/QUALITYLEVEL.md) | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `AVQUALITYGROUPDETAIL.QUALITYITEMTYPECOMPANYCODE = QUALITYLEVEL.ITEMTYPECOMPANYCODE AND AVQUALITYGROUPDETAIL.QUALITYITEMTYPECODE = QUALITYLEVEL.ITEMTYPECODE AND AVQUALITYGROUPDETAIL.QUALITYCODE = QUALITYLEVEL.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `AVQUALITYGROUPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.AVQUALITYGROUPCOMPANYCODE,
       t.AVQUALITYGROUPCODE,
       t.QUALITYITEMTYPECOMPANYCODE,
       t.QUALITYITEMTYPECODE,
       t.QUALITYCODE,
       t.SEQUENCE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.AVQUALITYGROUPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
