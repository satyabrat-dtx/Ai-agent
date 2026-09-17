# DB2ADMIN.FONSHIPGUIDEHEADER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `GUIDECOUNTERCODE`, `GUIDECODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69892

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `GUIDECOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `GUIDECODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `DRIVERCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `CARRIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 5 | `CARRIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 6 | `LICENSEPLATE` | CHAR(15) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 11 | `GUIDECOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 12 | `DRIVERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTER_GUIDECOUNTER` | `GUIDECOUNTERCOMPANYCODE`, `GUIDECOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FONSHIPGUIDEHEADER.GUIDECOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND FONSHIPGUIDEHEADER.GUIDECOUNTERCODE = COUNTER.CODE` |
| `CUSTOMERSUPPLIERDATA_CARRIER` | `COMPANYCODE`, `CARRIERTYPE`, `CARRIERCODE` | [`CUSTOMERSUPPLIERDATA`](../CORE_MASTER/CUSTOMERSUPPLIERDATA.md) | `COMPANYCODE`, `TYPE`, `CODE` | RESTRICT | `FONSHIPGUIDEHEADER.COMPANYCODE = CUSTOMERSUPPLIERDATA.COMPANYCODE AND FONSHIPGUIDEHEADER.CARRIERTYPE = CUSTOMERSUPPLIERDATA.TYPE AND FONSHIPGUIDEHEADER.CARRIERCODE = CUSTOMERSUPPLIERDATA.CODE` |
| `TRUCKDRIVER_DRIVER` | `DRIVERCOMPANYCODE`, `DRIVERCODE` | [`TRUCKDRIVER`](../CORE_MASTER/TRUCKDRIVER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FONSHIPGUIDEHEADER.DRIVERCOMPANYCODE = TRUCKDRIVER.COMPANYCODE AND FONSHIPGUIDEHEADER.DRIVERCODE = TRUCKDRIVER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FONSHIPGUIDEHEADER_LINES` | [`FONSHIPPINGGUIDE`](../OTHER/FONSHIPPINGGUIDE.md) | `FONSHIPGUIDEHEADERCOMPANYCODE`, `FONSHIPGUIDEHDRGUIDECNTCODE`, `FONSHIPGUIDEHEADERGUIDECODE` | `FONSHIPPINGGUIDE.FONSHIPGUIDEHEADERCOMPANYCODE = FONSHIPGUIDEHEADER.COMPANYCODE AND FONSHIPPINGGUIDE.FONSHIPGUIDEHDRGUIDECNTCODE = FONSHIPGUIDEHEADER.GUIDECOUNTERCODE AND FONSHIPPINGGUIDE.FONSHIPGUIDEHEADERGUIDECODE = FONSHIPGUIDEHEADER.GUIDECODE` |

## Indexes

- `FONSHIPGUIDEHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.GUIDECOUNTERCODE,
       t.GUIDECODE,
       t.DRIVERCODE,
       t.CARRIERTYPE,
       t.CARRIERCODE,
       t.LICENSEPLATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.GUIDECOUNTERCOMPANYCODE
FROM   DB2ADMIN.FONSHIPGUIDEHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
