# DB2ADMIN.LOCATIONMEASUREMENT

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `WHSLOCWHSZONEPHYWHSCMYCODE`, `WHSLOCWHSZONEPHYWAREHOUSECODE`, `WHSLOCATIONWAREHOUSEZONECODE`, `WAREHOUSELOCATIONCODE`, `MEASUREMENTTYPE`, `QUANTITYTYPE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 19129

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `WHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `WHSLOCWHSZONEPHYWAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `WHSLOCATIONWAREHOUSEZONECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `WAREHOUSELOCATIONCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `MEASUREMENTTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 5 | `QUANTITYTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 6 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 8 | `USEDQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `ENTERRESERVATIONQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `ISSUERESERVATIONQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LOCATIONMEASUREMENT.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `LOCATIONMEASUREMENT.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |
| `WAREHOUSELOCATION_LOCATIONMEASUREMENT` | `WHSLOCWHSZONEPHYWHSCMYCODE`, `WHSLOCWHSZONEPHYWAREHOUSECODE`, `WHSLOCATIONWAREHOUSEZONECODE`, `WAREHOUSELOCATIONCODE` | [`WAREHOUSELOCATION`](../WAREHOUSE/WAREHOUSELOCATION.md) | `WHSZONEPHYWHSCOMPANYCODE`, `WHSZONEPHYSICALWAREHOUSECODE`, `WAREHOUSEZONECODE`, `CODE` | RESTRICT | `LOCATIONMEASUREMENT.WHSLOCWHSZONEPHYWHSCMYCODE = WAREHOUSELOCATION.WHSZONEPHYWHSCOMPANYCODE AND LOCATIONMEASUREMENT.WHSLOCWHSZONEPHYWAREHOUSECODE = WAREHOUSELOCATION.WHSZONEPHYSICALWAREHOUSECODE AND LOCATIONMEASUREMENT.WHSLOCATIONWAREHOUSEZONECODE = WAREHOUSELOCATION.WAREHOUSEZONECODE AND LOCATIONMEASUREMENT.WAREHOUSELOCATIONCODE = WAREHOUSELOCATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOCATIONMEASUREMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.WHSLOCWHSZONEPHYWHSCMYCODE,
       t.WHSLOCWHSZONEPHYWAREHOUSECODE,
       t.WHSLOCATIONWAREHOUSEZONECODE,
       t.WAREHOUSELOCATIONCODE,
       t.MEASUREMENTTYPE,
       t.QUANTITYTYPE,
       t.UNITOFMEASURECODE,
       t.QUANTITY,
       t.USEDQUANTITY,
       t.ENTERRESERVATIONQUANTITY,
       t.ISSUERESERVATIONQUANTITY,
       t.CREATIONDATETIME
FROM   DB2ADMIN.LOCATIONMEASUREMENT t
FETCH FIRST 100 ROWS ONLY;
```
