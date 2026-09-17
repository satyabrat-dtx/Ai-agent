# DB2ADMIN.USAINBOUNDPRODASN

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 52
- **Primary key**: `COMPANYCODE`, `RECORDTYPE`, `ASNCODE`, `ASNLINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107773

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `RECORDTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `PROGRESSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 3 | `ASNCODE` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `ASNLINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 8 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 9 | `PURCHASEORDERLINEORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 10 | `PURCHASEORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 11 | `PURORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 12 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 13 | `SUPPLIERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 14 | `SUPPLIERCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 15 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 18 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 28 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 29 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 30 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 31 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 32 | `LOTCODE` | CHAR(10) |  |  |  |  |
| 33 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 34 | `USERPRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 35 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 36 | `USERSECONDARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 37 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 38 | `USERPACKAGINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 39 | `WEIGHTUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 40 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 41 | `WEIGHTNET` | DECIMAL(15,5) |  |  |  |  |
| 42 | `WEIGHTREALNET` | DECIMAL(15,5) |  |  |  |  |
| 43 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 44 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  | FK | foreign_key |  |
| 45 | `STTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 46 | `STTRANSACTIONDETAILNUMBER` | INTEGER |  |  |  |  |
| 47 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 48 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 49 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 50 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 51 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USAINBOUNDPRODASN.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `USAINBOUNDPRODASN.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND USAINBOUNDPRODASN.ITEMTYPECODE = ITEMTYPE.CODE` |
| `ORDERPARTNER_SUPPLIER` | `COMPANYCODE`, `SUPPLIERCUSTOMERSUPPLIERTYPE`, `SUPPLIERCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `USAINBOUNDPRODASN.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND USAINBOUNDPRODASN.SUPPLIERCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND USAINBOUNDPRODASN.SUPPLIERCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `QUALITYLEVEL_QUALITYLEVEL` | `QUALITYLVLITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `QUALITYLEVELCODE` | [`QUALITYLEVEL`](../QUALITY/QUALITYLEVEL.md) | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `USAINBOUNDPRODASN.QUALITYLVLITEMTYPECOMPANYCODE = QUALITYLEVEL.ITEMTYPECOMPANYCODE AND USAINBOUNDPRODASN.ITEMTYPECODE = QUALITYLEVEL.ITEMTYPECODE AND USAINBOUNDPRODASN.QUALITYLEVELCODE = QUALITYLEVEL.CODE` |
| `UNITOFMEASURE_USERPACKAGINGUOM` | `USERPACKAGINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `USAINBOUNDPRODASN.USERPACKAGINGUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_USERPRIMARYUOM` | `USERPRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `USAINBOUNDPRODASN.USERPRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_USERSECONDARYUOM` | `USERSECONDARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `USAINBOUNDPRODASN.USERSECONDARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_WEIGHTUOM` | `WEIGHTUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `USAINBOUNDPRODASN.WEIGHTUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USAINBOUNDPRODASNUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.RECORDTYPE,
       t.PROGRESSSTATUS,
       t.ASNCODE,
       t.ASNLINENUMBER,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.PRODUCTIONDEMANDCODE,
       t.PURCHASEORDERLINEORDERLINE,
       t.PURCHASEORDERLINEORDERSUBLINE,
       t.PURORDERDELIVERYDELIVERYLINE
FROM   DB2ADMIN.USAINBOUNDPRODASN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
