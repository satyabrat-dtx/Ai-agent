# DB2ADMIN.NETOPDIVISIONTCSDATA

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE`, `DIVISIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221704

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CUSTOMERSUPPLIERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 4 | `TYPEOFORDERPARTNER` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `PANNO` | CHAR(10) |  |  |  |  |
| 6 | `TCSAPPLICABILITY` | SMALLINT | NOT NULL |  |  |  |
| 7 | `TDSAPPLICABILITY` | SMALLINT | NOT NULL |  |  |  |
| 8 | `TCSEXEMPTION` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ITRNOTFILED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CUSTOMERSUPPLIERDATA_CUSTOMERSUPPLIER` | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | [`CUSTOMERSUPPLIERDATA`](../CORE_MASTER/CUSTOMERSUPPLIERDATA.md) | `COMPANYCODE`, `TYPE`, `CODE` | RESTRICT | `NETOPDIVISIONTCSDATA.CUSTOMERSUPPLIERCOMPANYCODE = CUSTOMERSUPPLIERDATA.COMPANYCODE AND NETOPDIVISIONTCSDATA.CUSTOMERSUPPLIERTYPE = CUSTOMERSUPPLIERDATA.TYPE AND NETOPDIVISIONTCSDATA.CUSTOMERSUPPLIERCODE = CUSTOMERSUPPLIERDATA.CODE` |
| `DIVISION_DIVISION` | `CUSTOMERSUPPLIERCOMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `NETOPDIVISIONTCSDATA.CUSTOMERSUPPLIERCOMPANYCODE = DIVISION.COMPANYCODE AND NETOPDIVISIONTCSDATA.DIVISIONCODE = DIVISION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETOPDIVISIONTCSDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CUSTOMERSUPPLIERCOMPANYCODE,
       t.CUSTOMERSUPPLIERTYPE,
       t.CUSTOMERSUPPLIERCODE,
       t.DIVISIONCODE,
       t.TYPEOFORDERPARTNER,
       t.PANNO,
       t.TCSAPPLICABILITY,
       t.TDSAPPLICABILITY,
       t.TCSEXEMPTION,
       t.ITRNOTFILED,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.NETOPDIVISIONTCSDATA t
FETCH FIRST 100 ROWS ONLY;
```
