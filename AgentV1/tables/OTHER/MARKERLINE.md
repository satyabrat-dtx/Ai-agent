# DB2ADMIN.MARKERLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `MARKERHEADERCOMPANYCODE`, `MARKERHDRPRODUCTIONORDERCODE`, `MARKERHDRRESERVATIONGROUPLINE`, `MARKERHEADERCODE`, `SIZESIZESTYPECOMPANYCODE`, `SIZESIZESTYPECODE`, `SIZECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105709

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MARKERHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MARKERHDRPRODUCTIONORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MARKERHDRRESERVATIONGROUPLINE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `MARKERHEADERCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SIZESIZESTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SIZESIZESTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SIZECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MARKERHEADER_LINES` | `MARKERHEADERCOMPANYCODE`, `MARKERHDRPRODUCTIONORDERCODE`, `MARKERHDRRESERVATIONGROUPLINE`, `MARKERHEADERCODE` | [`MARKERHEADER`](../PRODUCTION/MARKERHEADER.md) | `COMPANYCODE`, `PRODUCTIONORDERCODE`, `RESERVATIONGROUPLINE`, `CODE` | RESTRICT | `MARKERLINE.MARKERHEADERCOMPANYCODE = MARKERHEADER.COMPANYCODE AND MARKERLINE.MARKERHDRPRODUCTIONORDERCODE = MARKERHEADER.PRODUCTIONORDERCODE AND MARKERLINE.MARKERHDRRESERVATIONGROUPLINE = MARKERHEADER.RESERVATIONGROUPLINE AND MARKERLINE.MARKERHEADERCODE = MARKERHEADER.CODE` |
| `SIZES_SIZE` | `SIZESIZESTYPECOMPANYCODE`, `SIZESIZESTYPECODE`, `SIZECODE` | [`SIZES`](../PDM/SIZES.md) | `SIZESTYPECOMPANYCODE`, `SIZESTYPECODE`, `CODE` | RESTRICT | `MARKERLINE.SIZESIZESTYPECOMPANYCODE = SIZES.SIZESTYPECOMPANYCODE AND MARKERLINE.SIZESIZESTYPECODE = SIZES.SIZESTYPECODE AND MARKERLINE.SIZECODE = SIZES.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `MARKERLINE.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MARKERLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MARKERHEADERCOMPANYCODE,
       t.MARKERHDRPRODUCTIONORDERCODE,
       t.MARKERHDRRESERVATIONGROUPLINE,
       t.MARKERHEADERCODE,
       t.SIZESIZESTYPECOMPANYCODE,
       t.SIZESIZESTYPECODE,
       t.SIZECODE,
       t.UOMCODE,
       t.QUANTITY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.MARKERLINE t
FETCH FIRST 100 ROWS ONLY;
```
