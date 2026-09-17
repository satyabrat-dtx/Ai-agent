# DB2ADMIN.SHIFTROTATIONDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 2 of 2 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `SHIFTROTATIONCOMPANYCODE`, `SHIFTROTATIONCODE`, `SHIFTCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 156209

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SHIFTROTATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SHIFTROTATIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 3 | `SHIFTCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SHIFTROTATION_LINE` | `SHIFTROTATIONCOMPANYCODE`, `SHIFTROTATIONCODE` | [`SHIFTROTATION`](../HR/SHIFTROTATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SHIFTROTATIONDETAIL.SHIFTROTATIONCOMPANYCODE = SHIFTROTATION.COMPANYCODE AND SHIFTROTATIONDETAIL.SHIFTROTATIONCODE = SHIFTROTATION.CODE` |
| `SHIFT_SHIFT` | `SHIFTROTATIONCOMPANYCODE`, `SHIFTCODE` | [`SHIFT`](../HR/SHIFT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SHIFTROTATIONDETAIL.SHIFTROTATIONCOMPANYCODE = SHIFT.COMPANYCODE AND SHIFTROTATIONDETAIL.SHIFTCODE = SHIFT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SHIFTROTATIONDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SHIFTROTATIONCOMPANYCODE,
       t.SHIFTROTATIONCODE,
       t.LINENO,
       t.SHIFTCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SHIFTROTATIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
