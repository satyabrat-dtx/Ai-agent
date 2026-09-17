# DB2ADMIN.SKETCHTEMPLATEDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `SKETCHTEMPLATECOMPANYCODE`, `SKETCHTEMPLATECODE`, `SKETCHTYPEDETAILCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 215092

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SKETCHTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SKETCHTEMPLATECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SKETCHTYPEDETAILCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SKETCHTEMPLATE_DETAIL` | `SKETCHTEMPLATECOMPANYCODE`, `SKETCHTEMPLATECODE` | [`SKETCHTEMPLATE`](../OTHER/SKETCHTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SKETCHTEMPLATEDETAIL.SKETCHTEMPLATECOMPANYCODE = SKETCHTEMPLATE.COMPANYCODE AND SKETCHTEMPLATEDETAIL.SKETCHTEMPLATECODE = SKETCHTEMPLATE.CODE` |
| `SKETCHTYPEDETAIL_SKETCHTYPEDETAIL` | `SKETCHTEMPLATECOMPANYCODE`, `SKETCHTYPEDETAILCODE` | [`SKETCHTYPEDETAIL`](../OTHER/SKETCHTYPEDETAIL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SKETCHTEMPLATEDETAIL.SKETCHTEMPLATECOMPANYCODE = SKETCHTYPEDETAIL.COMPANYCODE AND SKETCHTEMPLATEDETAIL.SKETCHTYPEDETAILCODE = SKETCHTYPEDETAIL.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SKETCHTEMPLATEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SKETCHTEMPLATECOMPANYCODE,
       t.SKETCHTEMPLATECODE,
       t.SKETCHTYPEDETAILCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SKETCHTEMPLATEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
