# DB2ADMIN.EVRULEDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `EVRULECOMPANYCODE`, `EVRULECATEGORYICSTABLECODE`, `EVRULECATEGORYCODE`, `EVRLSUBCTGSUBCTGICSTABLECODE`, `EVRLSUBCTGSUBCATEGORYCODE`, `EVRULEEFFECTIVEFROMDATE`, `DIVISIONCODE`, `FACTORYCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 151536

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EVRULECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EVRULECATEGORYICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EVRULECATEGORYCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EVRLSUBCTGSUBCTGICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `EVRLSUBCTGSUBCATEGORYCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `EVRULEEFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 7 | `FACTORYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 8 | `FACTORYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `FIRSTNAME` | SMALLINT | NOT NULL |  |  |  |
| 10 | `MIDDLENAME` | SMALLINT | NOT NULL |  |  |  |
| 11 | `LASTNAME` | SMALLINT | NOT NULL |  |  |  |
| 12 | `FULLNAME` | SMALLINT | NOT NULL |  |  |  |
| 13 | `DATEOFBIRTH` | SMALLINT | NOT NULL |  |  |  |
| 14 | `FATHERNAME` | SMALLINT | NOT NULL |  |  |  |
| 15 | `MOTHERNAME` | SMALLINT | NOT NULL |  |  |  |
| 16 | `PANNUMBER` | SMALLINT | NOT NULL |  |  |  |
| 17 | `AADHARNUMBER` | SMALLINT | NOT NULL |  |  |  |
| 18 | `PASSPORTNUMBER` | SMALLINT | NOT NULL |  |  |  |
| 19 | `ESINUMBER` | SMALLINT | NOT NULL |  |  |  |
| 20 | `UANNUMBER` | SMALLINT | NOT NULL |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `RUNNINGEMPLOYEE` | CHAR(7) | NOT NULL |  |  |  |
| 28 | `EXITEMPLOYEE` | CHAR(7) | NOT NULL |  |  |  |
| 29 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DIVISION_DIVISION` | `EVRULECOMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVRULEDETAIL.EVRULECOMPANYCODE = DIVISION.COMPANYCODE AND EVRULEDETAIL.DIVISIONCODE = DIVISION.CODE` |
| `EVRULE_LINE` | `EVRULECOMPANYCODE`, `EVRULECATEGORYICSTABLECODE`, `EVRULECATEGORYCODE`, `EVRLSUBCTGSUBCTGICSTABLECODE`, `EVRLSUBCTGSUBCATEGORYCODE`, `EVRULEEFFECTIVEFROMDATE` | [`EVRULE`](../OTHER/EVRULE.md) | `COMPANYCODE`, `CATEGORYICSTABLECODE`, `CATEGORYCODE`, `SUBCTGSUBCATEGORYICSTABLECODE`, `SUBCATEGORYSUBCATEGORYCODE`, `EFFECTIVEFROMDATE` | RESTRICT | `EVRULEDETAIL.EVRULECOMPANYCODE = EVRULE.COMPANYCODE AND EVRULEDETAIL.EVRULECATEGORYICSTABLECODE = EVRULE.CATEGORYICSTABLECODE AND EVRULEDETAIL.EVRULECATEGORYCODE = EVRULE.CATEGORYCODE AND EVRULEDETAIL.EVRLSUBCTGSUBCTGICSTABLECODE = EVRULE.SUBCTGSUBCATEGORYICSTABLECODE AND EVRULEDETAIL.EVRLSUBCTGSUBCATEGORYCODE = EVRULE.SUBCATEGORYSUBCATEGORYCODE AND EVRULEDETAIL.EVRULEEFFECTIVEFROMDATE = EVRULE.EFFECTIVEFROMDATE` |
| `PLANT_FACTORY` | `FACTORYCOMPANYCODE`, `FACTORYCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EVRULEDETAIL.FACTORYCOMPANYCODE = PLANT.COMPANYCODE AND EVRULEDETAIL.FACTORYCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EVRULEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EVRULECOMPANYCODE,
       t.EVRULECATEGORYICSTABLECODE,
       t.EVRULECATEGORYCODE,
       t.EVRLSUBCTGSUBCTGICSTABLECODE,
       t.EVRLSUBCTGSUBCATEGORYCODE,
       t.EVRULEEFFECTIVEFROMDATE,
       t.DIVISIONCODE,
       t.FACTORYCOMPANYCODE,
       t.FACTORYCODE,
       t.FIRSTNAME,
       t.MIDDLENAME,
       t.LASTNAME
FROM   DB2ADMIN.EVRULEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
