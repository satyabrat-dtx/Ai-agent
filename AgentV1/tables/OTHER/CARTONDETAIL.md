# DB2ADMIN.CARTONDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `CARTONCOMPANYCODE`, `CARTONPREFIX`, `CARTONSTARTINGNUM`, `SLNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 126640

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CARTONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CARTONPREFIX` | CHAR(9) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CARTONSTARTINGNUM` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `COLORCODE` | CHAR(10) |  |  |  |  |
| 15 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 16 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `SLNO` | INTEGER | NOT NULL | PK | primary_key |  |
| 18 | `ORDPACKINGORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 19 | `RELEASENUM` | CHAR(10) |  |  |  |  |
| 20 | `SHIPPEDTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CARTON_LINE` | `CARTONCOMPANYCODE`, `CARTONPREFIX`, `CARTONSTARTINGNUM` | [`CARTON`](../CORE_MASTER/CARTON.md) | `COMPANYCODE`, `PREFIX`, `STARTINGNUM` | RESTRICT | `CARTONDETAIL.CARTONCOMPANYCODE = CARTON.COMPANYCODE AND CARTONDETAIL.CARTONPREFIX = CARTON.PREFIX AND CARTONDETAIL.CARTONSTARTINGNUM = CARTON.STARTINGNUM` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CARTONDETAILUID` (ABSUNIQUEID)
- `IDX_CARTONDETAIL` (CARTONCOMPANYCODE, RELEASENUM, ITEMTYPECODE, SUBCODE01, SUBCODE02, SUBCODE03, SUBCODE04, SUBCODE05, SUBCODE06, SUBCODE07, SUBCODE08, SUBCODE09, SUBCODE10)

## Starter query

```sql
SELECT t.CARTONCOMPANYCODE,
       t.CARTONPREFIX,
       t.CARTONSTARTINGNUM,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.CARTONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
