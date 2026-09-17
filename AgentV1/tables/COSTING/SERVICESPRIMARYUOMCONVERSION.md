# DB2ADMIN.SERVICESPRIMARYUOMCONVERSION

- **Module**: `COSTING` (low confidence — FK neighbourhood: 1 of 1 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `SERVICESCOMPANYCODE`, `SERVICESITEMTYPECODE`, `SERVICESSUBCODE01`, `UNITOFMEASURECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 15948

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SERVICESCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SERVICESITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SERVICESSUBCODE01` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `UNITOFMEASURECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CONVERSIONFACTOR` | DECIMAL(11,5) | NOT NULL |  |  |  |
| 5 | `CONVERSIONFACTORTYPE` | CHAR(2) |  |  |  |  |
| 6 | `MULTIPLIER` | DECIMAL(11,5) |  |  |  |  |
| 7 | `CONVERSIONFACTORPOLICYCODE` | CHAR(20) |  |  |  |  |
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
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SERVICESPRIMARYUOMCONVERSION.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `SERVICES_PRIMARYCONVERSION` | `SERVICESCOMPANYCODE`, `SERVICESITEMTYPECODE`, `SERVICESSUBCODE01` | [`SERVICES`](../COSTING/SERVICES.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `SERVICESPRIMARYUOMCONVERSION.SERVICESCOMPANYCODE = SERVICES.COMPANYCODE AND SERVICESPRIMARYUOMCONVERSION.SERVICESITEMTYPECODE = SERVICES.ITEMTYPECODE AND SERVICESPRIMARYUOMCONVERSION.SERVICESSUBCODE01 = SERVICES.SUBCODE01` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `SERVICESPRIMARYUOMCONVERSION.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SERVICESPRMUOMCONVERSIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SERVICESCOMPANYCODE,
       t.SERVICESITEMTYPECODE,
       t.SERVICESSUBCODE01,
       t.UNITOFMEASURECODE,
       t.CONVERSIONFACTOR,
       t.CONVERSIONFACTORTYPE,
       t.MULTIPLIER,
       t.CONVERSIONFACTORPOLICYCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.SERVICESPRIMARYUOMCONVERSION t
FETCH FIRST 100 ROWS ONLY;
```
