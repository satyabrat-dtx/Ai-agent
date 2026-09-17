# DB2ADMIN.MARKERDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `MARKERCOMPANYCODE`, `MARKERPRODUCTIONORDERCODE`, `MARKERMARKERCODE`, `SLNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 127033

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MARKERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MARKERPRODUCTIONORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MARKERMARKERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `INSEAMSIZE` | CHAR(10) |  |  |  |  |
| 4 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 5 | `SIZERATIO` | INTEGER | NOT NULL |  |  |  |
| 6 | `SLNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `PDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `PDCODE` | CHAR(15) |  |  |  |  |
| 9 | `ITEMCODE` | CHAR(140) |  |  |  |  |
| 10 | `SIZEPOSITION` | INTEGER | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MARKER_LINE` | `MARKERCOMPANYCODE`, `MARKERPRODUCTIONORDERCODE`, `MARKERMARKERCODE` | [`MARKER`](../OTHER/MARKER.md) | `COMPANYCODE`, `PRODUCTIONORDERCODE`, `MARKERCODE` | RESTRICT | `MARKERDETAIL.MARKERCOMPANYCODE = MARKER.COMPANYCODE AND MARKERDETAIL.MARKERPRODUCTIONORDERCODE = MARKER.PRODUCTIONORDERCODE AND MARKERDETAIL.MARKERMARKERCODE = MARKER.MARKERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MARKERDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MARKERCOMPANYCODE,
       t.MARKERPRODUCTIONORDERCODE,
       t.MARKERMARKERCODE,
       t.INSEAMSIZE,
       t.SIZECODE,
       t.SIZERATIO,
       t.SLNO,
       t.PDCOUNTERCODE,
       t.PDCODE,
       t.ITEMCODE,
       t.SIZEPOSITION,
       t.CREATIONDATETIME
FROM   DB2ADMIN.MARKERDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
