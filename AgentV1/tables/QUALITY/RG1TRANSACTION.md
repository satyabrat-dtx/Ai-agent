# DB2ADMIN.RG1TRANSACTION

- **Module**: `QUALITY` (low confidence — FK neighbourhood: 2 of 2 related tables are QUALITY)
- **Roles**: `business_data`
- **Columns**: 52
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `UNIQUEID`
- **FK degree**: referenced by 0 constraint(s), references 10 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 142534

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHAPTERID` | CHAR(5) |  |  |  |  |
| 1 | `CHAPTERINDICATION` | INTEGER | NOT NULL |  |  |  |
| 2 | `EXCISECATEGORYCODE` | CHAR(10) |  | FK | foreign_key |  |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `GROUPING` | CHAR(20) |  |  |  |  |
| 6 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 7 | `RG1TEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `EXCISEYEARREGNO` | CHAR(30) |  | FK | foreign_key |  |
| 9 | `EXCISEYEARCODE` | CHAR(4) |  | FK | foreign_key |  |
| 10 | `SEQNO` | INTEGER | NOT NULL |  |  |  |
| 11 | `TARIFFCODE` | CHAR(20) |  | FK | foreign_key |  |
| 12 | `PLANTINVOICECODE` | CHAR(15) |  | FK | foreign_key |  |
| 13 | `TRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 14 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 15 | `ITDATE` | DATE |  |  |  |  |
| 16 | `ADDDEDUCT` | INTEGER | NOT NULL |  |  |  |
| 17 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 20 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 30 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  | FK | foreign_key |  |
| 32 | `QUALITYCATEGORYCODE` | CHAR(2) |  | FK | foreign_key |  |
| 33 | `BALESCOUNT` | INTEGER | NOT NULL |  |  |  |
| 34 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 35 | `WIDTH` | DECIMAL(18,5) |  |  |  |  |
| 36 | `CONTAINER` | CHAR(15) |  |  |  |  |
| 37 | `ELEMENT` | CHAR(15) |  |  |  |  |
| 38 | `PLANT` | CHAR(8) |  |  |  |  |
| 39 | `SQMTRS` | DECIMAL(18,5) |  |  |  |  |
| 40 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 41 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 42 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 43 | `ORDERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 44 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 45 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 46 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 47 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 48 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 49 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 50 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 51 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 10

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RG1TRANSACTION.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_ORDERCOUNTER` | `ORDERCOUNTERCOMPANYCODE`, `ORDERCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RG1TRANSACTION.ORDERCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND RG1TRANSACTION.ORDERCOUNTERCODE = COUNTER.CODE` |
| `EXCISECATEGORY_EXCISECATEGORY` | `EXCISECATEGORYCODE` | [`EXCISECATEGORY`](../QUALITY/EXCISECATEGORY.md) | `CODE` | RESTRICT | `RG1TRANSACTION.EXCISECATEGORYCODE = EXCISECATEGORY.CODE` |
| `EXCISEYEAR_EXCISEYEAR` | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | [`EXCISEYEAR`](../SALES/EXCISEYEAR.md) | `COMPANYCODE`, `REGNO`, `CODE` | RESTRICT | `RG1TRANSACTION.COMPANYCODE = EXCISEYEAR.COMPANYCODE AND RG1TRANSACTION.EXCISEYEARREGNO = EXCISEYEAR.REGNO AND RG1TRANSACTION.EXCISEYEARCODE = EXCISEYEAR.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RG1TRANSACTION.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND RG1TRANSACTION.ITEMTYPECODE = ITEMTYPE.CODE` |
| `PLANTINVOICE_PLANTINVOICE` | `COMPANYCODE`, `DIVISIONCODE`, `PLANTINVOICECODE` | [`PLANTINVOICE`](../CORE_MASTER/PLANTINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `RG1TRANSACTION.COMPANYCODE = PLANTINVOICE.COMPANYCODE AND RG1TRANSACTION.DIVISIONCODE = PLANTINVOICE.DIVISIONCODE AND RG1TRANSACTION.PLANTINVOICECODE = PLANTINVOICE.CODE` |
| `QUALITYCATEGORY_QUALITYCATEGORY` | `COMPANYCODE`, `QUALITYCATEGORYCODE` | [`QUALITYCATEGORY`](../QUALITY/QUALITYCATEGORY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RG1TRANSACTION.COMPANYCODE = QUALITYCATEGORY.COMPANYCODE AND RG1TRANSACTION.QUALITYCATEGORYCODE = QUALITYCATEGORY.CODE` |
| `QUALITYLEVEL_QUALITYLEVEL` | `QUALITYLVLITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `QUALITYLEVELCODE` | [`QUALITYLEVEL`](../QUALITY/QUALITYLEVEL.md) | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `RG1TRANSACTION.QUALITYLVLITEMTYPECOMPANYCODE = QUALITYLEVEL.ITEMTYPECOMPANYCODE AND RG1TRANSACTION.ITEMTYPECODE = QUALITYLEVEL.ITEMTYPECODE AND RG1TRANSACTION.QUALITYLEVELCODE = QUALITYLEVEL.CODE` |
| `RG1TEMPLATE_RG1TEMPLATE` | `COMPANYCODE`, `DIVISIONCODE`, `RG1TEMPLATECODE` | [`RG1TEMPLATE`](../QUALITY/RG1TEMPLATE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `RG1TRANSACTION.COMPANYCODE = RG1TEMPLATE.COMPANYCODE AND RG1TRANSACTION.DIVISIONCODE = RG1TEMPLATE.DIVISIONCODE AND RG1TRANSACTION.RG1TEMPLATECODE = RG1TEMPLATE.CODE` |
| `TARIFF_TARIFF` | `TARIFFCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `RG1TRANSACTION.TARIFFCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RG1TRANSACTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CHAPTERID,
       t.CHAPTERINDICATION,
       t.EXCISECATEGORYCODE,
       t.COMPANYCODE,
       t.UNIQUEID,
       t.GROUPING,
       t.DIVISIONCODE,
       t.RG1TEMPLATECODE,
       t.EXCISEYEARREGNO,
       t.EXCISEYEARCODE,
       t.SEQNO,
       t.TARIFFCODE
FROM   DB2ADMIN.RG1TRANSACTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
