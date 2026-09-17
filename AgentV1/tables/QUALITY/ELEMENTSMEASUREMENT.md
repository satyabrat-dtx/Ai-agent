# DB2ADMIN.ELEMENTSMEASUREMENT

- **Module**: `QUALITY` (low confidence — table name starts with 'ELEMENT')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `ELEMENTSCOMPANYCODE`, `ELEMENTSITEMTYPECODE`, `ELEMENTSSUBCODEKEY`, `ELEMENTSCODE`, `MEASUREMENTTYPE`, `QUANTITYTYPE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24181

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ELEMENTSCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ELEMENTSITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ELEMENTSSUBCODEKEY` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ELEMENTSCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `MEASUREMENTTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 5 | `QUANTITYTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 6 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ELEMENTSMEASUREMENT.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ELEMENTS_MEASUREMENT` | `ELEMENTSCOMPANYCODE`, `ELEMENTSITEMTYPECODE`, `ELEMENTSSUBCODEKEY`, `ELEMENTSCODE` | [`ELEMENTS`](../QUALITY/ELEMENTS.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODEKEY`, `CODE` | RESTRICT | `ELEMENTSMEASUREMENT.ELEMENTSCOMPANYCODE = ELEMENTS.COMPANYCODE AND ELEMENTSMEASUREMENT.ELEMENTSITEMTYPECODE = ELEMENTS.ITEMTYPECODE AND ELEMENTSMEASUREMENT.ELEMENTSSUBCODEKEY = ELEMENTS.SUBCODEKEY AND ELEMENTSMEASUREMENT.ELEMENTSCODE = ELEMENTS.CODE` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `ELEMENTSMEASUREMENT.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ELEMENTSMEASUREMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ELEMENTSCOMPANYCODE,
       t.ELEMENTSITEMTYPECODE,
       t.ELEMENTSSUBCODEKEY,
       t.ELEMENTSCODE,
       t.MEASUREMENTTYPE,
       t.QUANTITYTYPE,
       t.UNITOFMEASURECODE,
       t.QUANTITY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.ELEMENTSMEASUREMENT t
FETCH FIRST 100 ROWS ONLY;
```
