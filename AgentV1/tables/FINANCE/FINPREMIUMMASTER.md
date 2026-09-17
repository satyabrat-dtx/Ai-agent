# DB2ADMIN.FINPREMIUMMASTER

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `POLICYTEUGENERICGROUPTYPECODE`, `POLICYTYPECODE`, `INCOMPANYCUSTOMERSUPPLIERTYPE`, `INCOMPANYCUSTOMERSUPPLIERCODE`, `VALIDFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224091

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `POLICYTEUGENGRPTECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `POLICYTEUGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `POLICYTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `INCOMPANYCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `INCOMPANYCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `BASICRATE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `STFIRATE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `TARIFF` | DECIMAL(18,5) |  |  |  |  |
| 10 | `OI` | DECIMAL(5,2) |  |  |  |  |
| 11 | `NETRATE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `STFI` | DECIMAL(18,5) |  |  |  |  |
| 13 | `EQRATE` | DECIMAL(18,5) |  |  |  |  |
| 14 | `PREMIUMRATE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `MILLIERATE` | DECIMAL(29,9) |  |  |  |  |
| 16 | `VALIDFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 17 | `VALIDTODATE` | DATE |  |  |  |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINPREMIUMMASTER.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPREMIUMMASTER.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINPREMIUMMASTER.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `ORDERPARTNER_INSURANCECOMPANY` | `COMPANYCODE`, `INCOMPANYCUSTOMERSUPPLIERTYPE`, `INCOMPANYCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `FINPREMIUMMASTER.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND FINPREMIUMMASTER.INCOMPANYCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND FINPREMIUMMASTER.INCOMPANYCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `USERGENERICGROUP_POLICYTYPE` | `POLICYTEUGENGRPTECOMPANYCODE`, `POLICYTEUGENERICGROUPTYPECODE`, `POLICYTYPECODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `FINPREMIUMMASTER.POLICYTEUGENGRPTECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND FINPREMIUMMASTER.POLICYTEUGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND FINPREMIUMMASTER.POLICYTYPECODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINPREMIUMMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.POLICYTEUGENGRPTECOMPANYCODE,
       t.POLICYTEUGENERICGROUPTYPECODE,
       t.POLICYTYPECODE,
       t.INCOMPANYCUSTOMERSUPPLIERTYPE,
       t.INCOMPANYCUSTOMERSUPPLIERCODE,
       t.BASICRATE,
       t.STFIRATE,
       t.TARIFF,
       t.OI,
       t.NETRATE
FROM   DB2ADMIN.FINPREMIUMMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
