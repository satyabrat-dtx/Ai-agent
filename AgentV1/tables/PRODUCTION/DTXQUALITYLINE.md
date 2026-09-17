# DB2ADMIN.DTXQUALITYLINE

- **Module**: `PRODUCTION` (low confidence — FK neighbourhood: 1 of 1 related tables are PRODUCTION)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `DTXQUALITYHEADERCOMPANYCODE`, `DTXQUALITYHEADERCODE`, `DTXQUALITYHEADERSUBGROUPCODE`, `DTXQUALITYHEADERNUMBERID`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 92064

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DTXQUALITYHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DTXQUALITYHEADERCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DTXQUALITYHEADERSUBGROUPCODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DTXQUALITYHEADERNUMBERID` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 6 | `CHARACTERISTICCODE` | CHAR(5) |  | FK | foreign_key |  |
| 7 | `MANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SUBCODEMIN` | CHAR(20) |  |  |  |  |
| 9 | `SUBCODEMAX` | CHAR(20) |  |  |  |  |
| 10 | `SUBCODEMEDIOMIN` | CHAR(20) |  |  |  |  |
| 11 | `SUBCODEMEDIOMAX` | CHAR(20) |  |  |  |  |
| 12 | `SUBCODESTANDARD` | CHAR(20) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DTXQUALITYCHARACTERISTICTYPE_CHARACTERISTIC` | `DTXQUALITYHEADERCOMPANYCODE`, `CHARACTERISTICCODE` | [`DTXQUALITYCHARACTERISTICTYPE`](../PRODUCTION/DTXQUALITYCHARACTERISTICTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DTXQUALITYLINE.DTXQUALITYHEADERCOMPANYCODE = DTXQUALITYCHARACTERISTICTYPE.COMPANYCODE AND DTXQUALITYLINE.CHARACTERISTICCODE = DTXQUALITYCHARACTERISTICTYPE.CODE` |
| `DTXQUALITYHEADER_LINE` | `DTXQUALITYHEADERCOMPANYCODE`, `DTXQUALITYHEADERCODE`, `DTXQUALITYHEADERSUBGROUPCODE`, `DTXQUALITYHEADERNUMBERID` | [`DTXQUALITYHEADER`](../PRODUCTION/DTXQUALITYHEADER.md) | `COMPANYCODE`, `CODE`, `SUBGROUPCODE`, `NUMBERID` | RESTRICT | `DTXQUALITYLINE.DTXQUALITYHEADERCOMPANYCODE = DTXQUALITYHEADER.COMPANYCODE AND DTXQUALITYLINE.DTXQUALITYHEADERCODE = DTXQUALITYHEADER.CODE AND DTXQUALITYLINE.DTXQUALITYHEADERSUBGROUPCODE = DTXQUALITYHEADER.SUBGROUPCODE AND DTXQUALITYLINE.DTXQUALITYHEADERNUMBERID = DTXQUALITYHEADER.NUMBERID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DTXQUALITYLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DTXQUALITYHEADERCOMPANYCODE,
       t.DTXQUALITYHEADERCODE,
       t.DTXQUALITYHEADERSUBGROUPCODE,
       t.DTXQUALITYHEADERNUMBERID,
       t.LINE,
       t.SEQUENCE,
       t.CHARACTERISTICCODE,
       t.MANDATORY,
       t.SUBCODEMIN,
       t.SUBCODEMAX,
       t.SUBCODEMEDIOMIN,
       t.SUBCODEMEDIOMAX
FROM   DB2ADMIN.DTXQUALITYLINE t
FETCH FIRST 100 ROWS ONLY;
```
