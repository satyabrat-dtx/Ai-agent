# DB2ADMIN.FINPAYMENTHOLDER

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `SUPPLIERCUSTOMERSUPPLIERTYPE`, `SUPPLIERCUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239146

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUPPLIERDISCRIPTION` | VARCHAR(270) |  |  |  |  |
| 5 | `HOLDINGON` | DATE |  |  |  |  |
| 6 | `FULLHOLD` | SMALLINT | NOT NULL |  |  |  |
| 7 | `HOLDINGAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 8 | `INVOICEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `REMARKS` | VARCHAR(255) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINPAYMENTHOLDER.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINPAYMENTHOLDER.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINPAYMENTHOLDER.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `ORDERPARTNER_SUPPLIER` | `COMPANYCODE`, `SUPPLIERCUSTOMERSUPPLIERTYPE`, `SUPPLIERCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `FINPAYMENTHOLDER.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND FINPAYMENTHOLDER.SUPPLIERCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND FINPAYMENTHOLDER.SUPPLIERCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINPAYMENTHOLDER_DETAILS` | [`FINPAYMENTHOLDERDETAIL`](../FINANCE/FINPAYMENTHOLDERDETAIL.md) | `FINPAYMENTHOLDERCOMPANYCODE`, `FINPAYMENTHOLDERBUNITCODE`, `FINPAYMENTHOLDERSUPCSMSUPTYPE`, `FINPAYMENTHOLDERSUPCSMSUPCODE` | `FINPAYMENTHOLDERDETAIL.FINPAYMENTHOLDERCOMPANYCODE = FINPAYMENTHOLDER.COMPANYCODE AND FINPAYMENTHOLDERDETAIL.FINPAYMENTHOLDERBUNITCODE = FINPAYMENTHOLDER.BUSINESSUNITCODE AND FINPAYMENTHOLDERDETAIL.FINPAYMENTHOLDERSUPCSMSUPTYPE = FINPAYMENTHOLDER.SUPPLIERCUSTOMERSUPPLIERTYPE AND FINPAYMENTHOLDERDETAIL.FINPAYMENTHOLDERSUPCSMSUPCODE = FINPAYMENTHOLDER.SUPPLIERCUSTOMERSUPPLIERCODE` |

## Indexes

- `FINPAYMENTHOLDERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.SUPPLIERCUSTOMERSUPPLIERTYPE,
       t.SUPPLIERCUSTOMERSUPPLIERCODE,
       t.SUPPLIERDISCRIPTION,
       t.HOLDINGON,
       t.FULLHOLD,
       t.HOLDINGAMOUNT,
       t.INVOICEAMOUNT,
       t.REMARKS,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.FINPAYMENTHOLDER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
