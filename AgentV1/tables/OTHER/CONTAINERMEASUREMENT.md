# DB2ADMIN.CONTAINERMEASUREMENT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `CONTAINERCOMPANYCODE`, `CONTAINERITEMTYPECODE`, `CONTAINERSUBCODE01`, `MEASUREMENTTYPE`, `QUANTITYTYPE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26561

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CONTAINERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CONTAINERITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `MEASUREMENTTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 4 | `QUANTITYTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 5 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CONTAINERMEASUREMENT.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `CONTAINER_MEASUREMENT` | `CONTAINERCOMPANYCODE`, `CONTAINERITEMTYPECODE`, `CONTAINERSUBCODE01` | [`CONTAINER`](../CORE_MASTER/CONTAINER.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `CONTAINERMEASUREMENT.CONTAINERCOMPANYCODE = CONTAINER.COMPANYCODE AND CONTAINERMEASUREMENT.CONTAINERITEMTYPECODE = CONTAINER.ITEMTYPECODE AND CONTAINERMEASUREMENT.CONTAINERSUBCODE01 = CONTAINER.SUBCODE01` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `CONTAINERMEASUREMENT.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CONTAINERMEASUREMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CONTAINERCOMPANYCODE,
       t.CONTAINERITEMTYPECODE,
       t.CONTAINERSUBCODE01,
       t.MEASUREMENTTYPE,
       t.QUANTITYTYPE,
       t.UNITOFMEASURECODE,
       t.QUANTITY,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.OWNINGCOMPANYCODE
FROM   DB2ADMIN.CONTAINERMEASUREMENT t
FETCH FIRST 100 ROWS ONLY;
```
