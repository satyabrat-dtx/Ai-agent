# DB2ADMIN.EPCGAPPLICATIONRECEIVED

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `COMPANYCODE`, `EPCGAPPLICATIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 138187

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `EPCGAPPLICATIONCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EPCGFILENO` | CHAR(15) | NOT NULL |  |  |  |
| 3 | `EPCGLICENSENO` | CHAR(30) | NOT NULL |  |  |  |
| 4 | `OMBOOKNO` | CHAR(15) | NOT NULL |  |  |  |
| 5 | `EDIREGNO` | CHAR(30) |  |  |  |  |
| 6 | `EPCGAPPLICATIONDATE` | DATE | NOT NULL |  |  |  |
| 7 | `EPCGFILEDATE` | DATE | NOT NULL |  |  |  |
| 8 | `EPCGLICENSEDATE` | DATE | NOT NULL |  |  |  |
| 9 | `OMBOOKDATE` | DATE | NOT NULL |  |  |  |
| 10 | `VALIDITYDATE` | DATE | NOT NULL |  |  |  |
| 11 | `CIFVALUEFC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `CIFUTILIZEDVALUEFC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 13 | `CIFVALUEINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 14 | `CIFUTILIZEDVALUEINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 15 | `EXCHANGERATE` | DECIMAL(28,15) | NOT NULL |  |  |  |
| 16 | `EOUNDERTAKENINR` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 17 | `UTILIZATIONAMTCC` | DECIMAL(15,5) |  |  |  |  |
| 18 | `EOUNDERTAKENFC` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 19 | `UTILIZATIONAMTFC` | DECIMAL(15,5) |  |  |  |  |
| 20 | `FINALAPPLICATIONFEE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `CUSTOMDUTY` | DECIMAL(18,5) |  |  |  |  |
| 22 | `DUTYLEVIABLE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `DUTYSAVED` | DECIMAL(18,5) |  |  |  |  |
| 24 | `IMPORTVALIDITYDATE` | DATE |  |  |  |  |
| 25 | `AEOAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 26 | `EOVFORIMPORTS` | DATE |  |  |  |  |
| 27 | `EOVFOREXPORTS1` | DATE |  |  |  |  |
| 28 | `EOVFOREXPORTS2` | DATE |  |  |  |  |
| 29 | `THIRDPARTYCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 30 | `THIRDPARTYCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 31 | `PORTCODE` | CHAR(10) |  | FK | foreign_key |  |
| 32 | `REMARK` | CHAR(100) |  |  |  |  |
| 33 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 34 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 35 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 36 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 37 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EPCGAPPLICATIONRECEIVED.COMPANYCODE = COMPANY.CODE` |
| `EPCGAPPLICATION_EPCGAPPLICATION` | `COMPANYCODE`, `EPCGAPPLICATIONCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGAPPLICATIONRECEIVED.COMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND EPCGAPPLICATIONRECEIVED.EPCGAPPLICATIONCODE = EPCGAPPLICATION.CODE` |
| `ORDERPARTNER_THIRDPARTY` | `COMPANYCODE`, `THIRDPARTYCUSTOMERSUPPLIERTYPE`, `THIRDPARTYCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `EPCGAPPLICATIONRECEIVED.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND EPCGAPPLICATIONRECEIVED.THIRDPARTYCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND EPCGAPPLICATIONRECEIVED.THIRDPARTYCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `PORT_PORT` | `PORTCODE` | [`PORT`](../CORE_MASTER/PORT.md) | `CODE` | RESTRICT | `EPCGAPPLICATIONRECEIVED.PORTCODE = PORT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EPCGAPPLICATIONRECEIVEDUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.EPCGAPPLICATIONCODE,
       t.EPCGFILENO,
       t.EPCGLICENSENO,
       t.OMBOOKNO,
       t.EDIREGNO,
       t.EPCGAPPLICATIONDATE,
       t.EPCGFILEDATE,
       t.EPCGLICENSEDATE,
       t.OMBOOKDATE,
       t.VALIDITYDATE,
       t.CIFVALUEFC
FROM   DB2ADMIN.EPCGAPPLICATIONRECEIVED t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
